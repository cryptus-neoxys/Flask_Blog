import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog import app, db, bcrypt, mail
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, RequestResetForm, ResetPasswordForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message


@app.route('/')
@app.route('/home', methods = ['POST', 'GET'])
def home():
	page = request.args.get('page', 1, type=int)
	posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
	return render_template('home.html', posts=posts)


@app.route('/about', methods = ['POST', 'GET'])
def about():
	return render_template('about.html', title='About')


@app.route('/register', methods = ['POST', 'GET'])
def register():
	if current_user.is_authenticated:
		return(redirect(url_for('home')))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash(f'Account Created! Login', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)


@app.route('/login', methods = ['POST', 'GET'])
def login():
	if current_user.is_authenticated:
		return(redirect(url_for('home')))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			flash(f'Logged in as {user.username}', 'success')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash(f'Login Unsuccessful. Invalid Email/Password.', 'danger')
	return render_template('login.html', title='Login', form=form)


@app.route('/logout', methods = ['POST', 'GET'])
def logout():
	logout_user()
	return(redirect(url_for('home')))


def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
	output_size = (125, 125)
	i = Image.open(form_picture)
	i.thumbnail(output_size)
	i.save(picture_path)
	return picture_fn


@app.route('/account', methods=['POST', 'GET'])
@login_required
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		if form.picture.data:
			picture_file = save_picture(form.picture.data)
			current_user.image_file = picture_file
		current_user.username = form.username.data
		current_user.email = form.email.data
		db.session.commit()
		flash(f'Account updated successfuly', 'success')
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.email.data = current_user.email
	image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
	return render_template('account.html', title='Account', image_file=image_file, form=form)


@app.route('/post/new', methods=['POST', 'GET'])
@login_required
def new_post():
	form = PostForm()
	if form.validate_on_submit():
		flash(f'New Blog Posted', 'success')
		post = Post(title=form.title.data, content=form.content.data, author=current_user)
		db.session.add(post)
		db.session.commit()
		return redirect(url_for('home'))
	return render_template('create post.html', title='New Post', form=form, legend='New Post')


@app.route('/post/<int:post_id>')
def post(post_id):
	post = Post.query.get_or_404(post_id)
	return render_template('post.html', title=post.title, post=post)


@app.route('/post/<int:post_id>/update', methods=['POST', 'GET'])
@login_required
def update_post(post_id):
	post = Post.query.get_or_404(post_id)
	if post.author != current_user:
		abort(403)
	form = PostForm()
	if form.validate_on_submit():
		post.title = form.title.data
		post.content = form.content.data
		db.session.commit()
		flash('Post Updated Successfully', 'success')
		return redirect(url_for('post', post_id=post.id))
	elif request.method ==  'GET':
		form.title.data = post.title
		form.content.data = post.content
	return render_template('create post.html', title='Update Post', form=form, legend='Update Post')


@app.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
	post = Post.query.get_or_404(post_id)
	if post.author != current_user:
		abort(403)
	db.session.delete(post)
	db.session.commit()
	flash(f'Post Deleted Successfully', 'success')
	return redirect(url_for('home'))



@app.route('/user/<string:username>', methods = ['POST', 'GET'])
def user_posts(username):
	page = request.args.get('page', 1, type=int)
	user = User.query.filter_by(username=username).first_or_404();
	posts = Post.query.filter_by(author=user).order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
	return render_template('user_post.html', posts=posts, user=user)


def send_reset_email(user):
	token = user.get_reset_token()
	msg = Message('Password Reset Request', sender=('Dev from Flask Blog','dared8002@gmail.com'), recipients=[user.email])
	msg.body = f'''Click the following link, to reset your password:
{url_for('reset_token', token=token, _external=True)}

If you didn't order this request, please ignore this email. No changes will be made to your account.'''
	mail.send(msg)

@app.route('/reset_password', methods=['POST', 'GET'])
def reset_request():
	if current_user.is_authenticated:
		return(redirect(url_for('home')))
	form = RequestResetForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		send_reset_email(user)
		flash(f'Password reset link sent. Check your Email', 'info')
		return redirect(url_for('login'))
	return render_template('reset_request.html', title='Reset Password', form=form)


@app.route('/reset_password/<token>', methods=['POST', 'GET'])
def reset_token(token):
	if current_user.is_authenticated:
		return(redirect(url_for('home')))
	user = User.verify_reset_token(token)
	if user is None:
		flash(f'Token Invalid/Expired', 'warning')
		return redirect(url_for('reset_request'))
	form = ResetPasswordForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user.password = hashed_password
		db.session.commit()
		flash(f'Password Updated! You May Now Login', 'success')
		return redirect(url_for('login'))
	return render_template('reset_token.html', title='Reset Password', form=form)