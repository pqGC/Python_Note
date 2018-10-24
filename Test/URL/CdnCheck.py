import dns.resolver
import threading
import time
import inspect
import ctypes


class CdnCheck(object):
    def __init__(self, url):
        super(CdnCheck, self).__init__()
        self.url = url
        self.true_url = ''
        self.cnames = []

    def get_cnames(self):
        self.true_url = self.url
        dns_resolver = dns.resolver.Resolver()
        try:
            answer = dns_resolver.query(self.true_url, 'CNAME')
        except Exception as e:
            self.cnames = None
        else:
            cname = [_.to_text() for _ in answer][0]
            self.cnames.append(cname)

    def check(self):
        get_cname = threading.Thread(target=self.get_cnames, args=())
        check_time = 0
        get_cname.start()
        while True:
            if check_time < 300 and get_cname.is_alive():
                time.sleep(0.01)
                check_time += 1
            elif not get_cname.is_alive():
                break
            else:
                stop_thread(get_cname)
                break
        if self.cnames:
            if len(self.cnames) > 1 or self.cnames[0] != self.true_url:
                return self.cnames
        return False


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)