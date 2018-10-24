# -*- coding: utf-8 -*-
import http.client


def send_message(data_time, file_name, file_path):
    file_name = ',\n\t'.join(file_name)
    # 报文内容
    soap_message = '''已生成{datetime}的csv文件,
文件名：{file_name}
请至{file_path}下载'''.format(datetime=data_time, file_name=file_name, file_path=file_path)
    soap_message = soap_message.encode()
    # 使用的WebService地址为http://116.62.102.44:8181/portal/services/CloudShieldService?wsdl
    webservice = http.client.HTTPConnection("116.62.102.44:8181")
    # 连接到服务器后的第一个调用。它发送由request字符串到到服务器
    webservice.putrequest("POST", "/portal/services/CloudShieldService")
    webservice.putheader("Host", "116.62.102.44:8181")
    webservice.putheader("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
    webservice.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
    webservice.putheader("Content-length", "%d" % len(soap_message))
    webservice.putheader("SOAPAction", "\"http://116.62.102.44:8181/portal/services/CloudShieldService\"")
    # 发送空行到服务器，指示header的结束
    webservice.endheaders()
    # 发送报文数据到服务器
    webservice.send(soap_message)
    # 获取返回HTTP 响应信息
    res = webservice.getresponse()
    return res


if __name__ == '__main__':
    code = send_message('2018-08-30', ['测试文件'], r'\ftp\2018-08-30')
    print(code.status, code.reason)
    print(code.read().decode('utf-8'))

