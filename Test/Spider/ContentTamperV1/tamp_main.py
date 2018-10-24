import time
from scrapy import crawler
from twisted.internet import reactor
from billiard.context import Process
from multiprocessing import Queue
from Spider.ContentTamperV1.crawl_source import yield_item
from Spider.ContentTamperV1.sourceSpider import SourceSpider


def run_spider(target_url):
    SourceSpider.start_urls = [target_url]

    def f(q):
        try:
            runner = crawler.CrawlerRunner()
            deferred = runner.crawl(SourceSpider)
            deferred.addBoth(lambda _: reactor.stop())
            reactor.run()
            q.put(None)

        except EOFError as e:
            q.put(e)

    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    result = q.get()
    p.join()

    if result is not None:
        raise result


def main(url_list: list):
    for url in url_list:
        print(url)
        run_spider(url)


if __name__ == '__main__':
    mylist = [
        'http://ggj.chuzhou.gov.cn:80'
    ]

    main(mylist)
