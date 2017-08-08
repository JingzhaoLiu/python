#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request
import webbrowser as web


webUrl = 'http://www.cnblogs.com/alex3714/articles/5885096.html'
aurl   = 'http://www.cnblogs.com/nima/p/4989482.html'

# b = 'http://mebook.cc/download.php?id=15725'

artName = aurl.split ('/')[-1]

with request.urlopen(aurl) as f:
    data = f.read()
    intData = open('articles_'+artName,'wb+')
    intData.write(data)
    intData.close()
    print('writed end')
    web.open('file:///Users/martin/Desktop/traning/'+'articles_'+artName)
