# Technical Readme
## Services:

This file will cover all the files & functions, found in the services directory, in more (technical) detail, all of which the functionality to build the 'back-end' of the application. All the functions found  in this directory are written in Python, with the main library used being Flask.

I've broken these functions up into 11 directories, each of which covers a specific area of functionality for the application:
-   Address book
-   Application Notes
-   Applications
-   Cleaning the values for presentation
-   Company
-   Company Notes
-   Contacts
-   Interview Preparation
-   Interviews
-   Job Offers
-   Users

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
This includes the functionality behind displaying the user's contacts (both company & individual) to the template: 'view_address_book.html'. 

This file relates to the respositories 'ContactRepository' & 'CompanyRepository', & draws its 'contact' entries from the SQL tables 'indiv_contacts' & 'company'. However, where necessary, it does also connect to the other repositories & SQL tables where necessary. 

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
This where you'll find all the Python functions related to Application Notes.  This file relates specifically to the 'ApplicationNotesRepository' & draws its 'application note' entries from the SQL table 'application_notes'. However, where necessary, it does also connect to the other repositories & SQL tables where necessary. 

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

Redirects the user:
-   To the template: 'view_app_note_details.html'
-   Via the route: '/applications/<int:application_id>/app_notes/<int:app_notes_id>/view_note'

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

Redirects the user:
-   To the template: 'view_notes_for_application.html'
-   Via the route: '/applications/<int:application_id>/view_application_notes'

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

Redirects the user:
-   To the template: 'view_app_note_details.html'
-   Via the route: '/applications/<int:application_id>/app_notes/<int:app_notes_id>/view_note'

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
This where you'll find all the Python functions related to Job Applications. This file relates specifically to the 'ApplicationsHistoryRepository' & draws its 'job application' entries from the SQL table 'job_applications'. However, where necessary, it does also connect to the other repositories & SQL tables where necessary. 

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

Redirects the user:
-   To the template: 'view_application.html'
-   Via the route: '/applications/<int:application_id>'.

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
    -   cleanup_urls()
        ->   Found in: services/cleanup_files/cleanup_general_fields.py. 

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

Redirects the user:
-   To the template 'view_application.html'
-   Via the route: '/applications/<int:application_id>'. 

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

Redirects the user:
-   To the template: 'applications.html'
-   Via the route: '/applications'. 

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

Redirects the user:
-   To the template: 'dashboard.html'
-   Via the route: '/dashboard'. 

### cleanup_files:
The files found in this directory focus on formating the data it receives, to improves how values are presented to the user (on the templates). 

I found that I was creating functions (in the service directory) to solve a specific problem, but noticed certain functions were all carrying out the same functionality. This caused unnecesary duplication of functionality. 

So, to address this, I created this directory 'cleanup_files', into which I created the following Python files:
-   cleanup_app_fields.py
-   cleanup_company_fields.py
-   cleanup_contact_fields.py
-   cleanup_datetime_display.py
-   cleanup_general_fields.py
-   cleanup_interview_fields.py
-   cleanup_job_offer_fields.py

By storing these functions in 1 directory, there's a center point where all similar functionality can be found. These functions also allow me to maintain consistent string formating, for each value presented, across all the templates. 

#### cleanup_app_fields.py
This file includes functions which specifically focus on the fields related to the 'job_application' SQL table. 

Functions included:
-   cleanup_emp_type_field()
-   cleanup_interview_stage()
-   cleanup_specific_job_application()
-   cleanup_application_fields()

##### cleanup_emp_type_field()
This function specifically focuses on the field 'employment_type', found in the 'job_applications' SQl table. 

Takes (input):
    employment_type (as received from a SQL query)

Functionality (algorithm):
-   Uses a 'if' statement to run through all potential values for the 'employment_type' field, formating how the value will be presented to the user in each case. The string is format to read like everyday language. 

EG: If 'emp_type' is 'full_time', 
    -   it updates the value to "Full Time". 

Returns: 
    The updated value (for the 'employment_type' field). 

An instance where this method is called:
    cleanup_application_fields(), in services/cleanup_files/cleanup_app_fields.py

##### cleanup_interview_stage()
This function specifically focuses on the field 'interview_stage', found in the 'job_applications' SQL table. 

Takes (input):
    interview_stage (as received from a SQL query), which is an integer-type value

Functionality (algorithm):
-   Creates an 'updated_interview_stage' variable, which will store the string to be displayed to the user. 

-   Uses 'if' conditional logic to checks the value for the 'interview_stage':
    -   If its 0, then the value for 'updated_interview_stage' will be updated to "No interview lined up yet."
    -   Otherwise, the value for the 'updated_interview_stage' will be updated to "Interview #{x}.", where x is the value stored for 'interview_stage'.  

EG: 
    If interview_stage is 0:
        updated_interview_stage = "No interview lined up yet."

    If Interview_stage is 1:
        updated_interview_stage = Interview #1."

Returns: 
    The 'updated_interview_stage' string. 

An instance where this method is called:
    cleanup_specific_job_application(), in services/cleanup_files/cleanup_app_fields.py

##### cleanup_specific_job_application()
This function specifically focuses on a specific entry from the 'job application' SQL table. 

Takes (input):
    application (a dictionary of fields related to a specific job application)

Functionality (algorithm):
-   Iterates through the dictionary keys & values, (stored in the 'application' dictionary). 
    -   Using conditional logic, it updates each value according to the key's ('heading') name, calling on another function to 'clean' it's value. 

This function doesn't return anything & it doesn't need to. This is due to the fact that dictionaries are an object, which passes values by reference (not by value). So any/ all updates made to the values in this dictionary, by this function, are made to the actual dictionary itself & go beyond the scope of this function. 

TLDR: Change the values in a dictionary here (in this function), and it changes the dictionary everywhere (where this dictionary is used).

An instance where this method is called:
    display_interview_preparation_form(), Line 31 in services/interview_preparation/add_interview_prep.py

##### cleanup_application_fields()
This function receives a dictionary with various job applications (from the 'job_applications' SQL table), & focuses on improving how the fields' values are presented to the user.  

Takes (input):
-   A dictionary of job applications
-   An unique ID (app_id) for a specific job application found in this dictionary

Functionality (algorithm):
-   Uses the application's unique ID (app_id), it can focus on a specific job application found within the dictionary.

-   Iterates through the keys & their perspective values,  for the job application. If any value is stored as "N/A", its value is replaced with "None" (a NoneType data type). If any field is saved as "None", it will not be displaying to the user.  

-   Calls on the function 'cleanup_interview_stage()' for update how the application's 'interview stage' field value will be displayed to the user. 

-   Calls on the function 'cleanup_emp_type_field()' for update how the application's 'employment_type' field value will be displayed to the user. 

-   Converts the 'app_date' value, for the job application's entry date, to a datetime object. It then calls on the 'cleanup_date_format()' to update how the date will be displayed to the user.  

This function doesn't return anything & it doesn't need to. This is due to the fact that dictionaries are an object, which passes values by reference (not by value). So any/ all updates made to the values in this dictionary, by this function, are made to the actual dictionary itself & go beyond the scope of this function. 

TLDR: Change the values in a dictionary here (in this function), and it changes the dictionary everywhere (where this dictionary is used). 

An instance where this method is called:
    display_applications_for_user(), Line 38 in services/applications/view_all_applications.py

#### cleanup_company_fields.py
This file includes functions which specifically focus on the fields related to the 'company' SQL table.

Function included:
-   check_if_all_company_fields_empty()
-   cleanup_company_profile()
-   cleanup_specific_company()
-   cleanup_company_fields()

##### check_if_all_company_fields_empty()
This function checks all the values stored in a 'company'-related dictionary, for any value that isn't stored as 'None'. If this function returns False, then the dictionary is not blank / empty. 

This is used by the 'cleanup_company_profile()' to check if the user has not yet provided any details for the company. If this is the case, the user gets a message, prompting them to update the company profile if they want to see more details for this company.

Takes (input):
    company_details (a dictionary containing fields for a specific company entry)

Functionality (algorithm):
-   Iterates through all the keys & values in the dictionary. Using conditional logic, it checks each value, whilst ignoring the 'key' named 'company_name'. If it finds a value that's not 'None', it instantly returns 'False. Otherwise it returns 'True' once it has completed iterating through all the values in the dictionary. 

Returns:
    True or False

An instance where this method is called:
    cleanup_company_profile() (below)

##### cleanup_company_profile()
This function is used specifically to clean the values of a 'company' dictionary, focusing specifically on a particular company's 'company profile'. 

Takes (input):
    company_details (a dictionary containing fields for a specific company entry)

Functionality (algorithm):
-   Calls the function 'check_if_all_company_fields_empty()' to check if all the fields in the dictionary are 'empty' (storing blank values). The "all_fields_empty" key in this dictionary is updated with the output from the 'check_if_all_company_fields_empty() function.  

-   Iterates through all the keys & values in the dictionary, ignoring the key names 'company_name' & 'all_fields_empty'. 
    -   Using conditional logic, it checks if the value is empty (stored as "N/A", "Unknown at present" or ""). 
        -   If value is empty, 
                The value is replaced with 'None' (NoneType data type).
        -   Otherwise: 
                The function calls on the 'cleanup_field_value()' function & uses the returned value to update the dictionary value.  

This function doesn't return anything & it doesn't need to. This is due to the fact that dictionaries are an object, which passes values by reference (not by value). So any/ all updates made to the values in this dictionary, by this function, are made to the actual dictionary itself & go beyond the scope of this function. 

TLDR: Change the values in a dictionary here (in this function), and it changes the dictionary everywhere (where this dictionary is used).

An instance where this method is called:
    display_company_profile(), Line 33 in services/company/view_company_profile.py


##### cleanup_specific_company()
This function is used specifically to clean the values of a 'company' dictionary & is called on by various functions across the 'services' directory, with the except of 'services/company/view_company_profile.py'.

Takes (input):
    company_details (a dictionary containing fields for a specific company entry)

Functionality (algorithm):
-   Iterates through all the keys & values in the 'company' dictionary. 
    -   Where it finds a value is "N/A", "Unknown at present" or "" (blank field):
        -   It replaces this value with 'None' ('NoneType' data type.)
    -   Otherwise, it 'cleans' the value by calling on the function 'cleanup_field_value' (found in 'services/cleanup_files/cleanup_general_fields.py'), with the value as its argument. The value (in the dictionary) is then updated, using the output returned by this 'cleanup_field_value()' function. 

This function doesn't return anything & it doesn't need to. This is due to the fact that dictionaries are an object, which passes values by reference (not by value). So any/ all updates made to the values in this dictionary, by this function, are made to the actual dictionary itself & go beyond the scope of this function. 

TLDR: Change the values in a dictionary here (in this function), and it changes the dictionary everywhere (where this dictionary is used).

An instance where this method is called:
    display_interview_preparation_form(), Line 24 in services/interview_preparation/add_interview_prep.py

##### cleanup_company_fields()
This function receives a dictionary with multiple companies (from the 'company' SQL table), & focuses on improving how the fields' values are presented to the user.  

Takes (input):
-   A dictionary of 'company' entries' details
-   An unique ID (company_id) for a specific company entry found in this dictionary

Functionality (algorithm):
-   It first checks the value stored in the dictionary's key: 'empty_list'. If its False, then it proceeds with the next steps (below):

-   It iterates through the keys & values in the 'fields' dictionary (stored within the 'company' dictionary). 
    -   If any value is stored as "N/A":
        -   The value is replaced with 'None' ('NoneType' Data type). This allows me to only present 'company' fields to the user if the user didn't leave these fields blank when creating this company's profile. 
    
    -   If it comes across the key 'view_company', then it moves along to the next key in the dictionary. It needs not change the value for this key.

    -   Otherwise (for all remaining values)
        -   It calls the function 'cleanup_field_value()' with the value & updates the value with the output from this function (cleanup_field_value()). This function focuses on formating the string (value) to improve how its displayed to the user. 

This function doesn't return anything & it doesn't need to. This is due to the fact that dictionaries are an object, which passes values by reference (not by value). So any/ all updates made to the values in this dictionary, by this function, are made to the actual dictionary itself & go beyond the scope of this function. 

TLDR: Change the values in a dictionary here (in this function), and it changes the dictionary everywhere (where this dictionary is used).

An instance where this method is called:
    display_address_book(), Line 26 in services/address_book/view_address_book.py

#### cleanup_contact_fields.py
This file includes functions which specifically focus on the fields related to the 'indiv_contacts' SQL table.

Function included:
-   cleanup_full_name()
-   cleanup_specific_contact_entry()
-   cleanup_each_contact_entry()

##### cleanup_full_name()
Takes (input):
    A string 'full_name', which represents the contact's Full Name.

Functionality (algorithm):
-  Uses the function 'join()' to break the string up into a string of 'words', capitalise the first letter of the word & then put the string back together separated by spaces. 

Returns:
    The updated version of the string, with the first letter of every word (in the string) capitalised. 
Eg: peter parker -> Peter Parker

An instance where this method is called:
    cleanup_specific_contact_entry(), Line 11 which is also found in the same file (cleanup_contact_fields.py). 

##### cleanup_specific_contact_entry()
This function is used specifically to clean the values of a 'indiv_contacts' dictionary & is called on by various functions across the 'services' directory.

Takes (input):
-   contact_details (a dictionary containing fields for a specific contact entry)

Functionality (algorithm):
-   Iterates through all the keys & values in the 'contact_details' dictionary. 
    -   Where it finds a value is "N/A" (blank field):
        -   It replaces this value with 'None' ('NoneType' data type.)

-   It calls on the function 'cleanup_field_value()' to update the value, stored in the dictionary, for the keys 'company_name' & 'job_title'. 

-   It calls on the function 'cleanup_full_name()' to update the value, stored in the dictionary, for the key 'full_name'. 

Since this function makes changes directly to the values stored in the dictionary itself, there is no need to return the dictionary (or its changes). 

This is due to the fact that dictionaries pass their values by reference. This means that all changes made to this dictionary are permanent / automatic changes to the dictionary itself & affects all occurrences of this dictionary (across all functions in the service directory).

An instance where this method is called:
    display_contact_details(), Line 32 in services/contacts_directory/view_contact_details.py. 

##### cleanup_each_contact_entry()
This function receives a dictionary with multiple contacts (from the 'company' SQL table), & focuses on improving how the fields' values are presented to the user.  

Takes (input):
-   contact_details (a dictionary containing fields for multiple contact entries)
-   a unique ID (contact_id) for a specific contact entry

Functionality (algorithm):
-   Iterates through all the keys & values in the 'contact_details' dictionary for a specific contact entry, using its unique ID (contact_id). 
    -   Where it finds a value is "N/A" (blank field):
        -   It replaces this value with 'None' ('NoneType' data type.)

-   It calls on the function 'cleanup_field_value()' to update the value, stored in the dictionary, for the keys 'company_name' & 'job_title'. 

-   It calls on the function 'cleanup_full_name()' to update the value, stored in the dictionary, for the key 'full_name'. 

Since this function makes changes directly to the values stored in the dictionary itself, there is no need to return the dictionary (or its changes). 

This is due to the fact that dictionaries pass their values by reference. This means that all changes made to this dictionary are permanent / automatic changes to the dictionary itself & affects all occurrences of this dictionary (across all functions in the service directory).

An instance where this method is called:
    display_contacts_for_user(), Line 28 in services/contacts_directory/view_contact_list.py. 

#### cleanup_datetime_display.py
This file includes functions which specifically focus on the fields related  to a 'Date' & 'Time'. 

Functions included:
-   cleanup_date_format()
-   cleanup_time_format()
-   verify_value_is_date_obj()
-   verify_value_is_time_obj()
-   past_dated()
-   present_dated()

##### cleanup_date_format()
This function takes a date object & creates a string to represent that date in simple, everyday language to the user. 

Takes (input):
    A 'date' object.

Functionality (algorithm):
-   It breaks the date up into its 'year', 'month' & 'day' components. 

-   It replaces the 'month' with a string shortcut for that month (from a list of 'months' shortcuts).
Eg: if the month is 3 
    -   the 'month' becomes 'Mar'. 

-   It converts the 'date' & 'year' values to string, and then builds a string with the new string values for 'date', 'month' & 'year'. 
Eg: If the date is Y: 2021 M: 5 D: 18:
    -   The string will be '18 May 2021'. 

Returns:
    The newly created date string. 

An instance where this method is called:
    display_all_user_notes(), Line 88 in services/display_all_notes.py. 

##### cleanup_time_format()
This function takes a 'time' object & creates a string to represent that date in simple, everyday language to the user. 

Takes (input):
    A 'time' object.

Functionality (algorithm):
-   It converts the 'time' object to a string. 

-   It grabs the 'hour' value from the 'time' object & determines whether the hour is before or after 12pm. 
    -   If before 12pm
            It adds 'am' to the string. 
    -   Else:
            It adds 'pm' to the string. 

EG: 
If the 'Hour' is 11 & the 'minute' is 30:
    -   Then the string will be '11:30am'
If the 'Hour' is 15 & the 'minute' is 30:
    -   Then the string will be '3:30pm'

Returns:
    The newly-created time string. 

An instance where this method is called:
    cleanup_specific_job_application(), Line 44 in services/cleanup_files/cleanup_app_fields.py.

##### verify_value_is_date_obj()
This function serves to ensure that the value it receives is returned as a 'date' object. 

Takes (input):
    A 'date' value. 

Functionality (algorithm):
-   It checks the data type for the value it receives, to see if its a string. 
    -   If yes:
            It converts the string to a 'date' object & returns this updated 'date' object. 
    -   Else:
            If it gets here then it should already be a 'date' object. So it gets returned without any changes. 

Returns:
    A 'Date' object

An instance where this method is called:
    past_dated(), Line 50 which is also found in services/cleanup_files/cleanup_app_fields.py.
    
##### verify_value_is_time_obj()
This function serves to ensure that the value it receives is returned as a 'time' object. 

Takes (input):
    A 'time' value. 

Functionality (algorithm):
-   It checks the data type for the value it receives, to see if its a string. 
    -   If yes:
            It converts the string to a 'time' object & returns this updated 'time' object. 
    -   Else:
            If it gets here then it should already be a 'time' object. So it gets returned without any changes. 

Returns:
    A 'time' object

An instance where this method is called:
    past_dated(), Line 51 which is also found in services/cleanup_files/cleanup_app_fields.py.

##### past_dated()
This function receives a 'date' & 'time' value for an event & determines whether / not the event is dated in the past.

Takes (input):
    -   A 'date' value. 
    -   A 'time' value. 

Functionality (algorithm):
-   It creates a boolean variable 'date_is_past_dated', with the default value of 'False'. 

-   It calls on functions 'verify_value_is_date_obj()' & 'verify_value_is_time_obj()' to ensure that the 'date' & 'time' values it receives are in fact 'date' & 'time' objects. 

-   It gets the current day's date & time.

-   It then compares the date and time objects it receives (as input) to the current date & time. 
    -   If the input 'date and time objects' are dated in the past:
            It updates the value for 'date_is_past_dated' to be True. 

Returns:
    The value stored in 'date_is_past_dated' (our boolean variable).

An instance where this method is called:
    display_upcoming_interviews(), Line 99 which is also found in services/display_dashboard_content.py.

##### present_dated()
This function receives a 'date' value for an event & determines whether / not the event is dated 'today'.

Takes (input):
    -   A 'date' value. 

Functionality (algorithm):
-   It creates a boolean variable 'date_is_today', with the default value of 'False'. 
-   It gets the current day's date.
-   It then compares the date object (it receives as input) to the current date.
    -   If these 2 date values match up:
            -   It updates the value for 'date_is_today' to be True. 

Returns:
    The value stored in 'date_is_today' (our boolean variable).

An instance where this method is called:
    get_users_stats(), Line 63 which is also found in services/display_dashboard_content.py.

#### cleanup_general_fields.py
This file includes functions which are general in natural & therefore can be used by any function in the Service directory. 

##### cleanup_urls()
This function specifically focuses on fields related to URL's and can be accessed by any function found in the Service directory.

Takes (input):
    url (as received from a SQL query)

Functionality (algorithm):
-   Uses 'if' conditional logic to checks the value stored for the field 'url':
    -   If it's "N/A" or "n/a", then its a blank field:
        -   Its value is replaced with "None",  (a 'NoneType' datatype). 
    -   If its "http://" or "https://", then the field was incomplete:
        -   So its value is replaced with "None" (a 'NoneType' datatype).
        -   This is especially important since 'update....' forms will display "https://" in 'URL-related fields. If the user submitted the form, without updating this field value, it will be stored in the SQL database as "https://". 

EG: 
    If 'url' is "N/A", "n/a", "http://" or "https://":
    -   Then its value is replaced with "None" (a NoneType value). 

Return:
    The updated value for 'job_url'. This value can now  get displayed to the user only when its value is not 'None'. 

An instance where this method is called:
    display_application_details(), Line 141 which is also found in services/applications/view_application_details.py.

#### cleanup_interview_fields.py
This file includes functions which specifically focus on the fields related to the 'interviews' SQL table.

Functions include:
-   cleanup_interview_type()
-   cleanup_interview_status()
-   cleanup_medium()
-   cleanup_interview_fields()
-   cleanup_specific_interview()

##### cleanup_interview_type()
This function takes a 'interview_type' field value & improves how the value will be presented to the user. 

Takes (input):
-   interview_type (a string value)

Functionality (algorithm):
-   It uses conditional logic to run through all the interview types, as stored in the 'interviews' SQL table, & returns a string (to represent that value to the user).

EG:  If interview_type is "video_or_online":
    The function returns the string "Video / Online"

Returns:
    A string to represent the interview type for an interview, based on the input the function received.

An instance where this method is called:
    cleanup_specific_interview(), Line 89 which is also found in services/cleanup_files/cleanup_interview_fields.py.

##### cleanup_interview_status()
This function takes a 'interview_status' / 'status' field value & improves how the value will be presented to the user. 

Takes (input):
-   status (a string value)

Functionality (algorithm):
-   It uses conditional logic to run through all the possible options offered for an interview's 'status', as stored in the 'interviews' SQL table, & returns a string (to represent that value to the user).

EG:  If interview_type is "upcoming":
    The function returns the string 'Upcoming Interview'

Returns:
    A string to represent an interview's current status, based on the input the function received.

An instance where this method is called:
    display_update_interview_prep_form(), Line 38 in services/interview_preparation/update_interview_prep.py.

##### cleanup_medium()
This function takes a 'interview_medium' / 'medium' field value & improves how the value will be presented to the user. 

Takes (input):
-   medium (a string value)
-   other_medium (a string value)

Functionality (algorithm):
-   It checks to see if the value of 'other_medium' is "N/A":
    -   IF yes, it replaces it's value with "Not provided" (since the user hasn't provided a value for this field yet).

-   It creates an empty string variable 'updated_medium'. 

-   It uses conditional logic to run through all the possible options offered for an interview's 'medium', as they're stored in the 'interviews' SQL table. It then updates the variable 'updated_medium' with the appropriate string representation of this value. 
    -   If the value for 'medium' is 'other':
        -   then the variable 'updated_medium' will be updated with the value stored in 'other_medium'. 

EG:  
If other_medium is "N/A" & 'medium' is 'other':
    The function returns the string 'Not provided'

If medium is "ms_teams":
    The function returns the string "Microsoft Teams"

Returns:
    The value stored in the variable 'updated_medium'.

An instance where this method is called:
    cleanup_specific_interview(), Line 87 which is also found in services/cleanup_files/cleanup_interview_fields.py.

##### cleanup_interview_fields()
This function receives a dictionary with multiple interviews (from the 'interviews' SQL table), & focuses on improving how the fields' values are presented to the user. 

Takes (input):
-   interview_details (a dictionary containing fields for multiple interview entries)
-   a unique ID (interview_id) for a specific interview entry
-   'other_medium' (a string value)

Functionality (algorithm):
-   Uses an interview's unique ID (interview_id), it can focus on a specific job interview found within the dictionary.

-   Iterates through all the keys & values in the 'interview_details' dictionary for a specific interview entry, using its unique ID (interview_id). 
    -   If the value is "N/A" (blank field):
        -   It replaces this value with 'None' ('NoneType' data type). If any field is saved as "None", it will not be displaying to the user.  

    -   If the key is 'status':
        -   It calls the function 'cleanup_interview_status()' with the value & uses the value returned (from cleanup_interview_status()) to update the interview's 'status' (in the dictionary).

    -   If the key is 'medium' or 'interview_medium:
        -   It calls the function 'cleanup_medium()' with both the value & 'other_medium (provided as input to the function cleanup_interview_fields()). It then uses the value returned (from cleanup_interview_fields()) to update the interview's 'medium' (in the dictionary).

    -   If the key is 'interview_type':
        -   It calls the function 'cleanup_interview_type()' with the value & uses the value returned (from cleanup_interview_type()) to update the interview's 'interview_type' (in the dictionary).

    -   If the key is 'time':
        -   It calls the function 'cleanup_time_format()' with the value & uses the value returned (from cleanup_time_format()) to update the interview's 'time' (in the dictionary).

    -   If the key is 'date':
        -   It calls the function 'cleanup_date_format()' with the value & uses the value returned (from cleanup_date_format()) to update the interview's 'date' (in the dictionary).

    -   If the key is 'contact_number' or 'video_link':
        -   If the value is empty:
            -   It replaces the value (for this key) with "Not Provided"
        -   Otherwise: It makes no changes & just moves along to the next key:value pair in the dictionary.

    -   If the key is 'number', 'past_dated' or 'view_more':
        -   It makes no changes & moves along to the next key:value pair in the dictionary. 

    -   If none of the above criteria is met:
        -   It calls the function 'cleanup_field_value()' with the value & updates the value (for this key) with the output returned from cleanup_field_value().

Since this function makes changes directly to the values stored in the dictionary itself, there is no need to return the dictionary (or its changes). 

This is due to the fact that dictionaries pass their values by reference. This means that all changes made to this dictionary are permanent / automatic changes to the dictionary itself & affects all occurrences of this dictionary (across all functions in the service directory).

An instance where this method is called:
    display_upcoming_interviews(), Line 118 in services/display_dashboard_content.py. 

##### cleanup_specific_interview()
This function is used specifically to clean the values of a 'interview' dictionary & is called on by various functions across the 'services' directory.

Takes (input):
-   interview_details (a dictionary containing fields for a specific interview entry)
-   'other_medium' (a string value)

Functionality (algorithm):
-   Carries out the exact same conditional logic as the function above 'cleanup_interview_fields()', except it receives a dictionary with the fields for a single interview.

Since this function makes changes directly to the values stored in the dictionary itself, there is no need to return the dictionary (or its changes). 

This is due to the fact that dictionaries pass their values by reference. This means that all changes made to this dictionary are permanent / automatic changes to the dictionary itself & affects all occurrences of this dictionary (across all functions in the service directory).

An instance where this method is called:
    display_interview_preparation_form(), Line 35 in services/interview_preparation/add_interview_prep.py. 

#### cleanup_job_offer_fields.py
This file includes functions which specifically focus on the fields related to the 'job_offers' SQL table.

Functions include:
-   cleanup_offer_response()
-   cleanup_specific_job_offer()
-   cleanup_job_offer()

##### cleanup_offer_response()
This function takes a job 'offer response' field value & improves how the value will be presented to the user. 

Takes (input):
-   offer_response (a string value)
-   company_name (a string value)

Functionality (algorithm):
-   It creates an empty string variable 'updated_offer_response'. 

-   It uses conditional logic to run through all the possible options offered for an interview's 'offer_response', as they're stored in the 'job_offers' SQL table. It then updates the variable 'updated_offer_response' with the appropriate string representation of this value, with the 'company name' included into this string. 

EG:  

If offer_response is "company_pulled_offer" & the company's name is "Barclays Bank":
    The function returns the string "Barclays Bank pulled the offer."

If offer_response is 'user_accepted':
    The function returns the string "Offer Accepted!"

Returns:
    The value stored in the variable 'updated_offer_response'.

An instance where this method is called:
    cleanup_specific_job_offer(), Line 28 which is also found in services/cleanup_files/cleanup_job_offer_fields.py.

##### cleanup_specific_job_offer()
This function is used specifically to clean the values of a 'job offer' dictionary & is called on by various functions across the 'services' directory.

Takes (input):
-   job_offer_details (a dictionary containing fields for a specific job offer entry)

Functionality (algorithm):
-   It gets the value, stored for the key 'company_name' within the dictionary, & stores it in a local variable.

-   Iterates through all the keys & values in the 'job_offer_details' dictionary. 
   
    -   If the key is 'starting_date':
        -   It calls the function 'cleanup_date_format()' with the value & uses the value returned (from cleanup_date_format()) to update the interview's 'starting_date' (in the dictionary).

    -   If the key is 'offer_response':
        -   It calls the function 'cleanup_offer_response()' with both the value & the variable 'company_name'. It then uses the value returned (from cleanup_offer_response()) to update the interview's 'offer_response' (in the dictionary).

    -   If the key is 'company_name' or 'job_offer':
        -   It calls the function 'cleanup_field_value()' with the value & uses the value returned (from cleanup_field_value()) to update that key's value' in the dictionary).

    -   If none of the above criteria is met:
        -   It makes no changes & moves onto the next key:value pair in the dictionary. 

Since this function makes changes directly to the values stored in the dictionary itself, there is no need to return the dictionary (or its changes). 

This is due to the fact that dictionaries pass their values by reference. This means that all changes made to this dictionary are permanent / automatic changes to the dictionary itself & affects all occurrences of this dictionary (across all functions in the service directory).

An instance where this method is called:
    display_job_offer(), Line 21 in services/job_offers/view_job_offer.py.

##### cleanup_job_offer()
This function receives a dictionary with multiple job offers (from the 'job_offers' SQL table), & focuses on improving how the fields' values are presented to the user. 

Takes (input):
-   job_offers_details (a dictionary containing fields for multiple interview entries)
-   'count', which is a key which serves as the 'unique ID' for job offer in this dictionary.

Functionality (algorithm):
-   It carries out the same functionality (basically) as the above function 'cleanup_specific_job_offer()', with a few exceptions:

-   1) This dictionary has multiple 'job offer' entries & so this function 'cleanup_job_offer()' uses the key 'count' to focus on the keys & values for a specific job offer in the dictionary.

-   2) If the value for the key 'offer_response' is 'Offer Accepted!' (after getting cleaned by the 'cleanup_offer_response()' function):
    -   Then it updates the value, for the key 'offer_accepted', to True.

Since this function makes changes to the dictionary directly, like the above function 'cleanup_specific_job_offer()', it does not return anything. 

An instance where this method is called:
    display_job_offers(), Line 77 in services/display_dashboard_content.py.

### company
This where you'll find all the Python functions related to 'Company' contacts. This file relates specifically to the 'CompanyRepository' & draws its 'company' entries from the SQL table 'company'. However, where necessary, it does also connect to the other repositories & SQL tables where necessary. 

The files in this directory:
-   add_company_job_applications.py
-   add_company.py
-   update_company.py
-   delete_company.py
-   view_all_companies.py
-   view_company_profile.py

#### add_company_job_applications.py
Handles the functionality behind adding a job application for a specific company. This covers everything from presenting the form to processing the information that the user provides & storing that data as a single entry in the 'job_applications' SQL table. 

Functions included:
-   display_add_company_application_form()
-   add_new_application_to_application_history()
-   post_add_company_job_application()


##### display_add_company_application_form()
This function handles the GET functionality for the route: '/company/<int:company_id>/add_job_application'. 

Takes: 
-   add_application_form (a blank instance of the 'AddCompanyJobApplicationForm()' class), 
-   company_id, companyRepo

Functionality (algorithm):
-   It puts together a dictionary consisting of the company name for a specific company (to which this application entry will link to) & the URL to be actioned (the very same route used display a job application form to the user). 

Renders the template:
-   'add_company_job_application.html'
-   With the add_application_form & the dictionary created by this function. 

##### add_new_application_to_application_history()
This function is called, by the 'post_add_company_job_application()', to extract the values from the application form & to insert these values into the 'job_applications' SQL table. 

Takes (input):
-   application_form (as completed by the user)
-   user_id, company_id, applicationsRepo

Functionality (algorithm):
-   Gets the date & time, for the current day, & converts these 2 values into strings (using the method 'strftime()'). 

-   It extracts the field values from the application_form, as completed by the user, & saves these values in a dictionary 'fields'. Since this dictionary will be used to insert this application's details into the 'job_applications' SQL table, the values 'user_id' & 'company_id' are also added to the dictionary. 

-   Iterates through every key:value pair in this dictionary, & where it finds a blank value (""), it replaces the value with 'N/A'. This is because the majority of the columns in the 'job_applications' SQL table require input (of some sort). 

-   Calls on the method 'createApplication()' (from the ApplicationsHistoryRepository), with the dictionary as its argument. This method returns the unique ID (application_id) for this newly-created entry. 

Returns:
    The application_id for the job_application.

##### post_add_company_job_application()
This function handles the POST functionality for the route: '/company/<int:company_id>/add_job_application'. 

Takes (input):
-   add_job_app_form (as completed by the user)
-   user_id, company_id, applicationsRepo

Functionality (algorithm):
-   Calls on the function 'add_new_application_to_application_history()' to insert the values for this job appliction into the 'job_applications' SQL table. 

Redirects the user:
-   To the template: 'view_application.html', 
-   Via the route: '/applications/<int:application_id>'.

#### add_company.py
Handles the functionality behind adding a company contact, and handles everything from presenting the form to processing the information that the user provides & storing that data as a single entry in the 'company' SQL table. 

Functions included:
-   display_add_company_form()
-   post_add_company()

##### display_add_company_form()
This function handles the GET functionality for the route: '/address_book/add_company'. 

Takes: 
-   add_company_form(), (a blank instance of the 'AddCompanyForm()' class)

Functionality (algorithm):
-   Creates a dictionary to store:
    - The 'action_url' responsible for displaying the add_company_form to the template. 

    -   A variable 'existing_company', which gets used by the 'post_add_company()', in the case that the user is redirected back to this form. This would happen if the user tries to add a company, which already exists in their company directory. 

Renders the template:
-   "add_company_form.html"
-   With the dictionary created by this function. 

##### post_add_company()
This function handles the POST functionality for the route: '/address_book/add_company'. 

Takes: 
-   add_company_form (as completed by the user)
-   user_id, companyRepo

Functionality (algorithm):
-   Extracts the value 'company name', from the form 'add_company_form' (provided by the user), & saves it in a variable. 

-   Calls on the method 'getCompanyByName()' (from the CompanyRepository), which checks if theres a 'company' by this name in the 'company' SQL table. 

-   If the above method returns a 'company' object, then this function redirects the user back to the template "add_company_form.html", with the message that there's already a company by this name in this user's company directory. The user will now see a link to update the company's profile, if they wish to do so. 

-   If the method produces no results (however), then this function puts together a dictionary with the values from the add_company_form & calls on the method 'createCompany()' to insert this company into the 'company' SQL table. 

Redirects the user:
-   To the template: 'view_company_profile.html'
-   Via the route '/company/<int:company_id>/view_company', so that the user can view the company profile for the new company they've just created.

#### update_company.py
Handles the functionality behind updating an existing company. This covers everything from displaying the form (to the user) to updating the values for this company in the 'company' SQL table.

Functions included:
-   display_update_company_profile_form()
-   post_update_company_profile()

##### display_update_company_profile_form()
This function handles the GET functionality for the route: '/company/<int:company_id>/update_company'. 

Takes (input):
-   update_form (An instance of the 'UpdateCompany' form, which is given the values for a specific company entry)
-   company_id, company (the 'Company' object)

Functionality (algorithm):
-   Puts together a dictionary with:
    -   The 'action_url' responsible for displaying the form to the user
    -   The Company's name. 

Renders the template:
    -   "update_company_profile.html"
    -   The update_form 
    -   The dictionary created by this function.

##### post_update_company_profile()
This function handles the POST functionality for the route: '/company/<int:company_id>/update_company'. 

Takes (input):
-   update_form (as completed by the user)
-   company_id, user_id, companyRepo

Functionality (algorithm):
-   Extracts the field values from the update_form & stores them in a dictionary 'company_details', together with the values for 'user_id' & 'company_id'. 

-   Calls on the method 'updateCompanyByID()' (in the CompanyRepository), to update an entry in the 'company' SQL table with the values provided by the user. 

Redirects the user:
-   To the template: 'view_company_profile.html'
-   via the route: '/company/<int:company_id>/view_company'



#### delete_company.py
Handles the functionality behind deleting a specific 'company'. 

Functions Include:
-   display_delete_company_form()
-   post_delete_company()

##### display_delete_company_form()
This function handles the GET functionality for the route: '/company/<int:company_id>/delete_company'.

Takes (input):
-   delete_company_form (a blank instance of the form class 'DeleteCompanyForm()')
-   company_id, companyRepo

Functionality (algorithm):
-   Puts together a dictionary with:
    -   The 'action_url' responsible for displaying the form to the user
    -   The Company's name. 

-   Puts together a list of choices to be presented to the user, via the form field 'confirm_choice'. 

-   The form field 'confirm_choice' is then updated with this new list of options. Now the user will be presented with a dropdown list with 2 choices to choose from. 

-   A default choice is selected for the 'confirm_choice' form field. The default option would take the user back to the company profile, with no changes made. This is so that the user doesn't speed through the form and choose something they may not actually want. They would have to consciously choose the option, which would actually delete the company profile if submitted.

Renders the template:
-   "delete_company_profile.html"
-   With the dictionary (created by this function) & the delete_company_form. 

##### post_delete_company()
This function handles the POST functionality for the route: '/company/<int:company_id>/delete_company'.

Takes (input):
-   delete_company_form (as submitted by the user)
-   company_id, 
-   companyRepo, applicationsRepo, interviewsRepo, interviewPrepRepo, companyNotesRepo, jobOffersRepo, appNotesRepo

Functionality (algorithm):
-   It stores the option that the user selected, in the field 'confirm_choice', in a variable 'customer_choice'. 

-   It checks the choice the user selected (which is now stored in our variable 'customer_choice') & what the function does going forward depends entirely on which choice the user selected. 

-   If the user selects the option 1 ('No....):
    -   No changes are made to this company & the user is redirected back to their Addressbook. 

-   Otherwise:
    -   The function carries out the following delete requests:
        -   'deleteCompanyByID()' to delete this company from the 'company' SQL table. 
        -   'deleteCompanyNotesByCompanyID()' to delete all the note entries, which link to this company. 
        -   'deleteJobOfferByCompanyID()' to delete any/all job offers which link to this company. 

    -   The function grabs all applications linked to this company & then for each company, it runs the following delete requests:
        -   'deleteInterviewsByApplicationID()' to delete all interviews linked to every job application (in the above list of applications). 
        -   'deleteInterviewPrepByApplicationID()' to delete all interview entries linked to every job application (in the above list of applications).  
        -   'deleteNoteByApplicationID()' to delete all note entries linked to every job application (in the above list of applications).  
    
    -   Finally it runs the method 'deleteApplicationByCompanyID()' to delete all the job applications linked to this company (being deleted by this function).

Redirects the user:
-   To the template: 'view_address_book.html'
-   via the route "/address_book"
-   With a flash message, confirming that the company (and all Applications, Notes, Interviews & Interview Prep, & job offers linked to this company) has been successfully deleted. 

#### view_all_companies.py
Handles the functionality behind displaying all the companies that the user has already added/created so far, with each company being a link to the 'view_company_profile.html' template for the selected company. 

Function included:
-   display_all_companies_for_user()

##### display_all_companies_for_user()
This function handles the GET functionality for the route: '/address_book/company_directory'.

Takes (input):
-   user_id, companyRepo

Functionality (algorithm):
-   Calls on the method 'getCompanyEntriesByUserID()' to get all the company entries for the current user, where each entry has been instantiated using the 'Company' class. By doing this, its so much easier to get the values, from the database, for each company entry. 

-   Creates a dictionary 'company_contacts' with 3 keys 'empty_list', 'fields' & 'message'. 

-   If there are any company entries, then the function iterates through every company in the list (received by the above method). Every entry is saved in the dictionary 'fields' (found within the bigger dictionary 'company_contacts'), with the company's unique ID (company_id) as it's dictionary key. 

-   Calls the function 'cleanup_company_fields()' on every entry in the company list (received from the SQL query), to improve how the company's values will be presented to the user. 

-   Creates a second dictionary 'general_details' to store:
    -   The 'action_url' (add_company_url, which is the route responsible for displaying this form to the user)
    -   The dictionary 'company_contacts', put together by this function. 

Renders the template:
-   "view_company_directory.html"
-   With the dictionary 'general_details'. 

#### view_company_profile.py
Handles the functionality behind displaying the details for a specific company, using its unique ID 'company_id'.

It also offers to links to: 
-   Add a job application
-   View the company website 
-   Add a note for this specific company
-   View all notes for this specific company 

Function included:
-   display_company_profile()

##### display_company_profile()
This function handles the GET functionality for the route: '/company/<int:company_id>/view_company'.

Takes (input):
-   company_id, companyRepo

Functionality (algorithm):
-   Calls on the method 'getCompanyById' (from the companyRepo) to get a specific entry from the 'company' SQL table. 

-   All information for the company is extracted from this sql query and stored in a dictionary: company_details. 
    
-   This information is then 'cleaned' using the 'cleanup_company_profile()' function found in the file: services/clean_files/cleanup_company_fields.py.

-   Its grabs & stores all the routes (required for the links to be presented to the user), together with the dictionary 'company_details', in a 'general_details' dictionary. 

-   Calls the function 'cleanup_urls()' (found in services/cleanup_files/cleanup_general_fields.py), with the company URL. This is to ensure that the link the user provided (when creating this company profile) is actually a valid link. 

Note: 
    If the link is in fact valid (its not blank or incomplete), then it will be displayed on the company profile as a button which directs the user to the company's website. 

Renders the template:
-   "view_company_profile.html" 
-   via the route ''
-   With the dictionary 'general_details', created by this function. 

### company_notes:
This where you'll find all the Python files related to a company note / list of company notes. This file relates specifically to the 'CompanyNotesRepository' & draws its 'company note' entries from the SQL table 'company_notes'. However, where necessary, it does also connect to the other repositories & SQL tables where necessary.  

Files in this directory:
-   add_company_note.py
-   view_specific_note.py
-   view_all_company_notes.py
-   update_company_note.py
-   delete_company_note.py

#### add_company_note.py
Handles the functionality behind displaying the 'AddCompanyNoteForm' form to the user & saving the information (the user has provided/entered into the form) into the 'company_notes' SQL table. 

Functions include:
-   display_add_company_note_form()
-   post_add_company_note()

##### display_add_company_note_form()
This function handles the GET functionality for the route: '/company/<int:company_id>/add_company_note'.

Takes (input):
-   company_note_form (a blank instance of the AddCompanyNoteForm())
-   company_id, companyRepo

Functionality (algorithm):
-   Calls on the method 'getCompanyById' (from the companyRepo) to get a specific entry from the 'company' SQL table. This will allow us to display the company's name on the template. 

-   Puts together a 'details' dictionary with:
    -   The company's name & unique ID (company_id)
    -   The action URL (the route responsible for displaying the form to the user)

Renders the template:
-   "add_company_note.html"
-   With the dictionary created by this function. 

##### post_add_company_note()
This function handles the POST functionality for the route: '/company/<int:company_id>/add_company_note'.

Takes (input):
-   company_note_form (as completed by the user)
-   company_id, user_id, companyNotesRepo

Functionality (algorithm):
-   Gets the current date & converts the date to string. This will represent the date that this note was created & entered into the database. 

-   Extracts the field values from the form & stores these values in a dictionary 'fields', together with the 'user_id' & 'company_id' for this entry. 

-   Calls on the method 'createNewCompanyNote()' (found in the CompanyNotesRepository), to insert this company note as entry in the 'company_notes' SQL table. The method returns the unique ID (company_note_id) for the newly-created entry. 

Redirects the user:
-   To the template 'view_specific_company_note.html' 
-   via the route:
    '/company/<int:company_id>/company_note/<int:company_note_id>/view_note_details'







#### view_specific_note.py
Handles the functionality behind displaying the details for a specific note, linked to a specific company, from the 'company_notes' SQL table (using its unique 'company_note_id'). 

Function included:
-   display_company_note_details()

##### display_company_note_details()
This function handles the GET functionality for the route: 
-   '/company/<int:company_id>/company_note/<int:company_note_id>/view_note_details'.

Takes (input):
-   company_id, company_note_id, companyRepo, companyNotesRepo

Functionality (algorithm):
-   Calls on the method 'getCompanyById' (from the companyRepo) to get a specific entry from the 'company' SQL table. This will allow us to display the company's name on the template. 

-   Calls on the method 'getCompanyNoteByID' (from the CompanyNotesRepository) to get a specific entry from the 'company_notes' SQL table. 

-   It puts together a dictionary 'general_details', which will act as a 'parent' dictionary & given the keys 'links' & 'note_details'. 

-   The 'links' key is then given a dictionary of route URL's, which will be utilized to displays button links to the user. 

-   The note's 'entry date' is extracted & converted to a string, so that its ready to be displayed to the user. 

-   The 'note_details' key is itself set up as a dictionary & is given the values to present a specific application note. This dictionary includes the company's name, the entry date, & the note's subject & note text (content). 

Renders the template:
-   "view_specific_company_note.html"
-   With the values stored in the parent dictionary 'general_details'. 

#### view_all_company_notes.py
Handles the functionality behind displaying all the notes, from the 'company_notes' SQL table (using its unique 'company_note_id'), which are linked to a specific company. 

Function included:
-   display_all_notes_for_a_company()

##### display_all_notes_for_a_company()
This function handles the GET functionality for the route: 
-   '/company/<int:company_id>/view_all_company_notes'.

Takes (input):
-   company_id, user_id, companyRepo, companyNotesRepo

Functionality (algorithm):
-   Calls on the method 'getCompanyById' (from the companyRepo) to get a specific entry from the 'company' SQL table. This will allow us to display the company's name on the template. 

-   Creates a dictionary 'general_details', which is used to store all the URL routes which will be used to display button links to the user. 

-   Calls the method 'getAllNotesByCompanyID()' (found in the Repo CompanyNotesRepository), to get all the notes from the 'company_notes' table which are linked to a specific company (for the current user).

-   If the above query 'notes_history' returns any note entries, then 2 additional keys are created in the dictionary 'general_details'. It also creates a second dictionary 'note_details'.

-   Iterates through every entry in the 'notes_history' (the list of notes returned from the method 'getAllNotesByCompanyID()'), storing each entry in the 'note_details' dictionary. The details for each note is stored in its own dictionary, with the note's unique ID (company_note_id) as the name of the dictionary. 

EG: If the 'notes_history' has 3 entries, then the 'note_details' dictionary will store 3 keys, with each key being a dictionary storing the details for a specific note.

In this case the 'note_details' dictionary would look like this:

note_details = {
    1: {}, 
    2: {},
    3: {},
}

Ofcourse each of these dictionaries are not empty; they'll be storing the details for a specific company note & the keys will be the very same fields / columns found in the 'company_notes' SQL table & in the 'Company' class. 

Renders the template:
-   "view_company_notes.html"
-   With the dictionaries: 'general_details' & 'note_details' (both created by this function)

#### update_company_note.py
Handles the functionality behind updating an existing note linked to a specific company. This covers everything from displaying the form (to the user) to updating the values for this company in the 'company_notes' SQL table.

Functions included:
-   display_update_company_note_form()
-   post_update_company_form()

##### display_update_company_note_form()
This function handles the GET functionality for the route: 
-   '/company/<int:company_id>/company_note/<int:company_note_id>/update_note'

Takes (input):
-   update_note_form (an instance of the 'AddCompanyNoteForm', with the values for a specific CompanyNotes object)
-   company_note_id, companyRepo, companyNotesRepo

Functionality (algorithm):
-   Calls on the method 'getCompanyById' (from the companyRepo) to get a specific entry from the 'company' SQL table. This will allow us to display the company's name on the template. 

-   Puts together a 'details' dictionary with:
    -   The company's name & unique ID (company_id)
    -   The action URL (the route responsible for displaying the form to the user)

Renders the template:
-   "update_company_note.html"
-   With the update_note_form & the 'details' dictionary

##### post_update_company_form()
This function handles the POST functionality for the route: 
-   '/company/<int:company_id>/company_note/<int:company_note_id>/update_note'

Takes (input):
-   update_note_form (as completed by the user)
-   company_id, company_note_id, companyNotesRepo

Functionality (algorithm):
-   Gets the current day's date & converts it to string. This update date is stored as the note's entry date. 

-   Extracts the field values from the update_note_form & stores these in a dictionary 'details', together with the entry date & note's unique ID (company_note_id). 

-   Calls on the method 'UpdateCompanyNoteByID()' (found in the Repo CompanyNotesRepository), with the dictionary created above. This updates an existing entry in the 'company_notes' SQL table.

Redirects to the template:
-   "view_specific_company_note.html"
-   Via the route: '/company/<int:company_id>/company_note/<int:company_note_id>/view_note_details'

#### delete_company_note.py
Handles the functionality behind deleting a note, from the 'company_notes' SQL table, which is linked to a specific 'company'.

Functions included:
-   delete_specific_company_note()

##### delete_specific_company_note()
This function handles the request to delete a company note from the 'company_notes' SQL table. 

Takes (input):
-   company_id, company_note_id, companyNotesRepo

Functionality (algorithm):
-   Calls on the method 'deleteCompanyNoteByID()' (found in the Repo CompanyNotesRepository), delete a specific entry from the 'company_notes' SQL table, using the note's unique ID (company_note_id).

Redirects the user:
-   To the template 'view_company_profile.html'
-   Via the route: '/company/<int:company_id>/view_company'



### contacts_directory:
This where you'll find all the Python files related to a contact / list of contacts. This file relates specifically to the 'ContactRepository' & draws its 'contact' entries from the SQL table 'indiv_contacts'. However, where necessary, it does also connect to the other repositories & SQL tables where necessary.  

Files in this directory:
-   add_new_contact.py
-   view_contact_details.py
-   view_contact_list.py
-   update_contact.py
-   delete_contact.py

#### add_new_contact.py
Handles the functionality behind displaying the 'AddNewContactForm()' (form) to the user & saving the information (the user has provided/entered into the form) into the 'indiv_contacts' SQL table. 

Functions included:
-   display_add_new_contact_form()
-   post_add_new_contact()

##### display_add_new_contact_form()
This function handles the GET functionality for the route: '/address_book/contact_list/add_contact'.

Takes (input):
    -   new_contact_form (a blank instance of the 'AddNewContactForm()' (form class))

Functionality (algorithm):
-   Puts together a 'details' dictionary with the action URL (the route responsible for displaying the form to the user). 

Renders the template:
-   "add_new_contact.html"
-   With the new_contact_form & the 'details' dictionary

##### post_add_new_contact()
This function handles the POST functionality for the route: '/address_book/contact_list/add_contact'.

Takes (input):
-   new_contact_form (as completed by the user)
-   user_id, contactRepo

Functionality (algorithm):
-   Extracts all the field values, from the 'new_contact_form', & saves these values in a 'details' dictionary, together with the 'user_id' for this user. 

-   Iterates through the values in the dictionary, & if any form value has not been completed by the user then it's value is replaced with 'N/A'.  

-   Calls on the method 'create_contact()' (from the ContactRepository), with the 'details' dictionary. This method then returns the unique ID (contact_id) for the newly-created contact entry. 

Redirects the user:
-   To the template 'view_contacts.html'
-   Via the route '/address_book/contact_list'

#### view_contact_details.py
Handles the functionality behind displaying the details for a specific 'contact', from the 'indiv_contacts' SQL table, to the template 'view_contact_details.html'.

Function included:
-   display_contact_details()

##### display_contact_details()
This function handles the GET functionality for the route: '/address_book/contact_list/<int:contact_id>/view_contact'.

Takes (input):
    contact_id, contactRepo

Functionality (algorithm):
-   Calls on the method 'getContactByID' (from the ContactRepository) to get a specific entry from the 'indiv_contacts' SQL table. 

-   Creates a 'contact_details' dictionary with a few base key:value pairs, which will be needed whether/not there are any details to display. 

-   If there is in fact a 'contact' to display, then it updates the key 'empty_contact' to be False & sets the key 'fields' as a dictionary. 

-   Extracts the relevant values from the 'contact' object & saves these field values in the 'fields' dictionary. This URL / routes to 'update_contact' & 'delete_contact' are also added to this dictionary. 

-   Calls on the function 'cleanup_specific_contact_entry()' (found in services/cleanup_files/cleanup_contact_fields.py), with this dictionary. This function will then improve how this contact's field values will be displayed to the user. 

Renders the template:
-   "view_contact_details.html"
-   With the 'contact_details' dictionary, created by this function.

#### view_contact_list.py
Handles the functionality behind displaying all the (individual) contact entries (added by the current user), from the 'indiv_contacts' SQL table, to the template 'view_contact_details.html'. 

Function included:
-   display_contacts_for_user()

##### display_contacts_for_user()
This function handles the GET functionality for the route: '/address_book/contact_list'.

Takes (input):
    user_id, contactRepo

Functionality (algorithm):
-   Calls on the method 'getContactsByUserID' (from the ContactRepository) to get all the contact entries, from the 'indiv_contacts' SQL table, for a specific user (using their unique ID 'user_id').

-   Creates a 'general_details' dictionary with a few base keys: 'empty_list' (set to True) & 'add_new_contact' (a route which will be used to display a link to the user). These key:value pairs will be useful, whether/not there are any contacts to display.

-   If there are any contact entries returned from the method 'getContactsByUserID()', then it iterates through each contact entry returned from the method. 

-   For each contact entry, the relevant field values are extracted & stored in its own dictionary, with the contact's unique ID (contact_id) set up as the dictionary's name. This helps to distinguish one contact entry from another. All entries are stored within the dictionary 'fields', which is a key in a parent dictionary 'contact_details'. 

EG: If there is 2 contact entries. 

contact_details["fields] = {
    1: {contact key:pairs go in here}, 
    2: {contact key:pairs go in here},
}

-   Calls on the function 'cleanup_each_contact_entry()' (found in services/cleanup_files/cleanup_contact_fields.py), for each contact entry, to improve how the contact's field values will be displayed to the user. 

Renders the template:
-   "view_contacts.html"
-   With the dictionaries: 'general_details' & 'contact_details'

#### update_contact.py
Handles the functionality behind displaying the 'AddNewContactForm()' (form), with the values for a specific contact entry, to the user. 

Once the form is submitted, the form values are extracted & used to update an existing entry in the 'indiv_contacts' SQL table (using the contact's unique ID (contact_id)).

Functions included:
-   display_update_contact_form()
-   post_update_contact()

##### display_update_contact_form()
This function handles the GET functionality for the route: '/address_book/contact_list/<int:contact_id>/update_contact'.

Takes (input):
-   update_contact_form (an instance of the 'AddNewContactForm()', with the values for a specific Contact object)
-   contact_id

Functionality (algorithm):
-   Puts together a 'details' dictionary with the action URL (the route responsible for displaying the form to the user). 

Renders the template:
-   "update_contact_form.html"
-   With the 'details' dictionary created by this function. 

##### post_update_contact()
This function handles the POST functionality for the route: '/address_book/contact_list/<int:contact_id>/update_contact'.

Takes (input):
-   update_contact_form (as completed / updated by the user)
-   contact_id, contactRepo

Functionality (algorithm):
-   Extracts the field values from the 'update_contact_form' & stores them in a dictionary 'details'. 

-   Iterates through the values in the dictionary, & if any form value has not been completed by the user then it's value is replaced with 'N/A'.  

-   Calls on the method 'updateContactByID()' (from the ContactRepository), with the 'details' dictionary. 

Redirects the user:
-   To the template 'view_contact_details.html'
-   Via the route '/address_book/contact_list/<int:contact_id>/view_contact'. 
-   With a message to confirm that the contact entry has been updated successfully. 

#### delete_contact.py
Handles the functionality behind deleting a specific contact entry from the 'indiv_contacts' SQL table. The user will then be redirected to the template 'view_address_book.html'. 

Function included:
-   delete_contact_details()

##### delete_contact_details()
Takes (input):
    contact_id, contactRepo

Functionality (algorithm):
-   Calls on the method 'deleteContactByID()' (in the repo ContactRepository), to delete a specific 'contact' entry from the 'indiv_contacts' SQL table. 

Redirects the user:
-   To the template 'view_address_book.html'
-   Via the route '/address_book'. 
-   With a message to confirm that the contact entry has been deleted successfully. 

### interview_preparation:
This file contains all the Python files which relate specifically to the 'InterviewPreparationRepository', which draws its entries from the SQL table 'interview_preparation'. However, where necessary, it does also connect to the other repositories & SQL tables where necessary.  

Files in this directory:
-   add_interview_prep.py
-   view_interview_prep_details.py
-   view_all_interview_prep.py
-   update_interview_prep.py
-   delete_interview_prep.py

#### add_interview_prep.py
Handles the functionality behind displaying the 'AddInterviewPrepForm()' (form) to the user & saving the information (the user has provided/entered into the form) into the 'interview_preparation' SQL table. 

Functions included:
-   display_interview_preparation_form()
-   post_add_interview_preparation()

##### display_interview_preparation_form()
This function handles the GET functionality for the route: '/applications/<int:application_id>/interview/<int:interview_id>/interview_preparation'.

Takes (input):
-   interview_prep_form (an instance of the 'AddInterviewPrepForm()', with the values for a specific 'InterviewPreparation' object)
-   application_id, interview_id, applicationsRepo, companyRepo, interviewPrepRepo, interviewsRepo

Functionality (algorithm):
-   Calls on the methods 'getApplicationByID()',  'getCompanyById()' & 'getInterviewByID()' to get the entry details for a specific job application, company & interview perspectively. These details are then extracted & stored in their own dictionaries 'application_details', 'company_details' & 'interview_details' perspectively. 

-   Calls on the functions 'cleanup_specific_job_application()', 'cleanup_specific_company()', & 'cleanup_specific_interview()' with the relevant dictionaries (application_details, company_details, & interview_details perspectively), to improve how these values will be presented to the user. 

-   Calls on the method 'getAllInterviewPrepEntriesByInterviewId()' to get all interviews linked to a specific interview, using the interview's unique ID (interview_id). If there are any interview preparation entries linked to this interview, then the details for each entry is extracted & stored in a dictionary 'interview_prep_details'. 

-   Stores all the URL's / routes, which will be used to display button links to the user, in a dictionary 'links'. 

-   Finally it takes all dictionaries, created so far by this function, & stores them all in a parent dictionary 'general_details'. This is so that all dictionaries can be can accessed via 1 single source: 'general_details'. 

Renders the template:
-   "interview_prep.html" 
-   With the parent dictionary 'general_details' & the form 'interview_prep_form'. 

Its important to note that the template 'interview_prep.html' displays not only the interview_prep_form, but also all the 'interview preparation' entries, which the user has already created for the current interview (that the user is preparing for). 

##### post_add_interview_preparation()
This function handles the POST functionality for the route: '/applications/<int:application_id>/interview/<int:interview_id>/interview_preparation'.

Takes (input):
-   interview_prep_form (as completed by the user)
-   user_id, application_id, interview_id, interviewPrepRepo

Functionality (algorithm):
-   Extracts all the field values, for the 'interview_prep_form' (form), & stores these values in a dictionary 'form_details', together with the 'user_id', 'application_id' & 'interview_id' (which relate to this specific interview preparation entry). 

-   Calls on the method 'createInterviewPreparation' (found in the repo 'InterviewPreparationRepository') & returns the unique ID 'interview_prep_id' for the newly-created entry. 

Redirects the user:
-   To the template: 'interview_prep.html'
-   Via the route: '/applications/<int:application_id>/interview/<int:interview_id>/interview_preparation'. 
-   With a message to confirm that the interview preparation entry has been created (in the 'interview_preparation' SQL table) successfully. 

#### view_interview_prep_details.py
Handles the functionality behind displaying the details for a specific entry, from the 'interview_preparation' SQL table, to the template 'interview_prep.html'.

Function included:
-   display_interview_prep_details()

##### display_interview_prep_details()
This function handles the GET functionality for the route: '/applications/<int:application_id>/interview/<int:interview_id>/interview_preparation/<int:interview_prep_id>/view_interview_prep_entry'.

Takes (input):
-   application_id, interview_id, interview_prep_id, interviewPrepRepo, applicationsRepo, companyRepo, interviewsRepo

Functionality (algorithm):
-   Calls on the methods 'getApplicationByID()',  'getCompanyById()', 'getInterviewByID()' & 'getInterviewPrepByID()' to get the entry details for a specific job application, company, interview & interview preparation (entry) perspectively. These details are then extracted & stored in their own dictionaries 'application_details', 'company_details', 'interview_details' & 'interview_prep_details' perspectively. 

-   Calls on the functions 'cleanup_specific_job_application()', 'cleanup_specific_company()', & 'cleanup_specific_interview()' with the relevant dictionaries (application_details, company_details, & interview_details perspectively), to improve how these values will be presented to the user. 

-   Stores all the URL's / routes, which will be used to display button links to the user, in a dictionary 'links'. 

-   Finally it takes all dictionaries, created so far by this function, & stores them all in a parent dictionary 'general_details'. This is so that all dictionaries can be can accessed via 1 single source: 'general_details'. 

Renders the template:
-   "view_interview_prep_details.html"
-   With the parent dictionary 'general_details', created by this function. 

#### view_all_interview_prep.py
Handles the functionality behind displaying all the interview preparation entries (added by the current user), from the 'interview_preparation' SQL table, to the template 'view_all_interview_prep.html'. 

Function included:
-   display_all_interview_prep_entries()

##### display_all_interview_prep_entries()
This function handles the GET functionality for the route: '/applications/<int:application_id>/interview/<int:interview_id>/view_all_preparation'.

Takes (input):
-   application_id, interview_id, user_id, applicationsRepo, interviewsRepo, interviewPrepRepo, companyRepo

Functionality (algorithm):
-   Calls on the methods 'getApplicationByID()',  'getCompanyById()' & 'getInterviewByID()' to get the entry details for a specific job application, company & interview perspectively. These details are then extracted & stored in their own dictionaries 'application_details', 'company_details' & 'interview_details' perspectively. 

-   Calls on the functions 'cleanup_specific_job_application()', 'cleanup_specific_company()', & 'cleanup_specific_interview()' with the relevant dictionaries (application_details, company_details, & interview_details perspectively), to improve how these values will be presented to the user. 

-   Calls on the method 'getAllInterviewPrepEntriesByInterviewId()' to get all interviews linked to a specific interview, using the interview's unique ID (interview_id). If there are any interview preparation entries linked to this interview, then the details for each entry is extracted & stored in a dictionary 'interview_prep_details'. 

-   Stores all the URL's / routes, which will be used to display button links to the user, in a dictionary 'links'. 

-   Finally it takes all dictionaries, created so far by this function, & stores them all in a parent dictionary 'general_details'. This is so that all dictionaries can be can accessed via 1 single source: 'general_details'. 

Renders the template:
-   "view_all_interview_prep.html"
-   With the parent dictionary 'general_details', created by this function.

#### update_interview_prep.py
Handles the functionality behind displaying the 'AddInterviewPrepForm()' (form), with the values for a specific interview preparation entry, to the user. Once the form is submitted, the form values are extracted & used to update an existing entry in the 'interview_preparation' SQL table.

Functions included:
-   display_update_interview_prep_form()
-   post_update_interview_preparation()

##### display_update_interview_prep_form()
This function handles the GET functionality for the route: '/applications/<int:application_id>/interview/<int:interview_id>/interview_preparation/<int:interview_prep_id>/update_interview_prep_entry'.

Takes (input):
-   update_interview_prep_form (an instance of the 'AddInterviewPrepForm()' (form) with the values for a specific 'InterviewPreparation' object)
-   application_id, interview_id, interview_prep_id applicationsRepo, interviewsRepo, companyRepo

Functionality (algorithm):
-   Calls on the methods 'getApplicationByID()',  'getCompanyById()' & 'getInterviewByID()' to get the entry details for a specific job application, company & interview perspectively. These details are then extracted & stored in their own dictionaries 'application_details', 'company_details' & 'interview_details' perspectively. 

-   Calls on the functions 'cleanup_specific_job_application()', 'cleanup_specific_company()', & 'cleanup_specific_interview()' with the relevant dictionaries (application_details, company_details, & interview_details perspectively), to improve how these values will be presented to the user. 

-   Stores all the URL's / routes, which will be used to display button links to the user, in a dictionary 'links'. 

-   Finally it takes all dictionaries, created so far by this function, & stores them all in a parent dictionary 'general_details'. This is so that all dictionaries can be can accessed via 1 single source: 'general_details'. 

Renders the template:
-   "view_all_interview_prep.html"
-   With the parent dictionary 'general_details', created by this function & the form 'update_interview_prep_form'.

##### post_update_interview_preparation()
This function handles the POST functionality for the route: '/applications/<int:application_id>/interview/<int:interview_id>/interview_preparation/<int:interview_prep_id>/update_interview_prep_entry'.

Takes (input):
-   update_interview_prep_form (as completed by the user)
-   application_id, interview_id, interview_prep_id, interviewPrepRepo

Functionality (algorithm):
-   Extracts all the field values, for the 'interview_prep_form' (form), & stores these values in a dictionary 'prep_fields', together with the 'interview_prep_id' (which relate to this specific interview preparation entry).

-   Iterates through the values in the dictionary, & if any form value has not been completed by the user then it's value is replaced with 'N/A'.  

-   Calls on the method 'updateInterviewPrepByID()' (found in the Repo InterviewPreparationRepository), with the 'details' dictionary. If the entry (linked to this interview preparation's unique ID 'interview_prep_id') was updated successfully, then this method will return True. Otherwise the method will return False.

Output of this function:
-   If the above method returns False, the function redirects the user:
    -   To the template: 'update_interview_prep.html',
    -   Via the route: '/applications/<int:application_id>/interview/<int:interview_id>/interview_preparation/<int:interview_prep_id>/update_interview_prep_entry'
    -   With a message notifying the user that the update request was not successful.

-   (Else) If the above method was successful (most likely case), then the function redirects the user:
    -   To the template: 'interview_prep.html'
    -   Via the route '/applications/<int:application_id>/interview/<int:interview_id>/interview_preparation'
    -   With the message to notify the user that the interview preparation entry has been updated successfully. 



#### delete_interview_prep.py
Handles the functionality behind deleting a specific interview preparation entry from the 'interview_preparation' SQL table. 

Function included:
-   delete_interview_prep_entry()

##### delete_interview_prep_entry()
This function hard deletes an entry from the 'interview_preparation' SQL table, using the entry's unique ID 'interview_prep_id'.

Takes (input):
-   application_id, interview_id, interview_prep_id, interviewPrepRepo

Functionality (algorithm):
-   Calls on the method 'getInterviewPrepByID' (from the InterviewPreparationRepository) to get a specific entry from the 'interview_preparation' SQL table.

-   Extracts, and stores' the entry's 'specific_question' field value. 

-   Calls on the method 'deleteByInterviewPrepID()' (in the repo InterviewPreparationRepository), to delete the entry, from the 'interview_preparation' SQL table. 

Redirects the user:
-   To the template: 'interview_prep.html'
-   Via the route: '/applications/<int:application_id>/interview/<int:interview_id>/interview_preparation'. 
-   With a message: "Interview preparation for subject: {} has been deleted.", where {} represents the subject of the entry that has been deleted by this function. 






### interviews:
This where you'll find all the Python files related to an interview entry / list of interview entries.

This file contains all the Python files which relate specifically to the 'InterviewsHistoryRepository', which draws its entries from the SQL table 'interviews'. However, where necessary, it does also connect to the other repositories & SQL tables where necessary.  