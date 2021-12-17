import requests
from bs4 import BeautifulSoup
import re

strData = []

def getStrategy():

    #--- トレジスタのストラテジー一覧を取得する
    url = "https://www.torezista.com/strategy/monthly/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    elems = soup.find_all(href=re.compile("/strategy/detail"), class_="u-td-u")
    strategy_links = [elem.attrs['href'] for elem in elems]
    #print(strategy_links)
    #print(len(strategy_links))

    for strategy_link in strategy_links[:5]:
        strategy = {}
        url = f"https://www.torezista.com{strategy_link}"
        res = requests.get(url)
        res.encoding = res.apparent_encoding
        soup = BeautifulSoup(res.text, "html.parser")

        #ストラテジー名称
        elems = soup.select("#str_detail > div.wrap > h1 > span")
        strategy["name"] = elems[0].contents[0]

        #トレード回数
        elems = soup.select(
            "#str_detail > div.wrap > div > div > div.main > section > section.u-mb40 > table > tbody > tr:nth-of-type(3) > td.bg-purple")
        strategy["cnt_a"] = int(elems[0].contents[0])
        elems = soup.select(
            "#str_detail > div.wrap > div > div > div.main > section > section.u-mb40 > table > tbody > tr:nth-of-type(3) > td.bg-yellow")
        strategy["cnt_b"] = int(elems[0].contents[0])

        #プロフィットファクター
        elems = soup.select(
            "#str_detail > div.wrap > div > div > div.main > section > section.u-mb40 > table > tbody > tr:nth-of-type(8) > td.bg-purple")
        strategy["pf_a"] = float(elems[0].contents[0])
        elems = soup.select(
            "#str_detail > div.wrap > div > div > div.main > section > section.u-mb40 > table > tbody > tr:nth-of-type(8) > td.bg-yellow")
        strategy["pf_b"] = float(elems[0].contents[0])

        #期待値
        elems = soup.select(
            "#str_detail > div.wrap > div > div > div.main > section > section.u-mb40 > table > tbody > tr:nth-of-type(12) > td.bg-purple")
        strategy["kitai_a"] = elems[0].contents[0]
        elems = soup.select(
            "#str_detail > div.wrap > div > div > div.main > section > section.u-mb40 > table > tbody > tr:nth-of-type(12) > td.bg-yellow")
        strategy["kitai_b"] = elems[0].contents[0]


        strData.append(strategy)

if __name__ == "__main__":
    getStrategy()
    print(strData)
    print(len(strData))
