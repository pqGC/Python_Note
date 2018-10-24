import requests


def download(url):
    req = requests.get(url)
    if req.status_code == 404:
        print("no file")
        return
    with open('1.docx', 'wb') as fobj:
        fobj.write(req.content)
    print("dowload over")