from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

DB_PATH = "db"


def create_vector_db():
    if not os.path.exists("data/sample.txt"):
        return

    loader = TextLoader("data/sample.txt")
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectordb = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=DB_PATH
    )

    vectordb.persist()


def load_vector_db():
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    return Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings
    )


def add_pdf_to_db(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectordb = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embeddings
    )

    vectordb.add_documents(chunks)
    vectordb.persist()