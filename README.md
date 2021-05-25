
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
This directory includes:
-   Images
-   The CSS file

#### Images
The images directory simply includes all the screenshots used for the landing page. I took screenshots of various pages on the application, completed with fictional data, to demonstrate how the information would be displayed to each page. 

#### styles.css
This is the CSS file for the project, which determines how the content, for each page, is displayed to you as the user. 

### 6: Technical Readme files:
I had initially intended to write up the technical readme in 1 file, however once I exceeded 1000 lines, I decided to split it up into 6 files: 
-   forms.md
    -   Goes over all the files in the Forms directory, in technical detail.
-   repos.md
    -   Goes over all the files in the Repos directory, in technical detail.
-   Services
    -   Goes over all the files in the Services directory, in technical detail.
-   Templates
    -   Goes over all the files in the Templates directory, in technical detail.
-   technical_readme.md
    -   I realised that this readme can get pretty technical, which isn't easy for the everyday-Jo to understand / follow. Since this is an academic piece, I've create the technical_readme files to cover what the functions do from a technical perspective. These files will cover:
    -   What the function does.
    -   Which other directories / files the function / method interacts with. 


### 7: Pages / Templates:
This file will cover all the templates used for this application, which are utilized by the files & functions in the Services directory.

Note: The technical readme, covering these template is found in jhmanager/technical_readme_files/templates.md.

##### layout.html: 
This template is used as the 'layout' / reference template, from which all templates (in this directory) get their structure, as well the necessary meta data, links & routes, & scripts. 

##### index.html
This is the landing page, the first page that the user sees when they're taken to this web application. Here the user is welcomed with the concept / pitch of the application, who I am & why I built this application. The user has the option to contact me or find out more about me / this project. 

Below this, I include screenshots of the application across the various pages. This serves to demonstrate the features & functionality of the application: what the user could do when using the Job Hunt Manager. 

I used background colouring to implement a clear set of sections, each highlighting something different. 

##### about_us.html:
This template gives the user information about the 'Job Hunt Manager, about the developer (myself), & the research carried out (prior to developing this application). I also included a means for the user to contact me if there any issues or if the user would like to provide any feedback related to this application. 

This page can be accessed via the 'About' link in the footer, on every page. 

##### dashboard.html
This page is the landing page for a user once they've logged in. This page serves as the 'update' center, where the user will see any/all interviews & job applications they've added today, as well any job offers they've received & any interviews they have coming up.  

##### view_all_user_notes.html:
This page displays all the notes the user has added to all their job applications & company contacts. A link to this page is found on the Nav bar as "Notes", but only when the user is logged in. 

#### Users:
This includes all the templates related to a user's account.

##### register.html (WTForm):
The user is presented with a registeration page, where the user can create an account on the application. Provided the user provides a username & email address which doesn't yet exist in our database, then the account is created & the user is redirected to the Dashboard. 

##### login.html (WTForm): 
The user is presented with a login form, where the user simply puts in their username (or email address) & password. Provided the username / email address matches an account in our database & the password is correct, then the user is logged in successfully. The user is then redirected to the Dashboard. 

##### userprofile.html:
This page displays the user's email address & username. Here the user can update their email, change their password & delete their account. 

##### update_email.html (WTForm):
The user is presented with an update email form, where the user simply enters their 'new' email address twice. Provided the user enters a valid email address in both fields & both email addresses are identical, the user's email address will be updated. The user will then be redirected back to the User Profile.  

##### change_password.html (WTForm): 
The user is presented with a 'change password' form, where the user simply enters their 'new' password twice. Provided the user enters the same password in both fields, the password linked to their account, will be updated. The user will then be redirected back to the User Profile.  

##### delete_account.html (WTForm): 
The user is presented with a 'change password' form, where the user simply enters their account password once. Provided the password matches the password linked to the user's account, the user's account will be successfully deleted. The user then gets redirected back to the landing page.  

#### Applications:
All pages / templates relevant to a job application.

##### add_job_application.html (WTForm):
The user is presented with a job application form, where the user will type / copy in the details (the user) provided for a specific job application. The job application will be added (as a new entry) in the database. The user will then be redirected to view the new job application details. 

##### applications.html:
Displays all the applications that this specific user has added. Each application is a link to 'view_application.html' where the user can view the specific details of the selected application. 

##### update_application.html (WTForm): 
The user is presented with a job application form, pre-filled with the details for an existing job application. The form is designed to allow the user to update the details for a job application that the user has already submitted, & all details in the form are used to update the application stored in the database. 

##### view_application.html:
User is presented with the details for a specific job application they've added. Over and above this, the user will also see the most recent interviews & job offers, which are linked to this application. 

#### Interviews:
All templates relevant to job interviews. 

##### add_interview.html (WTForm):
The user is presented with an interview form, where the user can provide the details for an upcoming interview they've scheduled. Each interview is linked to the job application they'd submitted for a specific company. Once the user submits the completed form, the details for this interview will be added (as a new entry) in the database. The user will then be redirected to view the details for this newly-created interview. 

##### view_all_interviews:
Displays all the interviews the user has received for a specific job application. Each interview is a link to 'view_interview_details.html', which will display the details for the job interview. The link to this page is found on 'view_application.html'. 

##### view_interview_details.html:
This page offers the user the option to update/delete a specific interview, prepare for the interview, or add notes. The link to this template can be found on the 'view_application.html' page / template. 

##### update_interview_status.html (WTForm): 
Presents the user with a form, with only 1 field 'Interview Status', which allows the user to simply update the status for a specific interview, without having to bother with the rest of the interview fields. 

The link to this form can be found when viewing an interview's 'profile' (on the 'view_interview_details.html' template).

##### update_interview.html (WTForm):
Presents the user with an AddInterviewForm() form, pre-filled with the entry details for a specific interview. It gives the user the option to update any/all of the details for an interview. 

The link to this page is found on the 'view_interview_details.html' page. Once the form has been successfully submitted and processed, the user will be redirected to 'view_interview_details.html'. 

#### Interview Preparation:
All templates related to Interview Preparation.

##### interview_prep.html (WTForm):
Presents the user with an AddInterviewPrepForm() form, where the user can prepare for a specific interview question. Over & above this, the user is given links to external sites offering advice on how to answer the top interview questions. 

It's important to note that this link will only be displayed to the user when the interview's status is still 'upcoming'. Once the interview's status has been updated to any other status, this link will no longer be displayed to the 'view_interview_details' page. 

Once an entry is successfully submitted, the user will be redirected back to this template, but the page will be updated to display the newly-added entry below the form itself. The link to this page is found on the 'view_interview_details.html' page. 

##### view_interview_prep_details.html:
This page offers the user the option to view a specific interview preparation entry, with links to update/delete the preparation entry. The user is also presented with 'cards' displaying details for the Job Application, Company & Interview, where each is link to view more details for the job Application, Company & Interview perspectively. The user can also continue adding preparation entries, or view the preparation entries that they've already added, for this interview. 

The link to this template can be found on the 'view_application.html' page / template. 

##### update_interview_prep.html (WTForm): 
Presents the user with the same layout & form as seen on the 'interview_prep.html' template. The difference is the template 'update_interview_prep.html' presents the user with an form prefilled with the details for a interview preparation entry. This allows the user to update the details / values they've provided for the 'Question' & 'Answer' fields.  

A link to this form is found on the 'view_interview_prep_details.html' page.

#### Job Offer:
All templates related to Job Offers.

##### add_job_offer.html (WTForm): 
The user is presented with a form, where the user can provide the details for a job offer they've received from a company. Each job offer is linked to the job application they'd submitted for a specific company. Once the user submits the completed form, the details for this interview will be added (as a new entry) in the database. The user will then be redirected to view the details for this newly-created job offer. 

##### view_job_offer.html:
This page offers the user the option to to view a specific job offer, with links to update/delete the offer. The user is also presented with 'cards' displaying details for the Job Application & Company, where each is link to view more details for the job Application & Company perspectively. 

The link to this template can be found on the 'view_application.html' page / template. 

Note:   These links will only be displayed to the user when there is a job offer to display.

##### update_job_offer.html (WTForm):
Presents the user with form, pre-filled with the details for a specific job offer entry. The form allows the user to update the details for an existing job offer they've received & once the form has been successfully submitted and processed, the user will be redirected to view the job offer's details. 

#### Address Book:
All templates related to the Address Book.

##### view_addressbook.html:
This page is divided into 2 sections:
-   Company Contacts, known as the company directory
-   Individual Contacts

In each section, the user can:
-   Add a new contact, view the top contacts & view all existing contacts. 

The link to this template can be found on the navigation bar as 'Address Book'.

#### Company Contacts / Directory:
All templates relevant to all company contacts & their perspective profiles. 

##### add_company_form.html (WTForm):
The user is presented with a form, where the user can provide the details for a company. Once the user submits the completed form, the details for this company will be added (as a new entry) in the database. The user will then be redirected to view the details for this newly-created company contact. 

##### view_company_directory.html:
The user is presented with a list of all the company contacts, which the user has already added/created. The user also gets an option to add another company contact.

The link to this page / template can be found on the 'view_addressbook.html'.

##### view_company_profile.html:
This page offers the user the option to to view a specific company contact, with links to update/delete the contact. Over and above this, the user can add a job application (which will link to this company specifically), view the company's website, and add a new note, or view existing notes, for this company contact.

The link to this page / template can be found in a few places, one of which is found by viewing the details of a job application (template: 'view_application.html'). 

##### add_company_job_application.html:
Presents the user with a job application form, except it doesn't include any fields related to this company (which the user applied to). This is because the user has already provided details for this company, so no point providing the same details twice. 

Once the user submits the form, the job application is added to the database, with the details from the form & from the company. The user is then redirected to the template 'view_application.html', to view the details for the newly-created job application. 

The link to this form can be on the template 'view_company_profile.html', for a specific company contact. 

##### update_company_profile.html (WTForm):
Presents the user with form, pre-filled with the details for a specific company contact. The form allows the user to update the details for the company contact & once the form has been successfully submitted and processed, the user will be redirected to view the company's profile. 

##### delete_company_profile.html (WTForm):
Presents the user with a form, which asks the user to confirm whether/not the user wants to delete the company contact entirely. 

If the user chooses not to delete the company, the user will be redirected back to the company's profile. However, if the user chooses to delete the company, the company contact will be deleted entirely & the user will be redirected back to the landing page.

The link to this template can be found on 'view_company_profile.html'.

#### Individual Contacts:
All templates linked directly to individual contacts:

##### add_new_contact.html (WTForm):
The user is presented with a form, where the user can provide the details for a (individual) contact. Once the user submits the completed form, the details for this contact will be added (as a new entry) in the database. The user will then be redirected to view the details for this newly-created contact. 

A link to this page can be found on the template 'view_address_book.html'. 

##### view_contacts.html:
The user is presented with all the contact contacts, which the user has already added/created, where each contact is  a link to view the contact in more detail. The user also gets an option to add another contact.

The link to this page / template can be found on the 'view_addressbook.html' as 'View Contacts'.

##### view_contact_details.html:
The user is presented with the details for a specific contact, with the option to update / delete the entry or to view the contact's Linkedin profile (if the user has provided the link to their profile). The user also has the option to return to the Address book or the contact directory. 

The link to this page / template can be found on the 'view_addressbook.html' as 'View Contacts'.

##### update_contact_form.html (WTForm):
Presents the user with form, pre-filled with the details for a specific (individual) contact. The form allows the user to update the details for the contact & once the form has been successfully submitted and processed, the user will be redirected to view the contact's profile. 

The link to this page / template can be found on the 'view_contact_details.html' as 'Update'.

#### Notes:
All templates related to notes.

##### view_all_user_notes.html:
The user is presented with all the note entries, which the user has already added/created, where each note is a link to view the note in more detail. The user also is presented with link to view the company directory & all the job applications (added by this user). 

The notes are split into 2 sections: Application notes & Company notes. The link to this page / template can be found on the navigational bar & is labelled as 'Notes'.

##### Company Notes:
All templates related specifically to Company Notes, where each note is linked to a specific company.

###### add_company_note.html (WTForm):
The user is presented with a form, where the the user can create a note for a specific company & includes 2 fields: a note heading & body / content. Once the user submits the completed form, the details for this 'note' will be added (as a new entry) in the database. The user will then be redirected to the template 'view_specific_company_note',  where the user can view the details for this newly-created note. 

A link to this page can be found on the template 'view_company_profile.html'. 

###### view_specific_company_note.html:
The user is presented with the details for a specific company note, with the option to update / delete the entry or to view the company's profile. The user also has the option to return to the Company Notes or to add another note for this company. 

The link to this page / template can be found on the 'view_all_notes.html', if there are any company notes, linked to this company, to display.

###### view_company_notes.html:
The user is presented with all the notes, which are linked to a specific company, where each note is a link to view the note in more detail. The user also gets an option to add another note, or view the company's profile, for a specific company. Alternatively the user can return to the Address book. 

The link to this page / template can be found on the 'view_addressbook.html' as 'View All Notes for (company name)'.

###### update_company_note.html (WTForm):
Presents the user with a form, pre-filled with the entry details for a specific company note, allowing the user to update the details that the user has already provided for this note. 

A link to this page is found on the 'view_specific_company_note.html' page. Once the form has been successfully submitted and processed, the user will be redirected back to 'view_specific_company_note.html'.

##### Application Notes:
All templates related specifically to Application Notes, where each note is linked to a specific job application.

###### add_application_note.html (WTForm):
The user is presented with a form, where the the user can create a note for a specific job application, which is useful at any stage of the job application.   

Once the user submits the completed form, the user is redirected to the template 'view_app_note_details.html', where the user can view the details for this newly-created note. 

A link to this page can be found on the template 'view_application.html', labelled as '+ Note'. 

###### view_notes_for_application.html:
The user is presented with all the notes, which are linked to a specific job application, where each note is a link to view the note in more detail. The user also gets an option to add another note, or view the company's profile, for a specific company. Alternatively the user can return to the job application. 

The link to this page / template can be found on the 'view_application.html' as 'View Notes'.

###### view_app_note_details.html:
The user is presented with the details for a specific application note, with the option to update / delete the entry or to add another note. The user also has the option to return to view all the job applications, view the job application, or to view the company profile.  

The link to this page / template can be found on the 'view_notes_for_application.html', if there are any notes, linked to this job application, to display.

###### update_application_note.html (WTForm):
Presents the user with a form, pre-filled with the entry details for a specific application note, allowing the user to update the details that the user has already provided for this note. 

A link to this page is found on the 'view_app_note_details.html' page. Once the form has been successfully submitted and processed, the user will be redirected back to the template 'view_app_note_details.html'.


### 9: __init__.py:
This file:
-   Imports all the required libraries, & files across the repository, forms & service directories
-   Sets up all the configurations for the Flask application
-   Sets up a connection to the application's database file 'jhmanager.db'
-   Connects all the Repositories to the above database, whilst also creating a variable for each Repository, which will then be accessed by the routes to access a specific table in the database. 
-   Sets up (& defines) all the routes to be used by the application

Each route includes:
-   The routing path & which methods will be used, which determines whether a page will:
    1)  simply display content or 
    2)  display content & process input from the user. 

-   A function which carries out the following functionality (where relevant):
    -   Define what information is rendered & to which template, by calling on the relevant function or by rendering the template directly. 

    -   Instantiate form classes, which can then be handed over to a function, from within the function, to display a form or extract user input from the form. 

    -   Extract the user's unique ID (user_id), from the current session, to ensure data is displayed, or extracted & stored in the database, for the user currently logged in. 

    -   Use conditional logic which checks that the user completes all required fields, in a form, & that the input meets the requirements set out by the form class & its attributes. If the requirements are met, the input is processed by the relevant 'post...' function. Otherwise, the user is redirected back to the form, with a notification message to let the user know why they've been redirected back to the form. 

### 10: helpers_from_cs50_finance.py
I chose to import the helper functions from the Finance section of Harvard's CS50's Computer Science course. In this file, you'll find the login & 'apology' functions, & although I didnt use these functions directly in my project, I used the concepts behind the login() function to create the login function for this project. 

I decided not to create an apology function in this project, mainly due to the scope of this project getting far too big. So I never did end up making use of an apology function in the end. 

### 11: jhmanager.db
This is the SQL Database used for storing all the information provided by the user everytime the user completes a form. I chose to use SQLite3, mainly because I had previously used SQLite3 whilst working through the modules of the CS50 course. Although SQLite3 didn't cause me any issues whilst building this application, I have become aware that it may not be the best choice of database for large datasets. Due to the nature of this application & how much data the database could end up storing, if this application were used by a large number of users, SQLite3 is definitely not ideal for long term.

For this reason, although this application has been launched online (via Heroku), I don't plan to promote the product until I find, & implement, a database tool - one that can offer a lot more storage to handle larger datasets. 

### 12: schema.sql
This file includes all the schematics for every table in the SQL database 'jhmanager.db'. This basically shows the user:
-   The name of every table
-   The names for every column in each table, together with the data type that column holds. If the column accepts an empty input, then it defines the default value that will be stored in that column. 
-   The primary key & all the foreign keys, which gives the user an idea which (of the other) tables connect to this table. 

I chose to lay out each table's columns like I define a dictionary, with each column on its own line, for better readability for anyone reading through the table fields / schematics. I believe this really makes a difference, especially when tables have several columns.  

### 13: Makefiles
This file defines the flask application & the flask environment. I set up this file to make it quicker & more convenient to run the flask environment. Now, to run the flask environment, I can simply run the application, from the terminal, using 'make start'. 

This is especially important since I had to run the environment on a daily basis through out the development process. 

### 14: requirements.txt
This file is really important for any one wanting to run this application as it includes all the required dependencies. This is basically a list of all the libraries that the user would need to have installed in order to run this application. 

For each library needed, it lists the version used to develop this application. As an example, whenever I run this application on Heroku, Heroku will set up a virtual environment for this application, with all these dependencies are installed.

### 15: setup.py


### 16: wsgi.py
