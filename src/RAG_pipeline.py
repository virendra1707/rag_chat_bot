from langchain_groq import ChatGroq
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

def create_rag_pipeline(groq_api_key):
    llm = ChatGroq(model="llama-3.1-8b-instant", api_key=groq_api_key)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory="./finance_db", embedding_function=embeddings)
    retriever = db.as_retriever(search_kwargs={"k": 3})

    prompt = ChatPromptTemplate.from_template("""
    You are a financial expert. Use only the following context to answer user queries.
    If the query is unrelated to finance, politely say:
    "Sorry, I can only answer questions related to finance."

    Context:
    {context}

    Question:
    {question}
    """)

    def retrieve_docs(inputs):
        query = inputs["question"]
        docs = retriever.invoke(query)
        return {"context": "\n\n".join([d.page_content for d in docs]), "question": query}

    rag_pipeline = (
        RunnablePassthrough.assign(**{"question": lambda x: x["question"]})
        | retrieve_docs
        | prompt
        | llm
        | StrOutputParser()
    )

    # print("RAG pipeline created successfully.....")
    return rag_pipeline
