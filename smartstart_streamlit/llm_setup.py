from langchain_together import Together
import os
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    return Together(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        temperature=0.0,
        max_tokens=50,
        together_api_key=os.getenv("TOGETHER_API_KEY")
    )
