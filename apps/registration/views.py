# encoding = utf-8

from . import *


@app_registration.route('/registration',methods=['GET','POST'])
def registration():
    if not session:
        session['deng'] = 'weidenglu'
        session['gly'] = 'False'
    if request.method == 'POST':
        userName = request.form['Name']
        userPassword = request.form['Password']
        userPassword2 = request.form['Password2']
        db = client.user
        s = db.login.find_one({"用户名":userName})
        if s != None or userName == "提交":
            return render_template('registration/registration.html',text='用户已存在',userPassword2=userPassword2,userPassword=userPassword,userName=userName)
        elif userPassword != userPassword2:
            return render_template('registration/registration.html',text='两次输入的密码不一致',userPassword2=userPassword2,userPassword=userPassword,userName=userName)
        elif userName.isspace():
            return render_template('registration/registration.html',text='用户名不能为空',userPassword2=userPassword2,userPassword=userPassword,userName=userName)
        elif userPassword.isspace() or userPassword.isspace():
            return render_template('registration/registration.html',text='密码不能为空',userPassword2=userPassword2,userPassword=userPassword,userName=userName)
        else:
            passwordList = []
            for i in userPassword:
                d = ord(i)
                passwordList.append(d)
            i = list(client.user.login.find())
            ipList = []
            for i in i:
                ipList.append(i["用户id"])
            ip = ''
            while True:
                for i in range(15):
                    ip += random.choice("1234567890QERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm@&")
                if ip not in ipList:
                    break
            a = {
                "用户名":userName,
                "密码":passwordList,
                "权限":1,
                "用户id":ip,
                "生日" : "",
                "年龄":"",
                "简介" : "",
                "手机号" : "",
                "地址" : "",
                "邮箱" : "",
                "爱好":[],
                "历史记录" : []
            }
            client.user.login.insert_one(a)
            session['wy'] = "注册成功请登录"
            return redirect("/login")
    return render_template('registration/registration.html')