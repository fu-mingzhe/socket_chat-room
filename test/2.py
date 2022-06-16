from flask import *


app = Flask(__name__)
app.secret_key = "1312jfjasdjfa"


@app.route('/')
def index():
    session["1"] = ["1","2"]
    return "<head><script src='https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js'></script></head><body>Hello</body>"

@app.route("/1",methods=["GET","POST"])
def d():
    if request.method == "POST":
        return (request.form["name"],request.form['url'])
    print(session["1"])
    return "2"

if __name__ == '__main__':
    app.run(debug=True)