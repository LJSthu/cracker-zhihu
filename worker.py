#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding("utf8")

import os 
from bs4 import BeautifulSoup
import requests
import time
import json


def login():   # 使用cookie进行登陆
    global s
    s = requests.session()
    global headers
    headers = {
    'Cookie': '',       # 自己填充
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }
    r = s.get('https://www.zhihu.com', headers=headers)
 

if __name__ == "__main__":
    login()

    zanBaseURL = 'https://www.zhihu.com/api/v4/answers/798743321/voters?limit=10&offset={0}'
    
    name = []
    text = []
    id = []
    page = 0
    while 1:
        zanURL = zanBaseURL.format(str(page))
        page += 10
        zanREQ = s.get(zanURL, headers=headers).content
        zandict = json.loads(zanREQ)
        usrlist = zandict['data']
        if len(usrlist) == 0:
            break
        for i in usrlist:
            name.append(i['name'])
            text.append(i['headline'])
            id.append(i['url_token'])


    f = open('./result.txt', 'w')
    for i in range(len(name)):
        f.write(name[i]+'\n')
        f.write(text[i]+'\n')
        f.write(id[i]+'\n')
        f.write('\n')
    