# src/config.py
import os
import streamlit as st

def load_api_key():
    if "OPENAI_API_KEY" not in os.environ:
        st.error("Please set the OPENAI_API_KEY environment variable.")