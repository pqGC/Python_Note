from concurrent.futures import ThreadPoolExecutor, as_completed
import time
from datetime import datetime as dt
from twisted.internet import reactor


def test1(num):
    i = 0
    while i < num:
        time.sleep(1)
        print('这是测试方法1')
        i += 1


def test_threadpool():
    # start_time = time.time()
    executor = ThreadPoolExecutor(2)
    all_task = list()
    for i in range(10):
        all_task.append(executor.submit(
            runpro,
            num=2
        ))
    reactor.run()
    # # 计数器 计数已完成任务
    # count_finished = 0
    # for future in as_completed(all_task):
    #     count_finished += 1
    #     data = future.result()
    #     print("---> {} 暗链扫描完成! 总进度 {}/{}".format(data, str(count_finished), str(len(range(20)))))
    # end_time = time.time()
    # print(end_time - start_time)
    # print('-' + str(dt.now()) + '-')
    # print('------  本次暗链扫描任务结束 ------')
    # print('------共计{}个网站扫描完成------'.format(str(len(range(20)))))
    # print('-----------------------------')

def runpro(num):
    # reactor.suggestThreadPoolSize(40)
    reactor.callInThread(test1, num=num)



if __name__ == '__main__':
    test_threadpool()
