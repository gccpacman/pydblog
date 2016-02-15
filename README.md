# Software Version:

Django 1.8 

python 3.5


# installation (Development)

1. install ```postgresql``` and create a database called ```django_blog``:

    sudo pacman -S postgresql
    su postgres
    createdb django_blog

        PS: follow [PostgreSQL - arch wiki](http://wiki.archlinux.org/index.php/PostgreSQL) OR other instruction if you are using other platform.

    
2. install ```virtualenv```, ```virtualenvwrapper```:

    sudo pacman -S python, python-pip
    sudo pip install virtualenv virtualenvwrapper

3. create a virtualenv:

    mkvirtualenv pydblog
    cd django_blog/


4. install python dependencies:

    pip install -r requirenments

5. migrate database:

    cd django_blog
    python manage.py makemigration
    python manage.py syncdb

6. run the web server:

    python manage.py runserver

7. open your browser and enter url: http://127.0.0.1:8000

# References:
[Django Tutorial](https://docs.djangoproject.com/en/1.8/intro/tutorial03/)
[A clean Bootstrap blog theme created by Start Bootstrap](https://github.com/IronSummitMedia/startbootstrap-clean-blog)


