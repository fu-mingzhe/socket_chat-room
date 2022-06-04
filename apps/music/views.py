# encoding = utf-8

from . import *

def get_music_name(name):
    url = 'https://music.163.com/#/search/m/?s={}&type=1'.format(name)
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=option)
    driver.get(url)
    driver.switch_to.frame('g_iframe')
    req = driver.find_element_by_id('m-search')
    try:
        a_id = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//a').get_attribute("href")
        song_id = a_id.split('=')[-1]
        song_name = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//b').get_attribute("title")
        # 构造字典
        item = {}
        item['song_url'] = 'http://music.163.com/song/media/outer/url?id={}.mp3'.format(song_id)
        item['song_name'] = song_name
        item['url'] = url
    except:
        item = None
    driver.quit()
    return item

@app_music.route("/music_get",methods=['GET'])
def zhu():
    if session.get('gly') == None:
        session['gly'] = 'False'
    if session.get('deng') == None:
        session['deng'] = 'weidenglu'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history()
        return render_template('music/music_get.html',ip=gethostbyname(gethostname()),user_name=session["userName"]),200
    else:
        return redirect("/login")

@app_music.route('/get_music')
def music():
    if session.get('gly') == None:
        session['gly'] = 'False'
    if session.get('deng') == None:
        session['deng'] = 'weidenglu'
        return redirect("/login")
    elif session['deng'] == 'yidenglu':
        history()
        name = request.args['music_name']
        item = get_music_name(name)
        if item == None:
            return render_template('music/music_w.html',music_name=name)
        else:
            music_url = item['song_url']
            music_name = item['song_name']
            return render_template('music/get_music.html',music_name=music_name,music_url=music_url,m_name=name,user_name=session["userName"]),200
    else:
        return redirect("/login")