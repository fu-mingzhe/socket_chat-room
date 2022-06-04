# encoding = utf-8

from . import *


@app_test.route('/index1')
def index1():
    if session.get('gly') == None:
        session['gly'] = 'False'
    if session.get('deng') == None:
        session['deng'] = 'weidenglu'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history()
        number = random.randint(0,9)
        return render_template('test/test02.html', t_number=number, t_name=session['userName']),200
    else:
        return redirect("/login")

