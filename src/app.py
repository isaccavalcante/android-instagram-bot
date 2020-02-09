from flask import Flask, render_template, request
import adb
import instagram
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    devices = adb.get_devices()
    print(devices)
    return render_template('index.html', devices=devices)

@app.route('/run', methods=['POST'])
def run():
    if request.form['feature'] == "unfollow_all":
        instagram.unfollow_all()
    return render_template('run.html', log=request.form)

if __name__ == '__main__':
    app.run(debug=True)