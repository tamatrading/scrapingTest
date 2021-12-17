import requests
from bs4 import BeautifulSoup
import re

def getYahooTopics():
    url = "https://www.yahoo.co.jp/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
    pickup_links = [elem.attrs['href'] for elem in elems]
    print(pickup_links)

if __name__ == "__main__":
    getYahooTopics()
