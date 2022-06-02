import pymongo

client = pymongo.MongoClient()
db = client.user.login
a = db.update_one({"用户名":"f"},{"$set":{"权限":3}})
print(a)
# import requests
# def translate(from_to,text):
#     if text == "":
#         return ""
#     headers = {
#         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36"
#     }
#     # a = {"英语":"en","法语":"fr","中文":"zh","日语":"ja","爱沙尼亚语":"et","保加利亚语":"bg","波兰语":"pl","丹麦语":"da","德语":"de","俄语":"ru","芬兰语":"fi","荷兰语":"nl","捷克语":"cs","拉脱维亚语":"lv","立陶宛语":"lt","罗马尼亚语":"ro","葡萄牙语":"pt","瑞典语":"sv","斯洛伐克语":"sk","斯洛文尼亚语":"sl","西班牙语":"es","希腊语":"el","匈牙利语":"hu","意大利语":"it"}
#     a = {"中文»英语":"ZH_CN2EN","中文»日语":"ZH_CN2JA","中文»韩语":"ZH_CN2KR","中文»法语":"ZH_CN2FR","中文»俄语":"ZH_CN2RU","中文»西语":"ZH_CN2SP","英语»中文":"EN2ZH_CN","日语»中文":"JA2ZH_CN","韩语»中文":"KR2ZH_CN","法语»中文":"FR2ZH_CN","俄语»中文":"RU2ZH_CN","西语»中文":"SP2ZH_CN"}
#     l = []
#     for i in a:
#         l.append(i)
#     print(l)
#     url = "http://fanyi.youdao.com/translate?&doctype=json&type={from_to}&i={text}".format(from_to=a[from_to],text=text)
#     try:
#         r = eval(requests.get(url,headers=headers).text)
#     except:
#         return "抱歉发现未知错误"
#     return r["translateResult"][0][0]["tgt"]
# a = translate("中文»日语",u"今天的天气怎么样？")
# print(a)