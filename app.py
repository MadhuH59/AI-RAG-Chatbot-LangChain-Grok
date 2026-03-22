import streamlit as st
import os
from agent import ask_agent, reload_vectordb, clear_memory
from rag import create_vector_db, add_pdf_to_db

st.set_page_config(page_title="Free AI Agent", layout="wide")

st.title("🚀 AI Agent (RAG + Web + PDF + Memory)")

# --- Init DB ---
if "db_ready" not in st.session_state:
    create_vector_db()
    st.session_state.db_ready = True

# --- Chat Memory for UI ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Upload Folder ---
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# --- Sidebar ---
with st.sidebar:
    st.header("📂 Upload PDF")

    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if uploaded_file:
        file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        add_pdf_to_db(file_path)
        reload_vectordb()

        st.success(f"✅ Uploaded & Indexed: {uploaded_file.name}")

    st.divider()

    # --- Clear Chat ---
    if st.button("🧹 Clear Chat"):
        clear_memory()
        st.session_state.messages = []
        st.success("Chat cleared!")

# --- Display Chat ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# --- Chat Input ---
user_input = st.chat_input("Ask something...")

if user_input:
    # show user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # get response
    response = ask_agent(user_input)

    # show assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.write(response)