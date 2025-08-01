# 🤖 Skynet PDF Chatbot

A conversational PDF assistant built using LangChain, ChromaDB, OpenAI, and Streamlit.

## 📦 Features
- Upload any PDF and ask questions about its content
- Uses LangChain's retrieval-augmented generation (RAG) flow
- Embeds chunks of the PDF with OpenAI embeddings
- Caches vector store using Chroma for fast retrieval
- Simple chat interface using Streamlit

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/skynet-pdf-chatbot.git
cd skynet-pdf-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set your OpenAI API key
```bash
export OPENAI_API_KEY=your-key-here  # or use .env
```

### 4. Run the app
```bash
streamlit run main.py
```

## 📁 Project Structure
```
skynet-pdf-chatbot/
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
├── data/                # Place your PDFs here
│   └── sample.pdf
├── chroma_db/           # Auto-generated DB
├── src/
│   ├── app.py
│   ├── pdf_utils.py
│   ├── db_utils.py
│   ├── chat_utils.py
│   ├── config.py
│   └── version.py
```

## 📂 Data
Place your PDF files in the `data/` folder manually or upload through the Streamlit UI.

## 📄 License
MIT © 2025 Gautam Naik
