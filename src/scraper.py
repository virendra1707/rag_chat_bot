import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, "html.parser")

    elements = soup.find_all(['p', 'div', 'span'])
    paragraphs = [el.get_text(strip=True) for el in elements if len(el.get_text(strip=True)) > 50]
    print(f"Total paragraphs scraped: {len(paragraphs)}")
    return paragraphs


def is_financial(text):
    keywords = ["stock", "finance", "investment", "revenue", "profit", "loss", "bank", "economy", "market"]
    return any(word in text.lower() for word in keywords)


def filter_financial_texts(texts):
    filtered = [t for t in texts if is_financial(t)]
    print(f"Financial paragraphs found: {len(filtered)} / {len(texts)}")
    return filtered
