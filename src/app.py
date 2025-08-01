# src/app.py
from src.pdf_utils import load_and_split, process_pdf
from src.db_utils import create_or_load_vectorstore
from src.chat_utils import clear_chat_history, render_sidebar, display_chat_history
from src.config import load_api_key
from src.version.py import VERSION, render_version_badge

import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

class App:
    def __init__(self):
        st.set_page_config("Skynet PDF Chatbot", layout="wide")
        load_api_key()
        render_version_badge()
        st.title("🤖 Skynet PDF Chatbot")

        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

        if uploaded_file is not None:
            file_path = process_pdf(uploaded_file)
            chunks = load_and_split(file_path)
            vectorstore = create_or_load_vectorstore(chunks)

            llm = ChatOpenAI()
            qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

            query = st.chat_input("Ask something about the PDF...")
            if query:
                response = qa_chain.run(query)
                st.session_state.chat_history.append(HumanMessage(content=query))
                st.session_state.chat_history.append(AIMessage(content=response))

            if st.button("Clear chat history"):
                clear_chat_history()

            display_chat_history()
            render_sidebar()