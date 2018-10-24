import re
# """(?:\"?|\')(?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|](?:\"?|\')"""
# pattern = "document\.write\(.<iframe.*?src=\s*(?:\"?|\')(?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|](?:\"?|\').*?>"
# content = """document.write("<iframe width="100" height="100" src="http://114.55.36.222/LittleHann/LittleHann.html"></iframe>")"""
# pattern2 = "<div\s*?id=.?\w{1,20}?.?>(\s*.*?)</div>\s*?<script>document\.getElementById\(.*?\)\.style\.display=.?none.?[;]?</script>"
# content2 = """<div id="aa" style="height:500"><a href="www.test.com"></a></div>/<script>document.getElementById("aa").style.display="none";</script>"""
# search_result = re.compile(pattern2, re.I | re.M | re.S)
# result = search_result.findall(content2)
# print(result)
#
# pattern_url = "(?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]"
# search_url = re.compile(pattern_url, re.I | re.M | re.S)
# result2 = search_url.findall(content2)
# print(result2)
# """<script.{0,60}>\s*window.location.href=.*?;</script>"""
# pattern_item = "<div[\S\s]*style=.{0,1}position\s*:\s*absolute.*(?:top|left|right)(?:.|):(?:.|)-[6-9][\d]{2,3}px\s*.*?>.*?</div>"
# search_item = re.compile(pattern_item, re.I | re.M | re.S)
# result3 = search_item.findall(content2)
# print(result3)


# pattern_item = "(127\.0\.0\.1)|(localhost)|(10\.\d{1,3}\.\d{1,3}\.\d{1,3})|(172\.((1[6-9])|(2\d)|(3[01]))\.\d{1,3}\.\d{1,3})|(192\.168\.\d{1,3}\.\d{1,3})"
pattern_item = "<marquee.{1,20}height=[0-9].{1,20}width=[0-9][^>]*?>[\S\s]{0,150}</marquee>"
content3 = """	
<marquee height=1 width=5 scrollamount=3000 scrolldelay=20000><a href=http://thief.one >暗链</a></marquee>
"""
# content = """window.setTimeout("window.location='"+wz+"'",1000); """
search_item = re.compile(pattern_item, re.I | re.M | re.S)
result4 = search_item.findall(content3)
# strIP = ''
# for single_tuple in result4:
#     for ip in single_tuple:
#         strIP = strIP + ip
# if len(strIP) == 0:
#     print('空')
# print(strIP)
print(result4)


