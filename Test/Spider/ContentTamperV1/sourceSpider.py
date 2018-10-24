import random
from datetime import datetime, timedelta
import scrapy
import time
from bs4 import BeautifulSoup
from scrapy import crawler
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from scrapy.exceptions import DropItem
from Spider.ContentTamperV1.crawl_source import get_md5
from Spider.ContentTamperV1.tamp_logical import content_tamper_main


class SourceSpider(scrapy.Spider):

    custom_settings = {
        'LOG_LEVEL': 'DEBUG',
        'LOG_FILE': 'ten.log',
        'FEED_FORMAT': 'jsonlines',
        'CLOSESPIDER_PAGECOUNT': 10,
        'DEPTH_LIMIT': 1,
        'COOKIES_ENABLED': False,
        'RETRY_ENABLED': False,
        'DOWNLOAD_TIMEOUT': 10,
        'REDIRECT_ENABLED': False,
        'BOT_NAME': 'Content',
        'ROBOTSTXT_OBEY': False,
        'FEED_EXPORT_ENCODING': 'utf-8',
        'DOWNLOADER_MIDDLEWARES': {
            'ContentTamperV1.sourceSpider.RoteUserAgentMiddleware': 400,
            'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None
        },
        'ITEM_PIPELINES': {
            'ContentTamperV1.sourceSpider.ContentPipeline': 400,
        }
    }

    name = 'sourceSpider'

    start_urls = []

    def parse(self, response):
        items = ComtentItem()

        items['page_url'] = response.url

        try:
            page_source = str(BeautifulSoup(response.text, "lxml"))
            items['html_content'] = page_source  # .encode('utf-8')
        except Exception as e:
            print(e)
            print('URL:{} response is not text'.format(items['page_url']))
            items['html_content'] = ''
        items['md5'] = get_md5(response.text)

        items['crawl_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        yield items


# -----------------------------------Pipelines-------------------------------------
class ContentPipeline(object):

    def process_item(self, item, spider):
        print(item)
        global valid
        valid = True

        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            d1 = datetime.now()
            t = d1 + timedelta(seconds=3600 * 24)  # 24个小时后过期
            time_setting = {'createAt': t, 'spider_way': 1}
            new_item = dict(item)
            new_data = {new_item, time_setting}
            print(new_data)
            return item


# ------------------------------middleware---------------------------------
class RoteUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent=None):
        super(RoteUserAgentMiddleware, self).__init__()
        self.user_agent = user_agent

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        if ua:
            request.headers.setdefault('User-Agent', ua)

    user_agent_list = [
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


# -----------------------------items------------------------------------
class ComtentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    page_url = scrapy.Field()
    html_content = scrapy.Field()
    md5 = scrapy.Field()
    crawl_time = scrapy.Field()


def run_spider():
    try:
        process = crawler.CrawlerProcess()
        process.crawl(SourceSpider)
        process.start()
    except Exception as e:
        print(e)



