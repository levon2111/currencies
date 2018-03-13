REST - example application based on Django and django-rest-framework
====================================================================


-----------------
Development setup
-----------------

Requirements:

- <a href="https://www.python.org/">python3.4+</a>
- <a href="https://www.djangoproject.com/">Django1.11</a>
- <a href="https://www.mysql.com/">mysql-server</a>
- <a href="http://www.django-rest-framework.org/">djangorestframework</a>
- <a href="https://github.com/marcgibbons/django-rest-swagger">django-rest-swagger</a>

Install required system packages:

    $ sudo apt-get install python3-pip
    $ sudo apt-get install libmysqlclient-dev
    $ sudo apt-get install python3-dev
    
Create www directory where project sits and environment dir

    $ mkdir /var/www && mkdir /var/envs && mkdir /var/envs/bin
    
Install virtualenvwrapper

    $ pip3 install virtualenvwrapper

You could add commands listed below to your ~/.bashrc in order to use virutualenvwrapper easier

    export WORKON_HOME=/var/envs
    export PROJECT_HOME=/var/www
    export VIRTUALENVWRAPPER_HOOK_DIR=/var/envs/bin
    source /usr/local/bin/virtualenvwrapper.sh
    export IS_LOCAL=1
    
Create virtualenv

    $ cd /var/envs && virtualenv --python=python3.4 rest_example
    
Install requirements for a project.

    $ cd /var/www/rest_example && pip3 install -r requirements/local.txt

Run migrations.

    $ python manage.py migrate

Run application in test mode.

    $ python manage.py runserver

Swagger-generated documentation URL.
* http://127.0.0.1:8000/docs/

Django-rest-framework interface URL.
* http://127.0.0.1:8000

Running tests.
    $ python manage.py test apps
