# 🚀 Streamlit Deployment Checklist

## Before Deployment

### ✅ Code Files
- [ ] `streamlit_app.py` exists and is the main entry point
- [ ] All custom modules are in `smartstart_streamlit/` folder
- [ ] Vector store files are in `smartstart_streamlit/smartstart_faiss_index/`

### ✅ Configuration Files
- [ ] `.streamlit/config.toml` exists in root directory
- [ ] `requirements.txt` has compatible package versions
- [ ] `packages.txt` specifies system dependencies

### ✅ Dependencies
- [ ] All imports in `streamlit_app.py` are available
- [ ] No version conflicts in requirements.txt
- [ ] PyTorch version is compatible (>=2.5.0)

## Deployment Steps

### 1. GitHub Setup
- [ ] Push all code to GitHub repository
- [ ] Ensure repository is public (for free Streamlit Cloud)
- [ ] Verify file structure matches deployment requirements

### 2. Streamlit Cloud Setup
- [ ] Go to [share.streamlit.io](https://share.streamlit.io)
- [ ] Connect GitHub repository
- [ ] Set main file path to: `streamlit_app.py`
- [ ] Add secret: `TOGETHER_API_KEY` with your API key

### 3. Environment Configuration
- [ ] Set Python version to 3.9+ (recommended: 3.11)
- [ ] Ensure all environment variables are set
- [ ] Check that API key is properly configured

## Troubleshooting Common Issues

### ❌ "installer returned a non-zero exit code"
- Check requirements.txt for incompatible versions
- Verify all packages are available for your Python version
- Remove version pins if needed (use >= instead of ==)

### ❌ "No module named X"
- Ensure all required packages are in requirements.txt
- Check for typos in import statements
- Verify package names match exactly

### ❌ "Environment variable not set"
- Add TOGETHER_API_KEY to Streamlit Cloud secrets
- Check secrets configuration in app settings
- Verify environment variable name matches code

## Local Testing

Before deploying, test locally:
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## File Structure for Deployment
```
Smart-Start-Rag/
├── streamlit_app.py              # ← Main entry point
├── requirements.txt              # Python dependencies
├── packages.txt                  # System dependencies
├── .streamlit/
│   ├── config.toml             # Streamlit config
│   └── secrets.toml            # Local API key (optional)
├── smartstart_streamlit/        # Custom modules
│   ├── __init__.py
│   ├── rag_chain.py
│   ├── llm_setup.py
│   ├── load_vectrostore.py
│   ├── embedding_model.py
│   ├── images/
│   ├── animations/
│   └── smartstart_faiss_index/
└── README.md
```
