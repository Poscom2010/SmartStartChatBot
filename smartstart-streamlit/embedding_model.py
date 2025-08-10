from langchain.embeddings import HuggingFaceEmbeddings

# Build HuggingFace embedding model
def get_embedding_model():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
