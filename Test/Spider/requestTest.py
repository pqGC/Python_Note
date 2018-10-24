import random
import re

import requests
from bs4 import BeautifulSoup
import urllib3


def crawl_spider(url):
    """
    将网页数据爬取下来
    :param url:
    :return:
    """
    agent = [
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 '
        'Safari/534.50',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 '
        'Safari/534.50',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR '
        '3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) '
        'Chrome/18.0.1025.166 Safari/535.19',
        'Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) '
        'Version/4.0 Mobile Safari/534.30',
        'Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) '
        'Version/4.0 Mobile Safari/533.1',
        'Mozilla/5.0 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 '
        'Mobile/13B143 Safari/601.1 (compatible; Baiduspider-render/2.0; +http://www.baidu.com/search/spider.html)',
        'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
        'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)',
        'Mozilla/5.0 (compatible; Yahoo! Slurp China; http://misc.yahoo.com.cn/help.html)'
    ]
    headers = {
        "User-Agent": random.choice(agent),
    }
    res = requests.get(url=url, headers=headers, timeout=5)
    return res.text


pattern_url = '(?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]'
pattern = '(?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]\.js'
pattern_js = '.*\.js'


def recursion_fun(url):
    content = crawl_spider(url)
    search_item = re.compile(pattern, re.I | re.M | re.S)
    search_url = re.compile(pattern_url, re.I | re.M | re.S)
    search_js = re.compile(pattern_js, re.I | re.M | re.S)
    result_js = search_js.findall(content.replace('\\', '').replace('"', "").replace("'", "").replace("+", ""))
    print('js:', result_js)
    result = search_item.findall(content.replace('\\', '').replace('"', "").replace("'", "").replace("+", ""))
    result_url = search_url.findall(content.replace('\\', '').replace('"', "").replace("'", "").replace("+", ""))
    if len(result_url) != 0:
        print('result_url:', result_url)
        if result:
            print('result1:', result)
            for url in list(set(result)):
                print('url:', url)
                return recursion_fun(url)
        else:
            print('结束1')
    else:
        if result:
            print('result2:', result)
            for url in list(set(result)):
                return recursion_fun(url)
        else:
            print('结束2')


if __name__ == '__main__':
    # crawl_spider('http://www.tyhotle.com/tz/3p3t.js')
    recursion_fun('http://www.lqzxyey.com')
