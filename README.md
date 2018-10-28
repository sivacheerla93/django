# Django
Django is a free and open-source web framework, written in Python, which follows the model-view-template (MVT) architectural pattern. It is maintained by the Django Software Foundation (DSF), an independent organization established as a non-profit.

Django's primary goal is to ease the creation of complex, database-driven websites. Django emphasizes reusability and "pluggability" of components, less code, low coupling, rapid development, and the principle of don't repeat yourself. Python is used throughout, even for settings files and data models. Django also provides an optional administrative create, read, update and delete interface that is generated dynamically through introspection and configured via admin models.

Some well-known sites that use Django include the Public Broadcasting Service, Instagram, Mozilla, The Washington Times, Disqus, Bitbucket, and Nextdoor. It was used on Pinterest, but later the site moved to a framework built over Flask. [Wikipedia](https://en.wikipedia.org/wiki/Django_(web_framework))

### Workspace Configuartion:
* OS: Windows 8.1 64-bit
* Python version: 3.4.4
* Database: MySQL 5.7
* Django version: 2.0.9
* IDE: PyCharm 2018.1 (Community Edition)

### Download Django using PIP:
```
pip install django
```
If you want specific version, then follw this command
```
 pip install django==2.0
```

### Start Project:
Before creating a project first locate your workspace folder using cmd, and then follow this command
```
django-admin startproject webdemo
```
Then you can create an application within your project using following command, Before creating an app change directory to your created project
```
python manage.py startapp demo
```

### Make app presence in Installed apps:
Go to settings.py under webdemo sub folder and make presence of your app in INSTALLED_APPS,
```
'demo'
```

### URL Patterns:
Views created in your application, make sure thier paths in urls.py under webdemo sub folder

Ex:
```
from demo.views import hello

urlpatterns = [ path('hello/', hello ]
```

Note: URL's can be in urls.py under your app also i.e., demo. For that we need to set path for our app in urls.py under webdemo sub folder
```
from django.urls import path, include

urlpatterns = [ path('demo/', include('demo.urls')) ]
```

And then set your view path in urls.py under your app, i.e., demo

Ex:
```
from django.urls import path
from demo.views import hello

urlpatterns = [ path('hello/', hello) ]
```

### Start Server:
To start the server, location should be Project folder only and then follow this command
```
python manage.py runserver
```

```
And then go to https://localhost:8000/demo/hello
```

### To migrate changes to database:
```
python manage.py migrate
```

### To launch interactive console or shell:
```
python manage.py shell
```

### ORM(Object Relational Model):
Follow these commands after creating models to migrate into database

```
python manage.py check
```

```
python manage.py makemigrations
```

```
python manage.py migrate
```
(or)
```
python manage.py sqlmigrate demo 0001
```

### Django Rest Framework:
To install rest framework using pip, follow this command from cmd
```
pip install djangorestframework
```

After installing rest, make it's presence into INSTALLED_APPS:
```
'rest_framework'
```

### Resources:
[Offical Django Documentation](https://docs.djangoproject.com/en/2.0/)

[Mozilla’s documentation on Django](https://developer.mozilla.org/en-US/docs/Learn/Serverside/Django)

[A very good book on all important topics of Django](https://djangobook.com/the-django-book)

[Nice tutorials from Vitor Freitas, Brazil](https://simpleisbetterthancomplex.com)

[Links to many tutorials related to Django](https://www.fullstackpython.com/django.html)

[A book on Django for Beginners](https://djangoforbeginners.com)

### Note:
If you find any error or want to give any suggestion, create an issue or write to sivacheerla@live.com