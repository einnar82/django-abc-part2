# Django Crash Course

Setup your pipenv and install

    $ pipenv install django

After installing django, create your project via

    $ django-admin startproject {project_name}

Then, after the project creation, to serve the project, access your {project_name} and type

    $ python manage.py runserver

Migrate your migration files by typing

    $ python manage.py migrate

Create a default superuser by typing

    $ python manage.py createsuperuser

To create a new app inside of django project

    $ python manage.py startapp {app_name}

To create migration files, or alter your exisiting migrations. first setup your [models](https://docs.djangoproject.com/en/3.0/topics/db/models/) and define your fields and then

    $ python manage.py makemigrations

If the object is an instance of [QuerySet](https://docs.djangoproject.com/en/3.0/ref/models/querysets), you must iterate it

To load static files, you must declare it on the `static` folder and go to settings.py and add to your `STATICFILES_DIRS`

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]

And declare it on top of your HTML Code, `{% load static %}`

Django forms serve as a [validation](https://docs.djangoproject.com/en/3.0/topics/forms/) class
