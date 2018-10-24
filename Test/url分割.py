import re
from urllib.parse import urlparse, splitnport
from urllib.request import urlsplit


# 判断ip格式是否正确
def is_ip(ip):
    if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip):
        return True
    else:
        return False


def splitURL(url):
    print(urlsplit(url))
    scheme = urlsplit(url)[0]
    if scheme not in ['http', 'https']:
        return print('请填写正确的url')
    print('scheme:', scheme)
    netloc = urlsplit(url)[1]
    print('netloc:', netloc)
    path = urlsplit(url)[2]
    print('path:', path)
    netloc = netloc.split(':')
    if len(netloc) > 1:
        address = netloc[0]
        port = int(netloc[1])
        print('address:', address)
        print('port', port)
    else:
        address = netloc[0]
        port = 80
        print('address:', address)
        print('port', port)

    this_url = '{proto}{url}{port}{path}'.format(proto="{}://".format(scheme),
                                                        url=address,
                                                        port=':{}'.format(port),
                                                        path=path
                                                        )
    print('this_url', this_url)


def add_http_if_no_scheme(url):
    """Add http as the default scheme if it is missing from the url."""
    match = re.match(r"^\w+://", url, flags=re.I)
    if not match:
        parts = urlparse(url)
        scheme = "http:" if parts.netloc else "http://"
        url = scheme + url

    return url


# add_http = add_http_if_no_scheme("www.blog.csdn.net/yyt8yyt8/article/details/6999565")
# print(add_http)
#
# # 获取域名
# print(splitnport(urlsplit(add_http).netloc)[0])
#
#
# a = add_http_if_no_scheme("https://blog.csdn.net")
# a = a.rstrip('/') + "yyt8yyt8/article"
# print(add_http_if_no_scheme(a))


if __name__ == '__main__':
    splitURL('www.runoob.com/redis/redis-backup.html')
