import requests
from bs4 import BeautifulSoup
import re

def getTopics():
    #url = "https://www.torezista.com/strategy/detail/683/"
    url = "https://www.torezista.com/strategy/detail/42/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    elems = soup.select("#str_detail > div.wrap > div > div > div.main > section > section.u-mb40 > table > tbody > tr:nth-of-type(8) > td.bg-purple")
    print(elems)

    elems = soup.select("#str_detail > div.wrap > div > div > div.main > section > section.u-mb40 > table > tbody > tr:nth-of-type(8) > td.bg-yellow")
    print(elems)

if __name__ == "__main__":
    getTopics()
