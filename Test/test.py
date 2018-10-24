from scrapy import crawler
from twisted.internet import reactor
from billiard.context import Process
from multiprocessing import Queue


def f(q):
    try:
        q.put(None)
    except Exception as e:
        q.put(e)


q = Queue()
p = Process(target=f, args=(q,))
p.start()
result = q.get()
p.join()


