#记得自己ctrl+C 停止，不然一直循环下去。
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    soup = BeautifulSoup(html)
    try:
        print(soup.h1.get_text())
        print(soup.find(id="mw-content-text").find_all('p')[0])
        print(soup.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print(u'页面缺少一些属性！不过不用担心！')

    for link in soup.find_all("a", href=re.compile("^(\/wiki\/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('-----------------\n' + newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")