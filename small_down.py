import requests
image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"

r = requests.get(
    'http://tsn.baidu.com/text2audio?tex=我是一个兵，来自老百姓，&lan=zh&cuid=98:01:a7:9e:e1:59&ctp=1&tok=24.a16af481b01bf8290915dd09fb6cfbd7.2592000.1507731236.282335-10125385&spd=5&pit=5&vol=5&per=4'
)  # create HTTP response object

with open("1.mp3", 'wb') as f:
    f.write(r.content)
