#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup 
from urllib import request
import os

'remove html'
   
soup = BeautifulSoup(open('articles.html'))

    
for link in soup.select(' p > a '):
    
    webUrl  = link.get('href')
    artName = webUrl.split ('/')[-1]
    os.remove(artName)
   

    
    
