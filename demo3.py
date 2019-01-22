from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

def getInternalLinks(soup, includerUrl):
    internalLinks = []
    for link in soup.find_all("a", href=re.compile('^(\/|.*' + includerUrl + ')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

def getExternalLinks(soup, excluderUrl):
    exinternalLinks = []
    for link in soup.find_all('a', href=re.compile('^(https|http|www)((?!' + excluderUrl + ').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in exinternalLinks:
                exinternalLinks.append(link.attrs['href'])
    return exinternalLinks

def splitAddress(address):
    addressParts = address.replace('http://', '').split('/')
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    soup = BeautifulSoup(html, 'lxml')
    externalLinks = getExternalLinks(soup, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        return getNextExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingPage):
    externalLinks = getRandomExternalLink('http://oreilly.com')
    print('随机外链是:' + externalLinks)
    followExternalOnly(externalLinks)

followExternalOnly('http://oreilly.com')