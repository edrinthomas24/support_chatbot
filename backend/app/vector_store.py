from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from ..config import settings

embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

def get_vector_store():
    if os.path.exists(settings.VECTOR_STORE_PATH):
        return FAISS.load_local(settings.VECTOR_STORE_PATH, embeddings)
    return FAISS.from_texts([""], embeddings)

async def add_document_to_store(file_path: str):
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    else:
        loader = TextLoader(file_path)
    
    documents = loader.load_and_split(text_splitter)
    vector_store = get_vector_store()
    vector_store.add_documents(documents)
    vector_store.save_local(settings.VECTOR_STORE_PATH)
    return [doc.metadata.get("source") for doc in documents]
