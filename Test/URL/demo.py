from URL.common import get_domain_new, get_domain
from URL.common import Url, is_same_ip
from URL.common import check_dns, check_dns_NS
from URL.CdnCheck import CdnCheck


def get_ip(url):
    host = get_domain(url)
    print(check_dns(host))


def get_NS(url):
    host = get_domain(url)
    print(check_dns_NS(host))


def get_domain_new2(url):
    print(get_domain_new(url))


def get_domain2(url):
    print(get_domain(url))


def is_out(url, target_url):
    """

    :param url: 暗链
    :param target_url: 被检测网页
    :return:
    """
    print(Url.is_outside_link(url, target_url))


def is_ip(url, target_url):
    print(is_same_ip(url, target_url))


def check_is_cdn(url: str):
    """
    根据传过来的url,检测url是否有cdn
    :param url:
    :return:
    """
    check_cdn = CdnCheck(url)
    is_cdn = check_cdn.check()
    if is_cdn:
        print(is_cdn)
        print('true')
    else:
        print('flase')


if __name__ == '__main__':
    """
    true:外链
    """
    # is_out('http://10.53.200.170/jcms', 'http://www.tcsxyz.com:80')
    # is_ip()
    # get_domain_new2('xcqyyxx.com.lo705.faipod.com.')  # 获取主域名
    # get_domain2('https://kscd.zking.com:10443')  # 获取url
    get_ip('www.bilibili.com')
    # check_is_cdn('www.bilibili.com')  # 只能填域名，即经过方法get_domain2()处理的返回值
    # get_NS('gf.ppgame.com')

