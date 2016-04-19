URL Scheme
==========

To quote *Django Unleashed* (p. 750) "We can tackle the problem (of building URLs) by organizing URLs according to
model and CRUC: how do we list, create, read, update, and delete objects?"  Going in the order of the models in
my models documentation I should start with the Users.

User and User Profile Models URLs
---------------------------------

The User model itself is from django/auth and will be initialized by me.  In other words, there will be no opportunity
for someone to create his or her own user and user profile data.  However, family members can CHANGE their personal
information and perhaps I will want, as the administrator, to view a chart listing everyone's activities.  Here is
an attempt at defining URLs for family members:

========================================================= ==========================================================
URL                                                       Notes
========================================================= ==========================================================
/user/                                                    list of users available only to the administrator
/user/<username>                                          user information available only to the administrator
/user/<username>/update                                   allows each user to update their information
========================================================= ==========================================================

Note Model URLs
---------------

Notes can be listed, created, updated, and edited by their authors, and deleted by the administrator.  After working
on this for a while, I decided that creating a "slug" for the note model would be helpful.  The slug would contain
reference to the year/month/day/hour/minute/second of the note's creation, and maybe the author too.  Here is what I
started with:

========================================================= ==========================================================
URL                                                       Notes
========================================================= ==========================================================
/note/                                                    paginated list of notes -- this is the starting page
/note/create/                                             this is where a user creates a note
/note/<author>/<year>/<month>/<day>/<h>/<m>/<s>/edit/     this is where the author or administrator edits a note
/note/<author>/<year>/<month>/<day>/<h>/<m>/<s>/read/     this is where an individual note is displayed
/note/<author>/<year>/<month>/<day>/<h>/<m>/<s>/delete/   this is where the administrator can delete the note
========================================================= ==========================================================

but the above urls seem too long and, considering the responses to the notes, it didn't seem to make sense to
double up on the use of year/month/day/hour/minute/second as a means of both notes AND their responses.  I thought
it might not be so bad to identify notes and their responses by their private keys <pk>, whether or not Andrew Pinkham,
the author of *Django Unleashed* would approve, but I tried it anyway:

========================================================= ==========================================================
URL                                                       Notes
========================================================= ==========================================================
/note/                                                    paginated list of notes -- this is the starting page
/note/create/                                             this is where a user creates a note
/note/<author>/<pk>/edit/                                 this is where the author or administrator edits a note
/note/<author>/<pk>/read/                                 this is where an individual note is displayed
/note/<author>/<pk>/delete/                               this is where the administrator can delete the note
========================================================= ==========================================================

But perhaps all the date and time information could be compressed into a slug, perhaps with the author's name too,
except that might cause problems if a family member should change their username.  Let's try this:

========================================================= ==========================================================
URL                                                       Notes
========================================================= ==========================================================
/note/                                                    paginated list of notes -- this is the starting page
/note/create/                                             this is where a user creates a note
/note/<author>/<note-slug>/edit/                          this is where the author or administrator edits a note
/note/<author>/<note-slug>/read/                          this is where an individual note is displayed
/note/<author>/<note-slug>/delete/                        this is where the administrator can delete the note
========================================================= ==========================================================

Response Model URLs
-------------------

Responses are related to their notes so it might make sense to have both represented in the URLs.  Also, I don't see
a need for listing all responses on a page separate from the note itself.  I do, however, see a need for displaying
a response on its own page:

========================================================= ==========================================================
URL                                                       Notes
========================================================= ==========================================================
/response/<note-slug>/create/                             this is where a user creates the response to a note
/response/<note-slug>/<author>/<response-slug>/read/      this is where an individual response can be read
/response/<note-slug>/<author>/<response-slug>/edit/      this is where the author or administrator edits a response
/response/<note-slug>/<author>/<response-slug>/delete/    this is where the administrator can delete the response
========================================================= ==========================================================

E-mail Model URLs
-----------------

Probably only the administrator will have access to the e-mail pages.  But, still, they have to be created, edited and
deleted.  Maybe there should be a page reporting on outcomes:  saved or sent for instance:

========================================================= ==========================================================
URL                                                       Notes
========================================================= ==========================================================
/email/create/                                            this is where the administrator creates an e-mail
/email/<email-slug>/edit/                                 this is where the administrator updates a saved e-mail
/email/<email-slug>/delete/                               this is where the administrator deletes a saved e-mail
/email/<email-slug>/outcome/                              this is where the system reports on the send/save outcome
========================================================= ==========================================================


