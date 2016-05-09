from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def sayhello():
    return render_template('index.html')

if __name__ == '__main__':
    manager.run()