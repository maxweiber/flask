from flask import Flask, render_template

app = Flask(__name__)

@app.route('/user/<name>')
def sayhello(name):
    return render_template('user.html', names = name)

if __name__ == "__main__":
    app.run(debug = True)
