# -*- coding: utf-8 -*-
import re
from urllib.parse import urlparse, splitnport, urlsplit
import dns.resolver
import tldextract as tldextract


def check_dns(url):
    ips = []
    dns_resolver = dns.resolver.Resolver()
    url = get_domain(url)
    print(url)
    try:
        answer = dns_resolver.query(url, 'A')
    except Exception as e:
        ips = None
        print("dns resolver error:" + str(e))
    else:
        for i in answer.response.answer:
            for j in i.items:
                if j.rdtype == 1:
                    ips.append(j.address)
                    print(j)
        # 精简写法
        dns_a = ', '.join([_.address for _ in answer])
        print('dns_a', dns_a)
    print(ips)
    return ips


def get_domain(url):
    url = add_http_if_no_scheme(url)
    return splitnport(urlsplit(url).netloc)[0]


def get_domain_new(url):
    split_url = tldextract.extract(url)
    domain = "{}.{}".format(split_url.domain, split_url.suffix)
    return domain


def add_http_if_no_scheme(url):
    """Add http as the default scheme if it is missing from the url."""
    match = re.match(r"^\w+://", url, flags=re.I)
    if not match:
        parts = urlparse(url)
        scheme = "http:" if parts.netloc else "http://"
        url = scheme + url
    return url


def is_num(url):
    url = url.replace('.', '')
    print(url)
    print(str.isdigit(url))


if __name__ == '__main__':
    check_dns('http://gf.ppgame.com/web/pc/index.html')
    # is_num('218.93.176.28')
    # get_web_request('221.228.219.71', 'gf.ppgame.com/web/pc/index.html')
    # get_domain('www.zgwj.gov.cn')


