dark_link_reg = [
    {'type': 'marquee', 'pattern':
        "<marquee.{1,20}height=[0-9].{1,20}width=[0-9][^>]*?>[\S\s]*?</marquee>"},
    {'type': 'marquee', 'pattern': "<marquee.{1,20}width=[0-9].{1,20}height=[0-9][^>]*?>[\S\s]*?</marquee>"},
    {'type': 'script', 'pattern': "<.?div[\S\s]{0,20}id=[\s\S]{0,20}>\s*.*?<.?/.?div.?>\s*<.?script.*?>\s*document\.getElementById\(\s*.*?\)\.style\.display=\s*none.?;\s*<.?/.?script.?>"},
    {'type': 'style', 'pattern': "<div[\S\s]{0,20}style=\s*position\s*:\s*absolute\s*;\s*(?:top|left|right)\s*:\s*-[1-9]+[0-9]{3,}px\s*;\s*(?:top|left|right)\s*:\s*-[1-9]+[0-9]{3,}px\s*;\s*.*?>\s*.*?</div>"},
    {'type': 'style',
     'pattern': "<div\s{0,20}[^>]style\s*=\s*position\s*:\s*absolute\s*;\s*(?:top|left)\s*:\s*expression\([\S\s]*?\).*?>.*?</div>"},
    {'type': 'style',
     'pattern': "<.?div[\S\s]{0,20}style\s*=\s*text-indent\s*:\s*-\d{4,}px.*?<.?/.?div.?>"},
    {'type': 'marquee', 'pattern': "<marquee\s*.(?:(?:width|height)=[0-9]+|scrollamount=[\d]{4,}[^>]*?scrolldelay=[\d]{5,}){1,5}\s*.*?>[\s\S]*?</MARQUEE>"},
    {'type': 'style',
     'pattern': "<.?div\s+style\s*=\s*overflow\s*:\s*hidden\s*;\s*[(?:height|width)\s*:\s*\d*px\s*;]{2,}.*?>[\S\s]*?<.?/.?div.?>"},
    {'type': 'style', 'pattern': "<.?div[\s\S]{0,50}style\s*=[\s\S]{0,50}display:none.*?>.*?<.?/.?div.?>"},
    {'type': 'meta', 'pattern': "<meta.{0,150}url.*?/>"},
    {'type': 'style', 'pattern': "<.?div.{0,20}style.{0,20}visibility\s*:\s*hidden.*?>.*?<.?/.?div.?>"},
    {'type': 'script', 'pattern': "<script.{0,60}>\s*window.location.href=.\S*.*?"},
    {'type': 'iframe', 'pattern': "<iframe[\S\s]{0,20}.*(?:marginwidth|marginheight)\s*=\s*0.*?</iframe>"},
    {'type': 'style', 'pattern': "<div.{0,50}style\s*=.{0,50}position\s*:\s*absolute.{0,100}z-index\s*:.*?<a\s*href.*?</div>"},
    {'type': 'style', 'pattern': "<a\s+href\s*=.{0,50}style\s*=.{0,50}margin-(?:top|left|right)\s*:\s*-\d{2,}.{0,50}"},
    {'type': 'style', 'pattern': "<a\s+href\s*=\s*.{0,50}\s*style\s*=.{0,50}position\s*:\s*absolute.{1,20}(?:top|left)\s*:\s*expression\(.*?\).*?>"},
    {'type': 'style', 'pattern': "<a[\s\S]{1,100}style\s*=[\s\S]{0,100}display\s*:\s*none.*?>"},
    {'type': 'style', 'pattern': "<a.{1,50}style\s*=\s*\s*visibility\s*:\s*hidden.*?>"},
    {'type': 'script', 'pattern': "<.?script.*?>\s*document\.getElementById\(\s*.*?\)\.style\.display=\s*none.?;\s*<.?/.?script.?>\s*<.?div[\S\s]{0,20}id=[\s\S]{0,20}>\s*.*?<.?/.?div.?>"},
]
li = list()
for reg in dark_link_reg:
    reg_list = list()
    reg_list.append(reg['pattern'])
    reg_list.append(reg['type'])
    reg_list = tuple(reg_list)
    li.append(reg_list)
# print(li)

for pattern, dark_type in li:
    print(dark_type)

'(?:\"?|\')(?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|](?:\"?|\')'

# 挂马特征列表
trojReList = [
    {'type': 'iframe', 'stri':
        "<iframe.*?src=\s*.(?:\"?|\')(?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|](?:\"?|\').\s*(?:width=\s*(?:\"?|'|.)[0-9](?:\"?|'|.)|height=\s*(?:\"?|'|.)[0-9](?:\"?|'|.)|frameborder=\s*(?:\"?|'|.)0(?:\"?|'|.)).*?>"},
    {'type': 'document', 'stri': "(?:document?|document\.\s*)\.write\(.<iframe.*?src=\s*(?:\"?|\')(?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|](?:\"?|\').*?>"},
    {'type': 'script', 'stri': "<script.*language=\s*.jscript.encode.*?src=\s*(?:\"?|\')(?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|](?:\"?|\').*?>"},
    {'type': 'body', 'stri': "<body.*onload=\"window\.location=\s*(?:\"?|\')(?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|](?:\"?|\').*?>"},
    {'type': 'top',
     'stri': "top\.document\.body\.innerHTML\s*=.*?(?:\"?|\')<iframe.*?src=\s*.(?:\"?|\')(?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|](?:\"?|\')\s*.*?>(?:\"?|\')"},
    {'type': 'javascript',
     'stri': "javascript\:(?:document|document\.\S*.)\.write\((?:\"?|\')\s*.<script\s+src=\s*.(?:\"?|\')(?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|](?:\"?|\').*?(?:\"?|\')\)"},
    # 还有这种操作？
    {'type': 'window', 'stri': "window\.open\s*\((?:\"?|'|.).*?(?:\"?|\')(?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|](?:\"?|\').*?(?:\"?|'|.)\)"},
    {'type': 'frame',
     'stri': "<frame\s+src=\s*(?:\"?|\')(?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|](?:\"?|\').*?(?:marginwidth=(?:\"?|'|.)0(?:\"?|'|.)|marginheight=(?:\"?|'|.)0(?:\"?|'|.)).*?>"},
    {'type': 'var', 'stri': "var\s*url\s*=\s*(?:\"?|\')(?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|](?:\"?|\')\s*.open\(url.*?NewWindow.*?\)"},
    {'type': 'javascript', 'stri': "javascript\s*:\s*open\(.*(?:\"?|\')(?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|](?:\"?|\').*?\)"},

]