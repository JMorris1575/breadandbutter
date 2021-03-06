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





Red/Green/Refactor and Triangulation
------------------------------------

From about 1/3 through Chapter 5 of *Test Driven Development in Python*::

    The unit-test/code cycle is sometimes taught as Red, Green, Refactor:

        * Start by writing a unit test which fails (Red).
        * Write the simplest possible code to get it to pass (Green), even if that means cheating.
        * Refactor to get to better code that makes more sense.

    So what do we do during the Refactor stage? What justifies moving from an implementation where we "cheat" to one
    we’re happy with?

    One methodology is eliminate duplication: if your test uses a magic constant (like the "1:" in front of our list
    item), and your application code also uses it, that counts as duplication, so it justifies refactoring. Removing
    the magic constant from the application code usually means you have to stop cheating.

    I find that leaves things a little too vague, so I usually like to use a second technique, which is called
    triangulation: if your tests let you get away with writing "cheating" code that you’re not happy with, like
    returning a magic constant, write another test that forces you to write some better code. That’s what we’re doing
    when we extend the FT to check that we get a "2:" when inputting a second list item.


Useful Commands Updated
-----------------------

Instructions on running tests from about 1/10 of the way through Chapter 6 of *Test Driven Development in Python*::


    To run the functional tests
        python3 manage.py test functional_tests
    To run the unit tests
        python3 manage.py test lists

    What to do if I say "run the tests", and you’re not sure which ones I mean? Have another look at the flowchart at
    the end of Chapter 4, and try and figure out where we are. As a rule of thumb, we usually only run the functional
    tests once all the unit tests are passing, so if in doubt, try both!


Installing Bootstrap
--------------------

Here are the instructions on installing bootstrap from *Test Driven Development in Python*, Chapter 7::

    $ wget -O bootstrap.zip https://github.com/twbs/bootstrap/releases/download/\
    v3.3.4/bootstrap-3.3.4-dist.zip
    $ unzip bootstrap.zip
    $ mkdir lists/static
    $ mv bootstrap-3.3.4-dist lists/static/bootstrap
    $ rm bootstrap.zip

However, wget did not work so I had to download the file for the current version myself.  Also, mkdir didn't make any
more than one directory at a time.  I don't know if that is a windows limitation or if I have something (Command
Extensions) turned off.

Bootstrap Documentation
-----------------------

The documentation for bootstrap's css can be found at `getbootstrap.com/css/`


How to Use ssh
--------------

I had trouble getting into jmorris.webfactional.com through ssh because I forgot how to do it.  Here's how:

    ssh jmorris@jmorris.webfactional.com

    When it asks for the password it is Dylan Selfie.

    I didn't like the prompt that shows up by default (-bash-4.1$ ) so I did some research to figure out how to change
    it.  The webpage at `http://www.cyberciti.biz/tips/howto-linux-unix-bash-shell-setup-prompt.html` helped the most.
    All I have to do is enter the command:

    PS1="-\w$ "

    to change the prompt to:

    -~/webapps$

    and other things that help me keep track of which folder I'm in.




How to Deploy to Webfaction.com
-------------------------------

I have a lot I need to include, but here are some thoughts as they occur to me:

* You need to go to webfaction.com to create a website, an app for that website and a database for it to use.
* Use Filezilla to edit /home/jmorris/webapps/<webfactional_app_name>/apache2/conf/httpd.conf
    * there are two lines where references to MyProject need to be changed to <webfactional_app_name>
    * You must first make sure you have set the default editor in Filezilla:  Edit->Settings->File editing
* When logging in on webfactional's phpPgAdmin your username and password are BOTH case sensitive.
* The 'HOST' and 'PORT' settings under DATABASES in the settings.py file need to be commented out.
* To restart the apache2 server, get into the apache2/bin directory and enter ./restart
* Be careful to include all your static files in the right places (check settings.py)


Solving Problem with Static Files
---------------------------------

Clues:

On `http://christmas.jmorris.webfactional.com/` the link to the css file (viewed through "View Page Source") is:
"/static/css/christmas15.css" but, somehow, it gets to the static files in the christmas15_static app.

By reading some of the Static-only documentation on ``https://docs.webfaction.com/software/static.html#static-only``
I find that a static-only application needs to be set up in webfaction's control panel and the tdd-staging website
needs to include it with the "Contents" section including a line that says:  "/static served by tdd2_static -Web419"

So I added a new application:  ``tdd2_static`` with App category = Static and App type = Static only (no .htaccess).
I added the new application to the TDD-Staging Tutorial website writing "static" into the url box.

I had to wait a couple of minutes before the change became effective so I looked at how I might change the
settings.py file to include the current static files.  I tried

    STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../../static'))

to see if it needed to reach two directories back.  That neither worked nor changed the link as viewed through
View Page Source.  I tried it with no double dots:  'static' and got the same results.

The tdd2_static application was ready so I moved the static files in webapps/tdd2_staging/static into
``webapps/tdd2_static`` and it worked!  This may not be the way I should be doing it, I suspect I should somehow
be using python3.5 manage.py collectstatic but that may be something to learn another day.  I think, on the webfactional
site at least, using a separate static-only app is the way to go since the information on it is served by another server
and doesn't tax the "dynamic" server so much.

