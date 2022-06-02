# encoding = utf-8

from flask import session,request
from pymongo import MongoClient
import os


client = MongoClient()
directory = (os.path.split(os.path.realpath(__file__))[0]).split("\\")
directory = "/".join(directory)+"/"
key = os.urandom(24)
# key = b'_5#y2L"F4Q8z\n\xec]/\xec\n/fd()\xde\xdc\n'


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