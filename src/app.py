from flask import Flask, render_template, request
import adb
import instagram
import os, sys
from pyfladesk import init_gui
import threading

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    devices = adb.get_devices()
    print(devices)
    return render_template('index.html', devices=devices)

@app.route('/run', methods=['POST'])
def run():
    if request.form['feature'] == "unfollow_all":
        t = threading.Thread(target=instagram.unfollow_all)
        t.start()
    return render_template('run.html', data=request.form)

if __name__ == '__main__':
    #app.run(debug=True)
    init_gui(app, window_title="Instagram Bot", icon="static/favicon.ico")
