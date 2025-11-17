import requests
from bs4 import BeautifulSoup

url = "https://timesofindia.indiatimes.com/home/headlines"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

# This selects ALL <a> tags inside <li> under <ul>, which TOI uses for headlines
links = soup.select("ul li a")

for a in links:
    text = a.get_text(strip=True)
    if len(text) > 20:   # filter short menu links
        print(text)
