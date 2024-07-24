from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/test/<name>")
def testFunc(name):
    return f"Hello, {escape(name)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)