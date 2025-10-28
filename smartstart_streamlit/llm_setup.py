from langchain_together import Together
import os
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    api_key = os.getenv("TOGETHER_API_KEY")
    return Together(
        model="mistralai/Mistral-7B-Instruct-v0.1",
        temperature=0.20,
        max_tokens=150,
        together_api_key=api_key
    )
