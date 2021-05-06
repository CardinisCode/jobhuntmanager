
# Project Hunt Manager

A Web-based application aimed at job hunters looking to manage all aspects of their job hunt in one place. 

## Video Demo:  <URL HERE> -> In progress...

## Link to Heroku-hosted site: 
    https://jobhuntmanger.herokuapp.com/

## Description: 
A web-based application for any one looking to manage their job hunting. Its intended to be a place where a user can store job applications, interviews, interview preparation, notes, & contacts. Plus the user can add companies from their wishlist. 

The application uses:
-   Python
    -   Flask, WTForms 
-   HTML, CSS & a little JavaScript. 

I have narrowed down the application for fellow software engineers, so the Job application form is very much in the scope of the software engineering industry. 

## Files:
The files in this project are divided into the following sections:

### 1: Forms:
All forms are created using WTForms - a library I found that works well with Python & Flask. Using WTForms allowed me to create Form templates that I could instantiate either as a blank form or with values from one of the SQL tables. WTForms also offers the field/data validation and comes included with CSRF protection. 
These forms are saved in jhmanager/forms. 

Below are the names of the files stored in the 'Forms' directory: 
-   add_application_form.py
-   add_application_note_form.py
-   add_company_form.py
-   add_company_job_app_form.py
-   add_company_note_form.py
-   add_interview_form.py
-   add_interview_prep_form.py
-   add_job_offer_form.py
-   add_new_contact_form.py
-   delete_account_form.py
-   delete_form.py
-   login_form.py
-   register_form.py
-   update_company_form.py
-   update_interview_status_form.py
-   update_user_details.py

Below I will go into detail to tell you what form/s are in each file and what the form does. 

#### add_application_form.py
##### Form name: 
    AddApplicationForm()
##### Functionality: 
    This form includes all the fields that I've commonly seen on job application forms (online and in person). 
##### Fields:
    date_posted, job_role, emp_type, job_ref, company_name, company_description, industry, job_description, job_perks, tech_stack, location, salary, user_notes, platform, job_url. 
##### Template used:
    add_job_application.html

#### add_application_note_form.py
##### Form name: 
    AddApplicationNoteForm()
##### Functionality: 
    This form is simple in nature and only has 2 fields: The subject and content for a form. 
##### Fields:
    description, notes_text
##### Template used:
    add_application_note.html

#### add_company_form.py
##### Form name: 
    AddCompanyForm()
##### Functionality: 
    This Form has fields relevant to a company and puts together 'contact' info for a specific company.
##### Fields:
    name, description, location, industry, interviewers, url
##### Template used:
    add_company_form.html

#### add_company_job_app_form.py
##### Form name: 
    AddCompanyJobApplicationForm()
##### Functionality: 
    This form is very similar to the AddApplicationForm(), except it doesn't include any fields relevant to a company. 
##### Fields:
    date_posted, job_role, emp_type, job_ref, job_description, job_perks, tech_stack, salary, user_notes, platform, job_url. 
##### Template used:
    add_company_job_application.html

#### add_company_note_form.py
##### Form name: 
    AddCompanyNoteForm()
##### Functionality: 
    I kept this form simple in nature, so that it resembles a note we'd scribble in a note book. 
##### Fields:
    subject, note_text
##### Template used:
    add_company_note.html

#### add_interview_form.py
##### Form name: 
    AddInterviewForm()
##### Functionality: 
    This form includes fields relevant to an interview. I added fields relevant to interviews done 1) in person, 2) over video call & 3) over a phone call. 
##### Fields:
    interview_date, interview_time, interviewer_names, interview_type, interview_location, interview_medium, other_medium, video_link, phone_call, status, extra_notes. 
##### Template used:
    add_interview.html

#### add_interview_prep_form.py
##### Form name: 
    AddInterviewPrepForm()
##### Functionality: 
    This form is similar in nature to the note forms, except the 2 fields are 'Question' and 'Answer'. It allows the user to add the interview Question and the answer the user is planning to say in response to the Question. 
##### Fields:
    question, answer
##### Template used:
    interview_prep.html
            
#### add_job_offer_form.py
##### Form name: 
    AddJobOffer()
##### Functionality: 
    This form allows the user to add a job offer they've received and gives the user the field 'offer_response' so the user can select if they've accepted (or rejected) the offer or if they're still thinking about it. 
##### Fields: 
    job_role, salary_offered, perks_offered, offer_response, starting_date. 
##### Template used:
    add_job_offer.html

#### add_new_contact_form.py
##### Form name:
    AddNewContactForm()
##### Functionality: 
    This form asks the user for information very much relevant for putting together contact information. Making connections is very important when looking for work as we often have a higher chance of getting a job when we know someone on the inside of the company we're looking to work for. We're also more likely to know of a vacacy through the network we build. 
##### Fields:
    full_name, job_title, contact_number, company_name, email_address, linkedin_profile.
##### Template used:
    add_new_contact.html

#### delete_account_form.py
##### Form name:
    DeleteAccountForm()
##### Functionality: 
    This form is presented to the user when they select the 'Delete Account' button in their User Profile. The form asks the user to enter their account password and once the user submits the form, their account is hard (entirely) deleted from the application's database. 
##### Fields:
    password
##### Template used:
    delete_account.html

#### delete_form.py
##### Form name:
    DeleteCompanyForm()
##### Functionality: 
    The user is presented with a select fields with 2 options. I believe by asking the user to manually select an option, they're less likely to make this choice by accident or by using a bot. If the user chooses the "Yes....", & submits the form, then the company (and all data related to this company) will be hard deleted from the application's databases. For this reason, there is a warning presented above this option to notify the user of the consequences of deleting this company contact.
##### Fields:
    confirm_choice
##### Template used:
    delete_company_profile.html

#### login_form.py
##### Form name: 
    LoginForm()
##### Functionality: 
    Presents the user with a simple form, which allows the user to log into their account on the application. 
##### Fields:
    username, password
##### Template used:
    login.html

#### register_form.py
##### Form name: 
    RegisterUserForm()  
##### Functionality: 
    This form as the registration form & the values of this form will be used to create an account for the user. The user is asked to provide an unique username & email address. If either already exists in our database, the user will be asked to provide another username / email address. The 'confirm_password' field serves to ask the user to type a password in twice & ensure that both password values match. 
##### Fields:
    username, email_address, password, confirm_password. 
##### Template used:
    register.html

#### update_company_form.py
##### Form name: 
    UpdateCompany() 
##### Functionality: 
    This form is very similar to the AddApplicationForm(), except it doesn't include any fields relevant to a company. 
##### Fields:
    date_posted, job_role, emp_type, job_ref, job_description, job_perks, tech_stack, salary, user_notes, platform, job_url. 
##### Template used:
    update_company_profile.html

#### update_interview_status_form.py
##### Form name: 
    UpdateInterviewStatusForm() 
##### Functionality: 
    This form is very simple and serves to allow the user to update only the status of an interview. Once an interview has been completed/deleted/post-poned, the user will want to update the status without having to worry/focus on any of the other interview fields (on AddInterviewForm()). 
##### Fields:
    status
##### Template used:
    update_interview_status.html

#### update_user_details.py
##### Form name: 
    UpdateEmailAddressForm() 
##### Functionality: 
    This form serves to allow the user to update the email address linked to their account. The user is asked to provide the new email address twice. I added validators to ensure that the user provides the same email address in both fields.
##### Fields:
    email, confirm_email
##### Template used:
    update_email.html

##### Form name: 
    ChangePasswordForm()
##### Functionality: 
    This form serves to allow the user to change the password on their account. The user is asked to provide the new password twice. I added validators to ensure that the user provides the same password in both fields. Since these two fields are each designated as a 'PasswordField', the fields hide what the user enters into these fields, even as they're typing. 
##### Fields:
    password, confirm_password
##### Template used:
    change_password.html

---------------------------------------------------------------
### 2: Models:



---------------------------------------------------------------
### 3: Preparation & Management:


---------------------------------------------------------------
### 4: Repo:
This file contains all the Repositories used for this project.


---------------------------------------------------------------
### 5: Service:
This includes all the Python functionality to build the 'back-end' of the application. 


---------------------------------------------------------------
### 6: Static:



---------------------------------------------------------------

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


