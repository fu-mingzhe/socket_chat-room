# encoding = utf-8

from . import *


@app_index.route('/',methods=['GET','POST'])
def index():
    if not session:
        session['deng'] = 'weidenglu'
        session['gly'] = 'False'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history()
        ad = client.user.login.find_one({"用户名":session["userName"]})
        age = ad["邮箱"]
        if age == "":
            return render_template('index/h1.html',user_name=session["userName"])
        return render_template('index/h.html',user_name=session["userName"]),200
    else:
        return redirect("/login")

@app_index.route('/user/<name>')
def user_name(name):
    if name == session.get("userName"):
        user = client.user.login.find_one({"用户名":name})
        return render_template("index/user_name.html",name=name,user=user)
    else:
        abort(404)

@app_index.route('/Personal_Information',methods=["GET","POST"])
def Personal_Information():
    if not session:
        session['deng'] = 'weidenglu'
        session['gly'] = 'False'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history()
        if request.method == "POST":
            sr = request.form['sr']
            phone = request.form['phone']
            email = request.form['email']
            dz = request.form['dz']
            grjj = request.form['grjj']
            f = sr.split('-')
            year = f[0]
            month = f[1]
            day = f[2]
            age = int((datetime.date.today() - datetime.date(int(year),int(month),int(day))).days/365)
            a = client.user.login.find_one({"用户名":session["userName"]})
            a["生日"] = sr
            a["手机号"] = phone
            a["年龄"] = str(age)
            a["简介"] = grjj
            a["邮箱"] = email
            a["地址"] = dz
            client.user.login.update_one({"用户名":session["userName"]},{"$set":a})
            return render_template('index/h.html',name="个人信息填写成功!",user_name=session["userName"],t=1)
        return render_template('index/Personal_Information.html',type=1)
    else:
        return redirect("/login")

@app_index.route('/x_Personal_Information')
def x_Personal_Information():
    if not session:
        session['deng'] = 'weidenglu'
        session['gly'] = 'False'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history()
        cir = client.user.login.find_one({"用户名":session['userName']})
        return render_template("index/Personal_Information.html",name=session['userName'],cir=cir,type=2)
    else:
        return redirect("/login")

@app_index.route('/birthday')
def birthday():
    if not session:
        session['deng'] = 'weidenglu'
        session['gly'] = 'False'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history()
        return render_template('index/birthday.html',user_name=session["userName"]),200
    else:
        return redirect("/login")