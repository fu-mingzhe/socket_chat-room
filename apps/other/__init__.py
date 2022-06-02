# encoding = utf-8

from flask import *
import requests
from main_settings import *
import random

app_other = Blueprint("main_other",__name__)
app_other.secret_key = key


URL_DICT = {
    "垃圾分类":"/Garbage_sorting",
    "摸鱼图片":"/moyu",
    "抖音视频":"/douyin"
}
NAMELIST = ["明星","风景","游戏","动物"]

from .views import *