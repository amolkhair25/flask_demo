from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, flash, url_for, redirect, render_template, session

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = "dev"
app.app_context().push()
db = SQLAlchemy(app)

class User(db.Model):
	id=db.Column(db.Integer, primary_key=True)
	username=db.Column(db.String(100), unique=True)
	password=db.Column(db.String(100))
	def __init__(self, username, password):
		self.username=username
		self.password=password

@app.route("/", methods=['GET'])
def home():
	if session.get('logged_in'):
		return render_template("home.html")
	else:
		return render_template("index.html", message="Hello Anonymous User")

@app.route("/register", methods=['GET', 'POST'])
def register():
	if request.method=='POST':
		try:
			db.session.add(User(username=request.form['username'], password=request.form['password']))
			db.session.commit()
			return redirect(url_for('login'))
		except:
			return "<h4>User already exists</h4>"
	else:
		return render_template("register.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
	if request.method=='GET':
		return render_template("login.html")
	else:
		un=request.form['username']
		pw=request.form['password']
		usr=User.query.filter_by(username=un, password=pw).first()

		if usr is not None:
			session['logged_in']=True
			return redirect(url_for("home"))
		else:
			return "Incorrect credentials"

@app.route("/logout", methods=['GET', 'POST'])
def logout():
	session['logged_in']=False
	return redirect(url_for("home"))





	return "<h4>User logged in successfully</h4>"

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)
