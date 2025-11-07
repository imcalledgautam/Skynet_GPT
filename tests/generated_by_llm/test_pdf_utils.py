# src/test_pdf_utils.py
import pytest
from tempfile import NamedTemporaryFile
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

@pytest.fixture
def sample_pdf():
    with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(b"This is a test PDF file.\n")
        yield tmp_file.name
        os.remove(tmp_file.name)

def process_pdf(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        return tmp_file.name

def load_and_split(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(documents)

# Test process_pdf function
def test_process_pdf():
    sample_pdf_content = b"This is a test PDF file.\n"
    with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(sample_pdf_content)
        uploaded_file = open(tmp_file.name, "rb")
        assert process_pdf(uploaded_file) == tmp_file.name

# Test load_and_split function
def test_load_and_split():
    sample_pdf_content = b"This is a test PDF file.\n"
    with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(sample_pdf_content)
        uploaded_file = open(tmp_file.name, "rb")
        documents = load_and_split(uploaded_file)
        assert len(documents) == 1

# Test error handling
def test_process_pdf_error():
    with pytest.raises(Exception):
        process_pdf(None)

def test_load_and_split_error():
    with pytest.raises(IOError):
        load_and_split("nonexistent.pdf")

# Edge case: empty PDF
sample_empty_pdf_content = b""
with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
    tmp_file.write(sample_empty_pdf_content)
    uploaded_file = open(tmp_file.name, "rb")
    with pytest.raises(Exception):
        process_pdf(uploaded_file)

def test_load_and_split_edge_case():
    sample_empty_pdf_content = b""
    with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(sample_empty_pdf_content)
        uploaded_file = open(tmp_file.name, "rb")
        documents = load_and_split(uploaded_file)
        assert len(documents) == 1

# Test with no PDF file
with pytest.raises(Exception):
    process_pdf(b"not_a_pdf_file")

def test_load_and_split_no_pdf():
    with pytest.raises(IOError):
        load_and_split("nonexistent.pdf")