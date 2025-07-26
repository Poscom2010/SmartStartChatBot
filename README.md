# SmartStart RAG Chatbot

SmartStart RAG Chatbot is an interactive Streamlit web application that leverages Retrieval-Augmented Generation (RAG) using LangChain and Together AI's LLMs to answer questions about SmartStart. It uses a custom embedding model and vector store for efficient document retrieval.

## Features

- Modern, responsive UI with custom CSS styling
- Logo and favicon branding
- User-friendly question input form
- AI-powered answers using RAG pipeline
- Vectorstore-backed retrieval for relevant context
- Built with Streamlit, LangChain, Together AI, and FAISS

## Directory Structure

```
smartstart-streamlit/
│
├── app.py                  # Main Streamlit app
├── embedding_model.py      # Embedding model setup
├── llm_setup.py            # LLM configuration (Together API)
├── load_vectrostore.py     # Vectorstore loading logic
├── rag_chain.py            # RAG chain setup
├── requirements.text       # (Typo: should be requirements.txt)
├── images/                 # Logo and favicon images
├── smartstart_faiss_index/ # FAISS vectorstore files
└── .env                    # Environment variables (API keys)
```

## Setup Instructions

### 1. Clone the Repository

```sh
git clone <your-repo-url>
cd smartstart-streamlit
```

### 2. Create and Activate a Python Virtual Environment

```sh
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

Make sure you have a correct `requirements.txt` file. If not, rename `requirements.text` to `requirements.txt`.

```sh
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in `smartstart-streamlit/` with your Together API key:

```
TOGETHER_API_KEY=your_together_api_key_here
```

### 5. Prepare Vectorstore

Ensure your FAISS index and related files are present in `smartstart_faiss_index/`. If not, run your data loading and chunking scripts to generate them.

### 6. Run the Application

```sh
streamlit run app.py
```

## Usage

- Open the app in your browser (Streamlit will provide a local URL).
- Enter your question about SmartStart in the input box.
- Submit to receive an AI-generated answer with relevant context.

## File Overview

- [`app.py`](app.py): Main Streamlit UI and app logic.
- [`llm_setup.py`](llm_setup.py): Loads Together AI LLM ([`get_llm`](llm_setup.py)).
- [`embedding_model.py`](embedding_model.py): Loads embedding model ([`get_embedding_model`](embedding_model.py)).
- [`load_vectrostore.py`](load_vectrostore.py): Loads FAISS vectorstore ([`load_vectorstore`](load_vectrostore.py)).
- [`rag_chain.py`](rag_chain.py): Sets up RAG chain ([`get_qa_chain`](rag_chain.py)).

## Customization

- Update images in `images/` for branding.
- Modify CSS in `app.py` for UI changes.
- Adjust retrieval parameters (`search_kwargs={'k': 3}`) for more/less context.

## Troubleshooting

- If you see errors about missing modules, check your `requirements.txt`.
- Ensure `.env` is present and contains a valid API key.
- Make sure vectorstore files exist in `smartstart_faiss_index/`.

## License

MIT License (add your license details here).

## Credits

Built by Poscom using Streamlit, LangChain, Together AI, and FAISS.
