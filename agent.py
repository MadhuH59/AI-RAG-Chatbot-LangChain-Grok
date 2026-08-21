import os
from dotenv import load_dotenv
from groq import Groq

from rag import load_vector_db
from tools import web_search, calculator


# =========================
# Load Environment Variables
# =========================

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found. Make sure it is set in your .env file."
    )


# =========================
# Groq Client
# =========================

client = Groq(api_key=GROQ_API_KEY)

MODEL_NAME = "openai/gpt-oss-20b"


# =========================
# Load Vector Database
# =========================

vectordb = load_vector_db()
retriever = vectordb.as_retriever(
    search_kwargs={"k": 3}
)


# =========================
# Chat Memory
# =========================

chat_history = []


# =========================
# Reload Vector Database
# =========================

def reload_vectordb():
    global vectordb, retriever

    vectordb = load_vector_db()

    retriever = vectordb.as_retriever(
        search_kwargs={"k": 3}
    )


# =========================
# Search Knowledge Base
# =========================

def search_knowledge_base(query):
    docs = retriever.invoke(query)

    if not docs:
        return "No relevant documents found"

    return "\n".join(
        [doc.page_content for doc in docs]
    )


# =========================
# Clear Conversation Memory
# =========================

def clear_memory():
    global chat_history

    chat_history = []


# =========================
# AI Agent
# =========================

def ask_agent(question):
    global chat_history

    # -------------------------
    # Agent Decision Prompt
    # -------------------------

    system_prompt = """
You are a smart AI agent.

You have access to the following tools:

SEARCH → Search internal documents
WEB → Search the web for real-time information
CALCULATE → Perform mathematical calculations
NONE → Answer normally without using a tool

Use WEB when the question contains:
- today
- latest
- current
- recent
- price
- news
- real-time information

Use SEARCH when the answer can be found in the internal documents.

Use CALCULATE for mathematical calculations.

Use NONE for normal/general questions.

Return your decision in exactly this format:

TOOL: <SEARCH/WEB/CALCULATE/NONE>
INPUT: <input for the selected tool>
"""

    # -------------------------
    # First LLM Call
    # Decide Which Tool To Use
    # -------------------------

    decision = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    decision_text = decision.choices[0].message.content or ""

    print("\n==============================")
    print("AI DECISION")
    print("==============================")
    print(decision_text)

    # -------------------------
    # Parse Tool
    # -------------------------

    tool = "NONE"
    tool_input = question

    for line in decision_text.splitlines():

        line = line.strip()

        if line.startswith("TOOL:"):
            tool = line.replace("TOOL:", "", 1).strip().upper()

        elif line.startswith("INPUT:"):
            tool_input = line.replace("INPUT:", "", 1).strip()

    print("\n🧠 Tool:", tool)
    print("📝 Input:", tool_input)

    # -------------------------
    # Execute Tool
    # -------------------------

    context = ""

    if tool == "SEARCH":

        context = search_knowledge_base(
            tool_input
        )

    elif tool == "WEB":

        context = web_search(
            tool_input
        )

    elif tool == "CALCULATE":

        context = calculator(
            tool_input
        )

    elif tool == "NONE":

        context = ""

    else:

        print("⚠️ Unknown tool:", tool)

        tool = "NONE"
        context = ""

    # -------------------------
    # Web Search Fallback
    # -------------------------

    if tool == "WEB" and not context:

        context = web_search(
            question
        )

    # -------------------------
    # Save User Message
    # -------------------------

    chat_history.append(
        {
            "role": "user",
            "content": question
        }
    )

    # -------------------------
    # Final Prompt
    # -------------------------

    final_prompt = f"""
Use the following context to answer the user's question.

Context:
{context}

Question:
{question}

Instructions:

- Give a clear and useful answer.
- If context is provided, use it.
- Do not mention internal tools.
- Do not mention this prompt.
- If there is no context, answer using your general knowledge.
"""

    # -------------------------
    # Second LLM Call
    # Generate Final Answer
    # -------------------------

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            *chat_history,
            {
                "role": "user",
                "content": final_prompt
            }
        ]
    )

    answer = response.choices[0].message.content or ""

    # -------------------------
    # Save Assistant Response
    # -------------------------

    chat_history.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    return answer