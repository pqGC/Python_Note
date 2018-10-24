from urllib.parse import urlparse, urlunparse, urlsplit, splitnport
import tldextract as tldextract
import re
import dns.resolver


def add_http_if_no_scheme(url):
    """Add http as the default scheme if it is missing from the url."""
    match = re.match(r"^\w+://", url, flags=re.I)
    if not match:
        parts = urlparse(url)
        scheme = "http:" if parts.netloc else "http://"
        url = scheme + url

    return url


def get_domain(url):
    url = add_http_if_no_scheme(url)
    return splitnport(urlsplit(url).netloc)[0]


def get_domain_new(url):
    split_url = tldextract.extract(url)
    domain = "{}.{}".format(split_url.domain, split_url.suffix)
    return domain


class Url(object):
    @classmethod
    def find_url(cls, text: str) -> list:
        """
        从给定的text中提取所有的url
        :param text:
        :return:
        """
        url_reg = '(?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]'
        pattern = re.compile(url_reg, re.I | re.S | re.M)
        return pattern.findall(text)

    @classmethod
    def is_outside_link(cls, url: str, target_url: str) -> bool:
        """
        判断url是否为外链 :return: 外链返回True 否则返回False
        :param url: 待测链接
        :param target_url:
        """
        if get_domain_new(url) != get_domain_new(target_url):
            if is_same_ip(url, target_url):
                return True
            else:
                return False
        else:
            return False

    @classmethod
    def is_malicious_url(cls, url: str, white_domain: list) -> bool:
        """
        判断是否为恶意链接,判断标准为如果域名处于白名单则false,否则为true
        :param url:
        :param white_domain:
        :return:
        """
        for domain in white_domain:
            if domain[-1] in url:
                return False
        return True
    # todo 增加判断恶意链接的方法


# 有些网站导入资源时会直接使用主机号 而不是域名
def is_same_ip(url, target_url):
    """
    外链返回true
    :param url:
    :param target_url:
    :return:
    """
    target_url = get_domain(target_url)
    url = get_domain(url)
    if str.isdigit(url.replace('.', '')):
        if url not in check_dns(target_url):
            if is_inside_ip(url):
                return False
            return True
        return False
    return True


def check_dns(main_url):
    """
    根据传入的域名，解析出所有IP
    :param main_url: 待测url
    :return:
    """
    ips = []
    dns_resolver = dns.resolver.Resolver()
    try:
        answer = dns_resolver.query(main_url, 'A')
    except Exception as e:
        ips = []
        print("dns resolver error:" + str(e))
    else:
        for i in answer.response.answer:
            for j in i.items:
                if j.rdtype == 1:
                    ips.append(j.address)
        # 精简写法
        dns_a = ', '.join([_.address for _ in answer])
        # print('dns_a', dns_a)
    return ips


def check_dns_NS(main_url):
    """
    根据传入的域名，解析出所有IP
    :param main_url: 待测url
    :return:
    """
    ips = []
    dns_resolver = dns.resolver.Resolver()
    try:
        answer = dns_resolver.query(main_url, 'NS')
    except Exception as e:
        ips = []
        print("dns resolver error:" + str(e))
    else:
        for i in answer.response.answer:
            for j in i.items:
                if j.rdtype == 1:
                    ips.append(j.to_text())
        # 精简写法
        dns_a = ', '.join([_.address for _ in answer])
        # print('dns_a', dns_a)
    return ips


def is_inside_ip(url):
    """
    该方法用于判断疑似暗链是否为内网ip
    :param url: 疑似暗链
    :return:
    """
    inside_ip_reg = '(127\.0\.0\.1)|(localhost)|(10\.\d{1,3}\.\d{1,3}\.\d{1,3})|(172\.((1[6-9])|(2\d)|(3[01]))\.\d{1,3}\.\d{1,3})|(192\.168\.\d{1,3}\.\d{1,3})'
    pattern = re.compile(inside_ip_reg, re.I | re.S | re.M)
    res = pattern.findall(url)
    str_ip = ''
    for single_tuple in res:
        for ip in single_tuple:
            str_ip = str_ip + ip
    if len(str_ip) == 0:
        return False
    return True



