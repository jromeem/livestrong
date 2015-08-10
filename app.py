from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('base.html')

@app.route("/practice")
def practice():
    return render_template('practice.html')

@app.route("/tiny")
def tiny():
    return render_template('tiny.html')

if __name__ == "__main__":
    app.run(debug=True)