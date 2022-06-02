# import os
# import sys

# def restart_program():
#   python = sys.executable
#   print(python)
#   os.execl(python, python, * sys.argv)

# print('123456')
# print('13243')
# restart_program()
from itsdangerous import json
import requests
# from bs4 import BeautifulSoup


r = requests.get("http://is.snssdk.com/api/news/feed/v51/")
jsonn = r.json()
for i in jsonn["data"]:
    b = eval(i["content"].replace("false","False").replace("true","True").replace("null","None"))
    for c in b:
        print(c,b[c])