import re
import requests
import threading
import queue
import os
import hashlib


class cmsRecognize(object):
    def __init__(self, url, threads=50):
        self.url = url
        self.filePath = 'Bin/'
        self.q = queue.Queue()
        self.threads = threads
        self.isKnown = False
        self.knew = 0

    def request(self, url):
        try:
            r = requests.get(url, timeout=10)
        except requests.exceptions.Timeout as e:
            print(e)
            return False
        except requests.exceptions.MissingSchema as e:
            print(e)
            return False
        except requests.exceptions.RequestException as e:
            print(e)
            return False
        return r.text if r.status_code == 200 else False

    # 获取ico的md5值
    def getMd5Info(self, path='/favicon.ico'):
        url = self.url + path
        response = self.request(url)
        if response:
            md5 = hashlib.md5()
            md5.update(response.encode('utf-8'))
            return md5.hexdigest()
        return False

    def readFile(self, filename):
        filename = self.filePath + filename
        with open(filename, 'r') as f:
            return f.readlines()

    def compareIco(self):
        res = self.getMd5Info()
        if res != False:
            for line in self.readFile('ico.txt'):
                if res == line.strip().split('#')[1]:
                    print('[*]Based on favicon.ico:', line.strip().split('#')[0])
                    return True
            print('[-]Based on favicon.ico: Unknown')

    def getFeature(self):
        files = os.listdir(self.filePath)
        files.remove('ico.txt')
        '''
        主要是此处做了修改，原本是将文件放入队列中，现在修改为读取之后将测试路径放到队列中
        '''
        for f in files:
            # self.q.put(f)
            i = 0
            for line in self.readFile(f):
                i = i + 1
                if i <= 2: continue
                line = line.strip().split('------')
                self.q.put(line)

                def compareFeature(self):
                    while

                not self.q.empty():  # i = 0 #knew = 0 # for line in self.readFile(self.q.get()): # i = i + 1 # if i <= 2: # continue content = self.q.get() response = self.request(self.url + content[0]) #print(threading.current_thread(), content[0]) if re.search(content[1], str(response)): self.knew = self.knew + 1 #print(knew) if self.knew >= 3:
                print('[*]Based on feature:', content[2])
                os._exit(0)  # 找到之后立即结束程序，减少开支


def run(self):
    self.compareIco()

    self.getFeature()
    for i in range(self.threads):
        t = threading.Thread(target=self.compareFeature)
        t.setDaemon(True)
        t.start()

    # for i in range(self.threads):
    # t.join()
    self.q.join()  # 线程数控制有问题，做了修改

    if not self.isKnown:
        print('[-]Based on feature: Unknown')


if __name__ == '__main__':
    cms = cmsRecognize('http://www.seacms.net')
    cms.run()