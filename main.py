"""
SmartStart RAG Chatbot - Main Entry Point
This file serves as the main entry point for Streamlit deployment.
"""

import streamlit as st
from smartstart_streamlit.rag_chain import get_qa_chain
from smartstart_streamlit.llm_setup import get_llm
from smartstart_streamlit.load_vectrostore import load_vectorstore
from smartstart_streamlit.embedding_model import get_embedding_model
import time
from PIL import Image
import base64
from io import BytesIO
from streamlit_lottie  import st_lottie, st_lottie_spinner
import json

# --- Page Configuration ---
favicon = Image.open("smartstart_streamlit/images/icon.png")
st.set_page_config(
    page_title="SmartStart ChatBot",
    layout="wide",
    page_icon=favicon
)


# --- Custom CSS Styling (Black background) ---
st.markdown("""
    <style>
        /* Full page background color */
        .stApp {
            background-color: black; 
        }

        /* Optional: make all default text white for readability */
        * {
            color: white;
        }

        .block-container {
            padding-top: 1rem !important;
            max-width: none !important;
            margin: 0 auto !important;
        }

        MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        .main-title {
            font-size: 36px;
            font-weight: 700;
            color: white;
            text-align: center;
            margin-bottom: 10px;
        }

        .subtitle {
            font-size: 18px;
            color: #ccc;
            text-align: center;
            margin-bottom: 30px;
        }

        .input-label {
            font-size: 18px;
            font-weight: 600;
            color: white; /* Changed from black to white for visibility */
            margin-bottom: 10px;
        }

        .stTextInput > div > div > input {
            border-radius: 10px;
            border: 2px solid #e0e0e0;
            padding: 12px 15px;
            font-size: 16px;
            color: black;
        }

        .answer-box {
            background-color: #222;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            font-size: 16px;
            color: white;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
            border-left: 4px solid #00aaff;
            width: 100%;
            box-sizing: border-box;
        }

        .answer-container {
            width: 100%;
            max-width: 900px;
            margin: 0 auto;
        }

        .custom-footer {
            text-align: center;
            margin-top: 80px;
            color: #aaa;
            font-size: 14px;
        }

        /* Force both normal and form submit buttons text to white */
        .stButton > button, div[data-testid="stFormSubmitButton"] > button {
            background-color: #00aaff !important; /* bright blue */
            color: white !important;              /* white text */
            border: none !important;
            border-radius: 8px !important;
            padding: 10px 20px !important;
            font-size: 16px !important;
            font-weight: 600 !important;
            cursor: pointer !important;
        }

        /* Hover effect */
        .stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover {
            background-color: #0088cc !important; /* darker blue on hover */
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- Load logo as Base64 ---
logo = Image.open("smartstart_streamlit/images/logo-purple.png")
buffered = BytesIO()
logo.save(buffered, format="PNG")
logo_base64 = base64.b64encode(buffered.getvalue()).decode()


#Load a lottie animation from local file
with open("smartstart_streamlit/animations/animation.json", "r", encoding= "utf-8") as f:
    lottie_animation = json.load(f) 



# --- Header with two columns ---
col1, col2, col3 = st.columns([4, 4,16])
with col1:    
        st_lottie(
            lottie_animation,
            speed=1,
            width=250,      # smaller width
            height=250,     # smaller height
            key="sidebar_animation",
            loop=True,
            quality="high",
        )

with col2:
    st.markdown(
        f"""
        <div style="background-color: #000; padding: 10px; display: inline-block; border-radius: 8px;">
            <img src="data:image/png;base64,{logo_base64}" style="width: 100%; height: auto;"/>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown('<div class="main-title">🤖 SmartStart RAG Chatbot</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Ask any question about SmartStart and get AI-powered answers instantly.</div>', unsafe_allow_html=True)

# --- Input Section ---
st.markdown('<div class="input-label">Your Question:</div>', unsafe_allow_html=True)
with st.form(key="query_form", clear_on_submit=True):
    query = st.text_input("Question", placeholder="e.g. Ask me anything about SmartStart?", key="user_query", label_visibility="collapsed")
    submitted = st.form_submit_button("Submit")

# --- Load Models and Vectorstore ---
embeddings = get_embedding_model()
llm = get_llm()
vectorstore = load_vectorstore(embeddings)
retriever = vectorstore.as_retriever(search_kwargs={'k': 3})
qa_chain = get_qa_chain(llm, retriever)

# --- Output ---
if submitted and query.strip() != "":
    with st.spinner("🤖 Thinking..."):
        time.sleep(1.5)
        result = qa_chain(query)
        answer = result["result"]

    st.markdown(
        f'<div class="answer-container"><div class="answer-box">✅ <strong>Answer:</strong><br>{answer}</div></div>', 
        unsafe_allow_html=True
    )

# --- Footer ---
st.markdown("""
    <div class="custom-footer">
        &copy; 2025 SmartStart | Built by Poscom with ❤️ using Streamlit, LangChain 
    </div>
""", unsafe_allow_html=True)
