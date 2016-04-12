Preliminaries
=============

Working Environment
-------------------

I wanted to use python 3.5 but, since I had originally installed virtualenvironmentwrapper-win
under python 3.4 it wasn’t working.  Even if I specified the python version I wanted to use,
including the full path to the executable, it just told me that executable did not exist in “...”
where "..." was the entire path variable.

Installing Python 3.5.1 with the default button installed it to the appdata\local (etc.) directory
and didn't help.

Finally, I installed Python 3.5.1 using the custom installation and putting it into C:\Python35\.
I also had to check the box to put it into the path variable.

That resulted in Python 3.5 being my default Python (I think) and, since mkvirtualenv was still
loading Python 3.4 I did::

	> pip install virtualenvwrapper-win

to get it into Python 3.5.

Finally::

	> mkvirtualenv bnb

created a bnb environment based on Python 3.5!

There is a webpage at:

	https://docs.python.org/3.3/using/windows.html#python-launcher-for-windows

explaining how to use different versions of python on the same machine if some of my old programs turn out not to work.

[Note: I think I just discovered what I was doing wrong. Trying to test PyInstaller for a PyQt program (which currently
only works under Python 3.4) I finally noticed the error message::

    >mkvirtualenv -p=c:/python34/python pyinstaller
    The executable =c:/python34/python (from --python==c:/python34/python) does not exist.

Notice the "=" before the path! It turns out that the correct command is::

    >mkvirtualenv -p c:/python34/python.exe pyinstaller

although I'm not sure I really needed to specify python.exe rather than just python.

Installing Django
-----------------

In C:\\Users\\Jim

I ran the command::

	> pip install Django

which downloaded and installed Django 1.9.5.  It can be seen in C:\Users\Jim\Envs\bnb\Lib\site-packages

Designinging the Project Structure
----------------------------------

After reviewing Chapter 3 of Two Scoops of Django (see especially section 3.3, pages 24-26),
I decided on something like the following project structure::

    C:\
     |-(other folders)
     \-Users\
       |-(other users)
       \-Jim\
         |-(other files for Jim)
         \-Documents\
           |-(other_documents)
           \-MyDjangoProjects\
             |-(other_projects)
             \-BnB_Development\ (Two-Scoops’ “Repository Root” and PyCharm's Project Root as well)
               |-.gitignore
               |-requirements.txt
               |-docs/
               |-readme.txt
               \-Bread_and_Butter_Notes\ (Two-Scoops’ “Project Root”)
                 |-manage.py
                 |-media/ # Development ONLY!
                 |-app1/
                 |-app2/
                 |-app3-etc/
                 |-static/
                 |-templates/
                 \-config/    (Two-Scoops’ “Configuration Root”)
                   |-__init__.py
                   |-settings/
                   |-urls.py
                   \-wsgi.py

In MyDjangoProjects\\BnB_Developoment I ran the command::

    django-admin startproject Bread_and_Butter_Notes

then renamed the inner Bread_and_Butter_Notes directory to config.

I used PyCharm's "File-->Open..." menu command to open a project at BnB_Development.

To simplify working on the project from a command prompt I created a bnb.bat file in
C:\\Users\\Jim.  It reads::

    echo off
    cd "Documents\MyDjangoProjects\BnB_Development\Bread_and_Butter_Notes"
    workon bnb

Now, upon entering the command window, simply typing::

    bnb

will change to the correct directory and enter the bnb virtual environment.

Changing the Mode of manage.py
------------------------------
Following the tutorial *Python Django Tutorial 2 new 1.7+ migrations* by Mike Hibbert at:
https://www.youtube.com/watch?v=fbJgeJjA7Cg&index=2&list=PLxxA5z-8B2xk4szCgFmgonNcCboyNneMD
I changed the mode of manage.py by using the command::

    chmod +x ./manage.py

Now simply typing ``manage.py <command>`` should work instead of ``python manage.py <command>``.
By the way, the tutorial said to do::

    chmod +x manage.py

but he had to type ``./manage.py``. If it really works, I like my way better.

Installing and Using Sphinx
---------------------------

Two Scoops of Django suggested using Sphinx for the development
of a website’s documentation so I found its own website at:

    http://www.sphinx-doc.org/en/stable/tutorial.html

To install it I opened a command prompt and immediately, without
getting into a virtual environment because they suggested it be
installed site-wide, typed::

    pip install Sphinx

It installed without incident.

Learning to use it will probably be an ongoing process. I did find
a tutorial at:

    http://matplotlib.org/sampledoc/

but it didn't work out as well as I had hoped.

Sphinx's own documentation is at http://www.sphinx-doc.org/en/stable/contents.html
I found a very useful page for html themes at http://www.sphinx-doc.org/en/stable/theming.html
For working with color schemes, this site is useful: http://www.w3schools.com/colors/colors_names.asp
Pygments styles information is found here: http://pygments.org/docs/styles/

.. note::

    When I added the project_specification.rst file its sidebar did not contain the previous and
    next page links. I was able to fix that by running::

        sphinx-build -b html -a . ./_build/html

    The -a option, not included in the make.bat file, writes all output files from the current directory (.)
    to the build directory (./_build/html). It may also create the necessary file in the html/.doctrees
    directory. Perhaps I could also have accomplished this by deleting the html/.buildinfo file.

Testing the Website
-------------------

Since I changed the name of the inner "Bread_and_Butter_Notes" folder to "config" I
had to modify the manage.py file before I could run migrate.  After the imports
it now reads::

    if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

There is a similar line in the wsgi.py file.  It reads::

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Bread_and_Butter_Notes.settings")

Starting the server with::

    python manage.py runserver

I found that wsgi is run when the server starts.  (I had inserted a print
statement to alert me as to when it was run.)  It hasn't caused any problems
yet but it may in the future.  I will leave it alone for now.

Going to http://localhost:8000/ got me to the Welcome to Django page.  So far, so good.

Changing the Database to PostgreSQL
-----------------------------------

According to https://wiki.postgresql.org/wiki/Running_%26_Installing_PostgreSQL_On_Native_Windows
PostgreSQL can best be installed by the One-Click installer found here:
http://www.postgresql.org/download/windows/

During the PostgreSQL installation I was asked to provide the following:
    * A password for the database superuser (postgres) --> I used Dylan Selfie
    * The port # server should listen on --> I used 5432 (the default)
    * The locale to be used by the new database cluster --> I used [Default locale] (the default)

It offered to run Stack Builder after the install in order to "download and install additional
tools, drivers and applications to complement your PostgreSQL installation." I ran it, but
didn't let it install anything.

According to https://docs.djangoproject.com/en/1.9/ref/settings/#databases , the following should
be in the settings.py file::

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.path.join(BASE_DIR, 'bnbnotes'),
            'USER': 'postgres',
            'PASSWORD': 'DaysOf49',
            'HOST': '127.0.0.1',
            'PORT': '5432'
        }
    }

Actually,the name they suggested was not prepended by BASE_DIR, so I'll see if this works.

.. Note::
    It didn't work. The 'NAME' should simply read `'NAME': 'bnbnotes',`

Running ``python manage.py migrate`` above created a db.sqlite3. I deleted that and tried
to run migrate again but it didn't work. I got an ``Import Error: No module named 'psycopg2'``

I tried again with ``'ENGINE': 'django.db.backends.postgresql_psycopg2',`` and got the same error.

I thought that perhaps psycopg2 was something that I should have let Stack Builder download and
install so I got back into it (it is in the start menu under the PostgreSQL heading) but it didn't
have anything called psycopg2 to install. Time for an internet search...

I eventually found an older version of psycopg2 at https://github.com/nwcell/psycopg2-windows and
and downloaded the .zip file to my C:\Users\Jim\Documents\Net Gleanings\PostgreSQL folder. I copied
the psycopg2 folder from the .zip file to C:\Users\Jim\Envs\bnb\Lib\site-packages and tried
migrate again.

This time I got this error: ``ImportError: Module use of python34.dll conflicts with this version
of Python.`` I investigated to see if I could change python34.dll to python35.dll. I couldn't. I
erased the psycopg2 folder from site-packages and tried again.

On http://stackoverflow.com/questions/28611808/how-to-install-psycopg2-for-python-3-5 I found this answer:

    *I ran into a similar issue on Windows. I had to install a compiled version of it and then easy_install it.*
    *You can find a compiled version of psycopg2 here: http://www.lfd.uci.edu/~gohlke/pythonlibs/*
    *And then do easy_install C:/locaiton/of/download.exe*
    *That's what I do to install it on my Windows machine.*

Followed by this one:

    *Try this one. It worked for me*
    *I Visited the http://www.lfd.uci.edu/~gohlke/pythonlibs/ and downloaded psycopg2-2.6.1-cp35-none-win32.whl*
    *file and copied it on C:\ later I activated my Virualenv by running this C:\mydjango\django19\Scripts\activate*
    *on the cmd which resulted to this (django19) C:/> and ran the following pip command,*
    *pip install psycopg2-2.6.1-cp35-none-win32.whl and the installation was successful.*

    *Note: Run the pip install psycopg2.......whl when you are in the current folder that has the*
    *psycopg2-2.6.1-cp35-none-win32.whl file via cmd*

The second one seemed best so I tried it. First, to make things simpler, I copied the .whl file to the C:\
directory. Then, while in the bnb virtual environment and after changing to the C:\ directory typed::

    pip install psycopg2-2.6.1-cp35-cp35m-win_amd64.whl

which I actually copied from here. It said it successfully installed and I could see it in my bnb site-packages.

.. Note::
    When I tried this on my computer in Kalamazoo it kept giving me a message saying:
    `psycopg2-2.6.1-cp35-cp35m-win_amd64.whl is not a supported wheel on this platform.`  I eventually learned that it
    was because I was using pip version 7 instead of pip version 8. When I ran `python -m pip install --upgrade pip` it
    worked just fine.

I tried migrate again and . . . I got a fatal error saying
FATAL:  database "C:\Users\Jim\Documents\MyDjangoProjects\BnB_Development\Bread_a" does not exist.
I suspect that is because I prepended BASE_DIR to my bnbnotes database. After I eliminated that I still
got the error saying that database bnbnotes did not exist. I suppose I have to create it ahead of time.

I got into PostgreSQL's pgAdmin III and started reading the help file. Double-clicking the PostgreSQL 9.5
server "connected" me after I entered the password (Dylan selfie). After some playing around I created
a new database named bnbnotes and owned by Jim with the Dylan selfie password. I tried migrate again
but password authentication failed for user Jim. I played around some more trying different roles for
Jim but to no avail. I found a PostgreSQL tutorial at http://www.postgresqltutorial.com/ and will try to
learn from that.

After mucking around in the pgAdmin I found that if I created a login role for the user Jim and gave him
the Dylan Selfie password with all the privileges then created the bnbnotes database with Jim as the owner
and otherwise the default settings then migrate would run without a hitch. Hurray!

Starting Version Control
------------------------

I used PyCharm's "VCS-->Enable Version Control Integration..." then selected Git to
start the version control.  I also had to add all of the existing files to be tracked.

Later Note: Somehow the sphinx-generated files did not get added to the repository. I have taken care
of that now by adding the docs directory, but I may have to watch out for this if generated files are
not automatically included.

Quick Outline of How to Get Started
-----------------------------------

#. Create Virtual Environment::
    ``mkvirtualenv <env_name>``

#. From within that environment install Django::
    ``pip install Django``

#. Create and move to the project folder and create a project::
    ``django-admin startproject <project_name>``

#. Change the name of the inner folder whose name matches the project
    name and modify manage.py (and wsgi.py) accordingly:
    ``os.environ.setdefault("DJANGO_SETTINGS_MODULE", "<project_name>.settings")``
    changes to:
    ``os.environ.setdefault("DJANGO_SETTINGS_MODULE", "<config_folder_name>.settings")``

#. Make the modifications necessary to use the postgreSQL database:
    * Install PostgreSQL on the local computer if necessary
    * Install psycopg2 into the virtual environment
    * Use PostgreSQL's pgAdmin to create a database
    * Modify the settings file to use PostgreSQL

#. Point PyCharm to the project:
    File-->Open... then select the Repository Root folder.

#. Initiate Version Control.
    In PyCharm VCS-->Enable Version Control Integration... then select Git.

#. Create the .gitignore file:
    (instructions still pending)

#. Test the website:
    * ``python manage.py migrate`` -- note: I'm not sure this is necessary
    * ``python manage.py runserver``
    * Visit ``localhost:8000`` to see if you arrive at the Welcome to Django page.
    * I need to learn how to design and run a series of tests for Test Driven
      Development as explained in the book *Test Driven Development in Python*
      by Harry Percival. It can be found at http://chimera.labs.oreilly.com/books/1234000000754/index.html

#. Perform the first commit:
    VCS-->Commit Changes...


This is the point of the first commit -- named "Initial Commit"
