# encoding = utf-8

from main_settings import *
from .index import app_index
from .admin import app_admin
from .login import app_login
from .other import app_other
from .music import app_music
from .registration import app_registration
from .gui import app_gui
from .filter import app_filter
from .translate import app_translate
from .test import app_test
from flask import *
import qrcode


app = Flask(__name__)
app.secret_key = key


app.register_blueprint(app_admin)
app.register_blueprint(app_index)
app.register_blueprint(app_login)
app.register_blueprint(app_other)
app.register_blueprint(app_music)
app.register_blueprint(app_registration)
app.register_blueprint(app_gui)
app.register_blueprint(app_filter)
app.register_blueprint(app_translate)
app.register_blueprint(app_test)


DEBUG = False
HOST = "0.0.0.0"
PORT = "5656"

@app.errorhandler(404)
def html404(error):
    return render_template('index/404.html'),404

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.ERROR_CORRECT_L
)
qr.add_data("http://{host}:{port}/".format(host=HOST,port=str(PORT)))
img = qr.make(fit=True)
# img.save(directory+"/static/images/qr.png")