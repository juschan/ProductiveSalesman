from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/")
def root():
    return render_template('index.html')