import streamlit as st
from agent import ask_agent
from rag import create_vector_db
import os

st.set_page_config(page_title="Free AI Agent")

st.title("🚀 Free AI Agent (RAG + Groq)")

if "db_ready" not in st.session_state:
    create_vector_db()
    st.session_state.db_ready = True

question = st.text_input("Ask something")

if question:
    answer = ask_agent(question)
    st.write(answer)