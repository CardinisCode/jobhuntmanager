# Technical Readme
## Services:

This file will cover all the files & functions, found in the services directory, in more (technical) detail, all of which the functionality to build the 'back-end' of the application. All the functions found  in this directory are written in Python, with the main library used being Flask.

I've broken these functions up into 11 directories, each of which covers a specific area of functionality for the application:
-   Address book
-   


Within each directory are the CRUD elements: 
-   Create
    -   I started such files & functions with 'add_...'
-   Read
    -   I started 'Read' files with 'view_...'
    -   & 'Read' functions with 'get_...'
-   Update
    -   These files / functions start with 'update_...'
-   Delete 
    -   These files / functions start with 'delete_...'

### address_book:
This includes the functionality behind displaying the user's contacts to the template: 'view_address_book.html'.

##### view_address_book.py
###### display_address_book():
Collects the top 8 company contacts:
-   Calls on the 'getTop8CompaniesByUserID()' method (in the CompanyRepository) to get the top 8 company contacts, ordered by the Company's name. 
-   These contacts are added to a dictionary, with their unique ID (company_id).
-   Calls on the 'cleanup_company_fields()' function to improve how the field values are presented to the user.

Collects the top individual contacts:
-   Calls on the 'getTop8ContactsByUserID()' method (in the 'ContactRepository') to get the top 8 individual contact entries, ordered by the contact's Full name.
-   These contacts are added to a dictionary, with their unique ID (contact_id).

Collects all the links needed to be displayed to the template.

Renders to template:
    'view_address_book.html'

### application_notes:
This where you'll find all the Python functions related to Application Notes.

The files in this directory:

##### add_app_note.py
This includes the functionality behind:
    -   Displaying a form to the user, giving the user the option to add a note which links to a specific job application.
    -   Storing the values provided (by the user) into the 'application_notes' table in the SQL database.
    -   Redirecting the user to view the details for the newly-created 'application'. 

Functions:

##### display_application_note_form()
This function handles the GET functionality for the route: 
    '/applications/<int:application_id>/app_notes/add_note'

Takes (input):
-   notes_form (a blank instance of the AddApplicationNoteForm() Form)
-   application_id, companyRepo, applicationsRepo

Functionality (algorithm):
-   Gets the company_name by:
    -   getting the application (via the 'getApplicationByID() in the applicationsRepo)
    -   getting the company (via the getCompanyById() in the companyRepo)
    -   using this company (above) to get the company's name using dot notation, since the 'getCompanyById()' method returns the company as a 'Company' object. 

-   Puts together the action_url to be displayed to the user, where the action URL is responsible for displaying the form to the user.

Renders the template:  
    -   'add_application_note.html'
    -   with a blank instance of the AddApplicationNoteForm() Form. 

##### post_application_add_note()
This function handles the POST functionality for the route: 
    '/applications/<int:application_id>/app_notes/add_note'

Takes (input): 
    -   notes_form (as submitted by the user)
    -   application_id, companyRepo, applicationsRepo

Functionality (algorithm):
-   Calls the 'getApplicationByID()' to get the application linked to this specific note. I used this 'Application' object to get the company_id. 
-   Stored the current date (using datetime.now().date() in a variable & converts the value to a string. 
-   Extracts the values from the form fields & stores these fields, the date string, user_id, application_id & company_id. 
-   Calls on the createApplicationNote() function (in the ApplicationNotesRepository), with the values from the dictionary, to create a note entry in the 'application_notes' SQL table.

Finally: 
    The User is redirected via the route: '/applications/<int:application_id>/app_notes/<int:app_notes_id>/view_note'

##### delete_app_note.py
This includes the functionality behind:
    -   Deleting an application note entry from the 'application_notes' table (in the SQL database). 
    -   Redirecting the user to route: '/applications/<int:application_id>/view_application_notes'. 

Functions:

###### delete_application_note()
This function handles the GET functionality for the route: 
    '/applications/<int:application_id>/app_notes/<int:app_notes_id>/delete_note'

Takes (input): 
    application_id, app_notes_id, appNotesRepo

Functionality (algorithm):
-   Calls on the 'deleteNoteByAppNoteID() method in the ApplicationNotesRepository. This hard deletes an entry from the 'application_notes' table in the SQL database, using the note's unique ID (app_notes_id). 

Finally: 
    The User is redirected via the route: '/applications/<int:application_id>/view_application_notes'

##### update_app_note.py

##### view_app_note_details.py

##### view_application_notes.py







