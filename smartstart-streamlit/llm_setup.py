from langchain.llms import Together
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")

def get_llm():
    return Together(
        model="mistralai/Mistral-7B-Instruct-v0.1",
        temperature=0.20,
        max_tokens=150
    )
