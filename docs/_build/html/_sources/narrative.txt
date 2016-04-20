Narrative Usage Notes
=====================

Here we discuss the usage of the Bread and Butter website
in a narrative format, explaining the experience a family
member might have once the site is completed.

This narrative can also form the structure of my functional tests.  See *Test Driven Development
in Python* by Harry Percieval, Chapter 2:
http://chimera.labs.oreilly.com/books/1234000000754/ch02.html#_using_a_functional_test_to_scope_out_a_minimum_viable_app

Writing a Note
--------------
Jim has just completed the website and enters it to write the first note. After logging
in he comes to the note listing page which currently has no notes on it. It does, however,
have a "Write New Note" button which he presses to enter the note composition page.

Composing and Saving a Note
---------------------------
In the note composition page Jim finds a blank area in which to compose his note. Instructions
printed on the page indicate that his note should be short, 1024 characters or less, counting
spaces and punctuation. He writes a note about building the website and his hopes for it. As
he writes, there is a running countdown as to how many characters he has left. When he is
finished composing the note he clicks on the "Submit" ("Publish", "Save"?) button to submit
the note. There is also a "Cancel" button that, if clicked, would leave the compostion page
without saving the note. Either way, Jim returns to the Note listing page with his new note
(if submitted) now visible.

Administrator Sending an E-mail
-------------------------------
Being the administrator of the website, Jim has more items in his navigation menu than the
rest of the family. One of these is labelled "Send E-Mails." He clicks this to enter an
e-mail composition page. There is a checklist of all the family members to whom to send
this e-mail. There is also a "Select All" checkbox to select them all. Jim checks this box
and composes the e-mail in text entry area provided. He writes an e-mail to invite all of
the family members to the new website. This is actually an e-mail template with some
keyword variables that will be replaced by each family member's username and password. When
finished composing the letter Jim clicks the "Test" button to see how the e-mails will look.
This displays in a box to the side (below?) the composition area. Once satisfied with his
e-mail, Jim clicks the "Send" button to send it out to all the family members.

Finding Out About the Site
--------------------------
Madeline checked her e-mail one day and found an e-mail from Bread and Butter Notes. The
e-mail explained the purpose of the site and gave the username and password she could use
to access the site as well as a link to the site itself. Interested, Madeline clicked the
link and was taken to the login page of the website.

Logging In
----------
The login page serves as a welcome page welcoming the currently unknown user. Madeline
enters the username and password she was given and presses the login button. Since she
entered her login information correctly, she goes to the note list page which lists all
the notes that have been entered so far.  If there are more than twenty notes they are
listed on several pages. Had she logged in incorrectly, she would come back to the login
page with the error(s) highlighted.

Visiting the Note List
----------------------
Since Madeline is the first to enter, the only note displayed is one that Jim
wrote. Only a part of Jim's message is visible below the header which has Jim's
name as the author and the date of the note. Below the note there is space for
the number of responses made, and the date and author of the most recent response.
This region currently says "Currently no responses." There is also a small message
that says "Click note to expand."

Viewing a Single Note
---------------------
Madeline clicks the note from Jim and is taken to the Note view page. The whole note
can be read under the note's author and date. Underneath that is an Add Response button.

Making a Response
-----------------
Madeline clicks the "Add Response" button and enters the Response Composition page. Jim's
note appears at the top of the page with an area for Madeline to response placed below. She
reads the explanation that says her response can be 512 characters or less and, as she types,
it displays a running count of how many characters she has left. When she is finished she
presses the "Save" button to save the note. She is returned to the note display page with
her response added under Jim's original note.

Editing a Response
------------------
When looking over the response she has written, Madeline notices a misspelled word and wants
to correct it. There is an "Edit" button next to her response along with an "Erase" button to
eliminate the whole thing. (These buttons only appear to Madeline for responses she has
written.) She clicks the "Edit" button and re-enters the Response Composition page which
appears as before but here response is already displayed in the composition area. She makes
the correction and clicks on the "Save" button. Her corrected response appears below Jim's
note with the edit date at the end.

Using the Navigation Bar
------------------------
Janet also responds to her invitation e-mail and visits the site. Once she logs in she sees
the note list page displaying Jim's original note. She clicks it to read it and Madeline's
response and then clicks the "Home" link in the navigation bar to go back to the note list
page. She notices a User Profile entry on the navigation bar and clicks it to see what it
does.

Changing One's User Profile
+++++++++++++++++++++++++++
Clicking on the User Profile navigation entry sends Janet to the User Profile Edit page
where she can change her e-mail, her password or her user name. I'll have to think
about whether I want her to be able to change her display name. In the future she may
be able to change her display picture. There are instructions on the page explaining,
among other things, that Jim is not able to tell the passwords they enter but can
restore their access to the site should they forget the one they choose. Janet changes
her password and presses "Submit." She is logged out and then logged in again with the
new profile. Perhaps an e-mail should be sent to confirm the changes before they are made.

Accessing the Help Pages
++++++++++++++++++++++++
Also on the Navigation Bar is a link marked Help. Janet presses that and is taken to a series
of pages generated by Sphinx that explain how to use the website. She reads for a bit, noticing
how she can change her User Profile then clicks the Bread and Butter Logo to return to the
Note list page.

