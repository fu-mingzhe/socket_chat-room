# encoding = utf-8

from selenium import webdriver
from flask import *
from socket import *
from main_settings import *


app_music = Blueprint("main_music",__name__)
app_music.secret_key = key

from.views import *