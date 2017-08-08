#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib.request
import os

'download girl img'

'__author__==Martin liu'


def url_open(url):
    '模拟浏览器打开链接，获取网页内容'
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36')
    response = urllib.request.urlopen(req)
    readhtml = response.read()
    return readhtml

def get_page(url):
    '获取第一页的页码'
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page')+23
    # 获取<span class="current-comment-page">[224]</span>到224的开始序号
    b = html.find(']',a)
    # 从a序号开始找到 224 结束符号 ]
    return html[a:b]
    # 返回 当前页的页码

def find_imgs(url):
    '查找图片'
    html = url_open(url).decode('utf-8')
    img_list = []
    # 图片列表
    a = html.find('img src')
    while a!=-1:
        b = html.find('.jpg',a,a+255)
        c = html.find('.gif',a,a+255)
        if b!=-1:
            img_list.append('http:'+html[a+9:b+4])
        elif c!=-1:
            img_list.append('http:'+html[a+9:c+4])
        else:
            b = a+9+1
        a = html.find('img src',b+c)

    return img_list




def save_imgs(folder,img_list):
    '保存图片'
    for each in img_list:
        filname = each.split('/')[-1]
        # 获取文件名
        with open(filname,'wb') as f:
            img = url_open(each)
            f.write(img)
            # f.close()
            # 文件会在语句结束后或者异常时自动关闭






def downgirlimg(folder='girl',pages=2):#爬取2页的图片
    '下载图片'
    os.mkdir(folder)
    # 建立一个girl文件夹
    os.chdir(folder)
    # 切换到girl文件夹
    url = 'http://jandan.net/ooxx'

    page_num = int(get_page(url))
    # 获取第一页的页码数字

    for i in range(pages):
        # http://jandan.net/ooxx/page-224#comments
        page_url = url + '/page-'+str(page_num)+'#comments'
        #每页图片网址
        img_addrs = find_imgs(page_url)
        #在网址页面查找图片
        save_imgs(folder,img_addrs)
        #保存图片在文件夹
        page_num-=1


# 调用主函数
if __name__=='__main__':
    downgirlimg()
