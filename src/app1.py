from flask import Flask, render_template, request
from pyfladesk import init_gui
import adb

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "HELLO"
    
if __name__ == '__main__':
    #app.run(debug=True)
    init_gui(app, window_title="Botgram", icon="static/favicon.ico")
