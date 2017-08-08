#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup 
from urllib import request
from buildhtml import createHtml

# artUrl = 'http://www.cnblogs.com/alex3714/articles/5885096.html'

# createHtml(artUrl,'articles.html')

soup = BeautifulSoup(open('articles.html'))

for link in soup.select(' p '):
    print(link.string)
    # 注意区别
    # print(link.get_text())
    
for link in soup.select(' p > a '):
    # print(link.string)
    # print(link.get_text())
    # print(link.get('href'))
    
    webUrl  = link.get('href')
    artName = 'articles_'+link.get_text()+'_'+webUrl.split ('/')[-1]
    
    createHtml(webUrl,artName)

    
    # webUrl  = link.get('href')
    # artName = webUrl.split ('/')[-1]

    # with request.urlopen(webUrl) as f:
    #     data = f.read()
    #     intData = open('articles_'+link.get_text()+artName,'wb+')
    #     intData.write(data)
    #     intData.close()
    #     print('writed end')