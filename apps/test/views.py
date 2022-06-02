# encoding = utf-8

from . import *


@app_test.route('/index1')
def index1():
    if not session:
        session['deng'] = 'weidenglu'
        session['gly'] = 'False'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history()
        number = random.randint(0,9)
        return render_template('test/test02.html', t_number=number, t_name=session['userName']),200
    else:
        return redirect("/login")

@app_test.route('/welcome')
def welcome():
    if not session:
        session['deng'] = 'weidenglu'
        session['gly'] = 'False'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history()
        now = time.localtime()
        now_time = time.strftime('%Y-%m-%d %H:%M:%S', now)
        return render_template('test/welcome.html', t_time=now_time),200
    else:
        return redirect("/login")

@app_test.route('/quiz')
def quiz():
    if not session:
        session['deng'] = 'weidenglu'
        session['gly'] = 'False'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history()
        return render_template('test/quiz.html'),200
    else:
        return redirect("/login")

@app_test.route('/home')
def home():
    if not session:
        session['deng'] = 'weidenglu'
        session['gly'] = 'False'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history("/login")
        return render_template('test/home.html'),200
    else:
        return redirect("/login")

@app_test.route('/task')
def task():
    if not session:
        session['deng'] = 'weidenglu'
        session['gly'] = 'False'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history()
        return render_template('test/task.html'),200
    else:
        return redirect("/login")

