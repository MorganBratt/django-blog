# django-blog



## Notes

``` bash
# start the server
python manage.py  runserver
```

``` bash
# take care of moving models
# run after every time you create or change models.py
python manage.py makemigrations
```

``` bash
# ???
python manage.py migrate
```

``` bash
# no more than 3 super users
$ python manage.py createsuperuser
```
```
Username (leave blank to use 'morga'): mb171
Email address: mb171@uw.edu
Password:
Password (again):
Superuser created successfully.
```

``` bash
# create an app
python manage.py startapp polling
# update settings.py INSTALLED_APPS section to include app
```

left off at 2:57