import schedule
import time
# ----这只是一个简单的案例，具体实现百度 flask scheduler 查看在flask任务中是如何启动的-------#
#  https://blog.csdn.net/blueheart20/article/details/70219411  #


def job():
    print("I'm working...")


schedule.every(5).seconds.do(job)
schedule.every(1).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("13:48").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(10)

