import csv
import os
import datetime as dt

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

file = os.path.join(d_basedir, "test-20180822.txt")
write = open(file, 'w', newline='', encoding='utf-8')
csv_write = csv.writer(write, delimiter=',')
dark_link_head = ['目标url', 'HTML特征target_url', '类型dark_type']
csv_write.writerow(dark_link_head)


for root, dirnames, filename in os.walk(basedir):
    for file in filename:
        print(file)
        print(os.path.join(root, file))


# csv路径操作
from flask import make_response
import mimetypes
# csv根目录
basedir = os.path.join(basedir, "csv")

def show_csv(date_time):
    path = get_path(date_time=date_time)
    global file_dict
    file_list = []
    for root, dirnames, filenames in os.walk(path):
        for file in filenames:
            file_dict = dict()
            file_dict['filename'] = file
            file_dict['file_path'] = os.path.join(root, file)
            file_list.append(file_dict)
    return return_list_json(200, 'csv文件', 1, 200, file_list)

def download_file(filename):
    try:
        url = get_path(csv_name=filename)
        r = requests.get(url, timeout=500)
        if r.status_code != 200:
            return return_json(0, 'Cannot connect with oss server or file is not existed', 200)
        response = make_response(r.content)
        mime_type = mimetypes.guess_type(filename)[0]
        response.headers['Content-Type'] = mime_type
        # response.headers['Content-Disposition'] = 'attachment; filename={}'.format(filename.encode().decode('latin-1'))
        return response
    except Exception as err:
        return return_json(0, 'download_file error: {}'.format(str(err)), 200)


# 根据csv文件名/日期 获取文件所在路径
def get_path(csv_name=None, date_time=None):
    if csv_name is not None:
        get_data = csv_name.split("-")[1]
        y_data = get_data[:4]  # 年份
        m_data = get_data[4:6]  # 月
        d_data = get_data[6:8]  # 日
    else:
        get_data = date_time.split("-")
        y_data = get_data[0]  # 年份
        m_data = get_data[1]  # 月
        d_data = get_data[2]  # 日
    y_basedir = os.path.join(basedir, "{}年".format(y_data))
    m_basedir = os.path.join(y_basedir, "{}月".format(m_data))
    d_basedir = os.path.join(m_basedir, "{}日".format(d_data))
    if csv_name is not None:
        path = os.path.join(d_basedir, csv_name)
        return path
    else:
        return d_basedir

