try:
    # Older/compatible import path
    from langchain.chains import RetrievalQA
except Exception:
    # Newer langchain versions expose RetrievalQA in a submodule
    from langchain.chains.retrieval_qa.base import RetrievalQA

from langchain.prompts import PromptTemplate

def get_qa_chain(llm, retriever):
    # Custom prompt template to control output format
    prompt_template = """Use the context below to answer the question in ONE SHORT SENTENCE ONLY.

Context: {context}

Question: {question}

Provide ONLY a direct answer. No explanations, no quotes, no extra information.
Answer:"""

    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )
