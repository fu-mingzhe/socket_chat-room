# encoding = utf-8

from flask import *
from main_settings import *


app_admin = Blueprint("main_admin",__name__)
app_admin.secret_key = key

from . import views