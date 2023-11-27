# practice 
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def test():
    return render_template("test.html")

@app.route("/hello")
def hello():
    return render_template("hello.html")

@app.route("/status")
def status():
    return render_template("status.html")


if __name__=="__main__":
    app.run(debug=True)
