import requests
import shutil
from urllib import quote

tok = "test"  #请根据实际情况改写access token
tex = ""
lan = "zh"
cuid = "apikey"  #请根据实际情况改写apikey
ctp = "1"


def getBaiduVoice(tex):
    data1 = {
        'tok': tok,
        'ctp': '1',
        'cuid': cuid,
        'lan': 'zh',
        'tex': quote(tex)
    }
    headers = {'content-type': 'application/json'}
    try:
        r = requests.post(
            "http://tsn.baidu.com/text2audio",
            data=data1,
            headers=headers,
            stream=True)
        if r.status_code == 200:
            with open(r"D:/a.mp3", 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
    except Exception as e:
        print str(e)
    finally:
        f.close()


if __name__ == "__main__":
    tex = "我是一个兵，来自老百姓，"
    getBaiduVoice(tex)




