#  Financial RAG Chatbot

This project is a **Finance-focused Retrieval-Augmented Generation (RAG) chatbot** built using **LangChain**, **Groq LLM**, and **Chroma vector store**.  
It scrapes financial content from websites (like Investopedia), stores it in a local vector database, and answers user queries using contextual retrieval and LLM responses.

---

## Features
- Scrapes and filters only **finance-related** content from the web  
- Creates and persists embeddings using **HuggingFace MiniLM**  
- Uses **Groq’s Llama-3.1-8B-Instant** model for responses  
- **Retrieval-Augmented Generation (RAG)** pipeline for accurate answers  
- Streamlit-based user interface for interactive chatting  
- Jupyter notebook (`experiments.ipynb`) for direct testing and experimentation  

---

---

##  Setup Instructions

### Clone the repository
```bash
git clone https://github.com/<link>/Financial_RAG_Chatbot.git
cd Financial_RAG_Chatbot

##  create and activate virtual env
python -m venv venv
venv\Scripts\activate


## install dependencies
pip install -r requirements.txt

##Run the project
streamlit run app.py

##Sample questions
"What is a stock?"
"Explain the difference between stock and bond."
"How to achieve financial freedom"




