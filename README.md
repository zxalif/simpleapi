# simpleapi

A simple application for serving macro service for game API

###### Contents
- Clone
- Install Requirements
- Migrations & Migrate
- Run The App
- Application
- Admin Panel
- API

#### Clone


At first clone the repository using git command or download it as zip.

```shell
$ git clone git@github.com:zxalif/simpleapi.git && cd simpleapi
```

#### Install Requirements

Use pip or pip3 to install dependencies (use virtual env).

```shell
$ pip3 install --upgrade -r requirements.txt
```
***Or***

```shell
$ pip install --upgrade -r requirements.txt
```

#### Migrations & Migrate

After installing the requirements.txt run this two command to create table and execute the sql.

```shell
$ ./manage.py makemigrations
No changes detected
$ ./manage.py migrate
Operations to perform:
  .......
```

#### Run The App

After finishing all the step just run the app using this bellow command!

```shell
$ ./manage.py runserver
System check identified no issues (0 silenced).
July 08, 2019 - 06:36:26
Django version 2.2.3, using settings 'simpleapi.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

#### Application

All done, now go to the server url i.e. ```http://127.0.0.1:8000/```.

#### Admin Panel

To view admin panel you have to create a superuser/admin first. To do so, run this following command to create a superuser and fill all the input.

```shell
$ ./manage.py createsuperuser
Username (leave blank to use 'alif'): alif
Email address:
Password:
Password (again):
Superuser created successfully.
```

Now, go to ```127.0.0.0:8000/admin/``` and fill the login user name and password.

#### API

Go to `127.0.0.1:8000/game/`
