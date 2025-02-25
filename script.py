import os
import json
from mistralai import Mistral
from web import *
from functions import *
from dotenv import load_dotenv

load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

if not MISTRAL_API_KEY:
    raise ValueError("❌ Missing Mistral API Key! Set MISTRAL_API_KEY before running.")

with open("function_definitions.json", "r") as file:
    tools = json.load(file)

names_to_funcs = {
    "addition": addition,
    "subtraction": subtraction,
    "multiplication": multiplication,
    "division": division,
    "remainder": remainder,
    "differentiation": differentiation,
    "integration": integration,
    "evaluation": evaluation,
    "exponentiation": exponentiation,
    "square_root": square_root,
    "logarithm": logarithm,
    "factorial": factorial,
    "gcd": gcd,
    "lcm": lcm,
    "absolute_value": absolute_value,
    "trigonometric": trigonometric,
    "inverse_trigonometric":inverse_trigonometric,
    "hyperbolic": hyperbolic
}

system_prompt = """
You are a helpful chatbot with access to specialized arithmetic tools. 
When a query involves any mathematical operation (like addition, subtraction, multiplication, division, etc.), you MUST invoke the appropriate function (e.g., "addition") instead of answering directly in plain text.
If the query involves a mathematical expression, extract the mathematical expression in a format that is directly compatible with Python's SymPy library. 
"""

model = "mistral-large-latest"
client = Mistral(api_key=MISTRAL_API_KEY)

def friendly_response(question, answer):    
    prompt = f"""
    The following is a question and its computed mathematical answer:
    
    Question: {question}
    Answer: {answer}
    
    Your task is to generate a user-friendly response that presents the answer naturally within the context of the question.
    Do NOT simply state the number. Instead, provide a natural and short response as a helpful assistant. Do NOT provide or point out any mistakes.
    Do NOT write the numerical part or the function part of the answer in words. Write the numerical or function part as it is.
    If the answer is an error statement or None then just say "Error generating response" and nothing else. Please Do NOT try to correct the answer.

    Now generate the response for the given question and answer:
    """
    
    response = client.chat.complete(
        model="mistral-medium",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    
    return response.choices[0].message.content.strip()

def generate_response(content):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": content}
    ]

    try:
        chat_response = client.chat.complete(
            model=model,
            messages=messages,
            tools=tools,
            tool_choice="auto",
            max_tokens=1024,
        )

        tool_calls = chat_response.choices[0].message.tool_calls

        if not tool_calls:
            search_results = ask_mistral(content)
            return search_results if search_results else "I couldn't find relevant information."

        tool_call = tool_calls[0]
        func_name = tool_call.function.name
        func_params = json.loads(tool_call.function.arguments)

        if func_name not in names_to_funcs:
            return "Unknown function call."

        try:
            func_result = names_to_funcs[func_name](**func_params)
        except Exception as e:
            return f"Error executing function {func_name}: {e}"

        if func_result is None:
            return "Error generating response."

        messages.append({
            "role": "tool",
            "name": func_name,
            "content": str(func_result),
            "tool_call_id": tool_call.id
        })

        return friendly_response(content, func_result)

    except requests.exceptions.RequestException as e:
        return "Network error. Please check your internet connection."

    except ValueError as e:
        return f"Invalid input: {e}"

    except Exception as e:
        return "Error generating response."
