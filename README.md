
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

-   This Readme simply describes what each function & file does/serves, so I'll give a brief TLDR for each file/function. I'll go into more technical depth in the relevant files found within the technical_readme_files (jhmanager/technical_readme_files). 
    -   Read line 761 (below) for more information.

## Files:
The files in this project are divided into the following sections:
-   Forms
-   Preparation & Management
-   Repo
-   Service
-   Static
-   Technical Readme files
-   Pages / Templates
-   Tests
-   __init__
-   helpers_from_cs50_finance
-   jhmanager.db
-   schema.sql
-   Makefiles
-   requirements.txt
-   setup.py
-   wsgi.py

### 1: Forms:
Each of the below forms request specific information from the user and link to a specific SQL database table. 

Note: The technical readme covering the Forms is covered in jhmanager/technical_readme_files/forms.md.

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

---------------------------------------------------------------
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

---------------------------------------------------------------
### 3: Repo:
Each file in the Repo directory interacts with a specific table in the SQL database & includes the following types of SQL queries:
-   Insert
-   Select
-   Update
-   Delete

Note: The technical readme covering the Repo is covered in jhmanager/technical_readme_files/templates.md.

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

#### database.py
This is a repository file which connects to the SQL database 'jhmanager.db' & includes two classes: Database & SqlDatabase. 
-   The Database class doesn't relate a specific database table, but rather it sets the rules for how the SqlDatabase() should interact with the database. 
-   SqlDatabase includes methods which can be called on by any of the repositories, when connecting to the SQL database.

#### interview_prep_history.py:
This is a repository file which relates specifically to Interview Preparation & includes the following 2 classes: InterviewPreparation & InterviewPreparationRepository. The InterviewPreparationRepository includes all the SQL queries which connect to the 'interview_preparation' table in the SQL database 'jhmanager.db'.

#### interviewsHistory.py:
This is a repository file which relates specifically to (job) Interviews & includes the following 2 classes: Interview & InterviewsHistoryRepository. The InterviewsHistoryRepository includes all the SQL queries which connect to the 'interviews' table in the SQL database 'jhmanager.db'.

#### job_offers_history.py:
This is a repository file which relates specifically to a (job) Job Offer & includes the following 2 classes: JobOffer & JobOffersRepository. The JobOffersRepository includes all the SQL queries which connect to the 'job_offers' table in the SQL database 'jhmanager.db'.

#### users.py
This is a repository file which relates specifically to a User (of the application) & includes the following 2 classes: User & UserRepository. The UserRepository includes all the SQL queries which connect to the 'users' table in the SQL database 'jhmanager.db'.

### 4: Service:
This includes all the Python functionality to build the 'back-end' of the application. 
These files are broken down into the 11 directories that cover specific sections / functionality of the application. 

Note: The technical readme covering the Forms is covered in jhmanager/technical_readme_files/services.md.

The directories found in the Services directory:
-   address_book
-   application_notes

#### address_book:
This includes the functionality behind displaying the user's contacts to the template: 'view_address_book.html'.

##### view_address_book.py
Gets the top individual & company contacts that the user has added & renders these contacts (& all the relevant links) to the 'view_address_book.html' template. Each of these contacts is a link to view that specific contact in more detail.  

#### application_notes:
This where you'll find all the Python functions related to Application Notes.

The files in this directory:
-   add_app_note.py
-   delete_app_note.py
-   update_app_note.py
-   view_app_note_details.py
-   view_application_notes.py

###### add_app_note.py:
This file contains the functionality behind:
    -   Presenting the AddApplicationNoteForm() form to the user
    -   Processing the information submitted on the form & adding the values (for the application note) to the 'application_notes' table in the 'jhmanager.db database.

###### delete_app_note.py:
This file contains the functionality behind deleting an application note. 

###### update_app_note.py:
This file contains the functionality behind:
    -   Presenting the AddApplicationNoteForm() form to the user, with the values for an existing application note.
    -   Processing the information submitted on the form & updating the values (for the application note) for an entry in the 'application_notes' table in the 'jhmanager.db database.

###### view_app_note_details.py:
This file contains the functionality behind presenting the user with the details they've provided for a specific note, where the note displayed is linked to a specific job application.

###### view_application_notes.py:
This file contains the functionality behind presenting the user with all the notes they've added for a specific application, where each note is a link to view the details for that specific note.

#### applications:
This where you'll find all the Python files related to job applications. 

The files in this directory:
-   add_application.py
-   view_application_details.py
-   view_all_applications.py
-   update_application.py
-   delete_an_application.py
-   delete_all_applications.py

###### add_application.py
This file contains the functionality behind displaying the 'AddApplicationForm' (form) to the user & inserting these values into the 'job_applications' table in the 'jhmanager.db database, before redirecting the user to the template 'view_application.html' for this newly-created job application.  

##### delete_all_applications.py:
In this file we find the functionality to delete all job applications, & all interview, interview_preparation, note, & job offer entries linked to these applications, from their perspective SQL tables. The user is then redirected back to the dashboard (template: 'dashboard.html'). 

##### delete_an_application.py:
In this file we find the functionality to delete both a specific job application, and all interview, interview_preparation, note, & job offer entries linked to this application, from their perspective SQL tables. The user is then redirected back to the 'applications.html' template.

##### update_application.py:
In this file we find the functionality to:
-    Display the AddApplicationForm() (form), with the details of a specific application, to the user via the template 'update_application.html'. 
-   Grab the details from the form, update the relevant entry in the 'job_applications' table.
-    Redirect the user to 'view_application.html' so that the user can view the application they've just updated. 

##### view_all_applications.py:
This file contains the functionality behind displaying the top 10 application entries (if there are any), added by current user, to the template 'applications.html'.  

##### view_application_details.py:
This file contains the functionality behind presenting the user with the details they've provided for a specific job application. 

---------------------------------------------------

#### cleanup_files:
In this file we find the functionality to clean up values in the various functions in the 'service' directory. So once a value has been extracted from the relevant SQL table, it will be "cleaned" to ensure it looks both presentable and just more like every day language. 
EG: random_value => Random Value. 

The files in this directory:
-   cleanup_app_fields.py
-   cleanup_company_fields.py
-   cleanup_contact_fields.py
-   cleanup_datetime_display.py
-   cleanup_general_fields.py
-   cleanup_interview_fields.py
-   cleanup_job_offer_fields.py

##### cleanup_app_fields.py
This file includes functions which specifically focus on the fields related to the 'job_application' SQL table. 

##### cleanup_company_fields.py
This file includes functions which specifically focus on the fields related to the 'company' SQL table.

##### cleanup_contact_fields.py
This file includes functions which specifically focus on the fields related to the 'indiv_contacts' SQL table.

##### cleanup_datetime_display.py
This file includes functions which specifically focus on the fields related  to a 'Date' & 'Time'. 

##### cleanup_general_fields.py
This file includes functions which are general in natural & therefore can be used by any function in the Service directory. 

##### cleanup_interview_fields.py
This file includes functions which specifically focus on the fields related to the 'interviews' SQL table.

##### cleanup_job_offer_fields.py
This file includes functions which specifically focus on the fields related to the 'job_offers' SQL table.

---------------------------------------------------

#### company:
This where you'll find all the Python files related to a 'company'. 

The files in this directory:
-   add_company.py
-   add_company_job_application.py
-   update_company.py
-   delete_company.py
-   view_all_companies.py
-   view_company_profile.py

##### add_company.py
Handles the functionality behind adding a company contact, and handles everything from presenting the form to processing the information that the user provides & storing that data as a single entry in the 'company' SQL table. 

##### add_company_job_application.py
Handles the functionality behind adding a job application for a specific company. This covers everything from presenting the form to processing the information that the user provides & storing that data as a single entry in the 'job_applications' SQL table. 

##### update_company.py
Handles the functionality behind updating an existing company. This covers everything from displaying the form (to the user) to updating the values for this company in the 'company' SQL table.

##### delete_company.py
Handles the functionality behind deleting a specific 'company'. 

##### view_all_companies.py
Handles the functionality behind displaying all the companies that the user has already added/created so far, with each company being a link to the 'view_company_profile.html' template for the selected company. 

##### view_company_profile.py
Handles the functionality behind displaying the details for a specific company, using its unique 'company_id'. 

It also offers to links to: Add a job application, View the company website, Add a note for this specific company & View all notes for this specific company.

---------------------------------------------------

#### company_notes:
This where you'll find all the Python files related to a company note / list of company notes. 

Files in this directory:
-   add_company_note.py
-   view_specific_note.py
-   view_all_company_notes.py
-   update_company_note.py
-   delete_company_note.py

##### add_company_note.py
Handles the functionality behind displaying the 'AddCompanyNoteForm' form to the user & saving the information (the user has provided/entered into the form) into the 'company_notes' SQL table. 

##### view_specific_note.py
Handles the functionality behind displaying the details for a specific note, linked to a specific company, from the 'company_notes' SQL table (using its unique 'company_note_id').  

##### view_all_company_notes.py
Handles the functionality behind displaying all the notes, from the 'company_notes' SQL table (using its unique 'company_note_id'), which are linked to a specific company. 

##### update_company_note.py
Handles the functionality behind updating an existing note linked to a specific company. This covers everything from displaying the form (to the user) to updating the values for this company in the 'company_notes' SQL table.

##### delete_company_note.py
Handles the functionality behind deleting a note, from the 'company_notes' SQL table, which is linked to a specific 'company'.

---------------------------------------------------

#### contacts_directory:
This where you'll find all the Python files related to a contact / list of contacts. 

Files in this directory:
-   add_new_contact.py
-   view_contact_details.py
-   view_contact_list.py
-   update_contact.py
-   delete_contact.py

##### add_new_contact.py
Handles the functionality behind displaying the 'AddNewContactForm()' (form) to the user & saving the information (the user has provided/entered into the form) into the 'indiv_contacts' SQL table. 

##### view_contact_details.py
Handles the functionality behind displaying the details for a specific 'contact', from the 'indiv_contacts' SQL table, to the template 'view_contact_details.html'.

##### view_contact_list.py
Handles the functionality behind displaying all the (individual) contact entries (added by the current user), from the 'indiv_contacts' SQL table, to the template 'view_contact_details.html'. 

##### update_contact.py
Handles the functionality behind displaying the 'AddNewContactForm()' (form), with the values for a specific contact entry, to the user. Once the form is submitted, the form values are extracted & used to update an existing entry in the 'indiv_contacts' SQL table.

##### delete_contact.py
Handles the functionality behind deleting a specific contact entry from the 'indiv_contacts' SQL table. The user will then be redirected to the Addressbook (template: 'view_address_book.html'). 

---------------------------------------------------

#### interview_preparation:
This where you'll find all the Python files related to an interview preparation entry / list of interview preparation entries. 

Files in this directory:
-   add_interview_prep.py
-   view_interview_prep_details.py
-   view_all_interview_prep.py
-   update_interview_prep.py
-   delete_interview_prep.py

##### add_interview_prep.py
Handles the functionality behind displaying the 'AddInterviewPrepForm()' (form) to the user & saving the information (the user has provided/entered into the form) into the 'interview_preparation' SQL table. 

##### view_interview_prep_details.py
Handles the functionality behind displaying the details for a specific entry, from the 'interview_preparation' SQL table, to the template 'interview_prep.html'.

##### view_all_interview_prep.py
Handles the functionality behind displaying all the interview preparation entries (added by the current user), from the 'interview_preparation' SQL table, to the template 'view_all_interview_prep.html'. 

##### update_interview_prep.py
Handles the functionality behind displaying the 'AddInterviewPrepForm()' (form), with the values for a specific interview preparation entry, to the user. Once the form is submitted, the form values are extracted & used to update an existing entry in the 'interview_preparation' SQL table.

##### delete_interview_prep.py
Handles the functionality behind deleting a specific interview preparation entry from the 'interview_preparation' SQL table. 

---------------------------------------------------

#### interviews:
This where you'll find all the Python files related to an interview entry / list of interview entries. 

Files in this directory:
-   add_interview_py
-   view_interview_details.py
-   view_all_interviews.py
-   update_interview_status.py
-   update_interview.py
-   delete_an_interview.py

##### add_interview_py
Handles the functionality behind displaying the 'AddInterviewForm()' (form) to the user & saving the information (the user has provided/entered into the form) into the 'interviews' SQL table. 

##### view_interview_details.py
Handles the functionality behind displaying the details for a specific entry, from the 'interviews' SQL table, to the template 'view_interview_details.html'.

##### view_all_interviews.py
Handles the functionality behind displaying all the interview entries (added by the current user), from the 'interviews' SQL table, which relate to a specific job application. These interview entries are then displayed to the template 'view_all_interviews.html'. 

##### update_interview_status.py
Handles the functionality behind displaying the 'UpdateInterviewStatusForm()' (form) to the user. Once the form is submitted, the interview's status, for a specific interview entry, is updated in the 'interviews' SQL table. 

##### update_interview.py
Handles the functionality behind displaying the 'AddInterviewForm()' (form), with the values for a specific interview entry, to the user. Once the form is submitted, the form values are extracted & used to update an existing entry in the 'interviews' SQL table.

##### delete_an_interview.py
Handles the functionality behind deleting a specific interview entry from the 'interviews' SQL table. 

---------------------------------------------------

#### job_offers:
This where you'll find all the Python files related to a job offer entry / list of job offer entries. 

Files in this directory:
-   add_job_offer.py
-   view_job_offer.py
-   update_job_offer.py
-   delete_job_offer.py

##### add_job_offer
Handles the functionality behind displaying the 'AddJobOffer()' (form) to the user & saving the information (the user has provided/entered into the form) into the 'job_offers' SQL table. 

##### view_job_offer.py
Handles the functionality behind displaying the details for a specific entry, from the 'job_offers' SQL table, to the template 'view_job_offer.html'.

##### update_job_offer.py
Handles the functionality behind displaying the 'AddJobOffer()' (form), with the values for a specific job offer entry, to the user. Once the form is submitted, the form values are extracted & used to update an existing entry in the 'job_offers' SQL table.

##### delete_job_offer.py
Handles the functionality behind deleting a specific job offer entry from the 'job_offers' SQL table. 

---------------------------------------------------

#### users:
This where you'll find all the Python files, with functionality related to a user entry / list of user entries, from the 'users' SQL table. 

Files in this directory:
-   register_user.py
-   login_user.py
-   user_profile.py
-   change_password.py
-   update_email.py
-   delete_user_account.py

##### register_user()
Handles the functionality behind displaying the 'RegisterUserForm()' (form) to the user & saving the user's details (provided/entered into the form) into the 'users' SQL table. The user is then logged into their newly-created account on the application. 

##### login_user.py
Handles the functionality behind displaying the 'LoginForm()' (form) to the user & validating the details provided by the user. If (and only if) the provided details are correct & valid, the user is logged into their account (on the application). 

##### user_profile.py
Handles the functionality behind displaying the user's  account details to their User Profile. From the User Profile, the user has the option to update their account email or password, or to even delete their account entirely. 

##### change_password.py
Handles the functionality behind displaying the 'ChangePasswordForm()' (form) to the user & using the new password (provided/entered into the form) to update the user's entry in the 'users' SQL table. The user is then redirected back to the User Profile. 

##### update_email.py
Handles the functionality behind displaying the 'UpdateEmailAddressForm()' (form) to the user & using the new email (provided/entered into the form) to update the user's entry in the 'users' SQL table. The user is then redirected back to the User Profile. 

##### delete_user_account.py
Handles the functionality behind displaying the 'DeleteAccountForm()' (form) to the user. If the user selects to proceed with deleting their account (and submits this request), then their user account is deleted from the 'users' SQL table, & the user is redirected back to the landing page. 

---------------------------------------------------------------
### 5: Static:
### 6: Technical Readme files:

I had initially intended to write up the technical readme in 1 file, however once I exceeded 1000 lines, I decided to split it up into 6 files: 
-   forms.md
    -   Goes over all the files in the Forms directory, in technical detail.
-   repos.md
    -   Goes over all the files in the Repos directory, in technical detail.
-   Services
    -   Goes over all the files in the Services directory, in technical detail.
-   Static
    -   Goes over the CSS file (found in the Services directory), in technical detail.
-   Templates
    -   Goes over all the files in the Templates directory, in technical detail.
-   technical_readme.md
    -   I realised that this readme can get pretty technical, which isn't easy for the everyday-Jo to understand / follow. Since this is an academic piece, I've create the technical_readme files to cover what the functions do from a technical perspective. These files will cover:
    -   What the function does.
    -   Which other directories / files the function / method interacts with. 

### 7: Pages / Templates:
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

Note: The technical readme covering the Forms is covered in jhmanager/technical_readme_files/templates.md.

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

### 7: Tests: 
### 8: __init__.py:
### 8: helpers_from_cs50_finance.py
### 9: jhmanager.db
### 10: schema.sql
### 11: Makefiles
### 12: requirements.txt
### 13: setup.py
### 14: wsgi.py