from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from ..models.llm import get_llm
from ..utils.vector_store import get_vector_store

prompt_template = """
As an internal support assistant, answer using ONLY the context below.
If unsure, say "I don't have that information."

Context: {context}

Question: {question}

Answer concisely and markdown-friendly:
"""

def get_qa_chain():
    llm = get_llm()
    vector_store = get_vector_store()
    
    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )
    
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_store.as_retriever(),
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )

async def handle_query(question: str):
    qa_chain = get_qa_chain()
    result = qa_chain({"query": question})
    
    return {
        "answer": result["result"],
        "sources": [doc.metadata.get("source", "") for doc in result["source_documents"]]
    }
