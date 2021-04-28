# Project Hunt Manager

## Video Demo:  <URL HERE>

## Description: 
A web-based application for any one looking to manage their job hunting. Its intended to be a place where a user can store job applications, interviews, interview preparation, notes, & contacts. Plus the user can add companies from their wishlist. 

The application uses Python, Flask, WTForms, HTML, CSS & a little JavaScript. 

I have narrowed down the application for fellow software engineers, so the Job application form is very much in the scope of the software engineering industry. 

## Pages / Templates:

### Layout: 
The general layout for all html templates, which is referenced to by all the remaining html templates. This template also includes the:
- Meta data
- links (favicons, styles, bootstrap & stylesheets)
- Scripts (JQuery)
- Page structure (header, body & footer)
- Nav Bar links 


### About us:
This page tells/informs the user:
- what this application is about, 
- why I developed this application, 
- the research I carried out before putting this application together,
- security, & 
- how they could contact me if they want to. 


### Form Templates: 
Each of these html templates provide the user with a WTForm, asking relevant details from the user. 

#### register.html:
Presents the user with a blank instance of the 'RegisterUserForm()' to create a Job Hunt Manager account.

The form provides the user with fields to provide their email address, a username of their choice, their password of choice & to confirm their password of choice. The page also includes a warning to potential users that the password they provided will be hashed but there is no password salting, with the recommendation to rather use fictional information - since this application is intentioned to only be used for testing purposes (for now). I want to continue looking around for a good salting algorithm, with the intention of both hashing & salting passwords - primarily because I value the importance of security & information protection. 

The link to this form is added to the Nav bar, for any user that has not successfully logged in (yet).

#### login.html: 
Presents the user with a blank instance of the LoginForm() form. The link to this page is found on the Nav bar at the top of the page, for any user that has not successfully logged in (yet).

On this form, the user is presented with the fields: Username & password. The 'Username' field will also accept the user's email address if the user prefers to rather use their email address.

#### change_password.html: 
Presents the user with a blank instance of the ChangePasswordForm() form. The link to this page is found on the 'userprofile.html' page.

This form allows the user to change their account password & has only 2 fields: password & confirm password. If the user uses the same password in both fields and the password meets the minimal requirements, the user will be redirected back to 'userprofile.html'.  

#### add_job_application.html:
Presents the user with a blank instance of the 'AddApplicationForm()'. The form allows the user to add a job application, with all the details of a regular job application.

The link to this page is found on the 'dashboard.html' & 'applications.html' pages.

#### add_application_note.html:
Presents the user with a blank instance of the 'AddApplicationNoteForm()'. This form allows the user to add a note for a specific application, which is useful at any stage of the job application. 

The link to this page is found on the 'view_application.html' & 'view_notes_for_application' pages. 

#### add_interview.html:
Presents the user with a blank instance of the 'AddInterviewForm()'. 

This form allows the user to add the details for an upcoming interview, with its date, time & the medium for the interview (video/phone call) or (if in person) the contact details & location for the interview. 

This interview will be linked to a specific application & the link to this form is added to the 'view_application.html' page.

#### add_job_offer.html: 
Presents the user with a blank instance of the 'AddJobOffer()' Form. This form allows the user to add the details of a job offer the user has received, 

As I've linked job offers with their corresponding job application, the link to this page is found on 'view_application.html' page.

#### add_company_form.html:
Presents the user with a blank instance of the 'AddCompanyForm()'. 

The form allows the user to create the company profile for a company & based on the idea that job hunters may have a wish list of companies they may want to work for. Once submitted successfully, this will create a company 'contact', where the user can also gather research, make notes or create a job application. 

A link to this page can be found on the 'view_address_book.html' & 'view_company_directory.html' pages.

#### add_company_note.html:
Presents the user with a blank instance of the 'AddCompanyNoteForm()'. This form allows the user to add a note for a specific company, which can be accessed at any point from the company's profile.
A link to this page can be found on the 'view_company_profile.html' page. 

#### add_company_job_application.html:
Presents the user with a blank instance of the 'AddCompanyJobApplicationForm()'.

This form allows the user to add a job application for a specific company. It is like the 'AddApplicationForm()' form but without the company details section, to make the application form shorter. I made this form as I believe it gives the user to add a job application for a company already in the user's company directory. Since the user has already provided details for the company, I don't believe there's any point making the user have to re-enter those details. By doing so, the form could be marginally shorter & simpler than the full 'AddApplicationForm()'. 

The link to this page can be found on the 'view_company_profile.html' page.

#### add_new_contact.html:
Presents the user with a blank instance of the 'AddNewContactForm()'.
Allows user to add details for a particular contact, including the individual's full name, contact details & a link to their Linkedin Profile. 

This is based on the idea (and from personal experience) that job hunters will want to build a network of contacts. The user could also use this form to add recruiters & hiring managers at the company they're applying to (or want to apply to in the future). 

A link to this page can be found on the 'view_address_book.html' & 'view_contacts.html' pages. 

#### interview_prep.html: 
Presents user with: 
- Research (where user is presented with link buttons to several well-known sources, each offering their advice/guidance on how to best answer commonly-asked interview questions).
- Background
    -> The user is presented with information provided for the company, application and interview in question

- A blank instance of the 'AddInterviewPrepForm()'. This form has 2 fields: 'Question' and 'Answer'. The idea behind this is the user provides a commonly asked question & then the user uses the 'answer' field to work out how they will/would answer this interview question.
- Existing interview prep done for this interview. So, as the user adds & submits each entry, these entries will be displayed below the form itself.

The link to this page is found on the 'view_interview_details.html' page, but is only displayed to the user when the status of the interview is 'upcoming'. Once the interview date & time is dated in the past, or if the user has updated the interview status to 'cancelled', 'post-poned', or 'done', then the user will no longer have the option to add new preparation for this interview. 

#### update_application.html: 
Presents the user with the the AddApplicationForm() but pre-filled with the entry details for a specific application. This allows the user to update fields or to add values to fields that that they may have previously left blank - especially since not all job specs provide all the information up front. 

The link to this page can be found on the 'view_application.html' page.

#### update_application_note.html:
Presents the user with the 'AddApplicationNoteForm()', but is populated with the values originally provided for this specific application note. The link to this page is found on the 'view_app_note_details.html' page. 

### update_company_profile.html:
Presents the user with the 'AddCompanyForm()' where the fields are populated with the field values already provided for a specific company. The form allows the user to update the details for a specific Company's profile & includes details like the company name, location, industry, & company website. 
A link to this page is found on the 'view_company_profile.html' page. 

#### update_company_note.html: 
Presents the user with the 'AddCompanyNoteForm()', where the fields are pre-populated with the values already provided for a specific company note. It allows the user to update the note however the user wants & then to submit those changes. 
A link to this page can be found on the 'view_specific_company_note.html' page.

#### update_contact_form.html:
Presents the user with the 'AddNewContactForm()' already pre-filled with the values already provided for a specific contact. 
Uses the 'add_new_contact.html' Form to allow the user to update the details already provided for an existing contact by the current user. 

The link to this page is found on the 'view_contact_details.html' page.

#### update_email.html:
Presents the user with a blank instance of the 'UpdateEmailAddressForm()', which allows the user to update the email address linked to their account. The user is also asked to 'confirm' their email address, just to iron out potential human typing errors. 

This form is accessible from the 'userprofile.html' page, to the right of the email address listed under their user profile. If the form is successfully submitted, the email address will be updated on the user profile.

#### update_interview.html: 
Presents the user with the 'AddInterviewForm', populated with the values already provided for a specific interview, allowing the user to update which value they would like. 
The link to this page is found on the 'view_interview_details.html' page.

#### update_interview_prep.html: 
Presents the user with the same layout & form as 'interview_prep.html', but the form on this page is populated with the values for a specific interview preparation entry. This allows the user to update what they've provided for the 'Question' or 'Answer' fields.  

A link to this form is found on the 'view_interview_prep_details.html' page.


#### update_interview_status.html:
Presents the user with a blank instance of the 'UpdateInterviewStatusForm()'. 

This form gives the user the option to update the interview status for a specific interview, without having to bother with the rest of the interview fields. Its intended to be used to update an interview, after the inteview has been completed / cancelled / post-poned. 

The link to this form is found on the 'view_interview_details.html' page.

#### delete_account.html: 
Presents the user with a blank instance of the 'DeleteAccountForm()'. This form presents the user with:
- A warning message asking the user to confirm if they want to delete their account.
- A 'password' field (where the user provides the current password for their Job Hunt Manager account) 
- 'confirm password' field -> where the user enters the same account password a second time.

If the password is correct, the user's account is successfully hard deleted and the user is redirected back to the 'index.html' page. Otherwise the user is redirected to the same 'DeleteAccountForm()' & an error message to "Complete all fields".

#### delete_company_profile.html:
Presents the user with a blank instance of the 'DeleteCompanyForm()'. 
On this form, the user is presented with:
- A warning message: If the user deletes this company, it will delete all applications, interviews, interview_prep, & job offers linked to this company profile.
- A select field with 2 options: 
    -> Yes: Will delete the company profile & redirect the user to the 'view_address_book.html' page
    -> No: User will be redirected to the 'view_company_profile.html' page. 



















