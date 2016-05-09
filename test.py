from flask import Flask, render_template, abort, redirect
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager
from flask.ext.moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
manager = Manager(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html', current_time = datetime.utcnow())

@app.route('/user/<name>')
def sayhello(name):
    return render_template('user.html', name = name)

@app.errorhandler(404)
def not_found_page(e):
    return render_template('404.html'),404

if __name__ == "__main__":
    manager.run()