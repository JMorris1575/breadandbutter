Model Design
============

Outline of Data Needed
----------------------

I made the following list from reading over the Project Specification
and the Narrative Usage Notes trying to discern the data the website
will need to keep track of.

===================== ===================== ==============================
Data                  Source                Comments
===================== ===================== ==============================
Note Author           Proj. Spec. 3.2.2
Note Date             Proj. Spec. 3.2.2
Note Edit Date        none                  Records note's last edit date
Note Contents         Proj. Spec. 3.2.2     1024 characters max
Note Responses        Proj. Spec.           Count programatically?
User Name             Proj. Spec. 3.2.3     For authentication
User E-mail           Proj. Spec. 3.2.3
User Password         Proj. Spec. 3.2.3
User Display Name     Proj. Spec. 3.2.3
User e-mail choice(s) Proj. Spec. 3.2.3
E-mail Title          Narrative 3.3.3       To store commonly sent e-mails
E-mail Contents       Narrative 3.3.3
Last E-mail Date      none                  To calculate next e-mail date
Response Author       Narrative 3.3.8
Response Date         Narrative 3.3.8
Response Edit Date    Narrative 3.3.9       Response's last edit date
Response Contents     Narrative 3.3.8       512 characters max
===================== ===================== ==============================

From this I can see that at least five models are necessary:

================ ===================================================
The Five Models:
================ ===================================================
User             from django's authentication system
User Profile
Note
Response
E-mail           although this may better be handled by static files
================ ===================================================

The models are outlined below:

User Model
----------
================ ===================================================================
Fields:          see auth
================ ===================================================================
**username**
**password**
**e-mail**
================ ===================================================================

User Profile Model
------------------
================ ===================================================================
Fields:
================ ===================================================================
**display_name** (char field - 40 characters)
**email_option** (boolean, default=True)
================ ===================================================================

Note Model
----------
================ ===================================================================
Fields:
================ ===================================================================
**author**       (foreign key to User - many to one)
**pub_date**     (date-time) - time needed for two notes in one day-display order
**edit_date**    (date-time)
**contents**     (text field)
**slug**         (char field ?? characters) - based on the publication date-time
================ ===================================================================

Response Model
--------------
================ ===================================================================
Fields:
================ ===================================================================
**author**       (foreign key to User - many to one)
**note**         (foreign key to Note - many to one)
**pub_date**     (date-time)
**edit_date**    (date-time)
**contents**     (text field)
**slug**         (char field, ?? characters) - based on the publication date-time
================ ===================================================================

E-mail Model
------------
================ ===================================================================
Fields:
================ ===================================================================
**name**         (char field, 40 characters) - used to identify the e-mail template
**slug**         (char field, ?? characters) - based on the name
**contents**     (text field)
================ ===================================================================