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

``manage.py runserver``

I would have to type

``manage.py runserver --settings config.settings.dev``

every time.

To get around this I can put into my bnb.bat file a line that sets an environment variable:

``set DJANGO_SETTINGS_MODULE=config.settings.dev``

and that should take care of it.

The Database Password
---------------------

It occurs to me (too late perhaps since I already have base.py on github) that I shouldn't be broadcasting the
password to my postgreSQL database for all the world to see.  I'll have to research what others do about this.


Initial Migrate
---------------

I was getting errors on my functional_tests.py even though the unit test was working perfectly well.  (I am still
at the stage of only pretending to have an html file. The fake is produced in the return statement of the view.  (See
*Unit Testing a View* in Chapter 3 of *Test Driven Development in Python* at
http://chimera.labs.oreilly.com/books/1234000000754/ch03.html#_the_unit_test_code_cycle)
So I tried a ``python manage.py migrate`` and everything worked fine.

By the way, on my rectory computer the chmod command didn't seem to work.

Useful Commands and Concepts
----------------------------

Here is a chart copied from *Test Driven Development in Python* (TDDP) at the end of Chapter 3:

**Useful Commands and Concepts**

    * Running the Django dev server: ``python3 manage.py runserver``
    * Running the functional tests: ``python3 functional_tests.py``
    * Running the unit tests: ``python3 manage.py test``
    * The unit-test/code cycle:
        * Run the unit tests in the terminal.
        * Make a minimal code change in the editor.
        * Repeat!

When ``chmod`` Didn't Seem to be Working
----------------------------------------

On the rectory computer, after running ``chmod +x ./manage.py`` and then trying something like ``manage.py runserver``
it would only open manage.py in Idle -- the Python 3.4.4 version of Idle!  I found out that \*.py files were set to open
in idle.bat.  When I right clicked a \*.py file, went into properties, and changed the "Opens With" setting so that they
opened with Python, it started working correctly.  I haven't figured out yet if it is opening in Python 3.4 or Python
3.5.

The Test-Driven-Development Cycle
---------------------------------

This is from the end of Chapter 4 of *Test Driven Development in Python*.  It is also my first attempt at including
an image.

.. image:: _images/tdd_cycle.png
    :scale: 50 %

Using render_to_string with a csrf_token
----------------------------------------

In chapter 5 of Test Driven Development with Python I was having trouble getting my unit tests to pass
once I included {% csrf_token %} in the template. The method ``render_to_string()`` was not converting
it to the proper hidden input token. I found i could at least partially correct that by including a
RequestContext in the parameters:

``expected_html = render_to_string('home.html', RequestContext(request))``

or

``expected_html = render_to_string('home.html', RequestContext(request, {'new_item_text': 'A new list item'}))``

But it still gave me a warning::

    C:\Users\frjam_000\Envs\tdd2\lib\site-packages\django\template\loader.py:97:
    RemovedInDjango110
    Warning: render() must be called with a dict, not a RequestContext.
    return template.render(context, request)





