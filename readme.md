# Django Demo

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

You are ready to implement the code.

End.