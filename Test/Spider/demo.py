from Spider.commons import *
from datetime import datetime
from time import sleep


def count_exec_time(fun):
    """
    装饰器
    计算程序执行所花费时间
    :param fun:
    :return:
    """
    def wrapper(*args, **kwargs):
        before = datetime.now()
        print(str(datetime.now()).split(' ')[1], '函数', fun.__name__, ' 开始执行!')
        try:
            return_data = fun(*args, **kwargs)
        except Exception as e:
            print('函数', fun.__name__, ' 执行出现异常-->', str(e))
            return_data = None
        after = datetime.now()
        print(str(datetime.now()).split(' ')[1], '函数', fun.__name__, ' 执行完成，耗时：', str(after-before))
        return return_data
    return wrapper


@count_exec_time
def selenium_task(address):
    # driver = get_chrome_driver(headless=False)
    driver = get_phantom_driver()
    script = "var page = this; page.onResourceError = function(res) {page.browserLog.push({'url': res.url, 'status': res.status});};"
    driver.command_executor._commands['executePhantomScript'] = ('POST', '/session/$sessionId/phantom/execute')
    driver.execute('executePhantomScript', {'script': script, 'args': []})

    driver.get(address)
    title = driver.title
    print('title-->'+title)
    print(address,  '-->', driver.current_url)
    # print(driver.page_source)
    # print(driver.get_log('browser'))

    har = driver.get_log('har')[0]['message']
    message = eval(har)
    print(message)

    for k, v in message.items():
        print(k)
        print(v)
        print()
        print('-'*40)
        print()

    driver.quit()
    return title


if __name__ == '__main__':
    url = 'http://www.lqzxyey.com'
    selenium_task(url)
