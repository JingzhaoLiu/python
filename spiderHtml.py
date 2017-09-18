# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time

def creatHtml(webUrl, artName):
    url = 'https://germey.gitbooks.io/python3webspider/content/' + webUrl
    print(url)
    print(artName)
    r = requests.get(url)
    with open(artName, 'wb') as f:
        f.write(r.content)

    print(artName + ' writed ' + ' end')

def getHtml(url):

    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html)
    # print(soup.a)

    # for link in soup.select(' section > ul > li > a '):
    for link in soup.select('.markdown-section a'):
        webUrl = link.get('href')
        artName = webUrl.split('/')[-1]
        time.sleep(10)
        if webUrl !='./':
            creatHtml(webUrl, artName)


if __name__=='__main__':

    url = 'https://germey.gitbooks.io/python3webspider/content/0-%E7%9B%AE%E5%BD%95.html'
    getHtml(url)



# import requests


# def getHtml(url):
#     r = requests.get(url)
#     filename = url.split('/')[-1]
#     creatHtml(filename,r)

# def creatHtml(filename,r):
#     with open(filename,'w') as f:
#         f.write(r.content)




# if __name__ = '__main__':
#     url = ''
#     getHtml(url)