# Project Hunt Manager: Technical Readme
This technical readme goes into more detailed look at how each function works & which Repositories each function connects to. 

To be clear this technical Readme only looks at the application's functions found in the following directories:
-   Forms
-   Repo
-   Services
-   Static

The files in this project:
## Forms: 
All forms are created using WTForms - a library I found that works well with Python & Flask. 

Each Form is a class, but WTForms is unique in that each form attribute is defined as a Field, but is also simultaneously a method. When I want to use a form, to get extract specific information from the user, I  instantiate it, either as a blank form, or with information from a specific entry in a SQL query. Since each form is a class, I can use dot notation to access the field values from the form.   

WTForms also offers the field/data validation and comes included with CSRF protection. These forms are saved in jhmanager/forms. 

These are the files in this directory:
### add_application_form.py
#### Form name: 
    AddApplicationForm()
#### Functionality: 
    This form includes all the fields that I've commonly seen on job application forms (online and in person). 
#### Form Fields:
    date_posted, job_role, emp_type, job_ref, company_name, company_description, industry, job_description, job_perks, tech_stack, location, salary, user_notes, platform, job_url. 
##### An instance where this method is called:

#### Renders to the template:
    add_job_application.html
##### Related to SQL table: 
    'job_applications'

#### add_application_note_form.py
##### Form name: 
    AddApplicationNoteForm()
##### Functionality: 
    This form is simple in nature and only has 2 fields: The subject and content for a form. 
##### Form Fields:
    description, notes_text
##### An instance where this method is called:

##### Renders to the template:
    add_application_note.html
##### Related to SQL table: 
    'application_notes'

#### add_company_form.py
##### Form name: 
    AddCompanyForm()
##### Functionality: 
    This Form has fields relevant to a company and puts together 'contact' info for a specific company.
##### Fields:
    name, description, location, industry, interviewers, url
##### An instance where this method is called:

##### Renders to the template:
    add_company_form.html
##### Related to SQL table: 
    'company'

#### add_company_job_app_form.py
##### Form name: 
    AddCompanyJobApplicationForm()
##### Functionality: 
    This form is very similar to the AddApplicationForm(), except it doesn't include any fields relevant to a company. 
##### Fields:
    date_posted, job_role, emp_type, job_ref, job_description, job_perks, tech_stack, salary, user_notes, platform, job_url. 
##### An instance where this method is called:

##### Renders to the template:
    add_company_job_application.html
##### Related to SQL table: 
    'job_applications'

#### add_company_note_form.py
##### Form name: 
    AddCompanyNoteForm()
##### Functionality: 
    I kept this form simple in nature, so that it resembles a note we'd scribble in a note book. 
##### Fields:
    subject, note_text
##### An instance where this method is called:

##### Renders to the template:
    add_company_note.html
##### Related to SQL table: 
    'company_notes'

#### add_interview_form.py
##### Form name: 
    AddInterviewForm()
##### Functionality: 
    This form includes fields relevant to an interview. I added fields relevant to interviews done 1) in person, 2) over video call & 3) over a phone call. 
##### Fields:
    interview_date, interview_time, interviewer_names, interview_type, interview_location, interview_medium, other_medium, video_link, phone_call, status, extra_notes. 
##### An instance where this method is called:

##### Renders to the template:
    add_interview.html
##### Related to SQL table: 
    'interviews'

#### add_interview_prep_form.py
##### Form name: 
    AddInterviewPrepForm()
##### Functionality: 
    This form is similar in nature to the note forms, except the 2 fields are 'Question' and 'Answer'. It allows the user to add the interview Question and the answer the user is planning to say in response to the Question. 
##### Fields:
    question, answer
##### An instance where this method is called:

##### Renders to the template:
    interview_prep.html
##### Related to SQL table: 
    'interview_preparation'

#### add_job_offer_form.py
##### Form name: 
    AddJobOffer()
##### Functionality: 
    This form allows the user to add a job offer they've received and gives the user the field 'offer_response' so the user can select if they've accepted (or rejected) the offer or if they're still thinking about it. 
##### Fields: 
    job_role, salary_offered, perks_offered, offer_response, starting_date. 
##### An instance where this method is called:

##### Renders to the template:
    add_job_offer.html
##### Related to SQL table: 
    'job_offers'

#### add_new_contact_form.py
##### Form name:
    AddNewContactForm()
##### Functionality: 
    This form asks the user for information very much relevant for putting together contact information. Making connections is very important when looking for work as we often have a higher chance of getting a job when we know someone on the inside of the company we're looking to work for. We're also more likely to know of a vacacy through the network we build. 
##### Fields:
    full_name, job_title, contact_number, company_name, email_address, linkedin_profile.
##### An instance where this method is called:

##### Renders to the template:
    add_new_contact.html
##### Related to SQL table: 
    'indiv_contacts'

#### delete_account_form.py
##### Form name:
    DeleteAccountForm()
##### Functionality: 
    This form is presented to the user when they select the 'Delete Account' button in their User Profile. The form asks the user to enter their account password and once the user submits the form, their account is hard (entirely) deleted from the application's database. 
##### Fields:
    password
##### An instance where this method is called:

##### Renders to the template:
    delete_account.html
##### Related to SQL table: 
    'users'

#### delete_form.py
##### Form name:
    DeleteCompanyForm()
##### Functionality: 
    The user is presented with a select fields with 2 options. I believe by asking the user to manually select an option, they're less likely to make this choice by accident or by using a bot. 
    
    If the user chooses the "Yes....", & submits the form, then the company (and all data related to this company) will be hard deleted from the application's databases. For this reason, there is a warning presented above this option to notify the user of the consequences of deleting this company contact.
##### Fields:
    confirm_choice
##### An instance where this method is called:

##### Renders to the template:
    delete_company_profile.html
##### Related to SQL table: 
    'company'

#### login_form.py
##### Form name: 
    LoginForm()
##### Functionality: 
    Presents the user with a simple form, which allows the user to log into their account on the application. 
##### Fields:
    username, password
##### An instance where this method is called:

##### Renders to the template:
    login.html
##### Related to SQL table: 
    'users'

#### register_form.py
##### Form name: 
    RegisterUserForm()  
##### Functionality: 
    This form as the registration form & the values of this form will be used to create an account for the user. The user is asked to provide an unique username & email address. If either already exists in our database, the user will be asked to provide another username / email address. The 'confirm_password' field serves to ask the user to type a password in twice & ensure that both password values match. 
##### Fields:
    username, email_address, password, confirm_password.
##### An instance where this method is called:

##### Renders to the template:
    register.html
##### Related to SQL table: 
    'users'

#### update_company_form.py
##### Form name: 
    UpdateCompany() 
##### Functionality: 
    This form has all the functionality found on the 'AddCompanyForm()' Form, yet the 'UpdateCompany()' Form was created first. This form gets instantiated using the details from a specific entry in the 'company' SQL table. 
##### Fields:
    date_posted, job_role, emp_type, job_ref, job_description, job_perks, tech_stack, salary, user_notes, platform, job_url. 
##### An instance where this method is called:

##### Renders to the template:
    update_company_profile.html
##### Related to SQL table: 
    'company'

#### update_interview_status_form.py
##### Form name: 
    UpdateInterviewStatusForm() 
##### Functionality: 
    This form is very simple and serves to allow the user to update only the status of an interview. Once an interview has been completed/deleted/post-poned, the user will want to update the status without having to worry/focus on any of the other interview fields (on AddInterviewForm()). 
##### Fields:
    status
##### An instance where this method is called:

##### Renders to the template:
    update_interview_status.html
##### Related to SQL table: 
    'company'

#### update_user_details.py
##### Form name: 
    UpdateEmailAddressForm() 
##### Functionality: 
    This form serves to allow the user to update the email address linked to their account. The user is asked to provide the new email address twice. I added validators to ensure that the user provides the same email address in both fields.
##### Fields:
    email, confirm_email
##### An instance where this method is called:

##### Renders to the template:
    update_email.html
##### Related to SQL table: 
    'users'

##### Form name: 
    ChangePasswordForm()
##### Functionality: 
    This form serves to allow the user to change the password on their account. The user is asked to provide the new password twice. I added validators to ensure that the user provides the same password in both fields. Since these two fields are each designated as a 'PasswordField', the fields hide what the user enters into these fields, even as they're typing. 
##### Fields:
    password, confirm_password
##### An instance where this method is called:

##### Renders to the template:
    change_password.html
##### Related to SQL table: 
    'users'

## Repo:
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

###### grabTop10ApplicationsFromHistory
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

###### grabApplicationByID
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

###### updateInterviewStage
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

###### deleteCompanyNoteByUserID
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
-   Runs a SQL 'SELECT' query to grab a specific entry in the 'company' table, using the company's primary key 'company_id'. It then instantiates the 'Company' class with the values received from the SQL query. 
Returns (output): 
    An instantiated object ('Company') with the values for a specific company note. 

An instance where this method is called:
FUNCTION:   display_company_profile()
FILE:       services/company/view_company_profile.py
LINE:       7

###### grabCompanyByNameAndUserID
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

###### deleteCompanyByUserID
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
