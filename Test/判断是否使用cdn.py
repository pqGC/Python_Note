import dns.resolver


def get_cnames(url):
    cnames = []
    dns_resolver = dns.resolver.Resolver()
    try:
        answer = dns_resolver.query(url, 'CNAME')
    except Exception as e:
        print(None)
    else:
        cname = [_.to_text() for _ in answer][0]
        cnames.append(cname)
        print(cnames)
    if cnames:
        if len(cnames) > 1 or cnames[0] != url:
            print(True)
        else:
            print(False)


if __name__ == '__main__':
    get_cnames('www.xcqyyxx.com')


