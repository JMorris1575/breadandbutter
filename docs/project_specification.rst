Project Specification
=====================

General Description
-------------------
The Bread and Butter Notes website is meant to be a simple means for members of
my family to keep in touch with one another by writing quick notes about whatever
is going on in their lives or writing responses to notes written by others.

Using the Website
-----------------
Notes are easily accessed through a series of pages displaying all of them in the
order of recent activity, through pages that list notes authored by a particular individual,
or, as the site ages, through archive pages.

Each note is displayed as a thumbnail containing the author's name, the date of its original
publication, the first part of the message, the number of responses and the date of the
most recent response and its author. Clicking on a note displays it in full with the author,
publication date, contents of the original note, any responses that have been made, including
their authors and publication dates and a button for adding a new response. If the current
user is the author of the original note or any of the responses to a note there is an
edit button next to it to allow for editing the notes or responses.

Site Users
----------
Membership on the website is by invitation only. Each family member will get an e-mail
explaining the site, how to get to the site and a username and password to use to login
to the site.

Upon entering the site an unauthenticated user comes to a login page welcoming them
to the Bread and Butter Notes website, explaining its background, and allowing them to
enter their username and password.

Once they are authenticated they are brought to the Note Display page to begin their
activity on the site. Every page they visit will have, at the top, their name and
a Logout button.

An authenticated user can update his or her User Profile to change their username,
password, e-mail address and/or display name. In the future it may be possible to
devise some means of displaying a thumbnail picture of their face. They may also
use this page to indicate whether or not they wish to receive automatic e-mails
about the activity on the site.

E-mails
-------
As the owner of the site I can send out individual or bulk e-mails to any or all
of the members. It may be good to develop some sort of templating language so
that one e-mail template can be written that has each individual's data, such
things as their name, inserted in the proper places. (Maybe Django already does
this?)

Also, the site can generate automatic e-mails informing users that have allowed it
that there is new content on the site. These e-mails will not be sent every time
there is new content, but no more than once per chosen interval. I'm thinking, no
more than once per week. These e-mails can tell who has written notes and who has
written responses.


Archives and Indexing
---------------------
As the site ages it may become impractical to have page after page after page of all the
notes. There needs to be some organizational scheme for saving them in archives. Notes in
the archives are still active, that is, they can be responded to by any member and edited
by their authors, but people need to have them out of the way. The notes can be archived
according to the year and month of their publication. But it may also be good to have an
index page of all the notes organized by date or by author or perhaps even by responses
made. Each main note entry should have the date, the author, the first part of the note
and a list of indented responses with dates, authors and first parts of responses. This
feature can definitely wait for later implementation but may need to be kept in mind
during the model design.

