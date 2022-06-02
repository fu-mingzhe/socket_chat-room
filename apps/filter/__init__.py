# encoding = utf-8

from PIL import Image,ImageFilter
from flask import *
from main_settings import *


app_filter = Blueprint('main_filter',__name__)
app_filter.secret_key = key

from .views import *