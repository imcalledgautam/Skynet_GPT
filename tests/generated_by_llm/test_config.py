# src/test_config.py
import os
import streamlit as st
from unittest.mock import patch, MagicMock

def test_load_api_key():
    # Test case: API key is not set in environment variables
    with patch.dict(os.environ, {'OPENAI_API_KEY': ''}):
        assert load_api_key() == "Please set the OPENAI_API_KEY environment variable."

    # Test case: API key is set in environment variables
    os.environ['OPENAI_API_KEY'] = 'your-api-key'
    assert load_api_key() != "Please set the OPENAI_API_KEY environment variable."
1. **Import Statements**: The test file imports necessary modules including `os`, `streamlit`, and `unittest.mock`.