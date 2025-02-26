# 🤖 SmartChatAI - AI Chatbot for Math & Real-World Questions

SmartChatAI is a **AI chatbot** that can **solve math problems** and **answer real-world factual questions** using **Mistral AI** and **Google Search API**.  
It provides **accurate calculations** for **integration, differentiation, LCM, factorials**, and **fetches up-to-date factual information** from the web.  

## 🚀 Features
✅ **Solves math problems** (integration, differentiation, LCM, factorial, etc.).

✅ **Answers real-world questions** using web search.

✅ **Interactive Chat UI** built with **Streamlit**.

✅ **Dark-themed chat bubbles** with **user & bot icons**.

## 🖥️ Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/ayushman-77/SmartChatAI.git
cd SmartChatAI
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
```
Activate the environment:  
- **Windows (CMD/PowerShell)**:  
  ```sh
  venv\Scripts\activate
  ```
- **Linux/macOS**:  
  ```sh
  source venv/bin/activate
  ```

### 3️⃣ Install Required Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up API Keys
You **must set up API keys** before running the chatbot.  

#### **Option 1: Using Environment Variables**
For **Windows (CMD)**:
```sh
set GOOGLE_API_KEY=your-google-api-key
set GOOGLE_CX_KEY=your-google-cx-key
set MISTRAL_API_KEY=your-mistral-api-key
```

For **PowerShell**:
```sh
$env:GOOGLE_API_KEY="your-google-api-key"
$env:GOOGLE_CX_KEY="your-google-cx-key"
$env:MISTRAL_API_KEY="your-mistral-api-key"
```

For **Linux/macOS**:
```sh
export GOOGLE_API_KEY="your-google-api-key"
export GOOGLE_CX_KEY="your-google-cx-key"
export MISTRAL_API_KEY="your-mistral-api-key"
```

#### **Option 2: Using a `.env` File**
1. **Create a `.env` file** in the project directory.
2. **Add API keys** inside:
   ```
   GOOGLE_API_KEY=your-google-api-key
   GOOGLE_CX_KEY=your-google-cx-key
   MISTRAL_API_KEY=your-mistral-api-key
   ```

### 5️⃣ Run the Chatbot
```sh
streamlit run app.py
```

## 🧠 Example Questions SmartChatAI Can Answer
### **Mathematical Questions:**
- **"What is the integration of 4x² + sin(x)?"**  
  *Response: The integral of 4x² + sin(x) is (4/3)x³ - cos(x) + C.*
- **"What is the LCM of 6 and 9?"**  
  *Response: The least common multiple of 6 and 9 is 18.*

### **Factual Questions:**
- **"What is the tallest mountain in the world?"**  
  *Response: The tallest mountain in the world is Mount Everest, with a height of 8,848.86 meters (29,031.7 feet).*
- **"What is the capital of Japan?"**  
  *Response: The capital of Japan is Tokyo.*
