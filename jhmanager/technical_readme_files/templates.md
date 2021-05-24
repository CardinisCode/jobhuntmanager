# Technical Readme
## Template:

This file will cover all the templates used for this application, which are utilized by the files & functions in the Services directory. These templates can be divided into the following categories: 
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

### General:
#### layout.html: 
This template is used as the 'reference' template, from which all templates (in this directory) get their structure. Since this template provides the layout & structure for all templates, it includes:
-   All meta data, 
-   Links to all stylesheets, bootstrap libraries & scripts (which can be used by any template), 
-   The navigational links & structure
-   The structural elements: head, body & footer 

By allocating one template to 'hold' all the above (required) elements, I could remove unnecessary duplication & thereby reduce the amount of storage required to store the 'templates' directory. 

##### about_us.html:
This page tells/informs the user:
-   what this application is about, 
-   why I developed this application, 
-   the research I carried out before putting this application together,
-   security, & 
-   how they could contact me if they want to. 

This page can be accessed via the 'About' link in the footer, on every page. 

##### dashboard.html
This page is the landing page for a user once they've logged in.  This page serves as the 'update' center, where the user will see all:
-   Upcoming interviews
-   Interviews the user has today
-   Applications submitted today
-   Job offers received
-   Progress stats:
    -   This shows the user how many applications, interviews and job offers they've submitted up til this point. 

The function 'create_dashboard_content()', in services/display_dashboard_content.py, handles what gets displayed to this template (with all routes/links).

##### view_all_user_notes.html
This page displays all the notes the user has added and is split up into 2 sections: 
1) notes added to applications
2) notes added to company profiles

A link to this page is found on the Nav bar as "Notes", but only when the user is logged in. 

The function 'display_all_user_notes()', in services/display_all_notes.py, handles what gets displayed to this template (with all routes/links).

### Users:
This includes all the templates related to a user's account.

#### register.html (WTForm):
Presents the user with a blank instance of the 'RegisterUserForm()' to create a Job Hunt Manager account.

The form provides the user with fields to provide their email address, a username of their choice, their password of choice & to confirm their password of choice. 

The username, email address & password, provided by the user in the form fields, will be validated by the function 'post_register_user()', in services/users/register_user.py. The user's password is hashed before the user's account is created. The function 'display_register_form()', also found in 'register_user.py', handles displaying the form, routes/links & general information to this template.

I would love to learn how to 'salt' passwords, to add an extra layer of protection which is also abstracted from the user. However, since the application was already growing outside the scope of this project, I decided to leave the salting for now. Alternatively I could just use Google's login, since its not always necessary to build something from scratch, when someone else has already perfected it. I will weigh out the options & updated this application at a later stage. 

The link to this form is added to the Nav bar, for any user that has not successfully logged in (yet). Once this form has been successfully submitted & processed, the user will be redirected to 'dashboard.html'.Going forward the user will only see details related to their specific account (until the user logs out).

#### login.html (WTForm): 
Presents the user with a blank instance of the LoginForm() WTForm. The link to this page is found on the Nav bar at the top of the page, for any user that has not successfully logged in (yet).

The username & password, provided by the user in both fields, will be validated by the function 'post_login()', in services/users/login_user.py. The function 'display_login_form()', also found in 'login_user.py', handles displaying the form, routes/links & general information to this template.

On this form, the user is presented with the fields: Username & password. The 'Username' field will also accept the user's email address if the user prefers to rather use their email address. Once this form has been successfully submitted & processed, the user will be redirected to 'dashboard.html'. Going forward the user will only see details related to their specific account (until the user logs out).

#### userprofile.html:
Presents the user's username & email address. User has the option to:
-   Update their email
    -   Directs the user to the update_email.html page
-   Update / Change their password
    -   Directs the user to the change_password.html page
-   Delete their account 
    -   Directs the user to the delete_account.html page.

The function 'display_user_profile()', in services/users/user_profile.py, handles what gets displayed to this template (with all routes/links).

#### update_email.html (WTForm):
Presents the user with a blank instance of the 'UpdateEmailAddressForm()', which allows the user to update the email address linked to their account. The user is also asked to 'confirm' their email address, just to iron out potential human typing errors. 

The email address, provided by the user in both fields, will be validated by the function 'post_update_email_address()', in services/users/update_email.py. The function 'display_update_email_form()', also found in 'update_email.py', handles displaying the form, routes/links & general information to this template.

This form is accessible from the 'userprofile.html' page, to the right of the email address listed under their user profile. Once this form has been successfully submitted & processed, the user will be redirected to 'userprofile.html', with their email address updated.

#### change_password.html (WTForm): 
Presents the user with a blank instance of the ChangePasswordForm() form. The link to this page is found on the 'userprofile.html' page.

The password, provided by the user in both fields, will be validated by the function 'post_change_password()', in services/users/change_password.py. The function 'display_change_password_form()', also found in 'change_password.py', handles displaying the form, routes/links & general information to this template.

This form allows the user to change their account password & has only 2 fields: password & confirm password. If the user uses the same password in both fields and the password meets the minimal requirements, the user will be redirected back to 'userprofile.html'.

#### delete_account.html (WTForm): 
Presents the user with a blank instance of the 'DeleteAccountForm()'. This form presents the user with:
-   A warning message asking the user to confirm if they want to delete their account.
-   A 'password' field (where the user provides the current password for their Job Hunt Manager account) 

If the password is correct, the user's account is successfully hard deleted and the user is redirected back to the 'index.html' page. Otherwise the user is redirected to the same 'DeleteAccountForm()' & an error message to "Complete all fields". 

The password, provided by the user, will be validated by the function 'post_delete_user()', in services/users/delete_user_account.py. The function 'display_delete_user_form()', also found in 'delete_user_account.py', handles displaying the form, routes/links & general information to this template. 

### Applications:
All pages / templates relevant to a job application.

#### add_job_application.html (WTForm):
Presents the user with a blank instance of the 'AddApplicationForm()'. The form allows the user to add a job application, with all the details of a regular job application. The function 'display_add_application_form()', in services/applications/add_application.py, handles displaying this form to this template.

The function 'post_add_application()', in the services/applications/add_job_application.py, handles:
-   Inserting the details, for this job application, into the database. 
-   Creating a company profile, or updating an existing company profile, for the company that the user applied to. 

The link to this page is found on the 'dashboard.html' & 'applications.html' pages. Once this form has been successfully submitted & processed, the user will be redirected to 'view_application.html'. 

#### applications.html:
Displays all the applications that this specific user has added. Each application is a link to 'view_application.html' where the user can view the specific details of the selected application. The link to this page is found on the Navigational bar as 'Applications'. 

The page also has 2 button links:
-   New Job Application
-   Delete All Applications

The function 'display_applications_for_user()', in services/applications/view_all_applications.py, handles what gets displayed to this template (with all routes/links).

#### update_application.html (WTForm): 
Presents the user with the AddApplicationForm() but pre-filled with the entry details for a specific application. This allows the user to update fields or to add values to fields that that they may have previously left blank - especially since not all job specs provide all the information up front. 

The link to this page can be found on the 'view_application.html' page. Once this form has been successfully submitted & processed, the user will be redirected to 'view_application.html'.

These functions:
-   display_update_application_form()
-   post_update_application()
are behind both displaying the form & processing the form (once submitted by the user). Both these functions are found in services/applications/update_application.py. 

#### view_application.html:
Presents the user with:
- The details of a specific job application
- links to:
    -   Update / Delete the application
    -   View the job posting (if provided by the user when completing the 'AddApplicationForm()')
    -   View the company profile

-   View the any/all Job offers & Interview which have been added to this job application, where each entry is a link to view the details for the the job offer or interview (perspectively). 

-   Notes: 
    - User can either add a new note for this application
    - OR the user can view the notes they've already added for this application.

The function 'display_application_details()', in services/applications/view_application_details.py, handles what gets displayed to this template (with all routes/links).

### Interviews:
All templates relevant to job interviews. 

#### add_interview.html (WTForm):
Presents the user with a blank instance of the 'AddInterviewForm()'. 

This form allows the user to add the details for an upcoming interview, with its date, time & the medium for the interview (video/phone call) or (if in person) the contact details & location for the interview. 

This interview will be linked to a specific application & the link to this form is added to the 'view_application.html' page. Once this form has been successfully submitted and processed, the user will be redirected to 'view_interview_details.html' for this newly-created entry. 

These functions:
-   display_add_interview()
-   post_add_interview()
are behind both displaying the form & processing the form (once submitted by the user). Both these functions are found in services/interviews/add_interview.py. 

#### view_all_interviews:
Displays all the interviews the user has received for a specific job application. Each interview is a link to 'view_interview_details.html', which will display the details for the job interview. The link to this page is found on 'view_application.html'. 

The function 'display_all_interviews_for_application()', in services/interviews/view_all_interviews.py, handles what gets displayed to this template (with all routes/links).

#### view_interview_details.html:
Displays:
- The interview details provided (by the user) for a specific interview. 
- It includes links to:
    - 'Update' the interview stage for this interview
    - 'Update' the interview  
    - 'Delete' the interview
    - View the Company website
    - Add / View interview Preparation
    - View the Job Application & Company linked to this interview
    - Notes: To add a new note & to view existing notes (both application & company notes)

This page offers the user the option to update/delete a specific interview, prepare for the interview, or add notes. I figured it would be useful to have the application and company profile easily accessible so that the user has all aspects related to this interview in 1 place. The user could keep this page open when preparing for the interview or when they're just about to have the interview, since it has the video link (if relevant) / interview location / contact number for the interview itself. 

The link to this template can be found on the 'view_application.html' page / template. 

The function 'display_interview_details()', in services/interviews/view_interview_details.py, handles what gets displayed to this template (with all routes/links).

#### update_interview_status.html (WTForm): 
Presents the user with a blank instance of the 'UpdateInterviewStatusForm()', which offers only 1 select field:
    - "Interview Status", with the choices:
        -   'Upcoming Interview', 
        -   'Interview Done', 
        -   'Interview Cancelled', 
        -   'Interview has been post-poned'

This form allows the user to simply update the interview status for a specific interview, without having to bother with the rest of the interview fields. 

The link to this form is found on the 'view_interview_details.html' page. Once the form has been successfully submitted and processed, the user will be redirected to 'view_interview_details.html'.

These functions:
-   display_update_status_form()
-   post_update_interview_status()
are behind both displaying the form & processing the form (once submitted by the user). Both these functions are found in services/interviews/update_interview_status.py. 

#### update_interview.html (WTForm):
Presents the user with the 'AddInterviewForm()' but pre-filled with the entry details for a specific interview. It gives the user the option to update any/all of the details for an interview. 

The link to this page is found on the 'view_interview_details.html' page. Once the form has been successfully submitted and processed, the user will be redirected to 'view_interview_details.html'. 

These functions:
-   display_update_interview_form()
-   post_update_interview()
are behind both displaying the form & processing the form (once submitted by the user). Both these functions are found in services/interviews/update_interview.py. 

### Interview Preparation:
All templates related to Interview Preparation.

#### interview_prep.html (WTForm):
Presents user with: 
- Research (where user is presented with link buttons to several well-known sources, each offering their advice/guidance on how to best answer commonly-asked interview questions).

- Background
    -> The user is presented with information provided for the company, application and interview in question

- A blank instance of the 'AddInterviewPrepForm()'. This form has 2 fields: 'Question' and 'Answer'. The idea behind this is the user provides a commonly asked question & then the user uses the 'answer' field to work out how they will/would answer this interview question.

- Existing interview prep done for this interview. So, as the user adds & submits each entry, these entries will be displayed below the form itself. Each entry is a link to the 'view_interview_prep_details.html', for that specific entry.

The link to this page is found on the 'view_interview_details.html' page, but is only displayed to the user when the status of the interview is 'upcoming'. Once the interview date & time is dated in the past, or if the user has updated the interview status to 'cancelled', 'post-poned', or 'done', then the user will no longer have the option to add new preparation for this interview. 

Once an entry is successfully submitted, the user will be redirected back to this template, but the page will be updated to display the newly-added entry below the form itself. 

These functions:
-   display_interview_preparation_form()
-   post_add_interview_preparation()
are behind both displaying the form (together with all the links/routing to be presented to the user) & processing the form (once submitted by the user). Both these functions are found in services/interview_preparation/add_interview_prep.py.

#### view_interview_prep_details.html:
Presents user with: 
-   The details for a specific Interview Prep entry.  
- Links to:
    -   Update /  delete the details for this specific entry 
    -   The Job application, Interview & Company linked to this Interview Prep entry, where each is link to view the details for the application, interview or company perspectively.  
    -   'Add Interview Preparation', where the user can add more interview preparation entries. 
    -   'View all Interview Preparation', where the user can view all entries added for this interview. 

The function 'display_interview_prep_details()', in services/interview_preparation/view_interview_prep_details.py, handles what gets displayed to this template (with all routes/links).

The link to this page is found on the 'view_interview_details.html' page. It's important to note that the link, to this template, will only be displayed to the 'view_interview_details.html' template when the interview's status is still 'upcoming'. Once the interview's status has been updated to any other status, this link will no longer be displayed to the user (on the 'view_interview_details.html' template). 

#### update_interview_prep.html (WTForm): 
Presents the user with the same layout & form as seen on the 'interview_prep.html' template. The difference is that the form (AddInterviewPrepForm()) is populated with the values for a specific interview preparation entry. This allows the user to update the details / values they've provided for the 'Question' & 'Answer' fields.  

A link to this form is found on the 'view_interview_prep_details.html' page.

These functions:
-   display_update_interview_prep_form()
-   post_update_interview_preparation()
are behind both displaying the form (together with all the links/routing to be presented to the user) & processing the form (once submitted by the user). Both these functions are found in services/interview_preparation/update_interview_prep.py.

### Job Offer:
All templates related to Job Offers.

#### add_job_offer.html (WTForm): 
Presents the user with a blank instance of the 'AddJobOffer()' Form. This form allows the user to add the details of a new job offer the user has received. The form asks the user to provide the job role & salary on offer, whether/not the user has accepted the offer & (if they've accepted the offer) the user can select the starting date when they'll start working for the company.

As I've linked job offers with their corresponding job application, the link to this page is found on 'view_application.html' page. Once the form has been successfully submitted and processed, the user will be redirected to 'view_job_offer.html'. 

These functions:
-   display_add_job_offer_form()
-   post_add_job_offer()
are behind both displaying the form (together with all the links/routing to be presented to the user) & processing the form (once submitted by the user). Both these functions are found in services/job_offers/add_job_offer.py.

#### view_job_offer.html:
Displays:
-   The details for a specific Job offer entry. 
-   Links to:
    -   Update / Delete the job offer 
    -   'Delete' the job offer
    -   The Job Application & Company, to which this job offer is linked, where each is a link to view the job application & company perspectively. 

The link to this page can be found on the pages / templates:
-   dashboard.html
-   view_application.html 
Note:   These links will only be displayed to the user when there is a job offer to display.

The function 'display_job_offer()', in services/job_offers/view_job_offer.py, handles what gets displayed to this template (with all routes/links).

#### update_job_offer.html (WTForm):
Presents the user with the 'AddJobOffer()' but pre-filled with the entry details for a specific job offer entry. The form allows the user to update the details for an existing job offer they've received. Once the form has been successfully submitted and processed, the user will be redirected to 'view_job_offer.html'.

These functions:
-   display_update_job_offer_form()
-   post_update_job_offer()
are behind both displaying the form (together with all the links/routing to be presented to the user) & processing the form (once submitted by the user). Both these functions are found in services/job_offers/update_job_offer.py.

### Address Book:
All templates related to the Address Book.

#### view_addressbook.html:
Displays:
-   Both Company & Individual contacts, where each entry is a link to view the contact in more detail
-   Links to:
    -   Add a new company contact
    -   View the company directory, with all the user's business contacts
    -   View contact directory with all the user's individual contacts

This page is divided into 2 sections:
-   Company (Contacts) 
    - Known as the company directory
-   Individual Contacts

The link to this template can be found on the navigation bar as 'Address Book'. The function 'display_address_book()', in services/address_book/view_address_book.py, handles what gets displayed to this template (with all routes/links).

### Company Contacts / Directory:
All templates relevant to all company contacts & their perspective profiles. 

#### add_company_form.html (WTForm):
Presents the user with a blank instance of the 'AddCompanyForm()'. 

The form allows the user to create the company profile for a company & based on the idea that job hunters may have a wish list of companies they may want to work for. Once submitted successfully, this will create a company 'contact', where the user can also gather research, make notes or create a job application. 

A link to this page can be found on the templates: 
-   'view_address_book.html' 
-   'view_company_directory.html' pages. 

Once the form has been successfully submitted and processed, the user will be redirected to the 'view_company_profile.html' for the newly-created company. 

These functions:
-   display_add_company_form()
-   post_add_company()
are behind both displaying the form & processing the form (once submitted by the user). Both these functions are found in services/company/add_company.py. 

#### view_company_directory.html:
Presents the user with: 
-   All the companies, that the user has added, as a list of company contacts, where each contact is a link to 'view_company_profile.html' (for that company's entry). 
-   Link to add a new company contact

The link to this page / template can be found on the 'view_addressbook.html'. The function 'display_all_companies_for_user()', in services/company/view_all_companies.py, handles what gets displayed to this template (with all routes/links).

#### view_company_profile.html:
Presents the user with: 
-   The details provided for a specific company entry. 
-   Links to:
    -   Update / Delete the company.
    -   Add Job Application, which will link to this specific company. 
    -   'View Company Website', if provided by the user. 
    -   Add a new note, or view existing notes, for this company

The link to this page / template can be found in a few places:
-   'view_application.html'
-   'view_address_book.html'
-   'view_company_directory'
-   'view_job_offer.html'
-   'view_interview_details.html'
-   'view_all_interviews.html'
-   'interview_prep.html
to name a few. 

The function 'display_company_profile()', in services/company/view_company_profile.py, handles what gets displayed to this template (with all routes/links).

#### add_company_job_application.html:
Presents the user with a blank instance of the 'AddCompanyJobApplicationForm()'.

This form allows the user to add a job application for a specific company. It is like the 'AddApplicationForm()' form but without the company details section, to make the application form shorter. I made this form as I believe it gives the user to add a job application for a company already in the user's company directory. Since the user has already provided details for the company, I don't believe there's any point making the user have to re-enter those details. By doing so, the form could be marginally shorter & simpler than the full 'AddApplicationForm()'. 

The link to this page can be found on the 'view_company_profile.html' page. Once the form has been successfully submitted and processed, the user will be redirected to the 'view_application.html' for the newly-created job application. 

These functions:
-   display_add_company_application_form()
-   post_add_company_job_application()
are behind both displaying the form & processing the form (once submitted by the user). Both these functions are found in services/company/add_company_job_application.py. 

#### update_company_profile.html (WTForm):
Presents the user with the 'AddCompanyForm()' where the fields are populated with the field values already provided for a specific company. The form allows the user to update the details for a specific Company's profile & includes details like the company name, location, industry, & company website. 

A link to this page is found on the 'view_company_profile.html' page. Once the form has been successfully submitted and processed, the user will be redirected to the 'view_company_profile.html'.

These functions:
-   display_update_company_profile_form()
-   post_update_company_profile()
are behind both displaying the form & processing the form (once submitted by the user). Both these functions are found in services/company/update_company.py. 

#### delete_company_profile.html (WTForm):
Presents the user with a blank instance of the 'DeleteCompanyForm()'. 

On this form, the user is presented with:
- A warning message: If the user deletes this company, it will delete all applications, interviews, interview_prep, & job offers linked to this company profile.
- A select field with 2 options: 
    -> Yes: Will delete the company profile & redirect the user to the 'view_address_book.html' page
    -> No: User will be redirected to the 'view_company_profile.html' page. 

This form basically allows the user to delete a company entirely. The link to this template can be found on 'view_company_profile.html'. 

These functions:
-   display_delete_company_form()
-   post_delete_company()
are behind both displaying the form & processing the form (once submitted by the user). Both these functions are found in services/company/delete_company.py. 

### Individual Contacts:
All templates linked directly to individual contacts:

#### add_new_contact.html (WTForm):
Presents the user with a blank instance of the 'AddNewContactForm()'. This form allows user to add details for a particular contact, including the individual's full name, contact details & a link to their Linkedin Profile. 

This is based on the idea (and from personal experience) that job hunters will want to build a network of contacts. The user could also use this form to add recruiters & hiring managers at the company they're applying to (or want to apply to in the future). 

A link to this page can be found on the 'view_address_book.html' & 'view_contacts.html' pages. Once this form has been successfully submitted & processed, the user will be redirected to 'view_contact_details.html'.

These functions:
-   display_add_new_contact_form()
-   post_add_new_contact()
are behind both displaying the form & processing the form (once submitted by the user). Both these functions are found in services/contacts_directory/add_new_contact.py. 

#### view_contacts.html:
Presents the user with: 
-   All Contact entries added by this user
    -   Where each contact entry is a link to 'view_contact_details.html'
-   Link to 'Add New Contact', which directs to 'add_new_contact.html'

A link to this template can be found on 'view_address_book.html'. The function 'display_contacts_for_user()', in services/contacts_directory/view_contact_list.py, handles what gets displayed to this template (with all routes/links).

#### view_contact_details.html:
Presents the user with: 
-   Details for a specific contact, including the contact's Full name, Job title, email address, contact number. It also includes the name of the company where this contact works & a link to the contact's linkedin profile.  

-   Links to:
    -   Update / Delete the contact
    -   View the contact's Linkedin profile, which displays when the user has provided a link to their linkedin profile
    -   View the Addressbook & View the contacts directory

The link to this page can be found on:
-   'view_addressbook.html'
    -   For every contact displayed on the addressbook
-   'view_contacts.html
    -   For every contact displayed on the addressbook

The function 'display_contact_details()', in services/contacts_directory/view_contact_details.py, handles what gets displayed to this template (with all routes/links).

#### update_contact_form.html (WTForm):
Presents the user with the 'AddNewContactForm()' but pre-filled with the entry details for a specific individual contact entry. This form gives the user the option to update a contact entry at any point, which is useful when you get to know more about a contact over time or with extra research. 

The link to this template can be found on 'view_contact_details.html'. Once this form has been successfully submitted & processed, the user will be redirected to 'view_contact_details.html'.

These functions:
-   display_update_contact_form()
-   post_update_contact()
are behind both displaying the form & processing the form (once submitted by the user). Both these functions are found in services/contacts_directory/update_contact.py. 

### Notes:
All templates related to notes.

#### view_all_user_notes.html:
The notes, displayed to this template, are split into 2 sections: 
-   Application notes, notes linked specifically to a job application
-   Company notes, notes linked specifically to a company contact 

Displays:
-   Company notes, where each entry is a link to the template 'view_specific_company_note.html'
-   Application Notes, where each entry is a link to the template 'view_app_note_details.html'

-   Links to view the company directory & 
    -   View the company directory
    -   'View all job applications

The link to this page / template can be found on the navigational bar & is labelled as 'Notes'. The function 'display_all_user_notes()', in services/display_all_notes.py, handles what gets displayed to this template (with all routes/links).

#### Company Notes:
All templates related specifically to Company Notes, where each note is linked to a specific company.

##### add_company_note.html (WTForm):
Presents the user with a blank instance of the 'AddCompanyNoteForm()'. This form allows the user to add a note for a specific company, which can be accessed at any point from the company's profile.

A link to this page can be found on the 'view_company_profile.html' & 'view_company_notes.html' templates. Once the form has been successfully submitted and processed, the user will be redirected to the 'view_specific_company_note.html'.

These functions:
-   display_add_company_note_form()
-   post_add_company_note()
are behind both displaying the form & processing the form (once submitted by the user). Both these functions are found in services/company_notes/add_company_note.py. 

##### view_specific_company_note.html:
Presents the user with: 
-   The entry details for a specific company note

-   Links to:
    -   Update / Delete the note
    -   Go back to Company Notes
    -   'View company profile'
    -   'Add New Note'

The link to this page / template can be found on the 'view_all_notes.html', if there are any company notes, linked to this company, to display.

The function 'display_company_note_details()', in services/company_notes/view_specific_note.py, handles what gets displayed to this template (with all routes/links).

##### view_company_notes.html:
Presents the user with: 
-   All company note entries for a specific company
    -   Each entry is a link to 'view_specific_company_note.html'.
-   Links to:
    -   'Add New Note'
    -   'Return to company profile'
    -   'Return to Address book'

The link to this template can be found on the template 'view_company_profile.html'. The function 'display_all_notes_for_a_company()', in services/company_notes/view_all_company_notes.py, handles what gets displayed to this template (with all routes/links).

##### update_company_note.html (WTForm):
Presents the user with the 'AddCompanyNoteForm()' but pre-filled with the entry details for a specific company note, allowing the user to update the details that the user has already provided for this note. 

A link to this page is found on the 'view_specific_company_note.html' page. Once the form has been successfully submitted and processed, the user will be redirected back to 'view_specific_company_note.html'.

These functions:
-   display_update_company_note_form()
-   post_update_company_form()
are behind both displaying the form & processing the form (once submitted by the user). Both these functions are found in services/company_notes/update_company_note.py. 

#### Application Notes:
All templates related specifically to Application Notes, where each note is linked to a specific job application.

##### add_application_note.html (WTForm):
Presents the user with a blank instance of the 'AddApplicationNoteForm()', which includes 2 fields: a note heading & body / content. This form allows the user to add a note for a specific application, which is useful at any stage of the job application. 

The link to this page can be found on the following templates:
-   'view_application.html'
-   'view_notes_for_application' 

Once this form has been successfully submitted & processed, the user will be redirected to 'view_app_note_details.html'. A link to this page can be found on the template 'view_application.html', labelled as '+ Note'. 

These functions:
-   display_application_note_form()
-   post_application_add_note()
are behind both displaying the form & processing the form (once submitted by the user). Both these functions are found in services/application_notes/add_app_note.py.

##### view_notes_for_application.html:
Presents the user with: 
-   All notes the user has added for a specific job application, where each note is a link to 'view_app_note_details.html'.  
-   Links to:
    -   'Add new note for (company name)
    -   'Go back to application'
    -   'View company profile'

The link to this page can be found on:
-   'view_application.html'
-   'view_interview_details.html'

The function 'display_application_notes()', in services/application_notes/view_application_notes.py, handles what gets displayed to this template (with all routes/links).

##### view_app_note_details.html:
Presents the user with: 
-   The details for a specific application note, including the date the user added this note, the note title & note's content

- links to:
    -   Update / Delete the note
    -   Add a new note
    -   Go back to application
    -   Go back to Application Notes
    -   View Company Profile

The link to this page can be found on the templates:
-   'view_application.html'
-   'view_interview_details.html'

The function 'display_application_note_details()', in services/application_notes/view_app_note_details.py, handles what gets displayed to this template (with all routes/links).

##### update_application_note.html (WTForm):
Presents the user with the 'AddApplicationNoteForm()' but pre-filled with the entry details for a specific note. Since the link to 'update_application_note' is added to a specific note's 'view_app_note_details.html' page, it will only update the details of this specific note. 

The form is designed to let the user update their existing notes; to fix minor mistakes or to add more content to a note. Once this form has been successfully submitted & processed, the user will be redirected to 'view_app_note_details.html'.

These functions:
-   display_update_app_note_form()
-   post_update_app_note()
are behind both displaying the form & processing the form (once submitted by the user). Both these functions are found in services/application_notes/update_app_note.py.


