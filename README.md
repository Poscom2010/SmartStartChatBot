# SmartStart RAG Chatbot

A powerful RAG (Retrieval-Augmented Generation) chatbot built with Streamlit and LangChain that answers questions about SmartStart using AI.

## 🚀 Quick Deploy on Streamlit

**Deploy this app in 3 simple steps:**

1. **Fork/Clone this repository**
2. **Connect to [Streamlit Cloud](https://streamlit.io/cloud)**
3. **Set main file path to: `streamlit_main.py`**

## 🔧 Setup Requirements

### Environment Variables
You need to set your `TOGETHER_API_KEY` in Streamlit secrets:

1. Go to your Streamlit app settings
2. Add this to your secrets:
```toml
TOGETHER_API_KEY = "your_together_api_key_here"
```

### Dependencies
The app automatically installs all required packages from `requirements.txt`.

## 🏗️ Project Structure

```
Smart-Start-Rag/
├── main.py                    # 🎯 Main Streamlit app (entry point)
├── requirements.txt           # 📦 Dependencies for Streamlit
├── smartstart-streamlit/      # 📁 Core package
│   ├── __init__.py           # 🐍 Python package init
│   ├── app.py                # 🔧 Alternative app entry
│   ├── rag_chain.py          # ⚡ RAG chain logic
│   ├── llm_setup.py          # 🤖 LLM configuration
│   ├── embedding_model.py    # 🧠 Embedding model
│   ├── load_vectrostore.py   # 💾 Vector store loader
│   ├── smartstart_faiss_index/ # 🔍 FAISS index files
│   ├── images/               # 🖼️ UI assets
│   └── animations/           # ✨ Lottie animations
├── .streamlit/               # ⚙️ Streamlit config
└── .gitignore               # 🚫 Git ignore rules
```

## 🎯 Key Features

- 🤖 **AI-Powered Q&A**: Uses Together AI's Mistral-7B model
- 📚 **RAG Technology**: Retrieves relevant context from SmartStart knowledge base
- 🎨 **Beautiful UI**: Black theme with animations and modern design
- 🔍 **Vector Search**: FAISS-based similarity search
- 💬 **Interactive Chat**: Real-time question answering

## 🛠️ Local Development

```bash
# Clone the repository
git clone <your-repo-url>
cd Smart-Start-Rag

# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run main.py
```


- **Streamlit Secrets**: Add your API key in Streamlit Cloud settings

## 📝 Notes

- The FAISS index files (`index.faiss` and `index.pkl`) are pre-built and included
- The app uses sentence-transformers for embeddings
- All dependencies are optimized for Streamlit deployment

## 🚨 Troubleshooting

If you get deployment errors:
1. Check that `streamlit_main.py` is set as the main file in Streamlit
2. Verify your `TOGETHER_API_KEY` is set in Streamlit secrets
3. Ensure all files are properly committed to GitHub

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Built with ❤️ by Poscom using Streamlit and LangChain
