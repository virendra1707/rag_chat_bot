def ask_bot(qa, query):
    non_financial_keywords = [
        "cricket", "movie", "food", "sports", "weather", "music", 
        "politics", "history", "geography", "travel", "health", 
        "fitness", "entertainment", "gaming"
    ]

    if any(k in query.lower() for k in non_financial_keywords):
        return "Sorry, I can only answer finance related questions.Please ask a finance related question."

    response = qa.invoke({"question": query})
    return response
