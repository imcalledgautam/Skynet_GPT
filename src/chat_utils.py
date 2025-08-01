# src/chat_utils.py
import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

def clear_chat_history():
    st.session_state.chat_history = []

def display_chat_history():
    for msg in st.session_state.chat_history:
        if isinstance(msg, AIMessage):
            st.chat_message("AI").write(msg.content)
        elif isinstance(msg, HumanMessage):
            st.chat_message("Human").write(msg.content)

def render_sidebar():
    with st.sidebar:
        st.markdown("Built using LangChain, Chroma, and OpenAI APIs.")