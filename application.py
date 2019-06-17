from flask import Flask, render_template
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/main")
def root(name=None):
    return render_template('index.html', name=name)
