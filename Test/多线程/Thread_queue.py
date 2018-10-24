import time
from queue import Queue
from concurrent.futures import ThreadPoolExecutor


# 两个队列
q1 = Queue()
q2 = Queue()

for i in range(10):
    q1.put(i)
for j in range(10, 20):
    q2.put(j)


# 函数1:取出队列1中的值，处理后装入队列2中
def worker1():
    while True:
        item = q1.get()
        print('get item from q1...', 'item = %s' % item)
        time.sleep(0.1)
        q1.task_done()


# 函数2:取出队列2中的值
def worker2():
    while True:
        item = q2.get()
        print('get item from q2...', 'item = %s' % item)
        time.sleep(0.1)
        q2.task_done()


def main():
    executor = ThreadPoolExecutor(5)
    executor.submit(worker1)
    executor.submit(worker2)


if __name__ == '__main__':
    main()

