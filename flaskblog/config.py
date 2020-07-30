import os



class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY_FOR_FLASK_BLOG')
	SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI_FOR_FLASK_BLOG')
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = '465'
	MAIL_USE_TLS = False
	MAIL_USE_SSL = True
	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
	MAIL_DEFAULT_SENDER = ('Dev form Flask Blog', 'dared8002@gmail.com')
