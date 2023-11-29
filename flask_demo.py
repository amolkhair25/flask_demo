# FLASK DEMO Done
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/hello")#(@app.route decorator is used to define a route for your web application),(/hello ->URL route that will trigger the greet function)
def hello():# hello function that will be called when a user visits the specified URL route
    return render_template("hello.html")

@app.route("/status")
def status():
    return render_template("status.html")


if __name__=="__main__":
    app.run(debug=True)
