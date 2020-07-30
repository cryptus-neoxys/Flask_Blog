from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from flaskblog.models import User



class RegistrationForm(FlaskForm):
	username = StringField('Username', 
		validators=[DataRequired(),
		 Length(min=3, max=20)])
	email = StringField('Email', 
		validators=[DataRequired(), Email()],)
	password = PasswordField('Password', 
		validators=[DataRequired(), Length(min=8)])
	confirm_password = PasswordField('Confirm Password', 
		validators=[DataRequired(),
		EqualTo('password')])
	submit = SubmitField('Sign Up')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Username taken. Please choose a different username')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email already in use')

class LoginForm(FlaskForm):
	email = StringField('Email', 
		validators=[DataRequired(), Email()],)
	password = PasswordField('Password', 
		validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
	username = StringField('Username', 
		validators=[DataRequired(),
		 Length(min=3, max=20)])
	email = StringField('Email', 
		validators=[DataRequired(), Email()],)
	picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpeg', 'png'])])
	submit = SubmitField('Update')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('Username taken. Please choose a different username')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('Email already in use')


class RequestResetForm(FlaskForm):
	email = StringField('Email', 
		validators=[DataRequired(), Email()],)
	submit = SubmitField('Request Password Reset')
	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is None:
			raise ValidationError('Email doesnt exist')

class ResetPasswordForm(FlaskForm):
	password = PasswordField('Password', 
		validators=[DataRequired(), Length(min=8)])
	confirm_password = PasswordField('Confirm Password', 
		validators=[DataRequired(),
		EqualTo('password')])
	submit = SubmitField('Reset Password')
