import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []
    for tag in soup.find_all(['h2', 'h3']):
        text = tag.get_text(strip=True)
        if text and len(text) > 20:
            headlines.append(text)


    if headlines:
        with open("headlines.txt", "w", encoding='utf-8') as file:
            for idx, title in enumerate(headlines, start=1):
                file.write(f"{idx}. {title}\n")

        print(f"Saved {len(headlines)} headlines to 'headlines.txt'")
    else:
        print(" No headlines found. The structure might have changed.")
else:
    print(f" Failed to fetch page. Status code: {response.status_code}")
