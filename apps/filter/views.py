# encoding = utf-8

from . import *


l = ['假日', '冬日', '初春', '日系', '暖色', '暴晒', '泛黄', '浓烈', '清新', '漂染', '秋意', '美好', '蓝调', '阳光', '雾气', '黑白','怀旧','高级灰','旅程','冰美人','阿宝色','江南','故事','樱花','平静','唯美','自然美颜-自然','自然美颜-粉嫩','自然美颜-果冻','自然美颜-黑白','自然美颜-红润','自然美颜-糖水色','自然美颜-蜜粉','柔光美颜-柔和','柔光美颜-粉色','柔光美颜-果酱','柔光美颜-黑白','柔光美颜-日出','柔光美颜-甜蜜','柔光美颜-暮光','柔光美颜-唯美','莱卡-光泽','莱卡-和谐','莱卡-黑白', '浮雕', '模糊', '锐化', '平滑', '平滑-阀值更大', '边界', '边界加强', '边界加强-阀值更大',  '轮廓', '细节', '高斯模糊']

def lj(tp, lj, userName, bz=False):
    num = userName
    i1 = f'{directory}apps/static/lj-images/'
    lj1 = f'{directory}apps/static/images-lj/'
    f = f'{directory}apps/static/filter/'
    filter = ['假日', '冬日', '初春', '日系', '暖色', '暴晒', '泛黄', '浓烈', '清新', '漂染', '秋意', '美好', '蓝调', '阳光', '雾气', '黑白','怀旧','高级灰','旅程','冰美人','阿宝色','江南','故事','樱花','平静','唯美','自然美颜-自然','自然美颜-粉嫩','自然美颜-果冻','自然美颜-黑白','自然美颜-红润','自然美颜-糖水色','自然美颜-蜜粉','柔光美颜-柔和','柔光美颜-粉色','柔光美颜-果酱','柔光美颜-黑白','柔光美颜-日出','柔光美颜-甜蜜','柔光美颜-暮光','柔光美颜-唯美','莱卡-光泽','莱卡-和谐','莱卡-黑白']
    if lj in filter:
        def position(rgb):
            x = (rgb[0] // 4) + (rgb[2] % 32) //4 * 64
            y = (rgb[1] // 4) + (rgb[2] // 32) * 64
            return [x, y]
        img = Image.open(i1 + tp)
        pix = img.load()
        color = Image.open(f+ lj + '.png')
        pixColor = color.load()
        for x in range(img.width):
            for y in range(img.height):
                rgb = pix[x, y]
                pos = position(rgb)
                pix[x, y] = pixColor[pos[0], pos[1]]
        if bz == True:
            img.save(lj1 + num + '.png')
    elif lj == '浮雕':
        img = Image.open(i1 + tp)
        img = img.filter(ImageFilter.EMBOSS)
        if bz == True:
            img.save(lj1 + num + '.png')
    elif lj == '模糊':
        img = Image.open(i1 + tp)
        img = img.filter(ImageFilter.BLUR)
        if bz == True:
            img.save(lj1 + num + '.png')
    elif lj == '锐化':
        img = Image.open(i1 + tp)
        img = img.filter(ImageFilter.SHARPEN)
        if bz == True:
            img.save(lj1 + num + '.png')
    elif lj == '平滑':
        img = Image.open(i1 + tp)
        img = img.filter(ImageFilter.SMOOTH)
        if bz == True:
            img.save(lj1 + num + '.png')
    elif lj == '平滑-阀值更大':
        img = Image.open(i1 + tp)
        img = img.filter(ImageFilter.SMOOTH_MORE)
        if bz == True:
            img.save(lj1 + num + '.png')
    elif lj == '边界':
        img = Image.open(i1 + tp)
        img = img.filter(ImageFilter.FIND_EDGES)
        if bz == True:
            img.save(lj1 + num + '.png')
    elif lj == '边界加强':
        img = Image.open(i1 + tp)
        img = img.filter(ImageFilter.EDGE_ENHANCE)
        if bz == True:
            img.save(lj1 + num + '.png')
    elif lj == '边界加强-阀值更大':
        img = Image.open(i1 + tp)
        img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        if bz == True:
            img.save(lj1 + num + '.png')
    elif lj == '轮廓':
        img = Image.open(i1 + tp)
        img = img.filter(ImageFilter.CONTOUR)
        if bz == True:
            img.save(lj1 + num + '.png')
    elif lj == '细节':
        img = Image.open(i1 + tp)
        img = img.filter(ImageFilter.DETAIL)
        if bz == True:
            img.save(lj1 + num + '.png')
    elif lj == '高斯模糊':
        img = Image.open(i1 + tp)
        img = img.filter(ImageFilter.GaussianBlur(radius=3))
        if bz == True:
            img.save(lj1 + num + '.png')

@app_filter.route("/filter",methods=["GET"])
def filter():
    if session.get('gly') == None:
        session['gly'] = 'False'
    if session.get('deng') == None:
        session['deng'] = 'weidenglu'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history()
        return render_template("filter/Filter.html",list=l,user_name=session['userName']),200
    else:
        return redirect("/login")


@app_filter.route("/check_filter",methods=["GET","POST"])
def check_filter():
    if request.method == "POST":
        history()
        f = request.files["f"]
        f.save(f"{directory}/apps/static/lj-images/"+session["userName"]+".jpg")
        lj(session["userName"]+".jpg",request.form["from"],session["userName"],True)
        from1 = "../../static/lj-images/"+session["userName"]+".jpg"
        to1 = "../../static/images-lj/"+session["userName"]+".png"
        return render_template("filter/Filter1.html",list=l,ff=request.form["from"],fro=from1,tt=to1,user_name=session['userName']),200
    abort(404)