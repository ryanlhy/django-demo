# Django Demo

Deployed on [http://ryanlhy.pythonanywhere.com/](http://ryanlhy.pythonanywhere.com/)

## Quick Setup

Step 1: Setup environment

```sh
mkdir django-demo 
cd django-demo
python3 -m venv djangoenv
source ./djangoenv/bin/activate
pip install django
```

Step 2: Setup main project and app

```sh
django-admin startproject main
django-admin startapp api
```

Step 3: Change `default_port` from `8000` to `9000` (in `runserver.py` file).

Step 4: Test run default project

```sh
cd main
python manage.py runserver
```

Step 5: Add the commented line in `settings.py` within the `main` project folder.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig' # add this line
]
```

Step 6: In the same `settings.py` file, comment CSRF middleware

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

## Setup Database

Step 1: Install postgres adapter

```sh
pip install psycopg2
```

Step 2: Login to PG console and insert the following SQL Commands

```sql
CREATE DATABASE djangodb;
CREATE USER djangouser WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE djangodb TO djangouser;
```

Step 3: Configure `settings.py` in main project

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangodb', 
        'USER': 'djangouser', 
        'PASSWORD': 'password',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}
```

You are ready to implement the code.

End.
