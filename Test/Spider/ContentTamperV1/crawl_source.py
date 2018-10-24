import hashlib
import time
import random
import requests
from datetime import datetime, timedelta
from Spider.ContentTamperV1.tamp_logical import content_tamper_main


def get_md5(source):
    m = hashlib.md5()
    m.update(source.encode('utf-8'))
    return m.hexdigest()


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
    time.sleep(2)

    # http = urllib3.PoolManager()
    #
    # response = http.request('GET', url, headers=headers)
    # soup = BeautifulSoup(response.data, 'html.parser')
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    return html


def yield_item(target_id: str, page_url: str):
    """
    打印中的 way 2 表示 reactor启动失败，调用request函数进行网页爬取, 没有打印出来 way 2 就是通过scrapy爬虫获取的网页源码
    :param target_id:
    :param page_url:
    :return:
    """
    page_content = str(crawl_spider(page_url))
    html_content = page_content
    md5 = get_md5(page_content)
    crawl_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    document = {'target_id': target_id, 'page_url': page_url, 'html_content': html_content,
                'is_home_url': 1, 'md5': md5, 'crawl_time': crawl_time, 'spider_way': 2}
    try:
        d1 = datetime.now()
        t = d1 + timedelta(seconds=3600 * 24)  # 24个小时后过期
        time_setting = {'createAt': t, 'logEvent': 2, "logMessage": "Success!"}

        new_data = {**document, **time_setting}
        judge_repeated_md5 = find_modified_md5_by_md5(md5)
        if not judge_repeated_md5:
            """
            如果md5不存在，存在两种情况:
            第一种: 爬取的新客户网站,入库
            第二种: 爬取的客户网站被篡改,针对这种情况，需要将篡改的网站入库到另一个数据库，然后进行数据分析
            """
            judge_repeated_url = get_url_from_mongo(page_url)
            if not judge_repeated_url:
                print('Insert Successfully! Way 2')
                return False
            else:
                print(page_url + 'may be modified! Way 2')
                find_repeate_md5 = find_compare_md5_by_md5(md5)
                if find_repeate_md5:
                    print('Same Modification Found! Way 2')
                else:
                    print('New modification Found! Way 2')
                    print('Modified page_content insert Successfully! Way 2')
                    print('Starting Page Tamper Analysing Way 2...')
                    content_tamper_main(target_id)
                return True
        else:
            print(md5 + ' is existed. Way 2')
            return False
    except Exception as e:
        print(e)

