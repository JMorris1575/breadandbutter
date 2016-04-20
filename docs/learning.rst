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

