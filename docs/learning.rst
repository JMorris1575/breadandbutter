Things I've Learned on this Project
===================================

The SECRET_KEY
--------------

It doesn't matter if the SECRET_KEY used during development is made public because it can be changed during production.
I learned this mostly from chapter 29 of Django Unleashed, which outlines steps to take for deployment.

One of these steps, there and in other tutorials I've run across, is to separate the settings.py file into three parts:
one for development, one for production and, possibly, one for staging.  The difficulty with doing that during
development, however, is that you have to specify where Django is to look for the settings file to use.  In other words,
instead of simply typing:

`manage.py runserver`

I would have to type

`manage.py runserver --settings config.settings.dev`

every time.

To get around this I can put into my bnb.bat file a line that sets an environment variable:

`set DJANGO_SETTINGS_MODULE=config.settings.dev`

and that should take care of it.

Initial Migrate
---------------

I was getting errors on my functional_tests.py even though the unit test was working perfectly well.  (I am still
at the stage of only pretending to have an html file. The fake is produced in the return statement of the view.  (See
*Unit Testing a View* in Chapter 3 of *Test Driven Development in Python* at
http://chimera.labs.oreilly.com/books/1234000000754/ch03.html#_the_unit_test_code_cycle)
So I tried a `python manage.py migrate` and everything worked fine.

By the way, on my rectory computer the chmod command didn't seem to work.


