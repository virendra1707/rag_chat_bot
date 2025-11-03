from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

def create_vector_db(financial_texts):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_texts(financial_texts, embedding=embeddings, persist_directory="./finance_db")
    # print("Vector DB created successfully.....")
    return db
