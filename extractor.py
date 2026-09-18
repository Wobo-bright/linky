import requests
from bs4 import BeautifulSoup

def extract_content(url: str) -> dict:
    response = requests.get(
        url,
        timeout=10,
        headers= {"User-Agent": "Mozilla/5.0"}
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.get_text(strip=True) if soup.title else ""

    paragraphs = soup.find_all("p")

    content = " ".join(
        paragraph.get_text(" ", strip=True)
        for paragraph in paragraphs
    )

    return {
        "title" : title,
        "content" : content[:3000]
    }