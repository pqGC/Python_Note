import re
from urllib.parse import urlparse
import requests
import json
import hashlib
import os
import optparse
from concurrent.futures import ThreadPoolExecutor


def main():
    usage="[-q MD5DE-CMS] " \
          "[- p URL gets CMS]"
    parser=optparse.OptionParser(usage)
    parser.add_option('-q',dest='md5',help='md5 cms')
    parser.add_option('-p',dest='url',help='url cms')
    (options,args)=parser.parse_args()
    if options.md5:
        log=options.md5
        panduan(log)
    elif options.url:
        log2=options.url
        panduan2(log2)
    else:
        parser.print_help()


def op():
    global lr
    if os.path.exists('data.json'):
        print('[+]Existing data.json file')
        js=open('data.json','r', encoding='utf-8')
        lr=json.load(js, encoding='utf-8')
    else:
        print('[-]Not data.json')
        exit()

op()

def panduan(log):
    global headers
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    for b in lr:
        try:
            url = log.rstrip('/') + b["url"]
            rest = requests.get(url=url, headers=headers, timeout=5)
            text = rest.text
            if rest.status_code != 200:
                print('[-]Not Found 200', rest.url)
            md5=hashlib.md5()
            md5.update(text.encode('utf-8'))
            g=md5.hexdigest()
            print(g)
            if g == b["md5"]:
                print("[+]CMS:",b["name"],"url:",b["url"])
                print("[+]CMS:",b["name"],"url:",b["url"],file=open('cms.txt','w', encoding='utf-8'))
            else:
                print('[-]not md5:',b["md5"])
        except requests.exceptions.ConnectTimeout:
            print("ConnectTimeout")
        except requests.exceptions.Timeout:
            print("Timeout")



def panduan2(log2):
    executor = ThreadPoolExecutor(20)
    all_task = list()
    for w in lr:
        all_task.append(executor.submit(
            check_url,
            url=log2,
            w=w
        ))


def check_url(url, w):
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        url = add_http_if_no_scheme(url)
        url = url.rstrip('/') + w["url"]
        rest = requests.get(url=url, headers=headers, timeout=5)
        text = rest.text
        if rest.status_code != 200:
            pass
        if w["re"]:
            if (text.find(w["re"]) != -1):
                print('[+]CMS:', w["name"], "url:", w["url"])
                print('[+]CMS:', w["name"], "url:", w["url"], file=open('cms.txt', 'a', encoding='utf-8'))

    except requests.exceptions.ConnectTimeout:
        print("ConnectTimeout")
    except requests.exceptions.Timeout:
        print("Timeout")
    except requests.exceptions.ChunkedEncodingError:
        print("Chunked编码错误")
    except:
        print("未知错误")


def add_http_if_no_scheme(url):
    """Add http as the default scheme if it is missing from the url."""
    match = re.match(r"^\w+://", url, flags=re.I)
    if not match:
        parts = urlparse(url)
        scheme = "http:" if parts.netloc else "http://"
        url = scheme + url

    return url


if __name__ == '__main__':
    main()
