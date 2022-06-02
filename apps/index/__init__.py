# encoding = utf-8

from flask import *
import datetime
from main_settings import *


app_index = Blueprint("main_index",__name__)
app_index.secret_key = key

from . import views