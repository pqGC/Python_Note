from twisted.internet import threads, reactor, defer
# from twisted.web.client import getPage
from Spider.beautifulsoup import crawl_spider
from twisted.internet import reactor


def inThread():
    try:
        result = threads.blockingCallFromThread(
            reactor, crawl_spider, "http://twistedmatrix.com/")
    except Exception as ex:
        print(ex)
    else:
        print(result)
    reactor.callFromThread(reactor.stop)

reactor.suggestThreadPoolSize(10)
reactor.callInThread(inThread)
reactor.run()


if __name__ == '__main__':
    inThread()

