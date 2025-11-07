import pytest
import os
from unittest.mock import patch, MagicMock
from src.config import load_api_key

@patch('src.config.st')
def test_load_api_key_not_set(mock_st):
    """Test when API key is not set in environment variables."""
    with patch.dict(os.environ, {}, clear=True):
        load_api_key()
        mock_st.error.assert_called_once_with("Please set the OPENAI_API_KEY environment variable.")

@patch('src.config.st')
def test_load_api_key_set(mock_st):
    """Test when API key is set in environment variables."""
    with patch.dict(os.environ, {'OPENAI_API_KEY': 'test-api-key'}):
        load_api_key()
        mock_st.error.assert_not_called()