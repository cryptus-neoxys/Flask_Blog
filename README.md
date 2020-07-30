# Flask_Blog 
[![forthebadge](https://forthebadge.com/images/badges/60-percent-of-the-time-works-every-time.svg)](https://forthebadge.com)
## Description
A full stack blog site made with Flask. This is the blog site made as a part of learning Flask.

----

## Functionalities/Features added successively:
- Responsive site design using **Bootstrap**, and layout using **Jinja2 Templates**.
- Login / Signup (**User authentication** added with **password hashing**)
- Update **Your Login and Profile** info
- Create, Update, Delete **Posts**
- **Pagination** for Posts display
- View all **posts by a User**
- **Password Reset** added (Password **reset link** to mail)
- App **Blueprints** configured
- **create_app** for instantiation added

----

## Requirements

**Run the following commands in your cmd(in project the directory)**

**Setting up virtual environment and installing dependencies.**

```shell
pip install virtualenv
virtualenv env
env\Scripts\activate
pip install -r requirements.txt
```

**Setup environment variables for sensitive info, for sending mails.**

```shell
set EMAIL_USER="your email"
set EMAIL_USER="your password"
set SECRET_KEY_FOR_FLASK_BLOG="secret key (protects against CSRF)"
set SQLALCHEMY_DATABASE_URI_FOR_FLASK_BLOG="sql uri (eg: sqlite:///site.db)"
```
**Don't use " "(quotes) for assigning values in cmd**
**use 'export' instead of 'set' with ' '(quotes) for Linux/MacOS.. terminal**

**Run the Module**

```shell
python run.py
```

## Tree Structure

<details>
<summary> <strong> Click to expand File Tree Structure </strong> </summary>

```shell
.
│   README.md
│   requirements.txt
│   run.py
│
└───flaskblog
    │   config.py
    │   models.py
    │   site.db
    │   __init__.py
    │
    ├───main
    │   │   forms.py
    │   │   routes.py
    │   │   __init__.py
    │   │
    │   └───__pycache__
    │           .gitignore
    │           routes.cpython-38.pyc
    │           __init__.cpython-38.pyc
    │
    ├───posts
    │   │   forms.py
    │   │   routes.py
    │   │   __init__.py
    │   │
    │   └───__pycache__
    │           forms.cpython-38.pyc
    │           routes.cpython-38.pyc
    │           __init__.cpython-38.pyc
    │
    ├───static
    │   │   main.css
    │   │
    │   └───profile_pics
    │           0e4f5224717d8b0e.jpeg
    │           8c73cc55f38af72e.jpeg
    │           8fb04984a0e64806.jpeg
    │           db7be03f6772c284.jpeg
    │           default.jpeg
    │
    ├───templates
    │       about.html
    │       account.html
    │       create post.html
    │       home.html
    │       layout.html
    │       login.html
    │       post.html
    │       register.html
    │       reset_request.html
    │       reset_token.html
    │       user_post.html
    │
    ├───users
    │   │   forms.py
    │   │   routes.py
    │   │   utils.py
    │   │   __init__.py
    │   │
    │   └───__pycache__
    │           forms.cpython-38.pyc
    │           routes.cpython-38.pyc
    │           utils.cpython-38.pyc
    │           __init__.cpython-38.pyc
    │
    └───__pycache__
            .gitignore
            config.cpython-38.pyc
            forms.cpython-38.pyc
            models.cpython-38.pyc
            routes.cpython-38.pyc
            __init__.cpython-38.pyc
```

</details>

## Tech Stack
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![ForTheBadge uses-html](http://ForTheBadge.com/images/badges/uses-html.svg)](http://ForTheBadge.com)
[![ForTheBadge uses-css](http://ForTheBadge.com/images/badges/uses-css.svg)](http://ForTheBadge.com)
<br><br><br><br>
[![forthebadge](https://forthebadge.com/images/badges/uses-badges.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
