# src/db_utils_test.py
import os
from langchain_community.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
import pytest
from unittest.mock import patch, MagicMock

@pytest.fixture
def chunks():
    return [{"text": "This is a sample document."}]

@pytest.fixture
def openai_embeddings():
    return MagicMock()

@pytest.fixture
def chroma_db(persist_dir):
    if os.path.exists(persist_dir) and os.listdir(persist_dir):
        return Chroma(persist_directory=persist_dir, embedding_function=OpenAIEmbeddings())
    return None

def test_create_or_load_vectorstore_with_existing_db(chroma_db, openai_embeddings, chunks):
    assert isinstance(create_or_load_vectorstore(chunks), Chroma)
    assert chroma_db is not None
    assert openai_embeddings is not None

def test_create_or_load_vectorstore_without_existing_db(chromadb, openai_embeddings, chunks):
    with patch('os.path.exists') as mock_exists:
        mock_exists.return_value = False
        assert isinstance(create_or_load_vectorstore(chunks), Chroma)
        mock_exists.assert_called_once_with("chroma_db")

def test_create_or_load_vectorstore_with_no_chunks():
    with pytest.raises(ValueError) as e:
        create_or_load_vectorstore([])
    assert str(e.value) == "chunks cannot be empty"

def test_create_or_load_vectorstore_with_invalid_chunk():
    with pytest.raises(ValueError) as e:
        create_or_load_vectorstore([{"text": "This is a sample document."}, {"text": 123}])
    assert str(e.value) == "chunks must be a list of dictionaries"

def test_create_or_load_vectorstore_with_missing_embeddings():
    with pytest.raises(ValueError) as e:
        create_or_load_vectorstore(chunks, embedding=OpenAIEmbeddings())
    assert str(e.value) == "embedding function cannot be None"