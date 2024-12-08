# django-blog


## assignment 8
Your assignment this week is to convert the function-based views in your blogging app into class-based views. 
Your work will be very similar to the work we did in the lesson content to create the polling class-based views, except:
- The blogging detail view doesn't accept POST requests, so there will be no need to create a `post` method in the blogging detail view.

- When you're done, the front page should continue to display only published posts and it should continue to display posts in reverse-chronological order. To accomplish this, you'll be providing a `queryset` class attribute in your list view instead of a `model` class attribute. See https://docs.djangoproject.com/en/2.1/topics/class-based-views/generic-display/#viewing-subsets-of-objectsLinks to an external site. for examples of filtering and sorting querysets. You'll want to apply both `filter` (or `exclude`) and `order_by` methods to your `Post.objects` queryset.

- The examples in the documentation use a `context_object_name` variable, but I would _not_ use that in your homework.


[Class based views](https://canvas.uw.edu/courses/1770754/pages/lesson-08-content?module_item_id=21395537#:~:text=grade%25%250A%250A%2520%2520%2520%2520return%2520body-,Class%2520Based%2520Views,-All%2520of%
)

Software Tests
Your submission passes the included software tests. Your submission will be graded based on the percentage of tests that pass: if your submission passes all of the tests then you will get 100% of the points for this criterion; if your submission passes half of the tests you will get 50% of the points for this criterion. Your points for this criterion will be rounded up to the nearest whole-point value.

## Notes
``` bash
update to test heroku

```


``` bash
django-admin startapp users_and_groups

```


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