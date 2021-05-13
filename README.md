
# Project Hunt Manager

A Web-based application aimed at job hunters looking to manage all aspects of their job hunt in one place. 

## Video Demo:  
```
    https://youtu.be/bX6YD33VKIw
```

This video is made using iMovie. 

## Link to Heroku-hosted site: 
```
    https://jobhuntmanger.herokuapp.com/
```
### Bugs:
    -   Heroku starts up the database every time the user logs in, creating the database from scratch every time. So the application doesn't successfully "save" the user's progress. 
    -   Heroku doesn't seem to accept / work with the CSRF tokens used by WTForms. So occassionally, upon submitting a form, the user is met with the error "CSRF token missing". There's a missing element/s that I'm missing to make this work. 

These bugs are exclusive to the Heroku-hosted site, and are not present when running this application locally on one's computer. 

## Description: 
A web-based application for any one looking to manage their job hunting. Its intended to be a place where a user can store job applications, interviews, interview preparation, notes, & contacts. Plus the user can add companies from their wishlist. 

The application uses:
-   Python
    -   Flask, WTForms 
-   HTML, CSS & a little JavaScript. 

I have narrowed down the application for fellow software engineers, so the Job application form is very much in the scope of the software engineering industry. 

## Please note: 
-   Deletes are hard deletes, for the purpose of this pilot product. So if the user selects to delete something, it will permanently delete the information from the SQLite3 database.

-   This Readme simply describes what each function & file does/serves, so I'll give a brief TLDR for each file/function. I'll go into more technical depth in the technical_readme.md (jhmanager/technical_readme.md).

## Files:
The files in this project are divided into the following sections:

### 1: Forms:
Each of the below forms request specific information from the user and link to a specific SQL database table. 

Below are the names of the files stored in the 'Forms' directory: 

#### add_application_form.py
Contains the Form class 'AddApplicationForm()', where each field name relates to the fields you'd expect on a typical job application form (online). The form allows the user a means to enter in the information for a specific job role they've applied to, which they've discovered on a job board / in a newspaper / via word-of-mouth. 

Each job application added (by the user) is added as an unique entry into the SQL database.

#### add_application_note_form.py
Contains the Form class 'AddApplicationNoteForm()' & when rendered to a template, it has 2 simple fields: description & notes_text. The form allows the user to add a note which will link directly to a specific job application. 

The logic behind this form is to allow the user to create a note for a specific job application at any point from the job application to the job offer. 

#### add_company_form.py
Contains the Form class 'AddCompanyForm()', & is used to pull together information regarding a specific company. Each company added (by the user) is added as an unique entry into the SQL database.

The logic behind this form comes from the idea that the user may want to build a directory of companies that they either want to work for or have already worked for.

The link to the form can be found on/in:
-   The addressbook (accessed by the 'Addressbook' tab at the top of the page)
-   The company directory (accessed via the Addressbook.)

#### add_company_job_app_form.py
Contains the Form class 'AddCompanyJobApplicationForm()' & it is used to add a job application entry for a specific company. The form has the same basic concept as the 'AddApplicationForm()', except it doesn't include any fields related to the company. 

The logic behind this form is the idea that the user is adding a job application for a company they've already created, so this form doesn't include any fields related to a company. This makes the form shorter and therefore quicker to complete. 

The link is this form can be found on a company's profile (on the 'view_company_profile.html' template). 

#### add_company_note_form.py
Contains the Form class 'AddCompanyForm()', & when rendered to a template, it has 2 simple fields: subject & note_text. The form allows the user to add a note which will link directly to a specific company.  

The logic behind this form is the idea that the user may want to add note linked to a specific company they've already added to their company directory.  

#### add_interview_form.py
Contains the Form class 'AddInterviewForm()' & is used to add a job interview that the user has lined up. It's linked both to a specific job application & the company with which they have the interview. 

The logic behind this form is the idea that the user will want to store the details of an upcoming interview & for that interview to be easily accessible. The interview form also has the option to add the link to the video call if the interview will be done remotely via Teams / Skype / Discord etc, which allows the user to quickly start up their interview session. 

Likewise the user can enter the location to the interview or contact details for the interviews for quick access on the day of the interview. The link to this form can be found on the 'view_application.html' template. 

#### add_interview_prep_form.py
Contains the Form class 'AddInterviewPrepForm()' & is used to allow the user to add an interview preparation entry for a specific interview. Each interview Preparation entry is linked to a specific interview, job application & company. 

The logic behind this form is the idea is to allow the user a place to prepare for an interview, where each entry has 2 fields:
-   Question:
    -   A question they're expecting to get asked in the interview 
-   Answer:
    -   Here the user can plan how to best answer this question in the context of the role they're interviewing for & the company they're interviewing with.

The link to this form can be found when viewing the details for a specific interview, and only whilst the interview date & time are still in the future. As soon as the interview date & time are in the past, the link to this form will no longer display to the user. In terms of templates this would be 'view_interview_details.html'. 

Another link to this form can be found by viewing the interview preparation that the user has already done. 
-   The link to view the interview preparation can also be found by viewing the details for a specific interview. 

#### add_job_offer_form.py
Contains the Form class 'AddJobOffer()', & is used to allow the user to add a job offer they've received from a company. This job offer is also connected to the specific job application they've submitted to this company. 

The idea behind this form is to allow the user to keep a track of any/all job offers they receive in their job hunt journey (and the company & job application to which these job offers are connected to). 

The link to this form can be found by viewing the details for a specific job application the user has already added to their profile.


#### add_new_contact_form.py
Contains the Form class 'AddJobOffer()' & used to put together all the information you'd expect for a 'contact' profil. This includes everything from the person's Full name to their email address.  

This form asks the user for information very much relevant for putting together contact information. Making connections is very important when looking for work as we often have a higher chance of getting a job when we know someone on the inside of the company we're looking to work for. We're also more likely to know of a vacacy through the network we build. 

The link to this form can be found:
-   On the Addressbook, via the 'Addressbook' tab on the top naviational bar. 
-   In the Contacts directory, which can be accessed via the Addressbook

#### delete_account_form.py
Contains the Form class 'DeleteAccountForm()', which is used to simply ask the user to confirm whether/not they want to delete their user account on this application. The user is only asked to complete 1 field: their account password. 

The idea behind this form is to ensure that the user is making a conscious decision to delete their account, thereby ruling out the possibility of the user accidentally clicking the 'delete account' button on their account. It simply acts to confirm the user's choice. 

The link to this form can be found on the User Profile, which can be accessed from the top navigational bar on the right hand side. 

#### delete_form.py
Contains the Form class 'DeleteCompanyForm()', which is used to allow the user to delete a company they've added to their company directory. 

The idea behind this form is to give the user the functionality to delete a company account if they ever need it. The form presents the user with 1 field: a drop list with 2 options: 
-   No, take me back to the company profile
-   Yes, please delete this company profile

'No, take me back to the company profile' is the default selection, so if the user doesn't make a selection on this form, no changes are made to the company account. Once again this is aimed at preventing accidental mistakes from being made by the user. This is especially important since a company account is hard deleted from the database with no ways to retrieve that company information at a later date. 

The link to this form can be found by viewing the company's 'company profile', which displays on the template 'view_company_profile.html'

#### login_form.py
Contains the Form class 'LoginForm()', which is used to display the login form that can be used (by the user) to log in their account on the application. The form simply has 2 fields: 'username' and 'password'.  

This form can be found via the 'Login' link on the top navigational bar of the application. 

#### register_form.py
Contains the Form class 'RegisterUserForm()', which is used to display an account registration form to the user. The form has the following fields: username, email_address, password, confirm_password. Each of these fields are required, so if any field is left blank, the user will be redirected to this form. 

This form can be found via the 'Register' link on the top navigational bar of the application.

#### update_company_form.py
Contains the Form class 'UpdateCompany()', but it has all fields found on the 'AddCompanyForm()'. It's important to note was this form was created before I created the 'AddCompanyForm()', when I didn't yet have the 'add company' functionality. 
        
This form gets called with all the information already provided for a specific company, & serves to allow the update the details for a specific company already in the user's company directory. This form can be found by viewing a company's 'company profile'. 

#### update_interview_status_form.py
Contains the Form class 'UpdateInterviewStatusForm()', which allows the user to simply update the 'status' for a specific interview. The link to this form can be found by viewing a specific job interview. 

The reason I created this form was to give the user the option to specifically update a specific interview field, without having to focus/worry about any of the other interview-related fields, which should make updating the status really quick & easy. The form presents the user with 1 field, which is a drop-down list with 4 options: Upcoming Interview, Interview Done, Interview Cancelled' & Interview has been post-poned.

#### update_user_details.py
##### Form name: 
Contains the following 2 Form classes:

###### UpdateEmailAddressForm() 
Offers the user the option to update the email address they have saved to their user account on the application.

###### ChangePasswordForm()
Offers the user the option to update the password they have saved to their user account on the application. The user is asked to enter their account password twice to minimize the chance of the user making an accidental typing error, when entering the new password. 

The links to both these forms can be found on the 'User Profile', the link to which is found on the top navigational bar.

# ---------------------------------------------------------------
### 2: Preparation & Management:
These are the files:
#### credits_and_resources_used.md
    This is where I stored links / resources I used / found useful for this project. 

#### notes_to_self.md
    These are notes I added as I researched and tried out various aspects. Info added in this file acts as a point of reference, since I figured I'd end up using this information a few times through out the development of this application.

#### pitch#1.md
    This is the pitch and premise of this project. I put this together before I even started working on the project. 

#### plan_project.md
    This is where I did some planning & acts as a story mapping session. Sadly I didn't get to use all of my ideas for this project as I realised the scope of this project was going far beyond what was expected for this course. 

#### sqlqueries.sql
    Includes all the queries I used when interacting with SQLite3 throughout the development of the application.

#### todo_list.md
    In the first few weeks of developing this application, I realised I was going all over the place and losing track of what I was working on & what needed to still get done. So I broke down what needed to get done for the project as big chunks, and then focused on 1 chunk at a time. When working on a chunk, I'd break it down into smaller/more detailed points. This allowed me to control what I focused on and I could keep track of what I'd already completed.

    I ended up using Trello, for this functionality, towards the end of the development process. I always had a notepad on me throughout the development process, and when I came up with new ideas/concepts that needed to get done, I added them to Trello. This allowed me to keep on track & focused, without losing those interesting ideas that come to mind while working. 

# ---------------------------------------------------------------
### 3: Repo:
Each file in the Repo directory interacts with a specific table in the SQL database & includes the following types of SQL queries:
-   Insert
-   Select
-   Update
-   Delete

The methods in each of these files are used / called on by the functions within the Services directory.

#### __init__.py

#### application_notes.py:
This is a repository file which relates specifically to Application notes & includes the following 2 classes: ApplicationNotes & ApplicationNotesRepository. The ApplicationNotesRepository includes all the SQL queries which connect to the 'application_notes' table in the SQL database 'jhmanager.db'.

#### applications_history.py:
This is a repository file which relates specifically to Job Applications & includes the following 2 classes: Application & ApplicationsHistoryRepository. The ApplicationsHistoryRepository includes all the SQL queries which connect to the 'job_applications' table in the SQL database 'jhmanager.db'.

#### company_notes.py:
This is a repository file which relates specifically to a Company Note & includes the following 2 classes: CompanyNotes & CompanyNotesRepository. Company Notes are notes that link directly to a specific Company. The CompanyNotesRepository includes all the SQL queries which connect to the 'company_notes' table in the SQL database 'jhmanager.db'.

#### company.py:
This is a repository file which relates specifically to a Company & includes the following 2 classes: Company & CompanyRepository. The CompanyRepository includes all the SQL queries which connect to the 'company' table in the SQL database 'jhmanager.db'.

#### contacts.py:
This is a repository file which relates specifically to a Contact & includes the following 2 classes: Contact & ContactRepository. The ContactRepository includes all the SQL queries which connect to the 'indiv_contacts' table in the SQL database 'jhmanager.db'.

The difference between the 'ContactRepository' & the 'CompanyRepository':
-   'ContactRepository' 
    -   connects to the 'indiv_contacts' SQL table, 
    -   Relates to data specific to people / individuals, 
-   'CompanyRepository' 
    -   connects to the 'company' SQL table
    -   Relates to data specific to a corporate/business.

#### interview_prep_history.py:
This is a repository file which relates specifically to Interview Preparation & includes the following 2 classes: InterviewPreparation & InterviewPreparationRepository. The InterviewPreparationRepository includes all the SQL queries which connect to the 'interview_preparation' table in the SQL database 'jhmanager.db'.

#### interviewsHistory.py:
##### SQL Table:
    interviews
##### Classes:
    Interview, InterviewsHistoryRepository

#### job_offers_history.py:
##### SQL Table:
    job_offers
##### Classes:
    JobOffer, JobOffersRepository

#### users.py
##### SQL Table:
    users
##### Classes:
    User, UserRepository

# ---------------------------------------------------------------
### 4: Service:
This includes all the Python functionality to build the 'back-end' of the application. 
These files are broken down into the 11 directories that cover specific sections / functionality of the application. 

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

#### address_book:
This manages the functionality for the address book template. 

##### view_address_book.py
###### display_address_book():
    Calls on both the 'Company' and 'indiv_contacts' tables & grabs the top 8 entries from each table. 
    Linked to Template: 'view_address_book.html'

#### application_notes:
This where you'll find all the Python files related to Application Notes.

###### add_app_note.py:
    Functions:
    -   display_application_note_form()
        -   Stores the company_name & action_url to be displayed to the user.
        -   Renders the template:  add_application_note.html
            -   with a blank instance of the AddApplicationNoteForm() Form. 
    -   post_application_add_note()
        -   Grabs the values added to the form fields & the current date
        -   Calls on the insertNewNote() function to insert these values, 
            as a single entry, into the SQL table 'application_notes'. 

###### delete_app_note.py:
    Function:
    -   delete_application_note()
        -   Deletes a specific application note from the 'application_notes' table in
            the SQL database, using the note's specific ID. 
        -   Redirects the user to template: 'view_notes_for_application.html'

###### update_app_note.py:
    Functions:
    -   display_update_app_note_form()
        -   Stores the company_name & action_url to be displayed to the user.
        -   Renders the template:  update_application_note.html
            -   with an instance of the AddApplicationNoteForm() Form, populated with the values for a specific application note entry. 

    -   post_update_app_note():
        1)  Grabs the values added to the form fields
        2)  Calls on the updateByID() function to update these values for a specific entry in the SQL table 'application_notes'. 
        3)  Redirects the user to template: 'view_app_note_details.html'

###### view_app_note_details.py:
    Functions:
    -   display_application_note_details()
        -   Grabs all the values / attributes for a specific application note entry
        -   Grabs the values needed for URL links to be presented to the user
        -   Values are 'cleaned' using functions from the 'clean_files' directory.
            -   To improve the presention of the values
            -   To implement consistency of string formats across all templates. 
        -   Renders the Template: 'view_app_note_details.html'

###### view_application_notes.py:
    Function:
    -   display_application_notes():
        -   Grabs all entries from the appNotesRepo for a specific user. 
        -   Grabs & stores all information to be displayed to the user, including URL links
        -   Renders the template: 'view_notes_for_application.html'


#### applications:
This where you'll find all the Python files related to job applications. 

##### add_application.py:
In this file we find the functionality to:
-   display the form to the user, 
-   extract the form field values
-   Insert these values into the relevant SQL table
-   Redirect the user to the template: 'view_application.html'

Functions:
-   display_add_application_form():
    -   Handles GET functionality
        -   with a blank instance of the AddApplicationForm() Form. 
    -   Renders Template: 'add_job_application.html'

-   add_new_application_to_application_history():
    -   Grabs the 'date' and 'time' form values & converts the values to the string type
    -   Grabs all the value arguments it receives & stores them in a single dictionary
    -   Inserts the values into the 'job_applications' table.

-   add_or_update_company():
    -   Determines if a company already exists in the 'company' table
        -   If yes: It updates the existing entry for this company
        -   Else: It inserts a new entry for this company. 

-   post_add_application():
    -   Handles POST functionality
    -   Calls on the add_or_update_company() function
    -   Calls on the add_new_application_to_application_history() function
    -   Redirects to the template: 'view_application.html'

##### delete_all_applications.py:
In this file we find the functionality to:
-   Delete all job application, and all interview, interview_preparation, note, & job offer entries linked to these applications, from their perspective SQL tables. 
-   Redirect the user back to the 'dashboard.html' template.

Function:
-   delete_all_applications_for_user()
    -   Deletes all application entries linked to the current user's user_id.
        -   These application entries are deleted from the 'job_applications' table
    -   This also deletes the following entries linked to this UserID:
        -   interviews (Table: interviews)
        -   interview preparations (Table: interview_preparation)
        -   application notes (Table: application_notes)
        -   job offers (Table: job_offers)
    -   Redirects to template: 'dashboard.html'

##### delete_an_application.py:
In this file we find the functionality to:
-   Delete both a specific job application, and all interview, interview_preparation, note, & job offer entries linked to this application, from their perspective SQL tables. 
-   Redirect the user back to the 'applications.html' template.

Function:
-   delete_application()
    -   Deletes a specific entry in the 'job_applications' table. 
    -   Deletes all entries linked to a specific application ID:
        -   interviews (Table: interviews)
        -   interview preparations (Table: interview_preparation)
        -   application notes (Table: application_notes)
        -   job offers (Table: job_offers)
    -   Redirects to template: 'applications.html'    

##### update_application.py:
In this file we find the functionality to:
-   Display the AddApplicationForm(), with the details of a specific application, to the user via the template 'update_application.html'
-   Grab the details from the form, update the relevant entry in the 'job_applications'
    table, and then redirect the user to 'view_application.html' so that the user can view the application they've just updated. 

Functions:
-   display_update_application_form()
    -   Handles GET functionality
    -   Stores the company_name & action_url to be displayed to the user.
    -   Renders the template:  update_application.html
        -   With an instance of the AddApplicationForm() Form, 
            populated with the values for a specific application entry.

-   post_update_application()
    -   Handles POST functionality
    -   Gets all the form values & stores them in a single dictionary
    -   Calls on the updateApplicationByID() method, in the 'ApplicationsHistoryRepository', to update a specific entry in the 'job_applications' (SQL) table.
    -   Gets all form values relevant to a Company & stores them in their own dictionary
    -   Using the 'Company' values, it calls on the updateUsingApplicationDetails(), in the CompanyRepository(), 
        to update a specific entry in the 'job_applications' (SQL) table.
    -   Redirects to the template: 'view_application.html'

##### view_all_applications.py:
In this file we find the functionality to:
-   Grab the top 10 application entries (if there are any), 
    and to add these entries to a dictionary (together with a few other necessary details). These details are displayed to the user on the template 'applications.html'. 

Function:
-   display_all_applications_current_user()
    -   Grabs the top 10 Application entries for a specific User
        -   From the 'job_applications' SQL table
    -   Creates a Dictionary
        -   With a key: 'empty_table' & value: True
    -   Determines if there are any applications in the SQL table for the User
        -   If yes: 
            -   It structures the values for each application in a dictionary
            -   Cleans up the values
            -   Updates the value for the 'empty_table' key to False
    -   Adds the links, to be displayed to the user, in the main dictionary.
    -   Renders the template: 'applications.html'

##### view_application_details.py:
In this file we find the functionality to:
-   Grab the entry details for a specific application 
-   Grab the entry details for the company linked to this application
-   Grab all Job offers linked to this Job Application
-   Grab all interviews linked to this Job Application
-   Store the links to be presented to the user
-   Store these details to a dictionary (together with a few other necessary details)
    in a dictionary. 
-   Display all this information to the user on the template 'view_application.html'

Functions:
-   grab_and_display_job_offers()
        Extracts the job offer entries from the 'job_offers' SQL table & adds the information to a dictionary
-   grab_and_display_interviews()
        Extracts the interview entries from the 'interviews' SQL table & adds the information to a dictionary
-   display_application_details()
    -   Extracts the job application entries from the 'job_applications' SQL table & adds the information to a dictionary
    -   Renders the "view_application.html" template, with the above 3 dictionaries. 


#### cleanup_files:
In this file we find the functionality to clean up values in the various functions in the 'service' directory. So once a value has been extracted from the relevant SQL table, it will be "cleaned" to ensure it looks both presentable and just more like every day language. 
EG: random_value => Random Value. 

The files in this directory:
##### cleanup_app_fields.py
Responsible for cleaning up all fields to related to the 'job_applications' SQL table. 

###### Functions:
-   cleanup_emp_type_field()
    -   Responsible for "cleaning up" how the 'employment_type' value is presented
-   cleanup_interview_stage()
    -   Responsible for "cleaning up" how the 'interview_stage' value is presented
-   cleanup_urls()
    -   Responsible for verifying a URL, provided by the user, to see if it's left blank or incomplete. If so, its value is replaced with 'None'. 
-   cleanup_specific_job_application()
    -   Responsible for "cleaning up" how the values for a specific 'job_application' entry is presented.
-   cleanup_application_fields()
    -   Responsible for "cleaning up" how the values, for each entry in a SQL query, are presented. It's related specifically to the 'job_applications' table. 

##### cleanup_app_note_fields.py
Responsible for cleaning up all fields to related to the 'application_notes' SQL table. 

###### Functions:
-   cleanup_app_notes()
    -   Responsible for cleaning up the presentation of a specific application note's 'date' value. 

##### cleanup_company_fields.py
Responsible for cleaning up all fields to related to the 'company' SQL table.

###### Functions:
-   cleanup_company_website()
    -   Takes a company URL that the user has provided and checks to see if its blank (which saves as "N/A") or incomplete ("Http://" or "https://"). If the value is classified as invalid, the function returns None. 

-   check_if_all_company_fields_empty()
    -   Runs through the field values stored for a company, and if all the values are empty (saved as "N/A"), then the function returns True.
    -   I created this function for the 'cleanup_company_profile()' function, which is in turn called on by the 'display_company_profile()' function in services/company/view_company_profile.py

-   cleanup_company_profile()
    -   This functions cleans the field values stored for a company, to improve how these values are presented to the user. If a field value is stored as "N/A", "Unknown at present" or if its entirely empty (""), then it's value is replaced with "None". 
    -   This allows me to only present information that that the user would actually want to see. If a field was left blank, then there's no point in displaying "N/A" or "" to the user.
    -   This function is used exclusively by the 'display_company_profile()' function in services/company/view_company_profile.py 

-   cleanup_specific_company()
    -   This function runs through all the field values for a specific company entry. For each entry, it checks if the field value is "N/A", "Unknown at present" or simply blank. 
        -   If so, it replaces those values with "None".
        -   Otherwise it "cleans" the value using the 'cleanup_field_value()' functionality. 

-   cleanup_company_fields()
    -   This works pretty much in the same way as cleanup_specific_company() except it's specifically used when iterating through several company entries. The dictionary format it receives will therefore have  a slightly different structure and use a "company_id" key to distinguish one company entry from the other entries in the dictionary. 
    -   This function also cleans a company's "view_company" field value (company website URL). 


##### cleanup_contact.py
Responsible for cleaning up all fields to related to the 'indiv_contacts' SQL table.

###### Functions:
-   cleanup_full_name()
    -   Specifically focuses on "cleaning" a "full_name" field. 
    -   Takes a long string, splits the string by its spaces, capitalises the first letter, and then joins everything together back together, seperated by spaces, before returning the final string. 

-   cleanup_specific_contact_entry()
    -   Responsible for dealing with a specific contact. 
    -   Takes a 'contact' dictionary & cleans up the values for each of the dictionary's keys (contact attributes)
    -   Calls on the functions cleanup_full_name() & cleanup_field_value to improve the presentation of the 'contact' attributes / keys. 

-   cleanup_each_contact_entry()
    -   Takes a 'contact' dictionary and is responsible for dealing with a 'contact' entry within a bigger dictionary of contacts. 
    -   Otherwise it works pretty much the same as cleanup_specific_contact_entry(), cleaning each value for a contact to improve it's presentation before a contact is displayed to the user. 


##### cleanup_datetime_display.py
Responsible for cleaning up all datetime, date & time type fields across all the files in the Service directory.

###### Functions:
-   cleanup_date_format()
    -   Takes a date object and restructures how the date object will be dsiplayed to the user (as a string)
    -   EG: "02-01-2021" / "%Y-%m-%d" -> "02 Jan 2021".
    -   One instance: services/application_notes/view_app_note_details.py, Line 30

-   cleanup_time_format()
    -   Takes a time object and determines if the time is before or after 12pm. It will then convert the date value back to string and add "am" or "pm" at the end, based on whether/not it's morning or afternoon/evening, before returning the final string. 
    -   EG: 
        -   "11:35" / "%H:%M" -> "11:35am".
        -   "15:09" / "%H:%M" -> "15:09pm". 
    -   One instance: services/cleanup_files/cleanup_app_fields.py, Line 54

-   verify_value_is_date_obj()
    -   Takes a 'date' value, and checks to see if the data type for this value value is the 'str' type. 
        ->  If yes, it will converts the 'date' value to its 'datetime.date' eqivalent & returns the result
        ->  Else: The 'date' value remains unchanged and is returned. 
    -   I created this function to ensure that the 'date' value provided when calling the 'past_dated()' function is in fact a 'datetime.date' data type. 
    -   Used by / called by the 'past_dated() function. 

-   verify_value_is_time_obj()
    -   Takes a 'time' value and checks to see if the data type for this value value is the 'str' type, pretty much the same as the 'verify_value_is_date_obj()' function does. 
    -   Like the 'verify_value_is_date_obj()' function, if the value is a 'str' value, this functions converts the value to a 'datetime.time' data type. 
    -   Used by / called by the 'past_dated() function. 

-   past_dated()
    -   Takes 2 arguments: a datetime.date and a datetime.time calues. 
    -   It compares these 2 values to the current date & time to establish if the provided date & time are past-dated / in the past.  
        -   If yes: It returns True
        -   Otherwise: False 
    -   One instance: services/display_dashboard_content.py, Line 102

-   present_dated()
    -   Takes a datetime.date-type value and compares it to the current day's date. 
        -   If the provided datetime value matches the current day's date, then it returns True
        -   Else: it returns False 
    -   One instance: services/display_dashboard_content.py, Line 66


##### cleanup_general_fields.py
Responsible for cleaning up fields that are used by multiple different functions across the Service directory, including files & functions from within the 'cleanup_files' directory.

###### Functions:
-   replace_na_value_with_none()
    -   Takes a 'str'-type value and checks if the value is "N/A". 
        -   If yes, it will return True
        -   Else: Returns False 
    -   Since I've replaced empty form values with "N/A" before storing / updating these values in the SQL database, this function replaces these values with 'None'. This serves to represent the fact that the user has not yet provided a value for that field.
    -   One instance: services/interview_preparation/view_all_interview_prep.py, Line 27

-   get_count()
    -   Takes a SQL list of entries, counts the number of entries and returns the end result/figure. 
    -   One instance: services/display_dashboard_content.py, Line 30

-   cleanup_field_value()
    -   Takes a string value, splits the string by the spaces, capitalizes the first letter of every word, and then adds  a space before joining everything back to together as a new string. 
    -   One instance: services/cleanup_files/acleanup_contact_fields.py, Line 16

##### cleanup_interview_fields.py
Responsible for cleaning up all fields to related to the 'interviews' SQL table.

###### Functions:
-   cleanup_interview_type()
    -   Takes a string value, specifically for the 'interview_type' field. 
    -   This function runs through the possible values for this field, since it as provided to the user as a Select list, and improves the presentation of the value. Once complete, it returns the updated value.
    -   This is used by the 'cleanup_interview_fields()' function from within the same file: 'cleanup_interview_fields.py'

-   cleanup_interview_status()
    -   Takes a string value, specifically for the interview 'status' field. 
    -   This function runs through the possible values for this field, since it as provided to the user as a Select list, and improves the presentation of the value. Once complete, it returns the updated value.
    -   This is used by the 'cleanup_interview_fields()' function from within the same file: 'cleanup_interview_fields.py'

-   cleanup_medium()
    -   Takes a string value, specifically for the 'interview_medium' field. 
    -   This function runs through the possible values for this field, since it as provided to the user as a Select list, and improves the presentation of the value. Once complete, it returns the updated value.
    -   This is used by the 'cleanup_interview_fields()' function from within the same file: 'cleanup_interview_fields.py'  

-   cleanup_interview_fields()
    -   Takes a dictionary of interview entries and a specific interview ID. 
    -   It cleans up all the values for a specific interview, using its unique interview ID, to improve how each value will be presented to the user (so it's in plain everyday language).
    -   One instance: services/applications/view_application_details.py, Line 85

-   cleanup_specific_interview()
    -   Takes a dictionary for a specific interview entry, with the interview attributes as its keys. 
    -   It cleans up the interview values to improve how each value will be presented to the user (so it's in plain everyday language).
    -   One instance: services/interviews/view_interview_details.py, Line 31


##### cleanup_job_offer_fields.py
Responsible for cleaning up all fields to related to the 'job_offers' SQL table.

#### company:
This where you'll find all the Python files related to a 'company'. 

The files in this directory:
##### add_company.py
Handles the functionality behind adding a company contact, and handles everything from presenting the form to processing the information that the user provides & storing that data as a single entry in the 'company' SQL table. 

###### Functions:
-   display_add_company_form()
    -   This function takes a blank instance of the 'add_company_form'. 
    -   It stores some data that is presented to the user, including the URL that gets actioned to present the form to the user in the form of a dictionary. 
    -   It renders the form to the template "add_company_form.html" together with the content from the dictionary.

-   post_add_company()
    -   Extracts the information received in each field of the 'add_company_form'.
    -   It checks the company name the user provides & runs a check against the current entries in the 'company' SQL table.
        -   If it finds another entry that's very similar, it redirects the user back to the form, with the flashed message notifying the user that they've already saved a company with a similar name.
    -   Otherwise, it grabs all the values provided for this specific company & stores it in a dictionary before inserting the entry into the SQL database before returning the unique ID for the newly-created entry.
        -> This calls on the 'createCompany' method within the 'companyRepo' & connects to the 'company' table. 
    -   Finally the user is redirectly to the route: '/company/{}/view_company', which renders to the 'view_company_profile.html' template. 

##### add_company_job_application.py
Handles the functionality behind adding a job application for a specific company. This covers everything from presenting the form to processing the information that the user provides & storing that data as a single entry in the 'job_applications' SQL table. 

###### Functions:
-   display_add_company_application_form()
    -   Takes a few arguments: 
        -   'add_application_form', which is a blank instance of the 'AddCompanyJobApplicationForm()' Form. 
        -   company_id
            ->  The unique ID for a specific company. 
        -   companyRepo 
    -   It puts together a dictionary consisting of the company name for a specific company (to which this application entry will link to) & the URL to be actioned (the very same route used display a job application form to the user). 
    -   It renders the template 'add_company_job_application.html' with the details from the 'add_application_form' form & the dictionary. 

-   add_new_application_to_application_history()
    -   Deals specifically with:
        -   Extracting data (input from the user) from the form
        -   Converting the interview 'date' and 'time' values to the 'str' data-type
        -   Storing all the required data into a single dictionary
        -   Checking all the 'job_application' attributes / keys for blank values & replacing these values with "N/A". 
            ->  This is because most of the columns in the 'job_applications' table do not accept 'NULL' (blank) values.
        -   Inserting these values into the 'job_applications' SQL table & returning the unique ID for the newly-created entry. 

-   post_add_company_job_application()
    -   Calls on the 'add_new_application_to_application_history()' function & redirects the user to the 'view_application.html' template for the newly created job application entry. 


##### update_company.py
Handles the functionality behind updating an existing company. This covers everything from displaying the form (to the user) to updating the values for this company in the 'company' SQL table.

###### Functions:
-   display_update_company_profile_form()
    -   Takes (as one of its arguemnts):  a blank instance of the 'UpdateCompany' Form.  
    -   Grabs the company name for a specific company & the action URL for this company (it's routing location) & stores it in a 'details' dictionary. 
    -   Renders the template "update_company_profile.html" with the 'UpdateCompany' Form and the values in the 'details' dictionary. 

-   post_update_company_profile()
    -   Grabs all the values from the 'UpdateCompany' Form, submitted by the user, & stores these values in a dictionary
    -   Calls on the 'updateByID' method, in the companyRepo, to update this entry in the 'company' SQL table. 
    -   Redirects the user back to the 'view_company_profile.html' template for this specific company. 

##### delete_company.py
Handles the functionality behind deleting a specific 'company'. 

###### Functions:
-   display_delete_company_form()
    -   Handles the functionality behind presenting a form to the user, asking them to confirm if they want to proceed with deleting a specific company. 
    -   Includes a dictionary with: 
        -   The company name
            ->  for the company the user wants to delete)
        -   The action_url 
            ->  the route which connects this form with the POST functionality for this delete request. 
    -   includes a list of choices the user will have to choose from on the form. These choices are then dynamically updated as the values for the 'confirm_choice' field which will be displayed on the form. 
        ->  This functionality allowed me to play around with the idea of providing a form dynamic values, which are added to a specific instantiation of a form. 
    -   Renders the 'delete_company_form' to the "delete_company_profile.html" template, together with the values from the dictionary. 

-   delete_company_from_db()
    -   Verifies which option the user selected from the 'confirm_choice' field. 
        -   If the user selects option 1:   
            -   The company entry remains untouched. 

        -   If the user selects option 0:
            -   The company entry is deleted from the 'company' SQL table, 
            -   All entries from all the other SQL tables, which  are linked to this company entry (identified by its unique company_id), are also deleted.

    -   The user is redirected back to the 'view_addressbook.html' template   


##### view_all_companies.py
Handles the functionality behind displaying all the companies that the user has already added/created so far, with each company being a link to the 'view_company_profile.html' template for the selected company. 

###### Functions:
-   display_all_companies_for_user()
    -   Grabs all existing company entries in the 'company' SQL table (if there are any)
    -   Iterates through every entry in the SQL query and adds each company to a 'company_contacts' dictionary, calling on the cleanup_company_fields() function to 'clean' a company entry's values/attributes for presentation. 
    -   Renders the template "view_company_directory.html" with access to the information in the 'company_contacts' dictionary. 

##### view_company_profile.py
Handles the functionality behind displaying the details for a specific company, using its unique 'company_id'. It also offers to links to: 
-   Add a job application
-   View the company website 
-   Add a note for this specific company
-   View all notes for this specific company 

###### Functions:
-   display_company_profile():
    -   Calls on the method 'getCompanyById' (from the companyRepo) to get a specific entry from the 'company' SQL table. 
    -   All information for the company is extracted from this sql query and stored in a dictionary: company_details. 
    -   This information is then 'cleaned' using the 'cleanup_company_profile()' function found in the file: services/clean_files/cleanup_company_fields.py. 
    -   Its grabs & stores all the routes (required for the links to be presented to the user) in a 'general_details' dictionary. 
    -   Renders this dictionary together with the template: "view_company_profile.html" 


#### company_notes:
This where you'll find all the Python files related to a company note / list of company notes. 

Files in this directory:
##### add_company_note.py
Handles the functionality behind displaying the 'AddCompanyNoteForm' form to the user & saving the information (the user has provided/entered into the form) into the 'company_notes' SQL table. 

###### Functions:
-   display_add_company_note_form()
    -   Responsible for displaying the 'AddCompanyNoteForm' form to the user, together with all information needed to be displayed to the user. 
    -   
-   post_add_company_note()
    -  Extracts the values from the 'AddCompanyNoteForm' form, saving it into a dictionary ('fields')
    -   Calls on the method 'insertNewNotes' (from the 'companyNotesRepo' repo. ) to insert these values into the 'company_notes' SQL table. 
    -   This SQL query returns the unique ID ('company_note_id') for this newly-created entry, which is then used to redirect the user to the template 'view_specific_company_note.html'. 

##### delete_company_note.py


##### update_company_note.py

##### view_all_company_notes.py

##### view_specific_note.py

#### contacts_directory:
This where you'll find all the Python files related to a contact / list of contacts . 

#### interview_preparation:
This where you'll find all the Python files related to an interview preparation entry / list of interview preparation entries. 

#### interviews:
This where you'll find all the Python files related to an interview entry / list of interview entries. 

#### job_offers:
This where you'll find all the Python files related to a job offer entry / list of job offer entries. 


#### users:
This where you'll find all the Python files related to a user  entry / list of user entries. 

# ---------------------------------------------------------------
### 5: Static:



# ---------------------------------------------------------------
### 6: Pages / Templates:
These templates can be divided into the following categories:
-   General
-   Users
-   Applications
-   Interviews
-   Interview Preparation
-   Job offers
-   Address Book
    -   Contacts Directory
    -   Company Directory
-   Notes
    -   Company Notes
    -   Application Notes

#### General:

##### layout.html: 
The general layout for all html templates, which is referenced to by all the remaining html templates. This template also includes the:
-   Meta data
-   links (favicons, styles, bootstrap & stylesheets)
-   Scripts (JQuery)
-   Page structure (header, body & footer)
-   Nav Bar links 

##### about_us.html:
This page tells/informs the user:
-   what this application is about, 
-   why I developed this application, 
-   the research I carried out before putting this application together,
-   security, & 
-   how they could contact me if they want to. 

##### dashboard.html
This page is the landing page for a user once they've logged in. The page contains the following: 
-   Upcoming interviews
-   Interviews the user has today
-   Applications submitted today
-   Job offers received
-   Progress stats:
    -   This shows the user how many applications, interviews and job offers they've submitted up til this point. 

##### view_all_user_notes.html:
This page displays all the notes the user has added and is split up into 2 sections: 
1) notes added to applications
2) notes added to company profiles

A link to this page is found on the Nav bar as "Notes", but only when the user is logged in. 

#### Users:
This includes all the templates related to a user's account.

##### register.html (WTForm):
Presents the user with a blank instance of the 'RegisterUserForm()' to create a Job Hunt Manager account.

The form provides the user with fields to provide their email address, a username of their choice, their password of choice & to confirm their password of choice. The page also includes a warning to potential users that the password they provided will be hashed but there is no password salting, with the recommendation to rather use fictional information - since this application is intentioned to only be used for testing purposes (for now). I want to continue looking around for a good salting algorithm, with the intention of both hashing & salting passwords - primarily because I value the importance of security & information protection. 

The link to this form is added to the Nav bar, for any user that has not successfully logged in (yet). Once this form has been successfully submitted & processed, the user will be redirected to 'dashboard.html'.Going forward the user will only see details related to their specific account (until the user logs out).

##### login.html (WTForm): 
Presents the user with a blank instance of the LoginForm() form. The link to this page is found on the Nav bar at the top of the page, for any user that has not successfully logged in (yet).

On this form, the user is presented with the fields: Username & password. The 'Username' field will also accept the user's email address if the user prefers to rather use their email address. Once this form has been successfully submitted & processed, the user will be redirected to 'dashboard.html'. Going forward the user will only see details related to their specific account (until the user logs out).

##### userprofile.html:
Presents the user's username & password. User has the option to:
-   Update their email
    -   Directs the user to the update_email.html page
-   Update / Change their password
    -   Directs the user to the change_password.html page
-   Delete their account 
    -   Directs the user to the delete_account.html page. 

##### update_email.html (WTForm):
Presents the user with a blank instance of the 'UpdateEmailAddressForm()', which allows the user to update the email address linked to their account. The user is also asked to 'confirm' their email address, just to iron out potential human typing errors. 

This form is accessible from the 'userprofile.html' page, to the right of the email address listed under their user profile. Once this form has been successfully submitted & processed, the user will be redirected to 'userprofile.html', with their email address updated.

##### change_password.html (WTForm): 
Presents the user with a blank instance of the ChangePasswordForm() form. The link to this page is found on the 'userprofile.html' page.

This form allows the user to change their account password & has only 2 fields: password & confirm password. If the user uses the same password in both fields and the password meets the minimal requirements, the user will be redirected back to 'userprofile.html'. 

##### delete_account.html (WTForm): 
Presents the user with a blank instance of the 'DeleteAccountForm()'. This form presents the user with:
-   A warning message asking the user to confirm if they want to delete their account.
-   A 'password' field (where the user provides the current password for their Job Hunt Manager account) 
-   'confirm password' field -> where the user enters the same account password a second time.

If the password is correct, the user's account is successfully hard deleted and the user is redirected back to the 'index.html' page. Otherwise the user is redirected to the same 'DeleteAccountForm()' & an error message to "Complete all fields".

#### Applications:
All pages / templates relevant to a job application.

##### add_job_application.html (WTForm):
Presents the user with a blank instance of the 'AddApplicationForm()'. The form allows the user to add a job application, with all the details of a regular job application.

The link to this page is found on the 'dashboard.html' & 'applications.html' pages. Once this form has been successfully submitted & processed, the user will be redirected to 'view_application.html'.

##### applications.html:
Displays all the applications that this specific user has added. Each application is a link to 'view_application.html' where the user can view the specific details of the selected application. 

##### update_application.html (WTForm): 
Presents the user with the AddApplicationForm() but pre-filled with the entry details for a specific application. This allows the user to update fields or to add values to fields that that they may have previously left blank - especially since not all job specs provide all the information up front. 

The link to this page can be found on the 'view_application.html' page. Once this form has been successfully submitted & processed, the user will be redirected to 'view_application.html'.

##### view_application.html:
Presents the user with:
- The details of a specific job application
- links to:
    -   Update the application details
    -   Delete the application
    -   View the job posting (if provided by the user when completing the 'AddApplicationForm()')
    -   View the company profile 
        -> Redirects the user to the company profile for the company, the user has applied to, for this specific job application.

-   Job offers: 
    - will display any/all job offers the user has received from this specific company after submitting this application. Each Job offer card will be a link to view the details for that specific job offer. 

-   Interviews: 
    - will display any/all interviews the user has received from this specific company after submitting this application. Each interview card will be a link to view the details for that specific interview. 

-   Notes: 
    - User can either add a new note for this application
    - OR the user can view the notes they've already added for this application.

#### Interviews:
All templates relevant to job interviews. 

##### add_interview.html (WTForm):
Presents the user with a blank instance of the 'AddInterviewForm()'. 

This form allows the user to add the details for an upcoming interview, with its date, time & the medium for the interview (video/phone call) or (if in person) the contact details & location for the interview. 

This interview will be linked to a specific application & the link to this form is added to the 'view_application.html' page. Once this form has been successfully submitted and processed, the user will be redirected to 'view_interview_details.html' for this newly-created entry. 

##### view_all_interviews:
Displays all the interviews the user has received for a specific job application. Each interview is a link to 'view_interview_details.html'. The link to this page is found on 'view_application.html'. 

##### view_interview_details.html:
Displays:
- The interview details provided (by the user) for a specific interview
- Links to:
    - 'Update' the interview stage for this interview
        - Directs the user to the 'update_interview_status.html' page. 
    - 'Update' the interview 
        - Designed to let the user update any/all fields for a specific interview
        - Directs the user to 'update_interview.html' page. 
    - 'Delete' the interview
        - This hard deletes the interview and then redirects the user to 'view_application.html' page.
    - 'View Company website':
        - Displayed if the user has provided a URL to the company they've applied to.
        - Redirects the user to the company website. 
    - Preparation
        - 'Prepare':
            - Displayed if the interview status (for this interview) is "Upcoming"
            - Directs the user to 'interview_prep.html' page. 
        - 'View All Interview Preparation
            - Directs the user to 'view_all_interview_prep.html'. 
    - Application
        - Directs the user to 'view_application.html' for the application linked to this interview
    - Company 
        - Directs the user to 'view_company_profile.html' for the company linked to this interview
    - Notes
        - 'Add new note':
            -   Directs to 'add_application_note.html'
        - 'View Application Notes' 
            -   Directs to 'view_notes_for_application.html'
        - 'View Notes for (company name)' 
            -   Directs to 'view_company_notes.html'

This page offers the user the option to update/delete a specific interview, prepare for the interview, or add notes. I figured it would be useful to have the application and company profile easily accessible so that the user has all aspects related to this interview in 1 place. The user could keep this page open when preparing for the interview or when they're just about to have the interview, since it has the video link (if relevant) / interview location / contact number for the interview itself. 

The link to this template can be found on the 'view_application.html' page / template.

##### update_interview_status.html (WTForm): 
Presents the user with a blank instance of the 'UpdateInterviewStatusForm()', which offers only 1 select field:
    - "Interview Status", with the choices:
        -   'Upcoming Interview', 
        -   'Interview Done', 
        -   'Interview Cancelled', 
        -   'Interview has been post-poned'

This form allows the user to simply update the interview status for a specific interview, without having to bother with the rest of the interview fields. 

The link to this form is found on the 'view_interview_details.html' page. Once the form has been successfully submitted and processed, the user will be redirected to 'view_interview_details.html'.

##### update_interview.html (WTForm):
Presents the user with the 'AddInterviewForm()' but pre-filled with the entry details for a specific interview. It gives the user the option to update any/all of the details for an interview. 

The link to this page is found on the 'view_interview_details.html' page. Once the form has been successfully submitted and processed, the user will be redirected to 'view_interview_details.html'. 

#### Interview Preparation:
All templates related to Interview Preparation.

##### interview_prep.html (WTForm):
Presents user with: 
- Research (where user is presented with link buttons to several well-known sources, each offering their advice/guidance on how to best answer commonly-asked interview questions).
- Background
    -> The user is presented with information provided for the company, application and interview in question

- A blank instance of the 'AddInterviewPrepForm()'. This form has 2 fields: 'Question' and 'Answer'. The idea behind this is the user provides a commonly asked question & then the user uses the 'answer' field to work out how they will/would answer this interview question.
- Existing interview prep done for this interview. So, as the user adds & submits each entry, these entries will be displayed below the form itself. Each entry is a link to the 'view_interview_prep_details.html', for that specific entry.

The link to this page is found on the 'view_interview_details.html' page, but is only displayed to the user when the status of the interview is 'upcoming'. Once the interview date & time is dated in the past, or if the user has updated the interview status to 'cancelled', 'post-poned', or 'done', then the user will no longer have the option to add new preparation for this interview. 

Once an entry is successfully submitted, the user will be redirected back to this template, but the page will be updated to display the newly-added entry below the form itself. 

##### view_interview_prep_details.html:
Displays:
-   Interview Prep details
    -   Question & Answer 
        -   Provided by the user for this specific entry.  
- Links to:
    -   'Update' 
        -   To update the details for this specific entry
        -   Will direct the user to 'update_interview_prep.html'
    -   'Delete'
        - To delete this prep entry, including the values provided for the 'Question' & 'Answer' fields. 
        - Hard deletes this specific prep entry and then redirects the user to tjhe 'interview_prep.html' template.  
    -   Interview
        -   Displays a few details of the interview to which all interview prep entries are linked. 
        -   Directs the user to the 'view_interview_details.html' template, specific for the interview linked to this prep entry. 
    -   Company
        -   Directs the user to 'view_company_profile.html' for the company linked to this interview 
    -   Application
        -   Directs the user to 'view_application.html' for the application linked to this interview
    -   'Add Interview Preparation'
        -   Directs the user to the 'interview_prep.html' template.
    -   'View all Interview Preparation'
        -   Directs the user to the 'view_all_interview_prep.html' template.

Basically this page lets the user:
-   See the details for the interview prep entry
-   Update / delete the entry
-   View the application, company profile & interview details for this entry
-   Add another entry or view all prep entries

##### update_interview_prep.html (WTForm): 
Presents the user with the same layout & form as seen on the 'interview_prep.html' template. The difference is that the form (AddInterviewPrepForm()) is populated with the values for a specific interview preparation entry. This allows the user to update the details / values they've provided for the 'Question' & 'Answer' fields.  

A link to this form is found on the 'view_interview_prep_details.html' page.

#### Job Offer:
All templates related to Job Offers.

##### add_job_offer.html (WTForm): 
Presents the user with a blank instance of the 'AddJobOffer()' Form. This form allows the user to add the details of a new job offer the user has received.  As I've linked job offers with their corresponding job application, the link to this page is found on 'view_application.html' page. Once the form has been successfully submitted and processed, the user will be redirected to 'view_job_offer.html'. 

##### view_job_offer.html:
Displays:
-   The details for a specific Job offer entry. 
-   Links to:
    -   'Update' the job offer
        -   Directs the user to 'update_job_offer.html'
    -   'Delete' the job offer
        -   Will hard delete the job offer entry entirely and then redirect the user to 'view_application.html'.
    -   Company
        -   Directs the user to 'view_company_profile.html' for the company linked to this interview 
    -   Application
        -   Directs the user to 'view_application.html' for the application linked to this interview

The link to this page can be found on the pages / templates:
-   dashboard.html
-   view_application.html 
Note:   These links will only display to the user when there is a job offer to display.

##### update_job_offer.html (WTForm):
Presents the user with the 'AddJobOffer()' but pre-filled with the entry details for a specific job offer entry. The form allows the user to update the details for an existing job offer they've received. Once the form has been successfully submitted and processed, the user will be redirected to 'view_job_offer.html'.

#### Address Book:
All templates related to the Address Book.

##### view_addressbook.html:
Displays:
-   Company contacts
    -   Where each contact entry is link to 'view_company_profile.html'
-   Individual contacts
    -   Where each contact entry is a link to 'view_contact_details.html'
-   Links to:
    -   Add 'New Company'
        -   Directs to 'add_company_form.html'
    -   'View company directory'
        -   Directs to 'view_company_directory.html'
    -   'Add New Contact'
        -   Directs to 'add_new_contact.html'
    -   'View Contacts'
        -   Directs to 'view_contacts.html'

This page is divided into 2 sections:
-   Company (Contacts) 
    - Known as the company directory
-   Individual Contacts

In each section, the user can:
-   Add a new contact, view the top contacts & view all existing contacts. 

The link to this template can be found on the navigation bar as 'Address Book'.

##### Company Contacts / Directory:
All templates relevant to all company contacts & their perspective profiles. 

###### add_company_form.html (WTForm):
Presents the user with a blank instance of the 'AddCompanyForm()'. 

The form allows the user to create the company profile for a company & based on the idea that job hunters may have a wish list of companies they may want to work for. Once submitted successfully, this will create a company 'contact', where the user can also gather research, make notes or create a job application. 

A link to this page can be found on the 'view_address_book.html' & 'view_company_directory.html' pages. Once the form has been successfully submitted and processed, the user will be redirected to the 'view_company_profile.html' for the newly-created company. 

###### view_company_directory.html:
Displays:
-   All the companies, that the user has added, in a list format. 
    -   Each entry in this list is a link to 'view_company_profile.html'. 
-   Link to add 'New Company':
    - Directs the user to 'add_company_form.html'

The link to this page / template can be found on the 'view_addressbook.html'. 

###### view_company_profile.html:
Displays: 
-   The details provided for a specific company entry. 
-   Links to:
    -   'Update' the company:
        -   Directs the user to 'update_company_profile.html'
    -   'Delete' the company:
        -   Directs the user to 'delete_company_profile.html'. 
    - 'Add Job Application for (company name)
        -   Allows the user to complete a job application form that does not include any company-related fields. The idea is that the user is adding a job application a company they've already created, so adding an application should be shorter / simpler. 
        - Directs the user to 'add_company_job_application.html'.
    -   'View Company Website' 
        -   If the user provided a URL to the company website, when creating this company profile, then this link will display for the user.
    -   Notes:
        -   'Add note for (company name)'
            -   Directs the user to 'add_company_note.html'.
        -   'View all notes for (company name)
            -   Directs the user to 'view_company_notes.html'.

Basically this page lets the user:
-   View the details for a specific company
-   Update / Delete the company profile
-   Add a job application for this specific company
-   View the website for this company
-   Add a new note, or view existing notes, for a specific company

###### add_company_job_application.html:
Presents the user with a blank instance of the 'AddCompanyJobApplicationForm()'.

This form allows the user to add a job application for a specific company. It is like the 'AddApplicationForm()' form but without the company details section, to make the application form shorter. I made this form as I believe it gives the user to add a job application for a company already in the user's company directory. Since the user has already provided details for the company, I don't believe there's any point making the user have to re-enter those details. By doing so, the form could be marginally shorter & simpler than the full 'AddApplicationForm()'. 

The link to this page can be found on the 'view_company_profile.html' page. Once the form has been successfully submitted and processed, the user will be redirected to the 'view_application.html' for the newly-created job application. 

###### update_company_profile.html (WTForm):
Presents the user with the 'AddCompanyForm()' where the fields are populated with the field values already provided for a specific company. The form allows the user to update the details for a specific Company's profile & includes details like the company name, location, industry, & company website. 

A link to this page is found on the 'view_company_profile.html' page. Once the form has been successfully submitted and processed, the user will be redirected to the 'view_company_profile.html'.

###### delete_company_profile.html (WTForm):
Presents the user with a blank instance of the 'DeleteCompanyForm()'. 
On this form, the user is presented with:
- A warning message: If the user deletes this company, it will delete all applications, interviews, interview_prep, & job offers linked to this company profile.
- A select field with 2 options: 
    -> Yes: Will delete the company profile & redirect the user to the 'view_address_book.html' page
    -> No: User will be redirected to the 'view_company_profile.html' page. 

This form basically allows the user to delete a company entirely. The link to this template can be found on 'view_company_profile.html'.

##### Individual Contacts:
All templates linked directly to individual contacts:

###### add_new_contact.html (WTForm):
Presents the user with a blank instance of the 'AddNewContactForm()'.
Allows user to add details for a particular contact, including the individual's full name, contact details & a link to their Linkedin Profile. 

This is based on the idea (and from personal experience) that job hunters will want to build a network of contacts. The user could also use this form to add recruiters & hiring managers at the company they're applying to (or want to apply to in the future). 

A link to this page can be found on the 'view_address_book.html' & 'view_contacts.html' pages. Once this form has been successfully submitted & processed, the user will be redirected to 'view_contact_details.html'.

###### view_contacts.html:
Displays:
-   All Contact entries added by this user
    -   Where each contact entry is a link to 'view_contact_details.html'
-   Link to 'Add New Contact'
    -   Directs to 'add_new_contact.html'

A link to this template can be found on 'view_address_book.html'.

###### view_contact_details.html:
Displays:
-   Details for a specific contact, including:
    -   The contact's Full name, Job title, email address, contact number,
    -   The Company name - where the contact works
    -   Linkedin profile (the link to their Linkedin profile)
-   Links to:
    -   'Update' the contact
        -   Directs to 'update_contact_form.html' 
    -   'Delete' the contact
        -   Hard deletes the contact entry and then redirects the user to 'view_addressbook.html'
    -   'View Linkedin profile'
        -   Only displays when the user provides a link to their linkedin profile
        -   Directs the user to view the contact's Linkedin profile
    -   'Go to Address Book'
        -   Redirects to 'view_addressbook.html'
    -   'Go to Contacts'
        -   Redirects to 'view_contacts.html'
    
Basically this page allows the user to:
-   See the contact details provided for a specific individual contact 
-   Update / Delete the contact entry
-   View the linkedin profile for this contact
-   Go to the address book or contacts list

The link to this page can be found on:
-   'view_addressbook.html'
    -   For every contact displayed on the addressbook
-   'view_contacts.html
    -   For every contact displayed on the addressbook

###### update_contact_form.html (WTForm):
Presents the user with the 'AddNewContactForm()' but pre-filled with the entry details for a specific individual contact entry. This form gives the user the option to update a contact entry at any point, which is useful when you get to know more about a contact over time or with extra research. 
The link to this template can be found on 'view_contact_details.html'. Once this form has been successfully submitted & processed, the user will be redirected to 'view_contact_details.html'.

#### Notes:
All templates related to notes.

##### view_all_user_notes.html:
Displays:
-   All notes added for the user currently logged in.
-   Company notes
    -   Where each entry is a link to 'view_specific_company_note.html'
-   Application Notes
    -   Where each entry is a link to 'view_app_note_details.html'
-   Links to:  
    -   'View Company Directory'
        -   Directs to 'view_company_directory.html'
    -   'View all applications'
        -   Directs to 'applications.html'

Basically this shows:
-   The company notes
-   The application notes
-   Links to view the company directory and to view all the applications.

##### Company Notes:
All templates related specifically to Company Notes, where each note is linked to a specific company.

###### add_company_note.html (WTForm):
Presents the user with a blank instance of the 'AddCompanyNoteForm()'. This form allows the user to add a note for a specific company, which can be accessed at any point from the company's profile.
A link to this page can be found on the 'view_company_profile.html' & 'view_company_notes.html' templates. Once the form has been successfully submitted and processed, the user will be redirected to the 'view_specific_company_note.html'.

###### view_specific_company_note.html:
Displays:
-   The entry details for a specific company note
-   Links to:
    -   'Update' the note
        -   Directs the user to 'update_company_note.html'
    -   'Delete' the note
        -   Hard deletes the (specific) company note & then redirects the user to 'view_company_notes.html'
    -   'Go back to Company Notes' 
        -   Directs the user to 'view_company_notes.html'
    -   'View company profile'
        -   Directs to 'view_company_profile.html'
    -   'Add New Note'
        -   Directs to 'add_company_note.html'. 

Basically this page lets the user:
-   View the details for a specific note
-   Update / Delete the note
-   Go to other pages related to this page

###### view_company_notes.html:
Displays:
-   All company note entries for a specific company & user
    -   Each entry is a link to 'view_specific_company_note.html'.
-   Links to:
    -   'Add New Note'
        -   Directs to 'add_company_note.html'. 
    -   'Return to company profile'
        -   Directs to 'view_company_profile.html'
    -   'Return to Address book'
        -   Directs to 'view_addressbook.html'

The link to this template can be found on:
-   'view_company_profile.html'
-   'view_all_user_notes.html'

###### update_company_note.html (WTForm):
Presents the user with the 'AddCompanyNoteForm()' but pre-filled with the entry details for a specific job offer entry. The form allows the user to update the details that the user has already provided for this note entry. 

A link to this page is found on the 'view_specific_company_note.html' page. Once the form has been successfully submitted and processed, the user will be redirected back to 'view_specific_company_note.html'.

##### Application Notes:
All templates related specifically to Application Notes, where each note is linked to a specific job application.

###### add_application_note.html (WTForm):
Presents the user with a blank instance of the 'AddApplicationNoteForm()'. This form allows the user to add a note for a specific application, which is useful at any stage of the job application. 

The link to this page can be found on the following templates:
-   'view_application.html'
-   'view_notes_for_application' pages. 

Once this form has been successfully submitted & processed, the user will be redirected to 'view_app_note_details.html'.

###### view_notes_for_application.html:
Displays:
-   All notes the user has added for a specific job application. 
    -   Each note entry is a link to 'view_app_note_details.html' where the user can view the specific details of the selected note. 
-   Links to:
    -   'Add new note for (company name)
        -   Directs the user to 'add_application_note.html'
    -   'Go back to application'
        -   Directs the user to 'view_application.html'
    -   'View company profile'
        -   Directs the user to 'view_company_profile.html'

Basically this lets the user:
-   View notes already added to this specific application
-   Add a new note
-   Return to the application or to view the company profile

The link to this page can be found on:
-   'view_application.html'
-   'view_interview_details.html'

###### view_app_note_details.html:
Displays:
-   The details for a specific application note:
    -   The date the user added this note, the note title & content
- links to:
    -   'Update' the note
        - Directs the user to 'update_application_note.html'
    -   'Delete' the note
        - Hard deletes the note & then redirects the user to 'view_notes_for_application.html'
    -   'Add a new note' 
        - Directs the user to 'add_application_note.html'.
    -   'Go back to application' 
        - Directs the user back to 'view_application.html'
    -   'Go back to Application Notes'
        - Directs the user back to 'view_notes_for_application.html'
    -   'View Company Profile'
        - Directs the user to 'view_company_profile.html'

###### update_application_note.html (WTForm):
Presents the user with the 'AddApplicationNoteForm()' but pre-filled with the entry details for a specific note. Since the link to 'update_application_note' is added to a specific note's 'view_app_note_details.html' page, it will only update the details of this specific note. 

The note is designed to let the user update their existing notes; to fix minor mistakes or to add more content to a note. Once this form has been successfully submitted & processed, the user will be redirected to 'view_app_note_details.html'.

# ---------------------------------------------------------------
### 7: Tests: 
### 8: __init__.py:
### 8: helpers_from_cs50_finance.py
### 9: jhmanager.db
### 10: schema.sql
### 11: Makefiles
### 12: requirements.txt
### 13: setup.py
### 14: wsgi.py