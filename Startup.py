from flask import Flask
from flask import render_template
from flask import send_from_directory
import os
import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    now = datetime.datetime.now()
    timestring = now.strftime("%Y-%m-%d %H:%M")

    templatedata = {
        'title': 'Rpi Info!',
        'time': timestring
    }

    return render_template('index.html', **templatedata)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static"), "favicon.ico",
                               mimetype="image/vnd.microsoft.icon")

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
# return render_template('index.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)
    app.run()

