import uuid
import base64
import oss2
import os

_access_key_id = os.getenv('OSS_TEST_ACCESS_KEY_ID', 'LTAIcqcnkprmyOHL')
_access_key_secret = os.getenv('OSS_TEST_ACCESS_KEY_SECRET', 'Z5204FvZSNVFclLv6EHFx58Y8p5LpG')
_bucket_name = os.getenv('OSS_TEST_BUCKET', 'njza-csv')
_endpoint = os.getenv('OSS_TEST_ENDPOINT', 'https://oss-cn-shanghai.aliyuncs.com/')
bucket = oss2.Bucket(oss2.Auth(_access_key_id, _access_key_secret), _endpoint, _bucket_name)


def get_sign_url(file_name, expires_time=3600):
    try:
        sign_url = bucket.sign_url('GET', file_name, expires_time)
    except KeyError:
        sign_url = 0
    return sign_url


def upload_file_to_oss(file_name, remote_name, file_path):
    # 开始上传文件并添加header
    try:
        with open(file_path, 'rb') as file_obj:
            headers = {'Content-Disposition': 'filename={}'.format(file_name).encode('utf-8')}
            file_obj.seek(0, os.SEEK_SET)
            result = bucket.put_object(remote_name, file_obj, headers=headers)
            res = result.status
    except Exception as e:
        print(e)
        res = 500
    return res


def get_name(file_name):
    # 根据文件名生成新的UUID文件名
    u = base64.b64encode(bytes(str(uuid.uuid1()), encoding="utf-8") + bytes(str(uuid.uuid4()), encoding="utf-8"))
    ls = file_name.split(".")
    ext = ""
    try:
        ext = ls[-1]
    except TypeError:
        pass
    new_name = "%s.%s" % (str(u, encoding="utf-8"), ext)
    return new_name


def upload_report_object(file_name, file_path):
    # 上传报表方法
    new_file_name = get_name(file_name)
    res = upload_file_to_oss(file_name, new_file_name, file_path)
    if res == 200:
        return new_file_name
    else:
        return ''