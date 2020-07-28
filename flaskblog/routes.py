from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


posts = [
	{
		'author' : 'Dev Sharma',
		'title' : 'Blog Post 1',
		'content' : 'First Post content',
		'date_posted' : 'July 20, 2020'
	},
	{
		'author' : 'Jane Doe',
		'title' : 'Blog Post 2',
		'content' : 'Second Post content',
		'date_posted' : 'July 21, 2020'
	}
]

@app.route('/')
@app.route('/home', methods = ['POST', "GET"])
def home():
	return render_template('home.html', posts=posts)

@app.route('/about', methods = ['POST', "GET"])
def about():
	return render_template('about.html', title='About')


@app.route('/register', methods = ['POST', "GET"])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account Created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route('/login', methods = ['POST', "GET"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash(f'You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash(f'Login Unsuccessful. Invalid Username/Password.', 'danger')
	return render_template('login.html', title='Register', form=form)
