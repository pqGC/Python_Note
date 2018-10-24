import re
from urllib.parse import urlparse
import requests
import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import functools


cms = []


def op():
    global lr
    if os.path.exists('data.json'):
        print('[+]Existing data.json file')
        js = open('data.json','r', encoding='utf-8')
        lr = json.load(js, encoding='utf-8')
    else:
        print('[-]Not data.json')
        exit()


op()


def cms_main(url):
    executor = ThreadPoolExecutor(10)
    all_task = list()
    for w in lr:
        all_task.append(executor.submit(
            check_url,
            url=url,
            w=w,
        ).add_done_callback(CmsList))
    # # 计数器 计数已完成任务
    # for future in as_completed(all_task):
    #     data = future.result()
    #     print("---> {} 完成!".format(data))
    # print('------  本次暗链扫描任务结束 ------')


def CmsList(cms_list):
    print(cms_list)


def check_url(url, w):
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        url1 = add_http_if_no_scheme(url)
        url = url1.rstrip('/') + w["url"]
        rest = requests.get(url=url, headers=headers, timeout=5)
        text = rest.text
        if rest.status_code != 200:
            pass
        if rest.status_code == 404:
            return
        cms_list = []
        if w["re"] and w['url'] != "/":
            if rest.status_code == 403 or text.find(w["re"]) != -1:
                cms_list.append(w["name"])
                print('[+]CMS:', w["name"], "url:", url, "status_code:", rest.status_code)
                print('[+]CMS:', w["name"], "url:", w["url"], file=open('cms.txt', 'w', encoding='utf-8'))
            else:
                url2 = url1.rstrip('/') + '/robots.txt'
                res = requests.get(url=url2, headers=headers, timeout=5)
                if res.text.find(w['re']) != -1 or res.text.find(w['url']) != -1:
                    print('[+]robot_CMS:', w["name"], "url:", url, "status_code:", rest.status_code)
        return cms_list

    except requests.exceptions.ConnectTimeout:
        print("ConnectTimeout")
    except requests.exceptions.Timeout:
        print("Timeout")
    except requests.exceptions.ChunkedEncodingError:
        print("Chunked编码错误")
    except:
        print("未知错误")


def add_http_if_no_scheme(url):
    match = re.match(r"^\w+://", url, flags=re.I)
    if not match:
        parts = urlparse(url)
        scheme = "http:" if parts.netloc else "http://"
        url = scheme + url

    return url


if __name__ == '__main__':
    cms_main('http://www.bufuzao.com/')
    # add_http_if_no_scheme('gf.ppgame.com')
