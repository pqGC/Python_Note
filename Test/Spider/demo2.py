from selenium import webdriver
import json
from collections import OrderedDict
from Spider.commons import *


def getResponseHeaders(browser):
    har = json.loads(browser.get_log('har')[0]['message'])
    return OrderedDict(sorted([(header["name"], header["value"]) for header in har['log']['entries'][0]['response']["headers"]], key=lambda x: x[0]))


def getResponseStatus(browser):
    har = json.loads(browser.get_log('har')[0]['message'])
    return (har['log']['entries'][0]['response']["status"],\
            str(har['log']['entries'][0]['response']["statusText"]))

browser = get_phantom_driver()

# Simple Test
print(">>>>> 404")
browser.get("http://www.lqzxyey.com")
print("status: ", getResponseStatus(browser))
headers = getResponseHeaders(browser)
for key in headers:
    print(key, "=>", headers[key])
