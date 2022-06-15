# encoding = utf-8

from . import *

@app_other.route("/other")
def other():
    if session.get('gly') == None:
        session['gly'] = 'False'
    if session.get('deng') == None:
        session['deng'] = 'weidenglu'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history()
        color_list = ["is-primary","is-link","is-info","is-success","is-warning","is-danger"]
        random.shuffle(color_list)
        color_list = color_list[:3]
        num = 0
        for i in URL_DICT:
            URL_DICT[i] = [URL_DICT[i],color_list[num]]
            num += 1
            if num+1 > len(color_list):
                num = 0
        return render_template('other/other.html',user_name=session["userName"],url_dict=URL_DICT),200
    else:
        return redirect("/login")

@app_other.route("/Garbage_sorting",methods=["GET","POST"])
def Garbage_sorting():
    if session.get('gly') == None:
        session['gly'] = 'False'
    if session.get('deng') == None:
        session['deng'] = 'weidenglu'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history()
        if request.method == "POST":
            Garbage = request.form.get("Garbage")
            r = requests.get("https://api.vvhan.com/api/la.ji?lj="+Garbage).json()
            return render_template('other/Garbage_sorting.html',ty=1,name=r['name'],sorting=r['sort']),200
        return render_template('other/Garbage_sorting.html'),200
    else:
        return redirect("/login")

@app_other.route("/moyu")
def moyu():
    if session.get('gly') == None:
        session['gly'] = 'False'
    if session.get('deng') == None:
        session['deng'] = 'weidenglu'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history()
        c = (eval(requests.get("https://api.vvhan.com/api/moyu?type=json").text.replace("true","True"))['url']).replace("\\/","/")
        return render_template("other/moyu.html",url=c),200
    else:
        return redirect("/login")

@app_other.route("/douyin",methods=["GET","POST"])
def douyin():
    if session.get('gly') == None:
        session['gly'] = 'False'
    if session.get('deng') == None:
        session['deng'] = 'weidenglu'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history()
        if request.method == "POST":
            type = request.form.get("type")
            r = requests.get("http://api.weijieyue.cn/api/douyin/api.php?n="+type)
            img_url = ""
            for i in r.text.split("±")[1].split("=")[1:]:
                img_url+="="+i
            img_url = img_url[1:]
            video_url = r.text.split("：")[-1]
            text = r.text.split("\n")[1].split("：")[1]
            return render_template("other/douyin.html",t=1,nameList=NAMELIST,video_url=video_url,img_url=img_url,text=text,type=type)
        return render_template("other/douyin.html",nameList=NAMELIST)
    else:
        return redirect("/login")
