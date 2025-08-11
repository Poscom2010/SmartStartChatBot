# SmartStart RAG App Deployment Guide

## Streamlit Cloud Deployment

### 1. Prerequisites
- GitHub repository with your code
- Together AI API key
- Streamlit Cloud account

### 2. Deployment Steps

1. **Push your code to GitHub** with the following structure:
   ```
   Smart-Start-Rag/
   ├── streamlit_app.py          # Main Streamlit app
   ├── requirements.txt          # Python dependencies
   ├── packages.txt             # System dependencies
   ├── .streamlit/
   │   └── config.toml         # Streamlit configuration
   └── smartstart_streamlit/    # Your modules
   ```

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub repository
   - Set the main file path to: `streamlit_app.py`
   - Add your secrets in the app settings:
     - Key: `TOGETHER_API_KEY`
     - Value: Your Together AI API key

### 3. Environment Variables
Make sure to set the following environment variable in Streamlit Cloud:
- `TOGETHER_API_KEY`: Your Together AI API key

### 4. Troubleshooting
If you get dependency errors:
1. Check that all packages in `requirements.txt` are compatible
2. Ensure system dependencies in `packages.txt` are correct
3. Verify the main file path is set to `streamlit_app.py`

### 5. Local Testing
To test locally before deployment:
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

### 6. File Structure for Deployment
- `streamlit_app.py` - Main Streamlit application (entry point)
- `requirements.txt` - Python package dependencies
- `packages.txt` - System-level dependencies
- `.streamlit/config.toml` - Streamlit configuration
- `smartstart_streamlit/` - Your custom modules and data
