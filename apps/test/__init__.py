# encoding = utf-8

from flask import *
import time
import random
from main_settings import *


app_test = Blueprint("main_test",__name__)
app_test.secret_key = key

from .views import *