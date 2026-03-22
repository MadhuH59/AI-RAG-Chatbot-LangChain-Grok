---

# 🤖 AI RAG Chatbot using LangChain + Groq + Streamlit

This project is a full-stack AI Agent that combines LLM reasoning, RAG (Retrieval-Augmented Generation), real-time web search, and document understanding with an interactive ChatGPT-like interface.

Here’s your **complete professional README.md** (ready to paste into GitHub) 🚀

---

# 🚀 AI Agent (RAG + Web Search + PDF + Memory)

A full-stack **AI Agent** built using LLMs that can:

* Answer questions from documents 📄
* Fetch real-time data from the internet 🌐
* Perform calculations ➗
* Maintain conversation memory 💬

---

# 📌 Features

## 🧠 AI Agent

* Intelligent **tool selection system**
* Chooses between:

  * SEARCH (documents)
  * WEB (real-time info)
  * CALCULATE (math)
  * NONE (general knowledge)

---

## 📄 RAG (Retrieval-Augmented Generation)

* Uses document-based context for accurate answers
* Supports:

  * `sample.txt`
  * Uploaded PDFs
* Semantic search using embeddings

---

## 📂 PDF Upload

* Upload PDFs directly from UI
* Automatically:

  * Extracts content
  * Splits into chunks
  * Stores in vector DB
* Ask questions from your documents

---

## 🌐 Web Search

* Fetches real-time data from internet
* Handles:

  * Latest news
  * Stock prices
  * Current events

---

## ➗ Calculator

* Solves math expressions dynamically

---

## 💬 Chat Memory

* Maintains conversation history
* Context-aware responses
* Reset option available

---

## 🧹 Clear Chat

* Clears:

  * Chat history
  * Agent memory
* Does NOT delete documents

---

## 🎨 ChatGPT-like UI

* Built using Streamlit
* Features:

  * Chat interface
  * Sidebar tools
  * Clean UI

---

# 🏗️ Project Architecture

## 🔷 High-Level Flow

```
User Input (UI)
      ↓
AI Agent (Tool Decision)
      ↓
 ┌───────────────┬───────────────┬───────────────┐
 │               │               │               │
SEARCH        WEB SEARCH     CALCULATOR       NONE
(RAG)         (Internet)     (Math)        (LLM Only)
 │               │               │               │
 └───────────────┴───────────────┴───────────────┘
      ↓
Context Generation
      ↓
LLM (Groq - llama3)
      ↓
Final Answer
      ↓
Displayed in UI
```

---

# 🧠 How It Works

## 📄 RAG Flow

```
Document → Chunking → Embeddings → Vector DB → Retrieval
```

## 📂 PDF Flow

```
Upload PDF → Save → Extract → Chunk → Embed → Store → Query
```

## 💬 Query Flow

```
User Question
      ↓
Agent selects tool
      ↓
Context generated
      ↓
LLM generates answer
```

---

# 📁 Project Structure

```
AI_agent/
│
├── app.py              # Streamlit UI
├── agent.py            # AI Agent logic
├── rag.py              # RAG pipeline
├── tools.py            # Web + Calculator
├── data/
│   └── sample.txt      # Default data
├── uploads/            # Uploaded PDFs
├── db/                 # Vector DB
└── requirements.txt
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone Repo

```
git clone <your-repo-url>
cd AI_agent
```

---

## 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 4️⃣ Set API Key

```
setx GROQ_API_KEY "your_api_key_here"
```

Restart terminal after this.

---

## 5️⃣ Run App

```
streamlit run app.py
```

---

# 🧪 Usage

## 📄 Upload PDF

* Use sidebar
* Ask questions from document

---

## 🌐 Real-time Queries

```
latest news today
BSE stock price today
```

---

## ➗ Math

```
234 * 56
```

---

## 📚 RAG (Local Data)

```
Ask about sample.txt content
```

---

# 🛠️ Tech Stack

* Python
* Streamlit
* Groq (LLM API)
* LangChain
* ChromaDB
* HuggingFace Embeddings
* DuckDuckGo Search

---

# 🎯 Skills Demonstrated

* AI Agent Design
* Retrieval-Augmented Generation (RAG)
* Vector Databases
* LLM Integration
* Prompt Engineering
* Tool-based AI Systems
* Full-stack AI App Development

---

# 🚀 Future Improvements

* Real-time stock API 📈
* Multi-PDF management 📂
* Streaming responses ⚡
* Chat history persistence 🗄️
* Deployment (Cloudflare / Render) 🌐

---

# 🙌 Conclusion

This project demonstrates a **real-world AI agent system** combining:

* LLM reasoning
* Document intelligence
* Real-time data access
* Interactive UI

---

# ⭐ If you like this project, give it a star!

---



---

# 🧠 What is RAG (Retrieval Augmented Generation)?

**RAG** is an AI technique where:

1️⃣ Documents are stored in a **vector database**
2️⃣ When a user asks a question, **relevant text chunks are retrieved**
3️⃣ The retrieved content is sent to the **LLM as context**
4️⃣ The LLM generates an answer using both:

* Retrieved document context
* Its own trained knowledge

This improves **accuracy and reduces hallucination**.

---

# ⚙️ Technologies Used

* **Python**
* **LangChain**
* **Groq LLM API**
* **Chroma Vector Database**
* **Streamlit UI**
* **HuggingFace Embeddings**

---

# 📂 Project Structure

```
AI_agent_using_APIKey
│
├── app.py
├── sample.txt
├── requirements.txt
├── README.md
│
├── db/
│   ├── chroma.sqlite3
│   └── index files
│
└── venv/
```

---

# 📄 Why `sample.txt`?

`sample.txt` contains **custom knowledge** that the chatbot should use while answering questions.

Example:

```
LangChain is a framework for building applications with LLMs.
Vector databases store embeddings of documents.
```

This file is:

1️⃣ Loaded
2️⃣ Split into small chunks
3️⃣ Converted into embeddings
4️⃣ Stored inside the **vector database**

---

# 🧠 How the Vector Database Works

When the project runs for the **first time**:

```
sample.txt
     ↓
Text Splitter
     ↓
Embeddings Created
     ↓
Stored in Vector Database
     ↓
db/ folder created
```

The `db` folder contains:

```
chroma.sqlite3
vector index files
metadata
```

These files allow the chatbot to **search documents quickly using similarity search**.

---

# 🔍 How Questions Are Answered

When a user asks a question:

### Step 1

User asks question in **Streamlit UI**

Example:

```
What is LangChain?
```

### Step 2

LangChain converts the question into **embedding**

### Step 3

Vector database searches for **similar text chunks**

Example retrieved chunk:

```
LangChain is a framework for building applications with LLMs.
```

### Step 4

Retrieved content + user question are sent to **Groq LLM**

### Step 5

LLM generates the final answer.

---

# ❓ Why Does the Chatbot Answer Questions Not in `sample.txt`?

You might notice the chatbot can answer **questions not present in `sample.txt`**.

Example:

```
What is Python?
```

Even though Python is not in `sample.txt`, the chatbot still answers.

This happens because:

The **LLM already has general knowledge from its training**.

So the final answer may come from:

| Source        | When Used                     |
| ------------- | ----------------------------- |
| sample.txt    | If relevant content found     |
| LLM knowledge | If document context not found |

So the chatbot uses **both**:

```
Document Knowledge + LLM Knowledge
```

This is why it can answer **general questions as well**.

---

# 🚀 How to Run the Project

### 1️⃣ Clone Repository

```
git clone https://github.com/yourusername/yourrepo.git
```

```
cd yourrepo
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

---

### 3️⃣ Activate Virtual Environment

Windows

```
venv\Scripts\activate
```

Mac / Linux

```
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 5️⃣ Add Groq API Key

Create `.env` file

```
GROQ_API_KEY=your_api_key
```

---

### 6️⃣ Run Streamlit App

```
streamlit run app.py
```

---

### 7️⃣ Open Browser

```
http://localhost:8501
```

---

# 💬 Example Questions

You can ask:

Document based:

```
What is LangChain?
```

General questions:

```
What is Python?
```

---

# 🎯 Key Concepts Demonstrated

✔ RAG Architecture
✔ Vector Databases
✔ Embeddings
✔ Semantic Search
✔ LangChain Retriever
✔ LLM Integration

---

# 📈 Future Improvements

* Upload multiple documents
* PDF support
* Chat history memory
* Voice input
* Deploy to cloud

---

# 👨‍💻 Author

**Madhu H**

AI / LLM Projects using LangChain

---

