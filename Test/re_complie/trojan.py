import re

content="""
        <html><head><title>The Dormouse's story</title>
        <meta http-equiv="refresh" content="1"; url="http://www.baodi.com6" />
        <meta name="xxxx"content="黑链及描述">
        <head>
        </head>
        <script language="JScript.encode" src="https://www.test123.com"></script>
        <body onload="window.location='https://www.baidui.com.cn'">
        <p class="title"><b>The Dormouse's story</b></p>
        <div style="display:none;"><a href = "http://www.baodi.com1">关键字  </a></div>
        <div style="visibility:hidden;"><a href="http://www.baodi.com2">关键字  </a></div>
        <div style="position:absolute; top:-999px;right:-999px;"><a href="http://www.baodi.com3">关键词</a></div> 
        <script>document.write(‘ <d' +' iv st' +' yle' +' =〃 po' +' si' + ' tio' +' n:a' +' bso' +' Iu' +' te ；1' +' ef' +' t:'+'+' 10' +' 00' + ‘0' +' ρ' +' χ；' +〃 “ +' >' ) > X X X X </script>
        XXXX<script>document.write('<'+'d' +'i' +'v>' )</script>
        <script>document.write("'<ifr'+'ame src='http://114.55.36.222/LittleHann/LittleHann.html' width='5' height='5'></iframe>");</script>
        <meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests" URL='http://www.baodi.com22' />
        <marquee height=1 width=4 scrollamount=3000 scrolldelay=20000><a href= "http://www.baodi.com4">关键字</a></marquee>

        <div  style=text-indent:-1213px   ><a href="http://www.baodi.com34"></div>
        <script language="javascript" type="text/javascript"> window.location.href="lianjie";
        window.location.href="lianjie";window.location.href="lianjie";</script>
        <div style="position:absolute;left:expression(s-900);top:expression(3-999);"><a href="http://www.baodi.com">关键词</a></div> 
        <div style="position:absolute; top:-999px;right:-999px;"><a href="http://www.baodi.com8">关键词</a></div> 
        <p class="story">Once upon a time there were three little siers; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
        <a href="http://www.45u.com" style="display:none">
        <a href="http://www.45u.com" style="visibility:hidden">
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        <a href = "http://www.45u.com" style =",,margin-left:-83791; ">
        <a href = "http://www.45u.com" style="position:absolute;left:expression(s-900);top:expression(3-999);">
        window.open('http://www.baodi.com')
        <script>top.document.body.innerHTML="<iframe src="http://www.test456.com" height='5' width='5'></iframe>"</script>
        and they lived at the bottom of a well.</p>
        <frame src="http://www.test789.com" marginwidth="0" marginheight=100></frame>
        <iframe src="http://www.test789.com" height=0 width='5'></iframe>
        <script>
            var url = "http://www.bilibili3.com.cn"
            open(url, "NewWindow", 400, 400)
            </script>
        <script>
            javascript: open("https://www.baidu.com")
        </script>
        <script>document.write("<a href='javascript:document.getElementById('ss').write("<script src="https://bilibili2.com.cn"></script>")'>点击</a>");</script>
        <div class="father" style="position:relative">
       <div class="topLever" style="position:absolute;left:0;top:0;z-index:999; width:90%;height:100px;"> 遮挡层：可以放图片等   <div class="hideDontent"><a href='http://www.baodi.com7'></a></div> 
        </div>
        <div class="topLever"          style="position:absolute;left:0;top:0;z-index:999; width:90%;height:100px;"> 遮挡层：可以放图片等   <div class="hideDontent"><a href='http://www.baodi.com7'></a></div> 
        </div>
        </div>
        <script language="javascript" type="text/javascript">
document.write("'<di'+'v style'+'='displ'+'ay:none;'>");
</script><div>
<a href=http://thief.one>暗链</a>
<script language="javascript" type="text/javascript">
document.write("</div>");
</script>
        <p class="story">...</p>
        <IFRAME src="http://www.baodi.com5" marginWidth=0 marginheight=0  frameBorder=0 width="226" scrolling=no height=3 name="haitan"></iframe>

    """
pattern="""<iframe[\S\s]{0,20}.{0,20}(?:marginwidth|marginheight)\s*=\s*0.*?</iframe>"""

search_pattern = re.compile(pattern, re.I | re.M | re.S)
result = search_pattern.findall(content.replace('"',"").replace("'","").replace("+",""))
print(result)

document="""document.write\(<div style=display:none;>\s*.*?\);[\S\s]*.<a href=\s*%s.*?>[\S\s]*</a>"""
