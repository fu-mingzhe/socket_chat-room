# encoding = utf-8

from . import *

@app_login.route('/login',methods=['GET','POST'])
def login():
    if session.get('gly') == None:
        session['gly'] = 'False'
    if session.get('deng') == None:
        session['deng'] = 'weidenglu'
    if request.method == 'POST':
        userName = request.form['Name']
        userPassword = request.form['Password']
        db = client.user
        s = db.login.find_one({"用户名":userName})
        if s != None:
            passwordl = s["密码"]
            Password = ''
            for i in passwordl:
                a = chr(i)
                Password += a
            if userPassword == Password:
                if s["权限"] == 3:
                    session['deng'] = "yidenglu"
                    session['userName'] = userName
                    info = 0
                    email = 0
                    ad = client.user.login.find_one({"用户名":session["userName"]})
                    if ad["生日"] == "":
                        info = 1
                    if ad["邮箱"] == "":
                        email = 1
                    return render_template('login/h.html',t=1,name='欢迎'+session['userName']+'登录',user_name=session["userName"],info=info,email=email)
                else:
                    if s["权限"] == 1:
                        return render_template('login/login.html',text='您的账号未开通使用权限!',text1='请联系管理员~',password=userPassword,username=userName)
                    elif s["权限"] == 2:
                        return render_template('login/login.html',text='您的账号由于某种原因已被查封!!!',password=userPassword,username=userName)
            else:
                return render_template('login/login.html',text='账号或密码错误',password=userPassword,username=userName)
        else:
            return render_template('login/login.html',text='账号或密码错误',password=userPassword,username=userName)
    if session.get('wy') == None:
        return render_template('login/login.html')
    else:
        wy = session["wy"]
        session.pop("wy")
        return render_template('login/login.html',text=wy)


@app_login.route("/login_t")
def login_t():
    if session.get('gly') == None:
        session['gly'] = 'False'
    if session.get('deng') == None:
        session['deng'] = 'weidenglu'
        abort(404)
    session.pop("userName")
    session["gly"] = 'False'
    session["deng"] = "weidenglu"
    session['wy'] = "您已成功退出登录"
    return redirect("/login")

@app_login.route('/zx_login',methods=["GET","POST"])
def zx_login():
    if session.get('gly') == None:
        session['gly'] = 'False'
    if session.get('deng') == None:
        session['deng'] = 'weidenglu'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        if request.method == "POST":
            cc = client.user.login.find_one({"用户名":session["userName"]})
            li = ""
            for i in cc["密码"]:
                li += chr(i)
            if li == request.form['Password']:
                client.user.login.delete_one({"用户名":session["userName"]})
                session['deng'] = 'weidenglu'
                session['gly'] = 'False'
                session["wy"] = "注销成功"
                return redirect("/login")
            else:
                return render_template("login/zx.html",name=session['userName'],text="密码错误")
        return render_template("login/zx.html",name=session["userName"])
    else:
        return redirect("/login")

@app_login.route('/x_password',methods=["GET","POST"])
def x_password():
    if session.get('gly') == None:
        session['gly'] = 'False'
    if session.get('deng') == None:
        session['deng'] = 'weidenglu'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        if request.method == "POST":
            cc = client.user.login.find_one({"用户名":session['userName']})
            yuan = request.form["Name"]
            p1 = request.form["Password"]
            p2 = request.form["Password2"]
            li = ""
            for i in cc["密码"]:
                li += chr(i)
            if yuan == li:
                if p1 == p2:
                    passwordList = []
                    for i in p1:
                        d = ord(i)
                        passwordList.append(d)
                    client.user.login.update_one({"用户名":session["userName"]},{"$set":{"密码":passwordList}})
                    return render_template('login/h.html',name='修改密码成功',user_name=session["userName"],t=1)
                else:
                    return render_template('login/x_password.html', text="两次输入的新密码不一致", userName=yuan, userPassword=p1,name=session['userName'],userPassword2=p2)
            else:
                return render_template('login/x_password.html',text="原密码错误",userName=yuan,userPassword=p1,userPassword2=p2,name=session['userName'])
        return render_template("login/x_password.html",name=session['userName'])
    else:
        return redirect("/login")
