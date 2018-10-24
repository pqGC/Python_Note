import requests
import threading
import os

us = []
ut = []
error = ['404', '不存在', '无权限访问', '403', 'D盾', '没有', '页面消失了']
okurl = []
noturl = []
user = input('url->>>')
if os.path.exists('cms_url.txt') and os.path.exists('cms_title.txt'):
    print('[+]cms_url.txt and cms_title.txt ok !')
else:
    print('[-]cms_url.txt or cms_title.txt not found')
    exit()


def jiazai():
    global cmspath
    title = []
    url = []
    cmspath = {}
    dk = open('cms_title.txt', 'r', encoding='utf-8')
    for d in dk.readlines():
        qc = "".join(d.split('\n'))
        title.append(qc)

    dk2 = open('cms_url.txt', 'r', encoding='utf-8')
    for d1 in dk2.readlines():
        qc2 = "".join(d1.split('\n'))
        url.append(qc2)

    for i in range(0, len(title)):
        cmspath[title[i]] = url[i]
    print('[+]CMSpath.txt Load completion')


jiazai()


def testing():
    try:
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}
        for t in cmspath.values():
            us.append(user.strip() + t.strip())

        for v in cmspath.keys():
            ut.append(v)

        for f in range(0, len(ut)):
            reqt = requests.get(url=us[f], headers=headers)
            for e in error:
                if reqt.status_code == 200 and e not in reqt.text() and len(reqt.text()) > 0:
                    ok = '[+]CMS path:{}   CMS name:{}'.format(reqt.url, ut[f])
                    if ok in okurl: continue
                    okurl.append(ok)
                    print(ok)
                else:
                    no = '[-]Not cms name:{}  cms path:{} status_code:{}'.format(ut[f], reqt.url, reqt.status_code)
                    if no in noturl: continue
                    noturl.append(no)

                    print(no)

    except:
        pass


if __name__ == '__main__':
    testing()


