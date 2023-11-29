# Done
from flask import Flask, render_template, url_for, redirect

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/courses")
def course():
    return render_template("course.html")

@app.route("/teacher")
def teacher():
    return render_template("teacher.html")

@app.route("/blog_list")
def blog_list():
    return render_template("blog_list.html")

@app.route("/blog_details")
def blog_details():
    return render_template("blog_details.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
    
