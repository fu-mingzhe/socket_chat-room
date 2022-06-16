# encoding = utf-8

from . import *


@app_index.route('/',methods=['GET','POST'])
def index():
    if session.get('gly') == None:
        session['gly'] = 'False'
    if session.get('deng') == None:
        session['deng'] = 'weidenglu'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history()
        phone = 0
        email = 0
        ad = client.user.login.find_one({"用户名":session["userName"]})
        if ad["年龄"] == "":
            phone = 1
        if ad["邮箱"] == "":
            email = 1
        return render_template('index/h.html',user_name=session["userName"],info=phone,email=email),200
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
    if session.get('gly') == None:
        session['gly'] = 'False'
    if session.get('deng') == None:
        session['deng'] = 'weidenglu'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history()
        if request.method == "POST":
            sr = request.form['sr']
            phone = request.form['phone']
            dz = request.form['dz']
            grjj = request.form['grjj']
            date = sr.split('-')
            year = date[0]
            month = date[1]
            day = date[2]
            age = int((datetime.date.today() - datetime.date(int(year),int(month),int(day))).days/365)
            a = client.user.login.find_one({"用户名":session["userName"]})
            a["生日"] = sr
            a["手机号"] = phone
            a["年龄"] = str(age)
            a["简介"] = grjj
            a["地址"] = dz
            client.user.login.update_one({"用户名":session["userName"]},{"$set":a})
            return render_template('index/h.html',name="个人信息填写成功!",user_name=session["userName"],t=1)
        return render_template('index/Personal_Information.html',type=1)
    else:
        return redirect("/login")

@app_index.route('/x_Personal_Information')
def x_Personal_Information():
    if session.get('gly') == None:
        session['gly'] = 'False'
    if session.get('deng') == None:
        session['deng'] = 'weidenglu'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history()
        cir = client.user.login.find_one({"用户名":session['userName']})
        return render_template("index/Personal_Information.html",name=session['userName'],cir=cir,type=2)
    else:
        return redirect("/login")

@app_index.route('/birthday')
def birthday():
    if session.get('gly') == None:
        session['gly'] = 'False'
    if session.get('deng') == None:
        session['deng'] = 'weidenglu'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history()
        return render_template('index/birthday.html',user_name=session["userName"]),200
    else:
        return redirect("/login")


@app_index.route("/email",methods=["GET","POST"])
def email():
    if session.get('gly') == None:
        session['gly'] = 'False'
    if session.get('deng') == None:
        session['deng'] = 'weidenglu'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history()
        if request.method == "POST":
            v = request.form["v"]
            e = request.form["email"]
            if session.get("verification") != None:
                if session["verification"][1] == v:
                    user = client.user.login.find_one({"用户名":session["userName"]})
                    user["邮箱"] = session["verification"][0]
                    client.user.login.update_one({"用户名":session["userName"]},{"$set":user})
                    em = session["verification"][0]
                    session.pop("verification")
                    return render_template("index/h.html",t=1,name="恭喜您成功绑定邮箱:"+em,user_name=session["userName"])
                else:
                    return render_template("index/email.html",text="验证码有误",e=session["verification"][0],ve=v)
            else:
                return render_template("index/email.html",text="请先点击发送验证码",e=e,ve=v)
        return render_template("index/email.html")
    else:
        return redirect("/login")

@app_index.route("/email_send",methods=["GET","POST"])
def email_send():
    if session.get('gly') == None:
        session['gly'] = 'False'
    if session.get('deng') == None:
        session['deng'] = 'weidenglu'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history()
        if request.method == "POST":
            email = request.form["email"]
            send_email(email,session['userName'])
            return ""
        abort(404)
    else:
        return redirect("/login")

