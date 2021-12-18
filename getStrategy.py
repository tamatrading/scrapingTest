import requests
from bs4 import BeautifulSoup
import re
import csv

strData = []
strData2 = []
strIndex = ["名称","回数(前)","回数(後)","PF(前)","PF(後)","期待値(前)","期待値(後)"]
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
        strategy = {}
        strategy2 = []
        url = f"https://www.torezista.com{strategy_link}"
        res = requests.get(url)
        res.encoding = res.apparent_encoding
        soup = BeautifulSoup(res.text, "html.parser")

        #ストラテジー名称
        elems = soup.select("#str_detail > div.wrap > h1 > span")
        strategy["name"] = elems[0].contents[0]
        strategy2.append(elems[0].contents[0])

        #トレード回数
        elems = soup.select(
            "#str_detail > div.wrap > div > div > div.main > section > section.u-mb40 > table > tbody > tr:nth-of-type(3) > td.bg-purple")
        strategy["cnt_a"] = int(elems[0].contents[0])
        strategy2.append(int(elems[0].contents[0]))

        elems = soup.select(
            "#str_detail > div.wrap > div > div > div.main > section > section.u-mb40 > table > tbody > tr:nth-of-type(3) > td.bg-yellow")
        strategy["cnt_b"] = int(elems[0].contents[0])
        strategy2.append(int(elems[0].contents[0]))

        #プロフィットファクター
        elems = soup.select(
            "#str_detail > div.wrap > div > div > div.main > section > section.u-mb40 > table > tbody > tr:nth-of-type(8) > td.bg-purple")
        strategy["pf_a"] = float(elems[0].contents[0])
        strategy2.append(float(elems[0].contents[0]))

        elems = soup.select(
            "#str_detail > div.wrap > div > div > div.main > section > section.u-mb40 > table > tbody > tr:nth-of-type(8) > td.bg-yellow")
        strategy["pf_b"] = float(elems[0].contents[0])
        strategy2.append(float(elems[0].contents[0]))

        #期待値
        elems = soup.select(
            "#str_detail > div.wrap > div > div > div.main > section > section.u-mb40 > table > tbody > tr:nth-of-type(12) > td.bg-purple")
        strategy["kitai_a"] = elems[0].contents[0]
        strategy2.append(changeStrToInt(elems[0].contents[0],"円"))

        elems = soup.select(
            "#str_detail > div.wrap > div > div > div.main > section > section.u-mb40 > table > tbody > tr:nth-of-type(12) > td.bg-yellow")
        strategy["kitai_b"] = elems[0].contents[0]
        strategy2.append(changeStrToInt(elems[0].contents[0],"円"))


        strData.append(strategy)
        strData2.append(strategy2)

def changeStrToInt(sstr, ddel):
    ss = sstr.replace(ddel,"")
    ss = ss.replace(",","")
    return int(ss)

if __name__ == "__main__":
    getStrategy()
    print(strData2)
    print(len(strData2))

    with open('test.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(strIndex)
        writer.writerows(strData2)
