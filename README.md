---

# 🤖 AI RAG Chatbot using LangChain + Groq + Streamlit

This project is a **Retrieval Augmented Generation (RAG) based AI chatbot** built using **LangChain, Groq LLM, Chroma Vector Database, and Streamlit UI**.

The chatbot can answer questions based on **custom documents (`sample.txt`)** while also using **LLM knowledge for general questions**.

---

# 📌 Project Architecture

```
User Question
     │
     ▼
Streamlit UI
     │
     ▼
LangChain Retriever
     │
     ▼
Vector Database (Chroma)
     │
Relevant Context Retrieved
     │
     ▼
Groq LLM (Llama Model)
     │
     ▼
Final AI Response
```

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

