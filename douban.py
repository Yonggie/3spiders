howmany=600
topic_number=60085
url='https://m.douban.com/rexxar/api/v2/gallery/topic/{}/items?from_web=1&sort=hot&start=1&count={}&status_full_text=1&guest_only=0&ck=_QLM HTTP/1.1'.format(topic_number,howmany)
headers={
'Host': 'm.douban.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
'Accept': "appl'ication/json, text/javascript, */*; q=0.01",
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding': 'gzip, deflate, br',
'Referer': 'https://www.douban.com/gallery/topic/60085/',
'Content-Type': 'application/x-www-form-urlencoded',
'Origin': 'https://www.douban.com',
'Connection': 'keep-alive',
'Cookie': 'bid=UEGUal5CH_s; __utma=30149280.676528091.1599136932.1613384950.161',
}

import requests
import time
response=requests.get(url,headers=headers)

# with open('web.json','w',encoding='utf8') as f:
#     f.write(response.text)

import json
data=json.loads(response.text)
with open('douban.json','w',encoding='utf8') as ff:
    ff.write(json.dumps(data,ensure_ascii=False))
print("there are {} in total in theorem.".format(data['total']))
print("in practice we get {}".format(len(data['items'])))