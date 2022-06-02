# encoding = utf-8

import requests
# import ybc_speech1 as speech
from flask import *
from main_settings import *


app_translate = Blueprint("main_translate",__name__)
app_translate.secret_key = key

from .views import *