# encoding = utf-8

from flask import *
from main_settings import *


app_gui = Blueprint("app_gui",__name__)
app_gui.secret_key = key

from .views import *