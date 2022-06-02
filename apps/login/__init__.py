# encoding = utf-8

from flask import *
from main_settings import *


app_login = Blueprint("main_login",__name__)
app_login.secret_key = key

from . import views