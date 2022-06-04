# encoding = utf-8

import time
from flask import *
from main_settings import *
import pymongo
from .quiz_app import quiz_app
from .home_app import home_app
from .task_app import task_app
from .user_app import user_app

app_newfamily = Blueprint("main_newfamily",__name__)
app_newfamily.secret_key = key

# 【提示3】把蓝图注册到web程序中(home_app、task_app、user_app)
app_newfamily.register_blueprint(quiz_app)
app_newfamily.register_blueprint(home_app)
app_newfamily.register_blueprint(task_app)
app_newfamily.register_blueprint(user_app)



# 创建数据库客户端
client = pymongo.MongoClient()
db = client.ybc


@app_newfamily.route('/welcome')
def welcome1():
    # 获取当前系统的时间
    now = time.localtime()
    # 转化日期格式
    date_time = time.strftime('%Y-%m-%d %H:%M', now)
    return render_template('newfamily/main/welcome.html',
                           t_time=date_time)

