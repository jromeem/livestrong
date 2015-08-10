from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def what_we_do():
    # return render_template('index.html')
    return render_template('what-we-do.html')

if __name__ == "__main__":
    app.run(debug=True)