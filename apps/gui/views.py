# encoding = utf-8

from . import *


@app_gui.route('/set_history',methods=["GET","POST"])
def set_history():
    userName = request.form.get('userName')
    text = request.form.get('Text')
    if userName != None and text != None:
        st = client.user.login.find_one({'用户名':userName})
        if st != None:
            h = st['历史记录']
            h.append(text)
            client.user.login.update_one({"用户名": userName}, {"$set": {"历史记录": h}})
            return ""
        else:
            abort(404)
    else:
        abort(404)