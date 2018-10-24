from selenium.webdriver.common import utils
from selenium import webdriver
import os
import platform


def get_phantom_driver():
    """
    为了访问 https 请尝试以下两种方案

    service_args=['--ignore-ssl-errors=true']
    or
    service_args=['--ssl-protocol=any']

    driver_path 在配置文件已封装成 get_driver_path 方法, 不同操作系统下调用会返回对应的驱动路径
    然后返回对应操作系统的可用 driver

    If you want to run the program with the browser invisible, install this
    selenium==2.48.0
    注: 新版 selenium 已经不再支持 此 js 工具 , 此处为程序可以运行在没有图形化界面的linux服务器上而选择 PhantomJS

    :return:
    """
    while True:
        # 确保生成可用的 driver 后才结束循环
        try:
            free_port = utils.free_port()
            driver = webdriver.PhantomJS(executable_path=get_phantom_driver_path(),
                                         service_args=["--ignore-ssl-errors=true"],
                                         port=free_port)
            return driver
        except Exception as e:
            print(str(e))
            continue


def get_phantom_driver_path():
    """
    返回相对应操作系统的 phantom驱动文件的路径
    :return:
    """
    basedir = os.path.abspath(os.path.dirname(__file__))

    # 为各个操作系统配上不同的驱动
    all_drivers = {
                    'windows': os.path.join(basedir, 'phantom', 'phantomjs-2.1.1-windows', 'bin', 'phantomjs.exe'),
                    'mac': os.path.join(basedir, 'phantom', 'phantomjs-2.1.1-macosx', 'bin', 'phantomjs'),
                    'linux': os.path.join(basedir, 'phantom', 'phantomjs-2.1.1-linux-x86_64', 'bin', 'phantomjs')
                }

    # 判断操作系统
    sys_str = str(platform.uname()).lower()
    sys_type = 'windows' if 'windows' in sys_str else ('linux' if 'linux' in sys_str else 'mac')

    # 取出适合当前操作系统的驱动类型
    driver_path = all_drivers.get(sys_type)
    return driver_path
