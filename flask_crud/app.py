#Install Flask-SQLAlchemy: pip install Flask Flask-SQLAlchemy
#create app.py file
#in your app.py file, import Flask and Flask-SQLAlchemy:
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, flash, url_for, redirect, render_template

#Configure your Flask app:
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "dev"
app.app_context().push()

#Create a model:
db = SQLAlchemy(app)
class students(db.Model):
	id = db.Column('student_id', db.Integer, primary_key = True)
	name = db.Column(db.String(100))
	city = db.Column(db.String(50))  
	addr = db.Column(db.String(200))
	pin = db.Column(db.String(10))

	def __init__(self, name, city, addr,pin):
		self.name = name
		self.city = city
		self.addr = addr
		self.pin = pin

#Using the database in your routes:
@app.route('/')
def show_all():
	return render_template('show_all.html', students = students.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
	if request.method == 'POST':
		if not request.form['name'] or not request.form['city'] or not request.form['addr']:
			flash('Please enter all the fields', 'error')
		else:
			student = students(request.form['name'], request.form['city'],
					request.form['addr'], request.form['pin'])

			db.session.add(student)
			db.session.commit()
			flash('Record was successfully added')
			return redirect(url_for('show_all'))
	return render_template('new.html')

#Create the database:
if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)