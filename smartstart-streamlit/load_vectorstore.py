from langchain_community.vectorstores import FAISS

import os
from langchain_community.vectorstores import FAISS

def load_vectorstore(embeddings):
    base_dir = os.path.dirname(__file__)  # directory of this script
    index_path = os.path.join(base_dir, 'smartstart_faiss_index')
    return FAISS.load_local(
        index_path,
        embeddings=embeddings,
        allow_dangerous_deserialization=True
    )

