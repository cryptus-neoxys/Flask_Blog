from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '13a6e298c62d24fdd18c7d740346c18b'

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

if __name__ == '__main__':
	app.run(debug=True)