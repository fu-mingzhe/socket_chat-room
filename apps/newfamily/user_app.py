# encoding = utf-8

from main_settings import *
from flask import *
import pymongo

# 创建蓝图对象
user_app = Blueprint('user_app',__name__)
# 设置 session 秘钥
user_app.secret_key = key

# 创建数据库客户端
client = pymongo.MongoClient()
db = client.ybc

# 路由：访问“注册页面”
@user_app.route('/new_register')
def register():
    # 返回“注册页面”
    return render_template('newfamily/user/register.html')


# 路由：实现注册功能
@user_app.route('/register_check', methods=['POST'])
def register_check():
    username = request.form['username']
    pwd = request.form['password']
    # 查询是否已注册
    result = db.user.find_one({'username': username})
    # 如果未注册
    if result == None:
        # 添加一条用户信息
        user = {'username': username, 'password': pwd}
        db.user.insert_one(user)
        # 注册成功，返回到“登录页面”
        return render_template('newfamily/user/login.html')
    # 否则就已注册
    else:
        # 返回“注册页面”和“提示信息”
        return render_template('newfamily/user/register.html',
                               t_error='此账号已注册')


# 路由：返回登录页面”
@user_app.route('/new_login')
def login():
    # 返回“登陆页面”
    return render_template('newfamily/user/login.html')


# 路由：实现登录功能
@user_app.route('/login_check', methods=['POST'])
def login_check():
    # 通过表单获取用户登录数据
    username = request.form['username']
    pwd = request.form['password']
    # 查询用户信息是否注册
    result = db.user.find_one({'username': username, 'password': pwd})

    # 如果未注册
    if result == None:
        # 返回提示
        return render_template('newfamily/user/login.html', t_error='账号或密码错误')

    # 否则已注册
    else:
        # 用户名存入session，进入空间主页
        session['username'] = username
        href = session.get('href')
        if href == 'home':
            return redirect('/home')
        elif href == 'task':
            return redirect('/task')

# 路由：退出登录
@user_app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/')