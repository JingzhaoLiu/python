#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request

'create html by reading web url'

__author__='Martin liu'

def createHtml(webUrl,artName):

    with request.urlopen(webUrl) as f:
        data = f.read()
        intData = open(artName,'wb+')
        intData.write(data)
        intData.close()
        print(artName+' writed '+' end')

if __name__ =='__main__':
    createHtml(webUrl,artName)
       