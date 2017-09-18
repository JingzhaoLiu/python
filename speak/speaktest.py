# -*- coding:utf-8 -*-
# tex	必填	合成的文本，使用UTF-8编码，请注意文本长度必须小于1024字节
# lan	必填	语言选择,目前只有中英文混合模式，填写固定值zh
# tok	必填	开放平台获取到的开发者 access_token
# ctp	必填	客户端类型选择，web端填写固定值1
# cuid	必填	用户唯一标识，用来区分用户，计算UV值。建议填写能区分用户的机器 MAC 地址或 IMEI 码，长度为60字符以内。
# spd	选填	语速，取值0-9，默认为5中语速
# pit	选填	音调，取值0-9，默认为5中语调
# vol	选填	音量，取值0-15，默认为5中音量
# per	选填	发音人选择, 0为普通女声，1为普通男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女声


# grant_type：必须参数，固定为“client_credentials”；
# client_id：必须参数，应用的 API Key；
# client_secret：必须参数，应用的 Secret Key;
# 例如：

# https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=Va5yQRHl********LT0vuXV4&client_secret= 0rDSjzQ20XUj5i********PQSzr5pVw2&


import requests
# import shutil
# from urllib import quote
import uuid
import os

def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])



API_Key='tWPDnXBfWcTlXFjtGg3C65zh'

Secret_Key= 'bb1cd4a2f4360419f8960d8786614ae8'

def getToken():
    url = 'https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + API_Key + '&client_secret=' + Secret_Key

    r = requests.get(url)
    if r.status_code == 200:
        print(r.json()['access_token'])
        return r.json()['access_token']



tok = '24.a16af481b01bf8290915dd09fb6cfbd7.2592000.1507731236.282335-10125385' #getToken()
cuid = '98:01:a7:9e:e1:59' #get_mac_address()



def getVoice(tex, folder='music',filename='1.mp3'):

    # url = 'http://tsn.baidu.com/text2audio?tex='+tex+'&lan=zh&cuid='+cuid+'&ctp=1&tok='+tok+'&spd='+spd+'&pit='+pit+'&vol='+vol+'&per='+per
    url = 'http://tsn.baidu.com/text2audio'

    payload = {
        'tex': tex,
        'lan': 'zh',
        'tok': tok,
        'ctp': '1',#wab
        'cuid': cuid,
        'spd': '5',
        'pit': '5',
        'vol': '5',
        'per': '4'
    }
    try:
        r = requests.get(url,params=payload)
        if r.status_code == 200:
            contentType = r.headers['content-type']
            if contentType == 'audio/mp3':
                # os.mkdir(folder)#建立一个‘ooxx’的文件夹
                # os.chdir(folder)#切换目录在‘ooxx’目录下

                with open('3.mp3', 'wb') as f:
                    f.write(r.content)


        else:
            print(r.status_code)

    except expression as e:
        print(e.json())




if __name__ == "__main__":
    tex = "我爱你，慧慧，"
    getVoice(tex)
