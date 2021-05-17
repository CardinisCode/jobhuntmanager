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

#### view_address_book.py
Function in this directory:

##### display_address_book():
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

#### add_app_note.py
This includes the functionality behind:
    -   Displaying a form to the user, giving the user the option to add a note which links to a specific job application.
    -   Storing the values provided (by the user) into the 'application_notes' table in the SQL database.
    -   Redirecting the user to view the details for the newly-created 'application note'. 

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

#### delete_app_note.py
This includes the functionality behind:
    -   Deleting an application note entry from the 'application_notes' table (in the SQL database). 
    -   Redirecting the user to route: '/applications/<int:application_id>/view_application_notes'. 

Functions:

##### delete_application_note()
This function handles the GET functionality for the route: 
    '/applications/<int:application_id>/app_notes/<int:app_notes_id>/delete_note'

Takes (input): 
    application_id, app_notes_id, appNotesRepo

Functionality (algorithm):
-   Calls on the 'deleteNoteByAppNoteID() method in the ApplicationNotesRepository. This hard deletes an entry from the 'application_notes' table in the SQL database, using the note's unique ID (app_notes_id). 

Finally: 
    The User is redirected via the route: '/applications/<int:application_id>/view_application_notes'

#### update_app_note.py
This includes the functionality behind:
    -   Displaying a form to the user, giving the user the option to add a note which links to a specific job application.
        -   Function: display_update_app_note_form()
    -   Using the values provided (by the user) to update an entry in the 'application_notes' table in the SQL database.
    -   Redirecting the user to view the details for the newly-created 'application note'. 
        -   Function: post_update_app_note()

Functions:

##### display_update_app_note_form()
This function handles the GET functionality for the route: 
    '/applications/<int:application_id>/app_notes/<int:app_notes_id>/update_note'

Takes (input):
-   update_app_note_form (an instance of the AddApplicationNoteForm() Form, with the values for an existing entry)
-   application_id, user_id, app_notes_id, companyRepo, appNotesRepo

Functionality (algorithm):
-   Gets the company_name by:
    -   getting the application (via the 'getApplicationByID() in the applicationsRepo)
    -   getting the company (via the getCompanyById() in the companyRepo)
    -   using this company (above) to get the company's name using dot notation, since the 'getCompanyById()' method returns the company as a 'Company' object. 

-   Puts together the action_url to be displayed to the user, where the action URL is responsible for displaying the form to the user.

Renders the template:  
    -   'update_application_note.html'
    -   an instance of the AddApplicationNoteForm() Form, with the values for an existing entry. 

##### post_update_app_note()
This function handles the POST functionality for the route: 
    '/applications/<int:application_id>/app_notes/<int:app_notes_id>/update_note'

Takes (input): 
    -   update_app_note_form (as submitted by the user)
    -   application_id, user_id, app_notes_id, companyRepo, appNotesRepo

Functionality (algorithm):
-   Extracts the field values from the update_app_note_form & saves it all to a 'details' dictionary, including the note's unique ID ('note_id'). 
-   Calls on the 'updateNoteByID' method (linked to the ApplicationNotesRepository), to update an entry in the 'application_notes' (SQL) table.

Finally: 
    The User is redirected via the route: '/applications/<int:application_id>/app_notes/<int:app_notes_id>/view_note'

#### view_app_note_details.py
This includes the functionality behind:
-   Displaying the details for a specific application note entry to the user.

Function included:

##### display_application_note_details()
This function handles the 
GET functionality for the route: 
    '/applications/<int:application_id>/app_notes/<int:app_notes_id>/view_note'

Takes (input): 
    -   app_notes_id (the unique ID for a specific note entry)
    -   application_id, appNotesRepo, companyRepo

Functionality (algorithm):
-   Get a specific note entry from the 'application_note' (SQL table), by calling on the method 'getNoteByAppNoteID' (via the ApplicationNotesRepository).
-   Get a specific entry from the 'company' (SQL table), by calling on the method 'getCompanyById' (via the CompanyRepository).  
-   Uses the 'application_id &  app_notes_id to put together the URLs / links to be displayed to the user.
-   Converts the note's 'entry date' value to a date.
-   Stores the values for the application note entry & cleans the values for presentation to the user using the methods:
    -   cleanup_date_format()
    -   cleanup_field_value() 

Renders the template:  
    -   'view_app_note_details.html'
    -   With a dictionary containing the links/URLS & note details to be displayed to the user. 

#### view_application_notes.py
This includes the functionality behind:
-   Displaying all the application notes, for a specific application, to the user.

Function included:

##### display_application_notes()
This function handles the GET functionality for the route: 
    '/applications/<int:application_id>/view_application_notes'

Takes (input):
    user_id, application_id, applicationsRepo, appNotesRepo, companyRepo

Functionality (algorithm):
-   Get all the note entries from the  'application_note' (SQL table), by calling on the method 'getAppNotesByApplicationID' (via the ApplicationNotesRepository).
-   Get a specific company entry from the 'company' (SQL table), by calling on the method 'getCompanyById' (via the CompanyRepository).  
-   Get a specific application entry from the 'job_applications' (SQL table), by calling on the method 'getAppNotesByApplicationID' (via the ApplicationsHistoryRepository).
-   Iterates through every note returned from the SQL query 'getAppNotesByApplicationID', saving each entry in a dictionary '(user_notes_details).
-   Uses the 'application_id' to put together the links to be displayed to the user, storing these in the dictionary.

Renders the template:  
    -   'view_notes_for_application.html'
    -   With a dictionary containing the links/URLS & notes to be displayed to the user. 

### applications
This where you'll find all the Python functions related to Application Notes.

The files in this directory:

#### add_application.py
This includes the functionality behind:
    -   Displaying the 'AddApplicationForm()' (form) to the user, giving the user the option to add a note which links to a specific job application.
    -   Storing the values provided (by the user) into the 'job_applications' (SQL) table.
    -   Redirecting the user to view the details for the newly-created 'job application'. 

Functions:

##### display_add_application_form()
This function handles the GET functionality for the route: '/add_job_application'

Takes (input):
-   add_application_form (a blank instance of the AddApplicationForm() Form)

Renders the template: 'add_job_application.html', with the 'add_application_form'. 

##### add_new_application_to_application_history()
This function handles the functionality behind adding an application entry to the 'job_applications' (SQL) table.

Takes (input):
    user_id, companyRepo, applicationsRepo, application_form, company_id

Functionality (algorithm):
-   Grabs the current day's date ('date_posted') & converts the field values 'date' & 'time', received from the 'application_form', into their string equivalents.
-   Extracts the rest of the form field values & stores them all into a dictionary. 
-   Iterates through the values in the dictionary, cleaning up each value (replacing any/all empty fields with 'N/A'). 
-   Calls on the method 'createApplication' (via the ApplicationsHistoryRepository), to insert these values as an entry into the 'job_applications' (SQL) table. 

Returns:
    The unique ID ('application_id') for the newly-created entry.

##### add_or_update_company()
This function checks the company's name (as provided by the user), to see if there are any company entries in the 'company' (SQL) table which are 'like' the name provided by the user. If yes, the company entry is updated using the values (related to this company). Otherwise, it creates a new entry in the 'company' table using these details.

Takes (input):
    user_id, application_form, companyRepo

Functionality (algorithm):
-   Extracts all the field values from the 'application_form' related to a 'company', storing these values in a dictionary 'fields'.
-   Calls on the method 'getCompanyByName()' (in the CompanyRepository). It runs through every entry (the 'company' (SQL) table), checking to see if the provided 'company_name' is 'like' the value stored in the column  'name'. Any entry that meets this requirement is then returned as a 'Company' object. 
-   If the above method (getCompanyByName()) returns an entry, then it gets the company's unique ID (company_id) & updates the entry in the 'company (SQL) table, with the details provided in the 'fields' dictionary. 
-   If no entry is returned (by the method 'getCompanyByName()'), then it calls on the method 'createCompany()' to create an entry in the 'company (SQL) table, with the details provided in the 'fields' dictionary.

Returns:
    The newly-created unique ID for the entry in the 'company' SQL table.

##### post_add_application()
This function handles the POST functionality for the route: '/add_job_application'. 

Takes (input):
-   application_form (as completed by the user)
-   user_id, applicationsRepo, companyRepo

Functionality (algorithm):
-   Calls on the function (above) 'add_or_update_company()' to determine whether/not the company (to which the user is applying for a job) already exists in the 'company (SQL) table. It then either inserts or updates an entry in the 'company' table accordingly. 

-   Calls on the function (above) 'add_new_application_to_application_history()' to insert the details for the job application into the 'job_applications' SQL table as a new entry. 

Finally: 
    The User is redirected via the route: '/applications/<int:application_id>'.

#### view_application_details.py
This includes the functionality behind:
-   Displaying the details for a specific job application entry to the user.

Function included:

#####  get_job_offers()
Responsible for collecting all the job offers added for a specific job application & adding all the entries to a dictionary. 

Takes: 
    application_id, user_id, company, jobOffersRepo

Functionality (algorithm):
-   Calls on the method 'getJobOffersByApplicationId()' (in the JobOffersRepository) to get all entries where the provided unique ID for a job application (application_id) matches the entry's foreign key 'application_id'. All entries which meet this requirement are instantiated (using the 'JobOffer' class), & added to a list.

-   Iterates through each entry (received from the above SQL query, storing the required values in a dictionary.

-   'Cleans' the values for each entry (Stored in the dictionary), using the function 'cleanup_job_offer()' (found in services/cleanup_files/cleanup_job_offer_fields.py). This is done to improve how these values will be presented to the user & allows me to present these values in a consistent format across all the templates.

Returns:
    job_offers_details (the dictionary created by this function).

#####  get_interviews()
Responsible for collecting all the interviews added by a specific user & adding all the entries to a dictionary.

Takes: 
    interviewsRepo, application_id

Functionality (algorithm):
-   Calls on the method 'getTop6InterviewsByApplicationID()' (in the InterviewsHistoryRepository) to get all entries where the provided unique ID (application_id) matches the entry's foreign key 'application_id'. All entries which meet this requirement are instantiated (using the 'JobOffer' class), & added to a list.

-   Iterates through each 'interview' entry (received from the above SQL query, storing the required values in a dictionary.

-   'Cleans' the values for each entry (Stored in the dictionary), using the function 'cleanup_interview_fields()' (found in services/cleanup_files/cleanup_interview_fields.py). This is done to improve how these values will be presented to the user & allows me to present these values in a consistent format across all the templates.

Returns:
    interview_details (the dictionary created by this function). 

#####  display_application_details()
This function handles the GET functionality for the route: '/applications/<int:application_id>'

Takes: 
    interviewsRepo, application_id

Functionality (algorithm):
-   Get a specific job application entry from the  'job_applications' (SQL table), by calling on the method 'getApplicationByID()' (in the ApplicationsHistoryRepository).

-   Get a specific company entry from the 'company' (SQL table), by calling on the method 'getCompanyById' (via the CompanyRepository).  

-   Get a specific company entry from the 'company' (SQL table), by calling on the method 'getCompanyById' (via the CompanyRepository). 

-   Calls on the above functions 'get_interviews()' & 'get_job_offers()' to get all the interviews & job offers perspectively, which are linked to the job application in question. 

-   Stores all the URLs/links to be presented to the user in a dictionary. 

-   The values for the application, company, interviews, job offers & URL's (to be presented to the user) are all stored in their own dictionaries.  

-   Cleans all the values in each of the above dictionaries, to improve the presentation of the data before its presented to the user. These functions include: 
    -   cleanup_specific_job_application()
        ->   Found in: services/cleanup_files/cleanup_app_fields.py. 
    -   cleanup_specific_company()
        ->   Found in: services/cleanup_files/cleanup_company_fields.py. 
    -   cleanup_company_website()
        ->   Found in: services/cleanup_files/cleanup_company_fields.py. 
    -   cleanup_urls()
        ->   Found in: services/cleanup_files/cleanup_app_fields.py. 

    -   Finally all dictionaries are stored as keys in a parent dictionary 'general_details'. 

Renders the template:
    -   "view_application.html"
    -   With the dictionary 'general_details'

#### view_all_applications.py
This includes the functionality behind:
-   Displaying all job applications to the user.

Function included:

##### display_applications_for_user()
This function handles the GET functionality for the route: '/applications'. 

Takes: 
    user_id, applicationsRepo, companyRepo

Functionality (algorithm):
-   Gets the last 10 job applications added by the user, by calling on the method 'getTop10Applications' (in the ApplicationsHistoryRepository). Each application entry (returned by the SQL query) is instantiated using the class 'Application' & added to a list of 10 'Application' objects.

-   Iterates over each entry (returned by the above function), storing the values for each 'Application' in a dictionary with its unique ID (application_id) as its key name. 

-   Calls on the function 'cleanup_application_fields()' (found in services/cleanup_files/cleanup_app_fields.py), to improve how the application values will be displayed to the user.

-   Stores all the links / URLs which will be displayed to the template. 

Renders the template: 
    -   'applications.html'
    -   With the dictionary created by this function. 

#### update_application.py
This includes the functionality behind:
    -   Displaying a form (AddApplicationForm) to the user, giving the user the option to add a job application which links to a specific user.
        -   Function: display_update_application_form()
    -   Using the values provided (by the user) to update an entry in the 'job_Applications' table in the SQL database.
    -   Redirecting the user to view the details for the 'job application' which has just been updated. 
        -   Function: post_update_application()

Function included:

##### display_update_application_form()
This function handles the GET functionality for the route: '/applications/<int:application_id>/update_application'. 

Takes: 
-   add_application_form ('AddApplicationForm' instantiated with the values for a specific job application entry)
-   user_id, application_id, update_form, company

Functionality (algorithm):
-   Puts together a dictionary with the company name & the URL's to be presented to the user.

Renders the template "update_application.html", with the dictionary created by this function. 

##### post_update_application()
This function handles the POST functionality for the route: '/applications/<int:application_id>/update_application'. 

Takes: 
-   add_application_form ('AddApplicationForm' as completed by the user)
-   user_id, application_id, update_form,company_id, applicationsRepo, companyRepo

Functionality (algorithm):
-   Extracts the values from the add_application_form and stores it all in a dictionary 'application_fields'. 

-   Calls on the repo method 'updateApplicationByID', (in the ApplicationsHistoryRepository) with the 'application_fields' dictionary for the job application, to update the entry in the 'job_applications' (SQL) table, using the entry's unique ID (application_id).

-   Extracts the values from the add_application_form which relate directly to a company and stores these values in a second dictionary 'company_details'. 

-   Calls on the repo method 'updateCompanyByApplication', (in the CompanyRepository) with the 'company_details' dictionary, to update the entry in the 'company' (SQL) table, using the entry's unique ID (company_id).   

Finally:
    The user is redirected to the route '/applications/<int:application_id>'. 

#### delete_an_application.py
This includes the functionality behind:
    -   Deleting an entry from the 'job_applications' table (in the SQL database). 

Function included:

#####  delete_application()
This function handles the GET functionality for the route: '/applications/<int:application_id>/delete'. 

Takes: 
-   application_id, applicationsRepo, interviewsRepo, interviewPrepRepo, appNotesRepo, jobOffersRepo

Functionality (algorithm):
-   Deletes a job application entry linked to its unique ID (application_id).

-   Deletes all interviews, interview prep, application notes & job offer entries linked to a specific application's unique ID (application_id).

-    To complete the above functionality, the following methods are called:
    -   deleteApplicationByID(), found in the ApplicationsHistoryRepository.
    -   deleteInterviewsByApplicationID(), found in the InterviewsHistoryRepository.
    -   deleteInterviewPrepByApplicationID(), found in the InterviewPreparationRepository.
    -   deleteNoteByApplicationID(), found in the ApplicationNotesRepository. 
    -   deleteJobOfferByApplicationID(), found in the JobOffersRepository.

Finally:
    The user is redirected to the route:
'/applications'. 

#### delete_all_applications.py
This includes the functionality behind deleting all application entries from the 'job_applications' table (in the SQL database), which are linked to the current user's unique ID (user_id). 

Function included:

##### delete_all_applications_for_user()
This function handles the GET functionality for the route: '/applications/delete_all_applications'. 

Takes: 
-   user_id, applicationsRepo, appNotesRepo, interviewPrepRepo, interviewsRepo, jobOffersRepo

Functionality (algorithm):
-   Deletes all job application, interview, interview prep, application note & job offer entries linked to the current user's unique ID (user_id).

-    To complete the above functionality, the following methods are called:
    -   deleteApplicationsByUserID(), found in the ApplicationsHistoryRepository.
    -   deleteInterviewsByUserID(), found in the InterviewsHistoryRepository.
    -   deleteInterviewPrepByUserID(), found in the InterviewPreparationRepository.
    -   deleteNoteByUserID(), found in the ApplicationNotesRepository. 
    -   deleteJobOfferByUserID(), found in the JobOffersRepository.

Finally:
    The user is redirected to the route:
'/dashboard'. 










