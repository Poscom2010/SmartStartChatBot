# SmartStart RAG Chatbot

A Streamlit-based RAG (Retrieval-Augmented Generation) chatbot that answers questions about SmartStart using AI.

## Features

- 🤖 AI-powered question answering
- 📚 RAG-based knowledge retrieval
- 🎨 Beautiful black-themed UI with animations
- 🔍 Vector search using FAISS
- 💬 Interactive chat interface

## Deployment on Streamlit

1. **Fork/Clone this repository**
2. **Set up environment variables:**
   - Create a `.env` file with your `TOGETHER_API_KEY`
   - Or set it in Streamlit's secrets management

3. **Deploy to Streamlit Cloud:**
   - Connect your GitHub repository
   - Set the main file path to: `smartstart-streamlit/app.py`
   - Add your `TOGETHER_API_KEY` to Streamlit secrets

## Dependencies

The app uses only essential dependencies:
- `streamlit` - Web framework
- `langchain` - RAG framework
- `faiss-cpu` - Vector database
- `sentence-transformers` - Embeddings
- `together` - LLM provider
- `streamlit-lottie` - Animations
- `Pillow` - Image processing

## Local Development

```bash
cd smartstart-streamlit
pip install -r requirements.txt
streamlit run app.py
```

## Note

Make sure your `smartstart_faiss_index` folder contains the pre-built FAISS index files (`index.faiss` and `index.pkl`) for the RAG functionality to work.
