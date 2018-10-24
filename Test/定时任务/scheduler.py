# 第一步 配置config文件
JOBS = [
        {  # 任务1 生成电信报表CSV文件存至阿里文件服务器
            'id': 'job1',
            'func': 'app.main.schedule_task.make_csv_task:generate_csv',  # 第三步py文件所在位置及其方法
            'trigger': 'cron',  # 定点执行任务
            'hour': 0,  # 0点01分
            'minute': 1
        },
        {  # 任务2 定时更新 BUSINESS 表的 signal 字段 使调度任务平均分配
            'id': 'job2',
            'func': 'app.main.schedule_task.update_business:update_signal',
            'trigger': 'interval',  # 计时执行  每隔3600秒
            'seconds': 3600,
            'args': (12,)
        }
    ]


# 第二步 配置init启动文件
from flask_apscheduler import APScheduler
scheduler = APScheduler()
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])  # 从config中读取定时任务的配置
    scheduler.init_app(app)  # 把任务列表放进flask
    scheduler.start()  # 启动任务列表


# 第三步
from app import scheduler
def generate_csv():

    with scheduler.app.app_context():
        # todo
        # 方法体
