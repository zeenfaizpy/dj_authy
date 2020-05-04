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
  ```bash
  $  curl -X POST http://127.0.0.1:8000/auth/users/ --data 'email=zeenfaiz@gmail.com&password=findmypassword'
  $  {"id":4,"email":"zeenfaiz@gmail.com"}
  ```
  Application will send an email with activation link like below
  
  http://example.com/users/activation/NQ/5g7-8306a07269ba35a5624e

- User Activation

  http://127.0.0.1:8000/auth/users/activation
  ```bash
  $  curl -X POST http://127.0.0.1:8000/auth/users/activation/ --data 'uid=NA&token=5g7-40b13e343ccab81c00a1'
  ```

- Login

  http://127.0.0.1:8000/auth/token/login/
  ```bash
  $  curl -X POST http://127.0.0.1:8000/auth/token/login/ --data 'email=zeenfaiz@gmail.com&password=findmypassword'
  $  {"auth_token":"0a732cd26be7f3b19d2dedc5959ca47b8f0e7746"}
  ```
    
- Change password

  http://127.0.0.1:8000/auth/users/set_password/
  ```bash
  $  curl -X POST http://127.0.0.1:8000/auth/users/set_password/ --data 'current_password=findmypasswordnew_password=findmypassword123'
  $ {"detail":"Authentication credentials were not provided."}
  ```

  ```bash
  $  curl -X POST http://127.0.0.1:8000/auth/users/set_password/ -H 'Authorization: Bearer 0a732cd26be7f3b19d2dedc5959ca47b8f0e7746' --data 'current_password=findmypassword&new_password=findmypassword123'
  ```

- Users list/detail

  http://127.0.0.1:8000/auth/users/

  ```bash
  $  curl -LX GET http://127.0.0.1:8000/auth/users/
  $  {"detail":"Authentication credentials were not provided."}
  ```

  ```bash
  $  curl -LX GET http://127.0.0.1:8000/auth/users/ -H 'Authorization: Bearer 0a732cd26be7f3b19d2dedc5959ca47b8f0e7746'
  $  [{"id":4,"email":"zeenfaiz@gmail.com","first_name":"","last_name":""}]
  ```