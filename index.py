from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/launch", methods=['POST'])
def launch():
    version = request.form['version']
    revision = request.form['revision']
    branch_url = request.form['branch_url']
    mysql = request.form['mysql']
    redis = request.form['redis']
    function = request.form['function']
    return request.form['version']


if __name__ == "__main__":
    app.run()
