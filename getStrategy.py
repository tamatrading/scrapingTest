import requests
from bs4 import BeautifulSoup
import re

def getStrategy():

    #--- トレジスタのストラテジー一覧を取得する
    url = "https://www.torezista.com/strategy/monthly/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    elems = soup.find_all(href=re.compile("/strategy/detail"), class_="u-td-u")
    strategy_links = [elem.attrs['href'] for elem in elems]
    #print(strategy_links)
    #print(len(strategy_links))

    for strategy_link in strategy_links:
        url = f"https://www.torezista.com{strategy_link}"
        res = requests.get(url)
        res.encoding = res.apparent_encoding
        soup = BeautifulSoup(res.text, "html.parser")
        elems = soup.find_all("tr")
        for elem in elems:
            if elem.text = "プロフィットファクター":
                pfs.

        print(elems)

if __name__ == "__main__":
    getStrategy()
