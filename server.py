from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/blog')
def blog():
    return 'Trying out a blog'


@app.route('/or not')
def blog2():
    return 'Trying out a blog or not'
