#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request
from bs4 import BeautifulSoup 


webUrl = 'http://www.cnblogs.com/alex3714/articles/5885096.html'


artName = webUrl.split ('/')[-1]

with request.urlopen(webUrl) as f:
    data = f.read()
    intData = open('articles_'+artName,'wb+')
    intData.write(data)
    intData.close()
    print('writed end')


