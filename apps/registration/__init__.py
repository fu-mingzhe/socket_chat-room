# encoding = utf-8

from flask import *
from main_settings import *
import random


app_registration = Blueprint("main_registration",__name__)
app_registration.secret_key = key

from .views import *