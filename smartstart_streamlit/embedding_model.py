from langchain_community.embeddings import HuggingFaceEmbeddings

# Build HuggingFace embedding model
def get_embedding_model():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}
    )
