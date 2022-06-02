# encoding = utf-8

from . import *


@app_admin.route('/admin',methods=['GET','POST'])
def admin():
    if not session:
        session['deng'] = 'weidenglu'
        session['gly'] = 'False'
    if request.method == 'POST' or session.get("gly") == "True":
        if request.method == "POST":
            name = request.form['Name']
        else:
            name = "刷新"
        if name == "提交":
            b = list(client.user.login.find())
            qx = {}
            for i in b:
                qx[i["用户名"]] = request.form[i["用户名"]]
            for c in qx:
                client.user.login.update_one({"用户名": c}, {"$set": {"权限": int(qx[c])}})
            b = list(client.user.login.find())
            a = {}
            for i in b:
                i.pop("_id")
                yym = i["用户名"]
                i.pop("用户名")
                a[yym] = [i[a] for a in i]
            password = {}
            for i in a:
                c = ""
                for aa in a[i][0]:
                    c += chr(aa)
                password[i] = c
            return render_template("admin/admin1.html", user=a, passwordList=password)
        elif name == '刷新':
            b = list(client.user.login.find())
            a = {}
            for i in b:
                i.pop("_id")
                yym = i["用户名"]
                i.pop("用户名")
                a[yym] = [i[a] for a in i]
            password = {}
            for i in a:
                c = ""
                for aa in a[i][0]:
                    c += chr(aa)
                password[i] = c
            return render_template("admin/admin1.html", user=a, passwordList=password)
        elif name[:2] == '删除':
            client.user.login.delete_one({'用户名':name[2:]})
            b = list(client.user.login.find())
            a = {}
            for i in b:
                i.pop("_id")
                yym = i["用户名"]
                i.pop("用户名")
                a[yym] = [i[a] for a in i]
            password = {}
            for i in a:
                c = ""
                for aa in a[i][0]:
                    c += chr(aa)
                password[i] = c
            return render_template("admin/admin1.html", user=a, passwordList=password)
        password = request.form['Password']
        if name in ADMIN_USER:
            if password == ADMIN_USER[name]:
                session['gly'] = 'True'
                b = list(client.user.login.find())
                a = {}
                for i in b:
                    i.pop("_id")
                    yym = i["用户名"]
                    i.pop("用户名")
                    a[yym] = [i[a] for a in i]
                password = {}
                for i in a:
                    c = ""
                    for aa in a[i][0]:
                        c += chr(aa)
                    password[i] = c
                return render_template("admin/admin1.html", user=a, passwordList=password)
            else:
                return render_template('admin/admin.html', text='输入有误')
        else:
            return render_template('admin/admin.html',text='输入有误')
    return render_template('admin/admin.html')

@app_admin.route('/admin1/<user_name>')
def user_id(user_name):
    if not session:
        session['deng'] = 'weidenglu'
        session['gly'] = 'False'
    if session["gly"] == "True":
        nik = client.user.login.find_one({"用户名":user_name})
        if nik != None:
            passwordList = nik["密码"]
            password = ""
            for i in passwordList:
                password += chr(i)
            if nik["邮箱"] != "":
                num = 1
            else:
                num = 2
            return render_template("admin/admin2.html",user_name=user_name,user=nik,password=password,num=num)
    abort(404)