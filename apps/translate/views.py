# encoding = utf-8

from apps.translate import *


def translate(_from,to,text):
    if text == "":
        return ""
    languageDict = {'自动检测':0,'中文':1,'英文':2,'日文':3,'韩文':4,'法文':5,'西班牙文':6,'葡萄牙文':7,'德文':8,'意大利文':9,'俄文':10}
    data = {
        "text":text,
        "from":languageDict[_from],
        "to":languageDict[to]
    }
    r = requests.post('https://www.yuanfudao.com/ada-student-app-api/api/translate',data=data).json()
    return r["result"]


@app_translate.route('/translation')
def Translation():
    if session.get('gly') == None:
        session['gly'] = 'False'
    if session.get('deng') == None:
        session['deng'] = 'weidenglu'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history(session['userName'], request.url)
        b = ['中文','英文','日文','韩文','法文','西班牙文','葡萄牙文','德文','意大利文','俄文']
        return render_template('translate/Translation.html', ty=2, list=b,user_name=session["userName"]),200
    else:
        return redirect("/login")

@app_translate.route('/check_translation')
def check_translation():
    if session.get('gly') == None:
        session['gly'] = 'False'
    if session.get('deng') == None:
        session['deng'] = 'weidenglu'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history(session['userName'], request.url)
        b = ['中文','英文','日文','韩文','法文','西班牙文','葡萄牙文','德文','意大利文','俄文']
        nr1 = request.args.get('nr')
        _from = request.args.get("from")
        to = request.args.get('to')
        if nr1.isspace():
            return render_template("translate/Translation.html",ty=1,n=nr1,nr="",list=b,list1=['自动检测']+b,to=to,user_name=session['userName'],a=1)
        if nr1 != None and _from != None and to != None:
            nr = translate(_from,to,nr1)
            # if to == "中文" or to == "英文":
            #     url = "./static/audio/user/{name}".format(name=session["userName"])
            #     if not os.path.exists(url):
            #         os.makedirs(url)
            #     lis = os.listdir(url)
            #     l = []
            #     for i in lis:
            #         l.append(i.split(".")[0])
            #     if l != []:
            #         count = str(int(l[-1])+1)
            #         speech.t2v(nr,"./static/audio/user/{name}/{count}.wav".format(name=session['userName'],count=count))
            #     else:
            #         count = 0
            #         speech.t2v(nr,"./static/audio/user/{name}/0.wav".format(name=session['userName']))
            #     return render_template("translate/Translation.html",ty=1,n=nr1,nr=nr,list=b,list1=['自动检测']+b,_from=_from,user_name=session['userName'],count=count,a=0)
            return render_template("translate/Translation.html",ty=1,n=nr1,nr=nr,list=b,list1=['自动检测']+b,to=to,user_name=session['userName'],a=1)
        else:
            abort(404)
    else:
        return redirect("/login")