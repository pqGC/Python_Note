from app.main.utils.util import return_json
from app.main import main
from app.main.views.auth import permission
from flask import request
from app.main.nosql.redis_conn import RedisCache
from app.main.views.verifycode.captcha import *
import base64


@main.route('/verify-code/verify-code/', methods=['POST'])
def verify_code():
    try:
        ver_code = request.json['ver_code']
        ver_code_id = request.json['ver_code_id']
    except KeyError as e:
        return return_json(0, '请输入验证码' + str(e), 200)

    # 从redis中取出uuid对应的验证码内容
    redis_code = RedisCache().get_data('pic_code_%s' % ver_code_id)
    if redis_code['result'] is None:
        return return_json(0, '验证码过期，请点击更换验证码', 200)
    else:
        redis_code = redis_code['result'].decode("utf-8")

    if ver_code == redis_code:
        return return_json(1, '验证成功', 201)
    else:
        return return_json(0, '验证失败', 200)


@main.route('/verify-code/change-code/', methods=['GET'])
def change_code():
    """
    点击改变验证码
    :return:
    """
    pre_uuid = request.values.get('pre_uuid', '', type=str)  # 初始验证码的id
    cur_uuid = request.values.get('cur_uuid')  # 当前验证码的id

    name, text, pic = captcha.generate_captcha()

    if pre_uuid:  # 若存在上一个验证码，则删除该验证码
        RedisCache().del_data('pic_code_%s' % pre_uuid)
    RedisCache().set_data_expire('pic_code_%s' % cur_uuid, text)  # 插入当前验证码

    res = base64.b64encode(pic)  # pic为返回图片的字节流，对其进行base64

    res_dict = dict()
    res_dict['pic'] = "data:image/jpg;base64," + res.decode("utf-8")  # 这一步操作后，前台获取这个值后加在src后就可显示图片

    return return_json(1, '验证码', 200, res_dict)



