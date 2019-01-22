from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now()) #根据时间生成随机数生成器的种子
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    soup = BeautifulSoup(html)
    return soup.find("div", {"id": "bodyContent"}).find_all("a", href=re.compile("^(\/wiki\/)((?!:).)*$"))
link = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].atrrs['href']
    print(newArticle)
    links = getLinks(newArticle)
