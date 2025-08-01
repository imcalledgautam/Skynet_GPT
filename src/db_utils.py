# src/db_utils.py
from langchain_community.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
import os

def create_or_load_vectorstore(chunks):
    persist_dir = "chroma_db"
    if os.path.exists(persist_dir) and os.listdir(persist_dir):
        return Chroma(persist_directory=persist_dir, embedding_function=OpenAIEmbeddings())
    return Chroma.from_documents(documents=chunks, embedding=OpenAIEmbeddings(), persist_directory=persist_dir)
