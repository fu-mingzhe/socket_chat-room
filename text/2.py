from flask import *
import pymongo


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
client = pymongo.MongoClient()


@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        passwordList = []
        for i in password:
            passwordList.append(ord(i))
        a = client.user.login.find_one({"用户名":name,"密码":passwordList})
        if a == None:
            return render_template('2.html',text="用户名或密码错误")
        else:
            session["denglu"] = "yidenglu"
            return "<h1>登陆成功成功</h1><br><a href=\"/\">前往主页</a>"
    return render_template('2.html')

@app.route("/")
def index():
    if not session:
        session["denglu"] = "weidenglu"
    if session.get("denglu") == "yidenglu":
        return "访问成功"
    else:
        return redirect("login")

if __name__ == '__main__':
    app.run(debug=True,port=1111,host="192.168.1.13")