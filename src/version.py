# src/version.py
import streamlit as st

VERSION = "v1.0"

def render_version_badge():
    st.markdown(f"<p style='text-align: right; font-size: 0.9em;'>Skynet {VERSION}</p>", unsafe_allow_html=True)