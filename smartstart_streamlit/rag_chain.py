try:
    # Older/compatible import path
    from langchain.chains import RetrievalQA
except Exception:
    # Newer langchain versions expose RetrievalQA in a submodule
    from langchain.chains.retrieval_qa.base import RetrievalQA

def get_qa_chain(llm, retriever):
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
