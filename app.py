import os
import streamlit as st
from src.scraper import scrape_website, filter_financial_texts
from src.vector_db import create_vector_db
from src.RAG_pipeline import create_rag_pipeline
from src.utils import ask_bot

#Streamlit Page Configuration......
st.set_page_config(page_title="Financial RAG Chatbot", layout="centered")
st.title("Financial RAG Chatbot")

#API Key.....
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    st.error("Please set your GROQ_API_KEY in environment variables.")
    st.stop()

#Sidebar...
st.sidebar.header("Web Scraper")
url = st.sidebar.text_input("Enter financial website URL:", "https://www.investopedia.com/terms/s/stock.asp")

if st.sidebar.button("Scrape & Build Knowledge Base"):
    with st.spinner("Scraping and processing data..."):
        texts = scrape_website(url)
        financial_texts = filter_financial_texts(texts)
        db = create_vector_db(financial_texts)
    st.sidebar.success("Knowledge base created successfully......")

#.....Create RAG pipeoline.......
qa = create_rag_pipeline(groq_api_key)

#......Chat Interface.....
query = st.text_input("Ask me anything about finance related queries:")
if st.button("Ask"):
    if query.strip():
        with st.spinner("Thinking....."):
            answer = ask_bot(qa, query)
        st.success("Answer:")
        st.write(answer)
