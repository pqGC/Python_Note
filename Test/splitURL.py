import tldextract
from dns_test import *


def get_domain_new(url):
    o = tldextract.extract(url)
    domain = "{}.{}".format(o.domain, o.suffix)
    return domain


def is_same_ip(url, target_url):
    if get_domain(url) in check_dns(target_url):
        return True
    return False


def is_outside_link(url, target_url):
    if get_domain_new(url) == get_domain_new(target_url) or is_same_ip(url, target_url):
        print("False")
    else:
        print("True")


if __name__ == '__main__':
    is_outside_link('http://www.jnbank.com.cn:8002/fund/notice/0000000000000mfdbz', 'http://www.jnbank.com.cn:8002/fund/index')
