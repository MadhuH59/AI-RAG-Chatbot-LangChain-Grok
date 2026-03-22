import os
from groq import Groq
from rag import load_vector_db
from tools import web_search, calculator

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not set")

client = Groq(api_key=GROQ_API_KEY)

vectordb = load_vector_db()
retriever = vectordb.as_retriever(search_kwargs={"k": 3})

chat_history = []


def reload_vectordb():
    global vectordb, retriever
    vectordb = load_vector_db()
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})


def search_knowledge_base(query):
    docs = retriever.invoke(query)
    return "\n".join([d.page_content for d in docs]) or "No relevant documents found"


def clear_memory():
    global chat_history
    chat_history = []

def ask_agent(question):
    global chat_history

    system_prompt = """
You are a smart AI agent.

TOOLS:
SEARCH → internal documents
WEB → real-time info
CALCULATE → math
NONE → general

If question has: today/latest/price → use WEB

Return:
TOOL: <...>
INPUT: <...>
"""

    decision = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
    )

    decision_text = decision.choices[0].message.content

    tool = "NONE"
    tool_input = question

    if "TOOL:" in decision_text:
        for line in decision_text.split("\n"):
            if "TOOL:" in line:
                tool = line.split("TOOL:")[-1].strip()

    if "INPUT:" in decision_text:
        tool_input = decision_text.split("INPUT:")[-1].strip()

    print(f"\n🧠 Tool: {tool} | Input: {tool_input}")

    context = ""

    if tool == "SEARCH":
        context = search_knowledge_base(tool_input)

    elif tool == "WEB":
        context = web_search(tool_input)

    elif tool == "CALCULATE":
        context = calculator(tool_input)

    # fallback
    if tool == "WEB" and not context:
        context = web_search(question)

    chat_history.append({"role": "user", "content": question})

    final_prompt = f"""
Use this context:

{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=chat_history + [{"role": "user", "content": final_prompt}],
    )

    answer = response.choices[0].message.content

    chat_history.append({"role": "assistant", "content": answer})

    return answer