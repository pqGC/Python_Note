import tldextract as tldextract
from urllib.parse import urlparse, splitnport, urlsplit
import re


# 获取主域名
def get_domain_new(url):
    split_url = tldextract.extract(url)
    domain = "{}.{}".format(split_url.domain, split_url.suffix)
    return domain


# 获取url
def get_domain(url):
    url = add_http_if_no_scheme(url)
    return splitnport(urlsplit(url).netloc)[0]


def add_http_if_no_scheme(url):
    """Add http as the default scheme if it is missing from the url."""
    match = re.match(r"^\w+://", url, flags=re.I)
    if not match:
        parts = urlparse(url)
        scheme = "http:" if parts.netloc else "http://"
        url = scheme + url
    return url

