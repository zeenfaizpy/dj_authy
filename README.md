DJ Starter
==========

Django Starter Project

This project is bootstrapped with Cookiecutter Django.


Requirments
-----------

1. Django >= 3.0
2. Django Rest Framework

Database Creation
-----------------

```bash
$ psql postgres
> create database dj_athy;
```


Setup
-----

```bash
$ mkdir dj_authy && cd $_
$ git clone https://github.com/zeenfaizpy/dj_authy .
$ mkvirtualenv dj_authy
$ pip install -r requirements/local.txt
$ python manage.py runserver
```


API Endpoints
---------------

- User Registration

  http://127.0.0.1:8000/auth/users/

- User Activation

  http://127.0.0.1:8000/auth/users/activation

- Login

  http://127.0.0.1:8000/auth/token/login/

- Change password

  http://127.0.0.1:8000/auth/users/set_password/

- Users list/detail

  http://127.0.0.1:8000/auth/users/