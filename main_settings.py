# encoding = utf-8

from flask import session,request
from pymongo import MongoClient
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Template
import random


client = MongoClient()
directory = (os.path.split(os.path.realpath(__file__))[0]).split("\\")
directory = "/".join(directory)+"/"
key = os.urandom(24)
ADMIN_USER = {
    "admin":"123456",
}


def history(*f):
    user_name = session["userName"]
    textList = request.url.split('/')[3:]
    text = ""
    for i in textList:
        text += "/{text}".format(text=i)
    st = client.user.login.find_one({'用户名':user_name})
    st['历史记录'].append(text)
    client.user.login.delete_one({'用户名':user_name})
    client.user.login.insert_one(st)

def send_email(receiver,name):
    sender = '你的QQ邮箱'
    password = "你的授权码"
    smtp_address = "SMTP服务器地址"
    port = 465
    email_content = open(directory+"templates/email.html",'r',encoding='utf-8').read()
    v = ""
    for i in range(6):
        v += str(random.randint(0,6))
    session["verification"] = [receiver,v]
    template = Template(email_content)
    template = template.render(name=name,Verification=v)
    message = MIMEText(template,'html','utf-8')
    multiMsg = MIMEMultipart()
    multiMsg.attach(message)
    multiMsg['Subject'] = '[FMZ] 验证码'
    multiMsg['From'] = sender
    multiMsg['To'] = ';'.join(receiver)
    content = multiMsg.as_string()
    server = smtplib.SMTP_SSL(smtp_address, port)
    server.login(sender, password)
    server.sendmail(sender, receiver, content)
    server.quit()