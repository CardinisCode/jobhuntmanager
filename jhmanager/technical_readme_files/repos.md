# Technical Readme
## Repo directory:
This file contains all the Repositories used for this project, with each Repository (Repo) interacting with a specific table in the database. 

In each Repo, there are two classes:
    1: Sets the field attributes which exist in a specific SQL table. 
    -   Each attribute is the name of a column in the table. 
    -   This can makes it so much easier to call on specific column values in each table entry. 

    2) Consists of the functions which interact with the SQL database. 
    -   These functions will carry out one of the following types of queries:
        -   Insert, Select, Update, Delete

    -   Each function:
        -   Sets up the cursor connection to the table
        -   Executes a command
        -   Commits the query
        -   Takes the result of the query & Instantiates either a single entry, or an entry in a list of entries, using the first class.
        -   At the end it returns either a single object or a list of objects.

These are the files in this directory:

#### __init__.py
This file has no functions within it & serves only to define this 'Repo' directory as a module.

#### application_notes.py:
This is a repository file which relates specifically to Application notes & includes the following 2 classes: ApplicationNotes & ApplicationNotesRepository. 

##### ApplicationNotes:
This is the class which defines the fields for a specific application note, where each field is a column name found in the 'application_notes' SQL table. 

Setting this class up allowed me to instantiate a specific ApplicationNote with a pre-set list of fields, which can be called on by another function in the Service directory for any application note.

###### Fields:
-   app_notes_id (Primary key)
-   user_id (Foreign key)
    -   Connecting this table to the 'users' table
-   application_id (Foreign key)
    -   Connecting this table to the 'job_applications' table
-   company_id (Foreign key)
    -   Connecting this table to the 'company' table
-   entry_date, description, notes_text

These field names are also the names for the columns in the 'job_applications' table.

##### ApplicationNotesRepository:
This class contains methods which interact with the 'application_notes' table in the SQL database, which carry out one of the following functions:
-   Insert
-   Select
-   Update
-   Delete

###### Connects to SQL table:
    application_notes

These methods include: 
###### createApplicationNote
Takes (input): 
    A dictionary of values for a specific note to be inserted (as a single entry) into the 'application_notes' table
Functionality (Algorithm):
    Runs a SQL 'INSERT' query to values for an application note into the perspective column fields. 
Returns (output): 
    The unique identifier (app_notes_id) for the newly created entry. 

An instance where this method is called:
FUNCTION:   post_application_add_note()
FILE:       services/application_notes/add_app_note.py
LINE:       35

###### getNoteByAppNoteID
Takes (input): 
    The app_notes_id for a specific application note
Functionality (Algorithm):
    Runs a SQL 'SELECT' query to grab a specific entry in the SQL table, using the note's 'app_notes_id'. It then instantiates the 'ApplicationNotes' class with the values received from the SQL query. 
Returns (output): 
    An instantiated object ('ApplicationNotes') with the values for a specific application note. 

An instance where this method is called:
FUNCTION:   display_application_note_details()
FILE:       services/application_notes/view_app_note_details.py
LINE:       8

###### getAppNotesByApplicationID
Takes (input): 
    application_id, user_id
Functionality (Algorithm):
-   Runs a SQL query to 'SELECT' all entries in the 'application_notes' table for a specific application (via the application_id) & for a specific user (via their user_id). The SQL query returns a list of entries. 
-   Iterates through each entry in the list, instantiating each entry using the 'ApplicationNotes' class, before adding these entries to a list of its own. 
Returns (output): 
    A list of application notes, where each note is an object. 

An instance where this method is called:
FUNCTION:   display_application_notes()
FILE:       services/application_notes/view_application_notes.py
LINE:       8

###### getAppNotesByUserId
Takes (input): 
    user_id
Functionality (Algorithm):
-   Runs a SQL query to 'SELECT' all entries in the 'application_notes' table for a specific user (via their user_id). The SQL query returns a list of entries. 
-   Iterates through each entry in the list, instantiating each entry using the 'ApplicationNotes' class, before adding these entries to a list of its own. 
Returns (output): 
    A list of application notes, where each note is an object. 

An instance where this method is called:
FUNCTION:   display_all_user_notes()
FILE:       services/display_all_notes.py
LINE:       9

###### deleteNoteByAppNoteID
Takes (input): 
    app_notes_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' an entry, from the 'application_notes' table, using the note's app_notes_id. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   delete_application_note()
FILE:       services/application_notes/delete_app_note.py
LINE:       5

###### deleteNoteByApplicationID
Takes (input): 
    application_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' all entries, from the 'application_notes' table, linked to the note's foreign key 'application_id'. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   delete_application()
FILE:       services/applications/delete_an_application.py
LINE:       8

###### deleteNoteByUserID
Takes (input): 
    user_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' all entries, from the 'application_notes' table, linked to the note's foreign key 'user_id'. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   post_delete_user()
FILE:       services/users/delete_user_account.py
LINE:       29

###### updateNoteByID
Takes (input): 
    A dictionary of fields related to a specific application note
Functionality (Algorithm):
-   Runs a SQL query to 'UPDATE' the entry in the 'application_notes' table where the 'app_notes_id' for a specific note matches with the primary key for an existing entry in the table.
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   post_update_app_note()
FILE:       services/application_notes/update_app_note.py
LINE:       27

#### applications_history.py:
This is a repository file which relates specifically to a Job Application & includes the following 2 classes: Application & ApplicationsHistoryRepository. 

##### Application
This is the class which defines the fields for a specific job application, where each field is a column name found in the 'job_applications' SQL table. 

Setting this class up allowed me to instantiate a specific Application with a pre-set list of fields, which can be called on by another function in the Service directory for any job application.

###### Fields:
-   app_id (Primary key)
-   user_id (Foreign key)
    -   Connecting this table to the 'users' table
-   company_id (Foreign key)
    -   Connecting this table to the 'company' table
-   app_date, app_time, date_posted, job_role, platform, interview_stage, employment_type, contact_received, location,job_description, user_notes, job_perks, tech_stack, job_url, job_ref, salary. 

These field names are also the names for the columns in the 'job_applications' table.

There are 2 additional methods to this class:
-   withCompanyDetails
    -   This method let me call an application with the company fields included. 
    -   This method also came about because the full job application form 'AddApplicationForm() also takes 'company'-related information.
-   '__str__'
    -   Returns a string with the main field values for an application.

##### ApplicationsHistoryRepository
This class contains methods which interact with the 'job_applications' table in the SQL database, which carry out one of the following functions:
-   Insert
-   Select
-   Update
-   Delete

###### Connects to SQL table:
    job_applications

These methods include: 
###### createApplication
Takes (input): 
    A dictionary of fields related to a specific job application.
Functionality (Algorithm):
-   Runs a SQL 'INSERT' query to create an entry in the 'job_applications' table, with the dictionary fields being allocated to the relevant columns in the table.
Returns (output): 
    The unique identifier (application_id) for the newly created entry.  

An instance where this method is called:
FUNCTION:   add_new_application_to_application_history()
FILE:       services/applications/add_application.py
LINE:       54

###### getTop10Applications
Takes (input): 
    user_id
Functionality (Algorithm):
-   Runs a SQL 'SELECT' query to get the top 10 applications where the foreign key 'user_id' matches the provided 'user_id' (input / argument), adding each query it finds into a list.
-   Iterates through each entry in the list, instantiating each entry using the 'ApplicationNotes' class, before adding these entries to a list of its own. 
Returns (output): 
    A list of 'application' objects.

An instance where this method is called:
FUNCTION:   display_all_applications_current_user()
FILE:       services/applications/view_all_applications.py. 
LINE:       8

###### getAllApplicationsByUserID
Takes (input): 
    user_id
Functionality (Algorithm):
-   Runs a SQL 'SELECT' query to get all applications where the foreign key 'user_id' matches the provided 'user_id' (input / argument), adding each query it finds into a list.
-   Iterates through each entry in the list, instantiating each entry using the 'Applications' class, before adding these entries to a list of its own. 
Returns (output): 
    A list of 'application' objects.

An instance where this method is called:
FUNCTION:   get_users_stats()
FILE:       services/display_dashboard_content.py
LINE:       170

###### getApplicationByID
Takes (input): 
    application_id
Functionality (Algorithm):
-   Runs a SQL 'SELECT' query to get a specific application entry the primary key 'application_id' matches the provided 'application_id' (input / argument).
-   It instantiates the 'Application' class with the values it gets from the 'application' entry (returned from the SQL query). 
Returns (output): 
    A single 'Application' object

An instance where this method is called:
FUNCTION:   display_upcoming_interviews() 
FILE:       services/display_dashboard_content.py 
LINE:       83

###### getApplicationsByCompanyID
Takes (input): 
    company_id
Functionality (Algorithm):
-   Runs a SQL 'SELECT' query to get all applications where the foreign key 'company_id' matches the provided 'company_id' (input / argument), adding each query it finds into a list.
-   Iterates through each entry in the list, instantiating each entry using the 'Applications' class, before adding these entries to a list of its own. 
Returns (output): 
    A list of 'application' objects.

An instance where this method is called:
FUNCTION:   delete_company_from_db() 
FILE:       services/company/delete_company.py 
LINE:       37

###### updateInterviewStageByID
Takes (input): 
    A dictionary of fields, which includes the interview_stage & the application_id
Functionality (Algorithm):
-   Runs a SQL query to 'UPDATE' the column 'interview_stage' for a specific entry in the 'job_application' table where the 'application_id' for a specific note matches with the primary key for an existing entry in the table.
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   update_interview_stage_in_applications_repo() 
FILE:       services/interviews/add_interview.py 
LINE:       86

###### updateApplicationByID
Takes (input): 
    A dictionary of fields related to a specific job application entry. 
Functionality (Algorithm):
-   Runs a SQL query to 'UPDATE' a specific entry in the 'job_application' table where the 'application_id' for a specific note matches with the primary key for an existing entry in the table.
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   post_update_application() 
FILE:       services/applications/update_application.py 
LINE:       31

###### deleteApplicationByID
Takes (input): 
    application_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' any entry (from the 'job_application' table) linked to a specific application's primary key 'application_id'. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   delete_application()
FILE:       services/applications/delete_an_application.py
LINE:       6

###### deleteApplicationsByUserID
Takes (input): 
    user_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' all entries, from the 'job_application' table, linked to the application's foreign key 'user_id'. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   post_delete_user()
FILE:       services/users/delete_user_account.py
LINE:       25

###### deleteApplicationByCompanyID
Takes (input): 
    company_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' all entries, from the 'job_application' table, linked to the application's foreign key 'company_id'. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   delete_company_from_db()
FILE:       services/company/delete_company.py
LINE:       46

#### company_notes.py
This is a repository file which relates specifically to a Company Note & includes the following 2 classes: CompanyNotes & CompanyNotesRepository. 

##### CompanyNotes
This is the class which defines the fields for a specific Company Note, where each field is a column name found in the 'company_notes' SQL table. 

Setting this class up allowed me to instantiate a specific Note with a pre-set list of fields, which can be called on by another function in the Service directory for any company note.

###### Fields:
-   company_note_id (Primary key)
-   user_id (Foreign key)
    -   Connecting this table to the 'users' table
-   company_id (Foreign key)
    -   Connecting this table to the 'company' table
-   entry_date, subject, note_text

These field names are also the names for the columns in the 'company_notes' table.

##### CompanyNotesRepository:
This class contains methods which interact with the 'company_notes' table in the SQL database, which carry out one of the following functions:
-   Insert
-   Select
-   Update
-   Delete

###### Connects to SQL table:
    company_notes

These methods include: 
###### createNewCompanyNote
Takes (input): 
    A dictionary of fields which relate to a specific company note
Functionality (Algorithm):
-   Runs a SQL 'INSERT' query to create an entry in the 'company_notes' table, with the dictionary fields being allocated to the relevant columns in the table.
Returns (output): 
    The unique identifier (company_note_id) for the newly created entry.  

An instance where this method is called:
FUNCTION:   post_add_company_note()
FILE:       services/company_notes/add_company_note.py
LINE:       29

###### getAllNotesByCompanyID
Takes (input): 
    A dictionary which includes the company_id & user_id
Functionality (Algorithm):
-   Runs a SQL 'SELECT' query to get all entries from the 'company_notes' table where the foreign key 'company_id' matches the provided 'company_id' (input / argument) & the foreign key 'user_id' matches the provided 'user_id' (input / argument). Each query that meets the requirements for this query is added to a list.
-   Iterates through each entry in the list, instantiating each entry using the 'CompanyNotes' class, before adding these entries to a list of its own. 
Returns (output): 
    A list of 'CompanyNotes' objects.

An instance where this method is called:
FUNCTION:   display_all_notes_for_a_company()
FILE:       services/company_notes/view_all_company_notes.py
LINE:       15

###### getCompanyNoteByID
Takes (input): 
    company_note_id
Functionality (Algorithm):
-   Runs a SQL 'SELECT' query to grab a specific entry in the 'company_notes' table, using the note's primary key 'company_note_id'. It then instantiates the 'CompanyNotes' class with the values received from the SQL query. 
Returns (output): 
    An instantiated object ('CompanyNotes') with the values for a specific company note. 

An instance where this method is called:
FUNCTION:   display_company_note_details()
FILE:       services/company_notes/view_specific_note.py
LINE:       8

###### getCompanyNotesByUserID
Takes (input): 
    user_id
Functionality (Algorithm):
-   Runs a SQL query to 'SELECT' all entries in the 'company_notes' table where the foreign key 'user_id' matches the provided 'user_id' (input / argument). Each query that meets the requirements for this query is added to a list.
-   Iterates through each entry in the list, instantiating each entry using the 'CompanyNotes' class, before adding these entries to a list of its own. 
Returns (output): 
    A list of 'CompanyNotes' objects.

An instance where this method is called:
FUNCTION:   display_all_user_notes()
FILE:       services/display_all_notes.py
LINE:       10

###### UpdateCompanyNoteByID
Takes (input): 
    A dictionary of fields related to a specific company note entry. 
Functionality (Algorithm):
-   Runs a SQL query to 'UPDATE' a specific entry in the 'company_notes' table where the provided 'company_note_id' matches with the primary key for an existing entry in the table.
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   post_update_company_form()
FILE:       services/company_note/update_company_note.py
LINE:       27

###### deleteCompanyNoteByID
Takes (input): 
    company_note_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' an entry, from the 'company_notes' table, using the note's company_note_id. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   delete_specific_company_note()
FILE:       services/company_notes/delete_company_note.py
LINE:       5

###### deleteAllCompanyNotesByUserID
Takes (input): 
    user_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' all entries, from the 'company_notes' table, linked to the note's foreign key 'user_id'. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   post_delete_user()
FILE:       services/users/delete_user_account.py
LINE:       29

###### deleteCompanyNotesByCompanyID
Takes (input): 
    company_note_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' all entries, from the 'company_notes' table, linked to the note's foreign key 'user_id'. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   delete_company_from_db()
FILE:       services/company/delete_company.py
LINE:       33

#### company.py
This is a repository file which relates specifically to a Company & includes the following 2 classes: Company & CompanyRepository. 

##### Company
This is the class which defines the fields for a specific Company, where each field is a column name found in the 'company' SQL table. 

Setting this class up allowed me to instantiate a specific company with a pre-set list of fields, which can be called on by another function in the Service directory for any company.

###### Fields:
-   company_id (Primary key)
-   user_id (Foreign key)
    -   Connecting this table to the 'users' table
-   name, description, location, industry, url, interviewers, contact_number

These field names are also the names for the columns in the 'company' table.

##### CompanyRepository
This class contains methods which interact with the 'company' table in the SQL database, which carry out one of the following functions:
-   Insert (Starts with 'create...')
-   Select ('starts with 'get....')
-   Update
-   Delete

###### Connects to SQL table:
    company

These methods include: 
###### createCompany
Takes (input): 
    A dictionary of fields which relate to a specific company
Functionality (Algorithm):
-   Runs a SQL 'INSERT' query to create an entry in the 'company' table, with the dictionary fields being allocated to the relevant columns in the table.
Returns (output): 
    The unique identifier (company_id) for the newly created entry.  

An instance where this method is called:
FUNCTION:   post_add_company()
FILE:       services/company/add_company.py
LINE:       41

###### getCompanyById:
Takes (input): 
    company_id
Functionality (Algorithm):
-   Calls on the 'getByField()' from the 'database' repo, to get a specific entry in the 'company' table, using the table's primary key 'company_id'. 
-   Instantiates the entry, returned from the SQL query, using the 'Company' class. 
Returns (output): 
    An instantiated object ('Company') with the values for a specific company. 

An instance where this method is called:
FUNCTION:   display_company_profile()
FILE:       services/company/view_company_profile.py
LINE:       7

###### getCompanyByName
Takes (input): 
    company_name, user_id
Functionality (Algorithm):
-   Runs a SQL 'SELECT' query to find & return any entry in the 'company' table where the 'company_name' (input) matches the 'name' column value & the provided 'user_id' matches the entry's foreign key 'user_id'.
-   It instantiates the 'Company' class with the values it gets from the 'company' entry (returned from the SQL query). 
Returns (output): 
    A single 'Company' object.

Note: This method accesses the 'company' table by calling on the 'getByName()' method which exists in 'databases.py'.

An instance where this method is called:
FUNCTION:   post_add_company()
FILE:       services/company/add_company.py
LINE:       19

###### getCompanyEntriesByUserID
Takes (input): 
    user_id
Functionality (Algorithm):
-   Runs a SQL 'SELECT' query to find all entries in the 'company' table where the 'user_id' (input) matches the entry's foreign key 'user_id'.
-   Iterates through each entry in the list, instantiating each entry using the 'Company' class, before adding these entries to a list of its own. 
Returns (output): 
    A list of 'Company' objects

An instance where this method is called:
FUNCTION:   display_all_companies_for_user()
FILE:       services/company/view_all_companies.py
LINE:       7

###### getTop8CompaniesByUserID
This method carries out the exact same functionality as the above 'getCompanyEntriesByUserID()', except it only returns to the top 8 entries, in the form of 'Company' objects. 

An instance where this method is called:
FUNCTION:   display_address_book()
FILE:       services/addressbook/view_addressbook.py
LINE:       7

###### updateCompanyByID
Takes (input): 
    A dictionary of fields which relate to a specific company
Functionality (Algorithm):
-   Runs a SQL 'UPDATE' query to update an entry which already exists in the 'company' table, with the dictionary fields being allocated to the relevant columns in the table.
Returns (output): 
    No output returned

An instance where this method is called:
FUNCTION:   post_update_company_profile()
FILE:       services/company/update_company.py
LINE:       25

###### updateCompanyByApplication
This method carries out the exact same functionality as the method 'updateCompanyByID' (above), except this query does not update all the columns for a company. It specifically focuses on updating the company fields which are found on the 'AddApplicationForm()':
-   name, description, industry, location

An instance where this method is called:
FUNCTION:   post_update_application()
FILE:       services/applications/update_application.py
LINE:       31

###### deleteCompanyByID
Takes (input): 
    company_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' an entry, from the 'company' table, using the company's primary key 'company_id'. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   delete_company_from_db()
FILE:       services/company/delete_company.py
LINE:       32

###### deleteAllCompaniesByUserID
Takes (input): 
    user_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' all entries, from the 'company' table, where the provided 'user_id' matches an entry's foreign key 'user_id'. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   post_delete_user()
FILE:       services/users/delete_user_account.py
LINE:       30

#### contacts.py
This is a repository file which relates specifically to a Contact & includes the following 2 classes: Contact & ContactRepository. 

The difference between the 'ContactRepository' & the 'CompanyRepository':
-   'ContactRepository' 
    -   connects to the 'indiv_contacts' SQL table, 
    -   Relates to data specific to people / individuals, 
-   'CompanyRepository' 
    -   connects to the 'company' SQL table
    -   Relates to data specific to a corporate/business.

##### Contact
This is the class which defines the fields for a specific (individual) Contact, where each field is a column name found in the 'indiv_contacts' SQL table. 

Setting this class up allowed me to instantiate a specific Contact with a pre-set list of fields, which can be called on by another function in the Service directory for any (individual) contact.

###### Fields:
-   contact_id (Primary key)
-   user_id (Foreign key)
    -   Connecting this table to the 'users' table
-   full_name, job_title, contact_number, company_name, email_address, linkedin_profile

These field names are also the names for the columns in the 'company' table.

##### ContactRepository
This class contains methods which interact with the 'indiv_contacts' table in the SQL database, which carry out one of the following functions:
-   Insert (Starts with 'create...')
-   Select ('starts with 'get....')
-   Update
-   Delete

###### Connects to SQL table:
    indiv_contacts

These methods include: 
###### create_contact
Takes (input): 
    A dictionary of fields which relate to a specific contact
Functionality (Algorithm):
-   Runs a SQL 'INSERT' query to create an entry in the 'indiv_contacts' table, with the dictionary fields being allocated to the relevant columns in the table.
Returns (output): 
    The unique identifier (contact_id) for the newly created entry.  

An instance where this method is called:
FUNCTION:   post_add_new_contact()
FILE:       services/contacts_directory/add_new_contact.py
LINE:       28

###### getContactByID
Takes (input): 
    contact_id
Functionality (Algorithm):
-   Runs a SQL 'SELECT' query to grab a specific entry in the 'indiv_contacts' table, using the contact's primary key 'contact_id'. It then instantiates the 'Company' class with the values received from the SQL query. 
Returns (output): 
    An instantiated object ('Contact') with the values for a specific contact. 

An instance where this method is called:
FUNCTION:   display_contact_details()
FILE:       services/contacts_directory/view_contact_details.py
LINE:       6

###### getContactsByUserID
Takes (input): 
    user_id
Functionality (Algorithm):
-   Runs a SQL 'SELECT' query to find all entries in the 'indiv_contacts' table where the 'user_id' (input) matches the entry's foreign key 'user_id'.
-   Iterates through each entry in the list, instantiating each entry using the 'Contact' class, before adding these entries to a list of its own. 
Returns (output): 
    A list of 'Contact' objects

An instance where this method is called:
FUNCTION:   display_contacts_for_user()
FILE:       services/contacts_directory/view_contact_list.py
LINE:       6

###### getTop8ContactsByUserID
Carries out the same functionality as the above 'getContactsByUserID', except it returns the top 8 entries, where each entry is an instantiated 'Contact' object.

An instance where this method is called:
FUNCTION:   display_address_book()
FILE:       services/address_book/view_address_book.py
LINE:       29

###### updateContactByID
Takes (input): 
    A dictionary of fields which relate to a specific contact.
Functionality (Algorithm):
-   Runs a SQL 'UPDATE' query to update an entry in the 'indiv_contacts' table, with the dictionary fields being allocated to the relevant columns in the table.
Returns (output): 
    No output returned

An instance where this method is called:
FUNCTION:   post_update_contact()
FILE:       services/contacts_directory/update_contact.py
LINE:       29

###### deleteContactByID
Takes (input): 
    contact_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' an entry, from the 'indiv_contacts' table, using the company's primary key 'contact_id'. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   delete_contact_details()
FILE:       services/contacts_directory/delete_contact.py
LINE:       5

###### deleteAllContactsByUserID
Takes (input): 
    user_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' all entries, from the 'indiv_contacts' table, where the provided 'user_id' matches an entry's foreign key 'user_id'. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   post_delete_user()
FILE:       services/users/delete_user_account.py
LINE:       32

#### database.py
Connects to the SQL database 'jhmanager.db' & includes two classes: Database & SqlDatabase. 

##### Database()
This class is an interface on how to access the database tables. 

I created this class as an experiment, but I felt it went a bit over my head & so I didn't use it consistently across the Repos (in this project / application).

##### methods:
###### insert()
States that an 'insert' query should receive 2 arguments: A table name & the data to be inserted into the table.

###### getByField()
States that any 'get...' method, to run a 'Select' query against a database table, should receive 2 arguments: a table name and the unique ID for that table.

##### SqlDatabase
This class connects to the 'jhmanager.db' database, & using the blueprints (provided in the 'Database' class above), the methods within this class will interact with the SQL database itself.

##### methods:
###### insert()
Takes (input):
    table name, data
Functionality:
    Interacts with the table (provided to this function), to insert the provided 'data'.
Returns:
    The last row's ID, which is the unique ID for the newly-created entry.

###### getByField()
Takes (input):
    table name, field, value
Functionality:
    Interacts with a specific table (as specified by the first argument 'table'), to get any entry where the provided 'field' & 'value' match up with an existing 'column' & its value perspectively. 
Returns:
    If it finds an entry that meets the above requirements, it returns that entry.

Called by the function / method:
    'getInterviewByID()' in the InterviewsHistoryRepository.

###### getByName()
Takes (input):
    table, name, name_value, user_id, userID_value
Functionality:
    Interacts with a specific table (as specified by the first argument 'table'). It runs through every entry in that table & compares the column's 'name' to the 'name_value' provided & it compares the column 'user_id' with the provided 'userID_value'. 
Returns:
    If any entry in the 'table' meets both the above requirements, it returns that entry.

Called by the function / method:
    'getCompanyByName()' in the CompanyRepository.


#### interview_prep_history.py
This is a repository file which relates specifically to Interview Preparation & includes the following 2 classes: InterviewPreparation & InterviewPreparationRepository. 

##### InterviewPreparation
This is the class which defines the fields for a specific Interview Preparation entry (or a list of Interview Preparation entries), where each field is a column name found in the 'interview_preparation' SQL table. 

Setting this class up allowed me to instantiate a specific Interview Preparation with a pre-set list of fields, which can be called on by another function in the Service directory for any Interview Preparation.

###### Fields:
-   interview_prep_id (Primary key)
-   interview_id (Foreign key)
    -   Connecting this table to the 'interviews' table
-   application_id (Foreign key)
    -   Connecting this table to the 'job_applications' table
-   user_id (Foreign key)
    -   Connecting this table to the 'users' table
-   question, answer

These field names are also the names for the columns in the 'interview_preparation' table.

##### InterviewPreparationRepository
This class contains methods which interact with the 'interview_preparation' table in the SQL database, which carry out one of the following functions:
-   Insert (Starts with 'create...')
-   Select ('starts with 'get....')
-   Update
-   Delete

###### Connects to SQL table:
    interview_preparation

These methods include: 
###### createInterviewPreparation
Takes (input): 
    A dictionary of fields which relate to a specific interview preparation (entry)
Functionality (Algorithm):
-   Runs a SQL 'INSERT' query to create an entry in the 'interview_preparation' table, with the dictionary fields being allocated to the relevant columns in the table.
Returns (output): 
    The unique identifier (interview_prep_id) for the newly created entry.  

An instance where this method is called:
FUNCTION:   post_add_interview_preparation()
FILE:       services/interview_preparation/add_interview_prep.py
LINE:       92

###### getInterviewPrepByID
Takes (input): 
    interview_prep_id
Functionality (Algorithm):
-   Runs a SQL 'SELECT' query to grab a specific entry in the 'interview_preparation' table, where the provided 'interview_prep_id' (input) matches the entry's primary key 'interview_prep_id'.
-   It then instantiates the 'InterviewPreparation' class with the values received from the SQL query. 
Returns (output): 
    An instantiated object ('InterviewPreparation') with the values for a specific Interview Preparation entry. 

An instance where this method is called:
FUNCTION:   display_interview_prep_details()
FILE:       services/interview_preparation/view_interview_prep_details.py
LINE:       11

###### getAllInterviewPrepEntriesByInterviewId
Takes (input): 
    interview_id
Functionality (Algorithm):
-   Runs a SQL 'SELECT' query to find all entries in the 'interview_preparation' table where the 'interview_id' (input) matches the entry's foreign key 'interview_id'.
-   Iterates through each entry in the list, instantiating each entry using the 'InterviewPreparation' class, before adding these entries to a list of its own. 
Returns (output): 
    A list of 'InterviewPreparation' objects

An instance where this method is called:
FUNCTION:   display_all_interview_prep_entries()
FILE:       services/interview_preparation/view_all_interview_prep.py
LINE:       12

###### updateInterviewPrepByID
Takes (input): 
    A dictionary of fields which relate to a specific interview preparation entry.
Functionality (Algorithm):
-   Runs a SQL 'UPDATE' query to update an entry in the 'interview_preparation' table, with the dictionary fields being allocated to the relevant columns in the table.
Returns (output): 
    No output returned

An instance where this method is called:
FUNCTION:   post_update_interview_preparation()
FILE:       services/interview_preparation/update_interview_prep.py
LINE:       68

###### deleteInterviewPrepByID
Takes (input): 
    interview_prep_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' an entry, from the 'interview_preparation' table, where the provided 'interview_prep_id' matches the entry's primary key 'interview_prep_id'. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   delete_interview_prep_details()
FILE:       services/interview_preparation/delete_interview_prep.py
LINE:       8

###### deleteInterviewPrepByInterviewID
Takes (input): 
    interview_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' all entries, from the 'interview_preparation' table, where the provided 'interview_id' matches an entry's foreign key 'interview_id'. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   delete_interview()
FILE:       services/interviews/delete_an_interview.py
LINE:       7

###### deleteInterviewPrepByApplicationID
Takes (input): 
    application_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' all entries, from the 'interview_preparation' table, where the provided 'application_id' matches an entry's foreign key 'application_id'. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   delete_company_from_db()
FILE:       services/company/delete_company.py
LINE:       34

###### deleteInterviewPrepByUserID
Takes (input): 
    user_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' all entries, from the 'interview_preparation' table, where the provided 'user_id' matches an entry's foreign key 'user_id'. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   post_delete_user()
FILE:       services/users/delete_user_account.py
LINE:       27

#### interviews_history.py
This is a repository file which relates specifically to Interviews & includes the following 2 classes: Interview & InterviewsHistoryRepository. 

##### Interview
This is the class which defines the fields for a specific Interview (or a list of Interview entries), where each field is a column name found in the 'interviews' SQL table. 

Setting this class up allowed me to instantiate a specific Interview with a pre-set list of fields, which can be called on by another function in the Service directory for any Interview entry.

###### Fields:
-   interview_id (Primary key)
-   application_id (Foreign key)
    -   Connecting this table to the 'job_applications' table
-   user_id (Foreign key)
    -   Connecting this table to the 'users' table
-   entry_date, interview_date, interview_time, interview_type, location, medium, other_medium, contact_number, status, interviewer_names, video_link, extra_notes. 

These field names are also the names for the columns in the 'interviews' table.

##### InterviewsHistoryRepository
This class contains methods which interact with the 'interviews' table in the SQL database, which carry out one of the following functions:
-   Insert (Starts with 'create...')
-   Select ('starts with 'get....')
-   Update
-   Delete

###### Connects to SQL table:
    interviews

These methods include: 
###### CreateInterview()
Takes (input): 
    A dictionary of fields which relate to a specific interview (entry)
Functionality (Algorithm):
-   Runs a SQL 'INSERT' query to create an entry in the 'interviews' table, with the dictionary fields being allocated to the relevant columns in the table.
Returns (output): 
    The unique identifier (interview_id) for the newly created entry.  

An instance where this method is called:
FUNCTION:   InsertFieldsIntoInterviewHistory()
FILE:       services/interviews/add_interview.py
LINE:       42

###### getInterviewByID()
Takes (input): 
    interview_id
Functionality (Algorithm):
-   Calls on the 'getByField()' from the 'database' repo, to get a specific entry in the 'interviews' table, using the table's primary key 'interview_id'. 
-   Instantiates the entry, returned from the SQL query, using the 'Interview' class. 
Returns (output): 
    An instantiated object ('Interview') with the values for a specific Interview entry.

An instance where this method is called:
FUNCTION:   display_interview_details()
FILE:       services/interviews/view_interview_details.py
LINE:       11

###### getInterviewsByUserID
Takes (input): 
    userID
Functionality (Algorithm):
-   Runs a SQL 'SELECT' query to find all entries in the 'interviews' table where the 'interview_id' (input) matches the entry's foreign key 'userID'.
-   Iterates through each entry in the list, instantiating each entry using the 'Interview' class, before adding these entries to a list of its own. 
Returns (output): 
    A list of 'Interviews' objects

An instance where this method is called:
FUNCTION:   display_today_interviews()
FILE:       services/display_dashboard_content.py
LINE:       126

###### getInterviewsByApplicationID
Takes (input): 
    application_id
Functionality (Algorithm):
-   Runs a SQL 'SELECT' query to find all entries in the 'interviews' table where the 'application_id' (input) matches the entry's foreign key 'application_id'.
-   Iterates through each entry in the list, instantiating each entry using the 'Interview' class, before adding these entries to a list of its own. 
Returns (output): 
    A list of 'Interviews' objects

An instance where this method is called:
FUNCTION:   display_all_interviews_for_application()
FILE:       services/interviews/view_all_interviews.py
LINE:       10

###### getTop6InterviewsByApplicationID
Carries out the same functionality as the above function 'getInterviewsByApplicationID()', except it only limits its query to only return the top 6 entries. These 6 entries are then instantiated using the 'Interview' class, before adding these entries to a list of its own. 

An instance where this method is called:
FUNCTION:   get_interviews()
FILE:       services/applications/view_application_details.py
LINE:       51

###### updateInterviewByID
Takes (input): 
    A dictionary of fields which relate to a specific interview entry.
Functionality (Algorithm):
-   Runs a SQL 'UPDATE' query to update an entry in the 'interviews' table, with the dictionary fields being allocated to the relevant columns in the table.
Returns (output): 
    No output returned

An instance where this method is called:
FUNCTION:   post_update_interview()
FILE:       services/interviews/update_interview.py
LINE:       46

###### updateInterviewStatusByID
Takes (input): 
    A dictionary of fields which includes the updated value for 'status' & interview_id. 
Functionality (Algorithm):
-   Runs a SQL 'UPDATE' query to specifically update the value stored in the 'interviews' table's 'status' column for a specific entry, where the provided 'interview_id' matches the entry's primary key 'interview_id'.
Returns (output): 
    No output returned

An instance where this method is called:
FUNCTION:   post_update_interview_status()
FILE:       services/interviews/update_interview_status.py
LINE:       33

###### deleteInterviewByID
Takes (input): 
    interview_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' an entry, from the 'interviews' table, where the provided 'interview_id' matches the entry's primary key 'interview_id'. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   delete_interview()
FILE:       services/interviews/delete_an_interview.py
LINE:       6

###### deleteInterviewsByApplicationID
Takes (input): 
    application_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' all entries, from the 'interviews' table, where the provided 'application_id' matches an entry's foreign key 'application_id'. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   delete_application()
FILE:       services/application/delete_an_application.py
LINE:       7

###### deleteInterviewsByUserID
Takes (input): 
    user_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' all entries, from the 'interviews' table, where the provided 'user_id' matches an entry's foreign key 'user_id'. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   post_delete_user()
FILE:       services/users/delete_user_account.py
LINE:       26

#### job_offers_history.py
This is a repository file which relates specifically to Job Offers & includes the following 2 classes: JobOffer & JobOffersRepository.

##### JobOffer
This is the class which defines the fields for a specific Job Offer (or a list of Job Offer entries), where each field is a column name found in the 'job_offers' SQL table. 

Setting this class up allowed me to instantiate a specific Job Offer with a pre-set list of fields, which can be called on by another function in the Service directory for any Job Offer entry.

###### Fields:
-   job_offer_id (Primary key)
-   user_id (Foreign key)
    -   Connecting this table to the 'users' table
-   company_id (Foreign key)
    -   Connecting this table to the 'company' table
-   application_id (Foreign key)
    -   Connecting this table to the 'job_applications' table
-   entry_date, job_role, starting_date, salary_offered, perks_offered, offer_response.

These field names are also the names for the columns in the 'job_offers' table.

##### JobOffersRepository
This class contains methods which interact with the 'job_offers' table in the SQL database, which carry out one of the following functions:
-   Insert (Starts with 'create...')
-   Select ('starts with 'get....')
-   Update
-   Delete

###### Connects to SQL table:
    job_offers

These methods include: 

###### CreateJobOffer
Takes (input): 
    A dictionary of fields which relate to a specific job offer (entry)
Functionality (Algorithm):
-   Runs a SQL 'INSERT' query to create an entry in the 'job_offers' table, with the dictionary fields being allocated to the relevant columns in the table.
Returns (output): 
    The unique identifier (job_offer_id) for the newly created entry.  

An instance where this method is called:
FUNCTION:   InsertFieldsIntoInterviewHistory()
FILE:       services/job_offers/add_job_offer.py
LINE:       35

###### getJobOfferByID()
Takes (input): 
    job_offer_id
Functionality (Algorithm):
-   Runs a SQL 'SELECT' query to grab a specific entry in the 'job_offers' table, where the provided input matches the entry's primary key 'job_offer_id'.
-   Instantiates the entry, returned from the SQL query, using the 'JobOffer' class. 
Returns (output): 
    An instantiated object ('JobOffer') with the values for a specific Job Offer entry.

An instance where this method is called:
FUNCTION:   display_job_offer()
FILE:       services/job_offers/view_job_offer.py
LINE:       9

###### getJobOffersByUserId()
Takes (input): 
    userID
Functionality (Algorithm):
-   Runs a SQL 'SELECT' query to find all entries in the 'job_offers' table where the provided input matches the entry's foreign key 'userID'.
-   Iterates through each entry in the list, instantiating each entry using the 'JobOffer' class, before adding these entries to a list of its own. 
Returns (output): 
    A list of 'JobOffer' objects

An instance where this method is called:
FUNCTION:   get_job_offers()
FILE:       services/applications/view_application_details.py
LINE:       126

###### updateJobOfferByID
Takes (input): 
    A dictionary of fields which relate to a specific job offer (entry), which includes the job_offer_id for the entry.
Functionality (Algorithm):
-   Runs a SQL 'UPDATE' query to update a specific entry in the 'job_offers' table, with the dictionary fields being allocated to the relevant columns in the table.
Returns (output): 
    No output returned

An instance where this method is called:
FUNCTION:   post_update_job_offer()
FILE:       services/job_offers/update_job_offer.py
LINE:       27

###### deleteJobOfferByID
Takes (input): 
    job_offer_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' an entry, from the 'job_offers' table, where the provided input matches the entry's primary key 'job_offer_id'. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   delete_job_offer_entry()
FILE:       services/job_offers/delete_job_offer.py
LINE:       5

###### deleteJobOfferByUserID
Takes (input): 
    user_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' all entries, from the 'job_offers' table, where the provided input matches an entry's foreign key 'user_id'. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   post_delete_user()
FILE:       services/users/delete_user_account.py
LINE:       31

###### deleteJobOfferByCompanyID
Takes (input): 
    company_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' all entries, from the 'job_offers' table, where the provided input matches an entry's foreign key 'company_id'. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   delete_company_from_db()
FILE:       services/company/delete_company.py
LINE:       34

###### deleteJobOfferByApplicationID
Takes (input): 
    application_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' all entries, from the 'job_offers' table, where the provided input matches an entry's foreign key 'application_id'. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   delete_application()
FILE:       services/applications/delete_an_application.py
LINE:       9

#### users.py
This is a repository file which relates specifically to Users & includes the following 2 classes: User & UserRepository. 

##### User
This is the class which defines the fields for a specific User (or a list of User entries), where each field is a column name found in the 'users' SQL table. 

Setting this class up allowed me to instantiate a specific User with a pre-set list of fields, which can be called on by another function in the Service directory for any User entry.

###### Fields:
-   user_id (Primary key)
-   username, hash, email, date.

These field names are also the names for the columns in the 'users' table.

##### UserRepository
This class contains methods which interact with the 'interviews' table in the SQL database, which carry out one of the following functions:
-   Insert (Starts with 'create...')
-   Select ('starts with 'get....')
-   Update
-   Delete

###### Connects to SQL table:
    users

These methods include: 

###### createUser()
Takes (input): 
    A dictionary of fields which relate to a specific User (entry)
Functionality (Algorithm):
-   Runs a SQL 'INSERT' query to create an entry in the 'users' table, with the dictionary fields being allocated to the relevant columns in the table.
Returns (output): 
    The unique identifier (user_id) for the newly created entry.  

An instance where this method is called:
FUNCTION:   post_register_user()
FILE:       services/users/register_user.py
LINE:       34

###### getUserByID()
Takes (input): 
    user_id
Functionality (Algorithm):
-   Runs a SQL 'SELECT' query to grab a specific entry in the 'users' table, where the provided input matches the entry's primary key 'user_id'.
-   Instantiates the entry, returned from the SQL query, using the 'User' class. 
Returns (output): 
    An instantiated object ('User') with the values for a specific User entry.

An instance where this method is called:
FUNCTION:   display_user_profile()
FILE:       services/users/user_profile.py
LINE:       6

###### getUserByUsername()
Takes (input): 
    username
Functionality (Algorithm):
-   Runs a SQL 'SELECT' query to find & return any entry in the 'user' table where the input matches the 'username' column value.
-   It instantiates the 'User' class with the values received from the SQL query. 
Returns (output): 
    A single 'User' object.

An instance where this method is called:
FUNCTION:   post_register_user()
FILE:       services/users/register_user.py
LINE:       21

###### getUserByEmail
Takes (input): 
    email
Functionality (Algorithm):
-   Runs a SQL 'SELECT' query to find & return any entry in the 'user' table where the input matches the 'email' column value.
-   It instantiates the 'User' class with the values received from the SQL query. 
Returns (output): 
    A single 'User' object.

An instance where this method is called:
FUNCTION:   post_register_user()
FILE:       services/users/register_user.py
LINE:       26

###### updateUserEmailByID
Takes (input): 
    A dictionary of fields which includes the updated value for 'email' & user_id. 
Functionality (Algorithm):
-   Runs a SQL 'UPDATE' query to specifically update the value stored in the 'user' table's 'email' column for a specific entry, where the provided 'user_id' matches the entry's primary key 'user_id'.
Returns (output): 
    No output returned

An instance where this method is called:
FUNCTION:   post_update_email_address()
FILE:       services/users/update_email.py
LINE:       18

###### updateUserHashByID
Takes (input): 
    A dictionary of fields which includes the updated value for 'hash' & user_id. 
Functionality (Algorithm):
-   Runs a SQL 'UPDATE' query to specifically update the value stored in the 'user' table's 'hash' column for a specific entry, where the provided 'user_id' matches the entry's primary key 'user_id'.
Returns (output): 
    No output returned

An instance where this method is called:
FUNCTION:   post_change_password()
FILE:       services/users/change_password.py
LINE:       31

###### deleteUserByID
Takes (input): 
    user_id
Functionality (Algorithm):
-   Runs a Try statement, which runs a SQL query to 'DELETE' an entry, from the 'users' table, where the provided input matches the entry's primary key 'user_id'. 
Returns (output): 
    No output is returned

An instance where this method is called:
FUNCTION:   post_delete_user()
FILE:       services/users/delete_user_account.py
LINE:       24