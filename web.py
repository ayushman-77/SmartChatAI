import re
import os
import requests
from newspaper import Article
from mistralai import Mistral
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
CX = os.getenv("GOOGLE_CX_KEY")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("❌ Missing API key! Set GOOGLE_API_KEY before running.")

if not CX:
    raise ValueError("❌ Missing CX key! Set GOOGLE_CX_KEY before running.")

if not MISTRAL_API_KEY:
    raise ValueError("❌ Missing Mistral API Key! Set MISTRAL_API_KEY before running.")

def search(query, num_results=3):
    """Fetch top search results from Google."""
    url = "https://www.googleapis.com/customsearch/v1"
    params = {"q": query, "key": GOOGLE_API_KEY, "cx": CX, "num": num_results}
    response = requests.get(url, params=params)
    data = response.json()

    links = []
    if "items" in data:
        for item in data["items"]:
            links.append(item["link"])
    return links

def scrape_content(url):
    """Scrape text content from a webpage."""
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text[:1500]
    except Exception as e:
        return None

def fetch_context(query):
    """Get search results and scrape their content."""
    links = search(query)
    scraped_texts = []
    for link in links:
        content = scrape_content(link)
        if content:
            scraped_texts.append(content)

    return "\n\n".join(scraped_texts[:2])

def clean_response(response):
    """Removes unnecessary disclaimers and confidence statements from the AI response."""
    patterns = [
        r",?\s*according to the (?:context|provided information|data)",
        r",?\s*confidence: \d+%",
        r",?\s*as mentioned earlier",
        r"note:.*$",
    ]
    for pattern in patterns:
        response = re.sub(pattern, "", response, flags=re.IGNORECASE)
    
    return response.strip()

def ask_mistral(original_query):
    """Send query + scraped context to Mistral AI."""
    client = Mistral(api_key=MISTRAL_API_KEY)
    
    context = fetch_context(original_query)

    prompt = (
        "You are a highly professional AI assistant. "
        "Answer the question concisely and naturally, as an expert would. "
        "Do not give vague answers—provide detailed and well-structured explanations unless explicitly asked to be brief. "
        "DO NOT mention phrases like 'according to the context,' 'as mentioned in the information provided,' "
        "'the context indicates,' or anything similar. "
        "Your answer should sound as if it is general knowledge, even if it is based on the context. "
        "Simply provide the direct answer without extra disclaimers.\n\n"
        f"Context:\n{context}\n\n"
        f"Question:\n{original_query}\n\n"
        "Provide a direct and natural response:"
    )

    full_response = ""
    while True:
        response = client.chat.complete(
            model="mistral-medium",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=600
        )
        
        answer = response.choices[0].message.content.strip()
        full_response += " " + answer

        if response.choices[0].finish_reason == "length":
            prompt = "Continue the answer from where it left off:"
        else:
            break

    cleaned_response = clean_response(full_response.strip())
    return cleaned_response