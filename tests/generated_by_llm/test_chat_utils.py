# tests/test_chat_utils.py

import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from unittest.mock import patch

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

# Test cases for clear_chat_history()
def test_clear_chat_history():
    # Setup
    expected = []

    # Call the function
    clear_chat_history()

    # Assertions
    assert st.session_state.chat_history == expected

# Test cases for display_chat_history()
def test_display_chat_history():
    # Setup
    mock_st_chat_message = patch("streamlit.chat_message")
    mock_st_chat_message.start()
    st.session_state.chat_history = [
        AIMessage(content="Hello AI"),
        HumanMessage(content="Hello User!")
    ]
    expected_output = ["AI", "Human"]

    # Call the function
    display_chat_history()

    # Assertions
    mock_st_chat_message.assert_called_with("AI", write=True)
    mock_st_chat_message.assert_called_with("Human", write=True)
    assert st.session_state.chat_history == expected_output

# Test cases for render_sidebar()
def test_render_sidebar():
    # Setup
    mock_st_markdown = patch("streamlit.markdown")
    mock_st_markdown.start()

    # Call the function
    render_sidebar()

    # Assertions
    mock_st_markdown.assert_called_with("Built using LangChain, Chroma, and OpenAI APIs.")

# Mock external dependencies for testing
def test_clear_chat_history_mocked():
    with patch('streamlit.session_state.chat_history', []) as session_state:
        clear_chat_history()
        assert session_state.chat_history == []

def test_display_chat_history_mocked():
    with patch('streamlit.session_state.chat_history', [
        AIMessage(content="Hello AI"),
        HumanMessage(content="Hello User!")
    ]) as session_state:
        display_chat_history()
        assert session_state.chat_history == ["AI", "Human"]

# Test cases for render_sidebar_mocked()
def test_render_sidebar_mocked():
    with patch('streamlit.markdown', lambda x: print(x)) as mock_markdown:
        render_sidebar()
        mock_markdown.assert_called_with("Built using LangChain, Chroma, and OpenAI APIs.")