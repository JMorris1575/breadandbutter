==================================
Bread and Butter Development Notes
==================================

This section serves as a means of documenting the process
of creating the Bread and Butter Notes website so that I
may refer to this documentation when building new websites.

Preliminaries
+++++++++++++

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

but it didn't work out as well as I had hoped. I will probably have
to work my way through Sphinx's own documentation.

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

Starting Version Control
------------------------

I used PyCharm's "VCS-->Enable Version Control Integration..." then selected Git to
start the version control.  I also had to add all of the existing files to be tracked.

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

#. Modify the settings.py file to use the postgreSQL database:
    (Instructions still pending)

#. Point PyCharm to the project:
    File-->Open... then select the Repository Root folder.

#. Initiate Version Control.
    In PyCharm VCS-->Enable Version Control Integration... then select Git.

#. Create the .gitignore file:
    (instructions still pending)

#. Test the website:
    ``python manage.py migrate`` -- note: I'm not sure this is necessary
    ``python manage.py runserver``
    Then, visiting localhost:8000 should arrive at the Welcome to Django page.

#. Perform the first commit:
    VCS-->Commit Changes...


This is the point of the first commit -- named "Initial Commit"





