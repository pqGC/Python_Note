import csv
import os
import datetime as dt
from ftplib import FTP

basedir = os.path.abspath(os.path.dirname(__file__))
# csv根目录
basedir = os.path.join(basedir, "csv")
# 年目录
year = dt.datetime.now().strftime("%Y")
y_basedir = os.path.join(basedir, "{}年".format(year))
# 月目录
month = dt.datetime.now().strftime("%m")
m_basedir = os.path.join(y_basedir, "{}月".format(month))
# 日目录
day = dt.datetime.now().strftime("%d")
d_basedir = os.path.join(m_basedir, "{}日".format(day))

# 创建多层目录
if not os.path.exists(basedir):
    os.makedirs(basedir)
if not os.path.exists(y_basedir):
    os.makedirs(y_basedir)
if not os.path.exists(m_basedir):
    os.makedirs(m_basedir)
if not os.path.exists(d_basedir):
    os.makedirs(d_basedir)

fp = open(d_basedir, 'rb')
print(fp)


# 链接ftp服务器
def ftp_connect(ip, port, username, password):
    ftp = FTP()
    # ftp.set_debuglevel(2)
    ftp.connect(ip, port)
    ftp.login(username, password)
    return ftp


# 从本地上传文件到ftp
def upload_file(ftp, local_path, generate_time):
    bufsize = 1024
    ftp.cwd('/ftp')
    # ftp.mkd('/' + generate_time)
    for root, dirnames, filename in os.walk(local_path):
        for file in filename:
            fp = open(os.path.join(root, file), 'rb')  # fp本地文件地址   file文件名
            ftp.storbinary('STOR %s' % file, fp, bufsize)
            ftp.set_debuglevel(0)
            fp.close()
    print("已上传至FTP服务器")
