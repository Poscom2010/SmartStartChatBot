from langchain.vectorstores import FAISS

def load_vectorstore(embeddings):
    return FAISS.load_local(
        'smartstart_faiss_index',
        embeddings=embeddings,
        allow_dangerous_deserialization=True
    )
