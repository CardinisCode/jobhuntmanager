Project Management

#1: [ ] Setup:
        [X] Connect directory to Github
        [X] Create repo directory
        [X] Create service directory
        [X] Create style directory
        [x] Set up SQLite3 database
                [X]     Create db
                [x]     Create connection to db
        [X]     Create repo for users
                [X]     Within Users:
                        Create file consisting of classes to perform various SQL queries
        [X] Create templates directory
                -> Create files:
                [x]     layout.html
                [x]     register.html 
                [x]     home.html
                [x]     applications.html
                [x]     interviews.html
                [x]     calendar.html
                [x]     tipsandadvise.html
                [x]     userprofile.html

------------------------------------------------------------------------------

#2: [x] Registration   
        [X]     Create registration.py
        [x]     Add registration router & function
                [x]     GET 
                [x]     POST
        [X]     Verify user details dont already exist
                [x]     username
                [X]     email address
        [X]     Create rules for password 
                [X]     Add these requirements on the html page
                [X]     Verify that the password provided meets those requirements
        [X]     Add user to user table (sqlite3 database)
                [X]     username
                [X]     hash password
                [X]     email address
                [X]     date & time account was created

------------------------------------------------------------------------------

#3: [x] Login
        [x]     Create a service page login.py
                [x]     Create post_login functionality
                        [x]     Verify email address against db
                                [x]     search db for email address provided
                                [x]     hash login password provided
                        [x]     hash login password & compare to hashed password for that user
        [x]     If valid: login in user
                [x]     Take user to home page
        [x]     If invalid:
                [x]     username doesn't exist:
                        [x]     provide error message to login page
                [x]     password doesn't match password on system for that user
                        [x]     provide error message to login page
                        [ ]     fix problem -> it displays error message 2x 

------------------------------------------------------------------------------

#4: [x] Layout.html
        [x]     Create a root templates folder
        [x]     Create the Layout template 
        [x]     Add the necessary libraries
        [x]     Include a banner to display notifications to user
        [x]     Include a footer 

------------------------------------------------------------------------------


#5: [x] Home page
        [x]     Create homepage.html
        [x]     Create route for index.html 
                [x]     include the @login decorator
                [X]     Create index function
                        [X]     GET:
                                -> render template to display index.html
                        [X]     POST:
                                -> refer to create_homepage_content function in services directory
        [x]     In index.html 
                [x]     Design layout of headings, messages & links
                [x]     Design layout for tables & add headings:
                        [x]     Interviews
                        [x]     Applications
                        [x]     Job Offers
                [x]     Create Company Directory table
                        [x]     id (AUTOINCREMENT) 
                        [x]     Company name TEXT (From add_application)
                [x]     Create Company Repo
                                [X]     Create a method to Add a new company to the profile 
                                        -> Returns the company Id
                [X]     Add Repo to application.py

------------------------------------------------------------------------------

#6: [x] Job Applications:
        [x]     Add interview 
                [x]     Create a SQL query to add values to relevant table
                [x]     Create html page
                [x]     Create route & function
                        [x]     GET: render template to the html page
                                [x]     Create the add_interview form 
                        [x]     POST: Take the info & display user's input on a 2nd html page
                                [x]     Create a interview_details html page 
                                [x]     Create a function to grab the details & insert the details into the relevant SQL table
                                [x]     Display the details to the interview_details html page
        [x]     Display Interviews
                [X]     Create SQL query to grab top 10 interviews by date in DESC order 
                [ ]     Create function to display details to interviews.html
                        [x]     calls on SQL query to grab top 10 interviews 
                        [x]     saves the details from this query & saves them in a Dict
                        [x]     render these details to interviews.html
                [x]     Design the html page to display the details in a table
                [x]     Set conditions for what gets displayed to the table in html page
                        [x]     If 'medium' == 'other' -> Display the info for 'other_medium'
                        [x]     Change the values from variable names -> actual text 
                                EG: "in_person" -> "In person"
                [x]     Bugs: 
                        [x]     Data displayed is ordered by Date but not by time, so all rows of a specific date are in mixed order
                                [x]     Correction: In SQL query: Sort by Date, then by time 
                        [x]     Form on 'add_interview.html' does not display data for 'other_medium' on interview_details.html 
                                if user selects 'Other' for 'video_medium' field
                                [x]     Correction: Update function  post_add_interview() to display 'other_medium' 
                                        when 'Other is selected for 'video_medium'
                        [x]     Interview status' value is displayed in it's variable form.
                                [x]     Correction: Capitalise the value of 'status'
                                        EG: 'status' -> 'Status'

------------------------------------------------------------------------------ 

#7: [x] Add Interview
        [x]     Add route & function for "/add_interview"
        [x]     Create InterviewHistoryRepo
                [x]     Create a method to grab details and add to repo:
        [x]     GET
                [x]     Create form on add_interview.html:
        [x]     POST
                [x]     Grab details from form
                [x]     call on relevant method to add details to repo
                [ ]     Display message to user to confirm the interview has been added

------------------------------------------------------------------------------
#8: [x] In service/homepage, update create_homepage_content (function) 
        (All content displayed to Index.html)
        [x]     Grab today's date
        [x]     Display Today's date on index.html
        For Applications:
        [x]     Create a SQL query to pull together all applications made today / current day. 
        [x]     Count the number of applications and save that to a variable
                [x]     Display to page:
                        EG: "You have made {{ X }} number of applications today"
                [x]     If no applications made today: 
                        [x]     Display message to user:
                                "Have you had any applications yet?" 
                        [x]     Add button / link: 
                                [x]     Add an application
        For Interviews:
        [x]     Set up a Repo for Interview History
        [x]     Connect to this new repo in your applications.py
        [x]     Create a SQL query to pull all interviews for current date
        [x]     Pull all the day current_day interviews to a variable
                [x] Save how many items were returned & display to user
                        EG: "You have {{ X }} number of Interviews today" 
                [x] IF no interviews lined up today: 
                        EG: "You have {{ X }} number of Interviews today" 
                        [x]     Add option to add lined up interview
                                "Have a lined up Interview? Add it!"

------------------------------------------------------------------------------
#9: [x] Redo Add_application functionality using WTForms:
        [x] Create a form Class for Applications
                [x]     Create fields in AddApplicationForm class
        [x]     Render fields on test_add_application.html 
        [x]     Grab data from user input
                [x]     Create  function to grab the data from the fields on test_add_application.html 
                [x]     Create a test_details.html page 
                [x]     Format the data received & add it to a dict
                [x]     Render the data to the test_details.html page 
        [x]     Replace:
                [x]     Form: Data on add_application.html with test_add_application.html
                [x]     Details: Data on test_details.html with application_details.html 
                        [x]     REMEMBER: update the post route to "/add_application"
                [x]     Function: function with post_add_application()
                [x]     Route: "/test_add_application" with "/add_application"
        [x]     Add the option to insert the details into "application_history" table
                [x]     Make sure it works as expected
                
------------------------------------------------------------------------------

#10: [x] Redo add_interview functionality using WTForms:
        [x]     Create a test_add_interview route with its own function
                [x]     GET: directs to "test_add_interview.html
                        [x]     Structure html page as a form and make sure it displays the fields as expected
                [x]     GET: directs to a function post_add_interview_test
                        [x]     Add user input to a dict & render to test_interiew_details.html page
        [x]     Replace:
                [x]     Form: Data on add_interview.html with test_add_interview.html
                [x]     Details: Data on test_inteview_details.html with interview_details.html 
                        [x]     REMEMBER: update the post route to "/add_interview"
                [x]     Function: function with post_add_interview()
                [x]     Route: "/test_add_interview" with "/add_interview"
        [x]     Add the option to insert the details into "interviews_history" table
                [x]     Make sure it works as expected

------------------------------------------------------------------------------
#11: [x] Display Applications & Interviews:
        [x]     Applications page
                [x]     Make sure all applications display as expected on Applications.html
                [x]     Check that all entries are in order of the most recent application first
                [x]     Optimise the data displayed on Applications.html
                        [x]     Create SQL query to grab the top 10 applications 
                        Order by Date
                        [x]     Adjust function to call this SQL query & rename function accordingly
                        [x]     Grab values, improve their presentation & add to dict
                        [x]     Display the updated values to applications.html
        [x]     Interviews page
                [x]     Make sure all interviews display as expected on Interviews.html
                [x]     Check that all entries are in order of the most recent interview first
        [x]     Index page
                [x]     Top 5 Applications: 
                        [x]     Check that it displays the latest 5 application entries
                        [x]     Check that all entries are in order 
                                of the most recent application first (By Date)
                        [x]     Improve how Fields & headings are displayed to the table        
                [x]     Top 5 Interviews:
                        [x]     Create a SQL query to grab last 5 interviews for this user
                                (ORDER BY: First: Date, Second: Time)
                        [x]     Update function homepage.create_homepage_content():
                                [x]     Call on relevant SQL query to grab top_five_interview details
                                [x]     Add fields to variables & add to dict
                                [x]     render dict to index.html 
                        [x]     Customise the table on index.html:
                                [x]     Recreate the table to receive top5interviews
                        [x]     Test that it displays the top 5 interviews as expected

------------------------------------------------------------------------------

#12: [x] Add a fixed side bar to all pages

------------------------------------------------------------------------------

#13: [x]  Update Application_history when user adds a new interview
        [x]     Check if that company name already exists in application_history for that user
                [x]     Create SQL query to check a company name in application_history
                [x]     If yes: Update the interview_stage for that application 
                        in application_history
                        [x]     Update interview_stage in application_history
                        [x]     Update how interview stage is displayed to user:
                                [x]     applications.html
                                [x]     interview_details.html
                                [x]     index.html
                [x]     If no: Add a new application for that company in application_history
                        [x]     In post_add_interview, call insertApplicationDetailsToApplicationHistory() with interview_details


------------------------------------------------------------------------------

#14: [x]  Add shortcuts on tables:
        [x]     Add "+" to represent 'add_application' feature to:
                [x]     applications.html
                [x]     top5applications on index.html
        [x]     Add "+" to represent 'add_interview' feature to":
                [x]     interviews.html
                [x]     top5interviews on index.html

------------------------------------------------------------------------------

#15: [x] Redo Register using WTForms 
        [x]     Install pip3 install passlib
        [x]     Create a Register class & allocate fields
                [x]     Username 
                [x]     Password
                [x]     Confirm Password
                [x]     Email
                [x]     Submit field
                (Refer to https://pythonprogramming.net/flask-user-registration-form-tutorial/)
        [x]     Create test Register page & allocate it a route & function 
        [x]     GET: render test_register.html
        [x]     POST: Create function
                [x]     Grab values from form & test that they're pulling through as expected
                [x]     Create SQL query in users table, to check if the username provided already exists
                [x]     Create SQL query in users table, to check if the email address provided 
                        already exists
                [x]     Encrypt password
                (refer to https://pythonprogramming.net/flask-registration-tutorial/?completed=/flask-user-registration-form-tutorial/)
        [x]     If all successful: replace the current with the updated registeration process

------------------------------------------------------------------------------

#16: [x] Redo Register using WTForms 
        [x]     Create a Login class & allocate fields
                [x]     Username 
                [x]     Password
                [x]     Submit field
        [x]     Create test Login page & allocate it a route & function 
        [x]     GET: render test_login.html
        [x]     POST: Create function
                [x]     Grab values from form & test that they're pulling through as expected
                [x]     Create SQL query in users table, to check if the username provided already exists
                        already exists
                [x]     Verify that the password on file matches the password that the user provides (via the form)
        [x]     If all successful: replace the current files & functions with the updated login process

------------------------------------------------------------------------------

#17: [x]        Create UserProfile Content
        [x]     Create a function to pull relevant data & render it to userprofile.html
                [x]     Display username
                [x]     Display email 
        [x]     From the route function call above function

------------------------------------------------------------------------------

#18: [ ]  Update post_add_application functionality
        [ ]     Check if company name already exists in application_history
        [ ]     If company_name already exists in application_history
                [ ]     Updates details for entry in application_history
        [ ]     Else:
                [ ]     Treats application as brand new application
                        [ ]     Adds new_application as new entry in applications_history

------------------------------------------------------------------------------

ONGOING:
[ ]     Bugs to be fixed:
        [x]     There's a huge gap at the top of each page, due to the side bar.
        [x]     Details received from 'add_interview.html' display on interview_details.html' 
                as text boxes that can be edited. 
                [x]     Figure out solution to adjust the values for each field so they display as plain text.
        [x]     Interview_details.html: interviewer_names field is an edit text box
        [x]     Interview History: 
                [x]     "Video / Online" is displaying "skype" instead of "Skype"
                [x]     In_person interviews are displaying "Contact number" 
                        instead of "In Person"
                [x]     In person interviews are displaying the medium (eg: "zoom")
                        Where medium should display "N/A" 

------------------------------------------------------------------------------

Yet to do:

#: [ ]  Add Companies to CompanyDirectory table
        [ ]     Create SQL query to check a provided company name (arg) 
                against those saved in the company directiory
        [ ]     Create SQL query to add a company to the CompanyDirectory
        [ ]     in post_add_application(), Check if company already exists in CompanyDirectory
                        [ ]     If not: Add company to CompanyDirectory
        [ ]     in post_add_interview(), check if company already exists in CompanyDirectory
                [ ]     If No:
                        [ ]     Add company to CompanyDirectory  


#: [ ]  Index page: 
        [ ]     Update to Display how many applications user has submitted over the last 7 days
                [ ]     Create SQL Query to grab all applications added over the past 7 days
                [ ]     Pull that data in homepage.py
                [ ]     Calculate interview count
                [ ]     Display to Index.html
        [ ]     Update to Display how many Interviews user has submitted over the last 7 days
                [ ]     Create SQL Query to grab all interviews added over the past 7 days
                [ ]     Pull that data in homepage.py
                [ ]     Calculate interview count
                [ ]     Display to Index.html

#: [ ]  Job offers:
        [ ]     Create SQL table "job_offers"
        [ ]     Creating a new Job offer
                [ ]     Create SQL query to add a job offer to the job_offers table
                [ ]     Create html form to allow user to input a new job offer
                [ ]     Add Side bar option to add a job offer
        [ ]     Display Job Offers added by user
                [ ]     Create SQL query to grab top5JobOffers for the user
                [ ]     Display top5JobOffers to Index.html

#: [ ] Nav bar 
        [ ]     import relevant library for icons
        [x]     import libraries for css styles
        [x]     Create structure for Nav bar:


#: [ ] interview_preparation
        [ ]     Add Interview Preparation:
                [ ]     Create template add_interview_prep.html
                [ ]     Create route & function
                [ ]     Create InterviewPrep class 
                        [ ]     Add top 10 interview Q's as the fields 
                                & set values as Text fields 
                        [ ]     Add button -> To save the user's answers
                [ ]     GET: Design form on add_interview_prep
                        [ ]     Pull form fields & display to user
                        [ ]     Add option to get advice on how to answer these Q's
                                [ ]     Link to Indeed's Q behind the Q (Indeed)
                [ ]     POST: 
                        [ ]     Create post_add_interview_prep function 
                        [ ]     Create repo: InterviewPrepRepository 
                        [ ]     Create interview_prep table
                        [ ]     Create SQL query to add an post_add_interview_prep entry into 
                        the interview_prep table
                        [ ]     Save details from current entry to interview_prep table

        [ ]     Display Interview Preparation:
                [ ]     Create SQL query to grab Top 10 Interviews_prep entries for that user
                [ ]     Create route & function
                [ ]     GET: Display these entries onto interview_prep.html page in table

#: [ ] Styling
        [ ]     Add a CSS file
        [ ]     #1:     Nav bar
        [ ]     #2:     Headings
        [ ]     #3:     buttons (general)
        [ ]     #4:     Tables
        [ ]     #5:     Forms
        [ ]     #6:     Pages:
                [ ]     #1:     Home page
                [ ]     #2:     Applications
                [ ]     #3:     User Account
                [ ]     #4:     Calendar
                [ ]     #5:     View Applications history
                [ ]     #6:     Add Applications
                [ ]     #7:     Update Applications
                [ ]     #8:     Delete Applications
                [ ]     #9:     View Interviews history
                [ ]     #10:    Add Interview
                [ ]     #11:    Update Interview
                [ ]     #12:    Delete Interview
        [ ]     #8:    Side bar

#: [ ] Updating details 
        [ ]     Add option to Update a make changes to individual entries:
                [ ]     Interviews
                [ ]     Applications
                [ ]     Job Offers
                -> Where the user will presented with the relevant form with all that form's field names & data provided for that entry
                -> User Can SAve their changes or Delete the entry altogether or go back without making changes.
        [ ]     Add option to delete an entry:
                [ ]     Applications
                [ ]     Interviews
                [ ]     Job Offers
                -> Offer the user the chance to confirm that they'd like delete that entry.
        ->      User will be instructed to provide the company name
                ->      User will be shown (in table format) all applications made to that company
                ->      User can select an application 
                        ->      User will be given the options to:
                                ->      Add / view Interviews 
                                ->      add / view Communication received
                                ->      Add / view notes made


#: [ ] Add Interview prep
        [ ]     Create method to Insert entry into InterviewPrepRepository
        [ ]     Create add_interview_prep.html
        [ ]     Add router & function in application.py
        [ ]     GET 
                [ ]     Render template to add_interview_prep.html
        [ ]     POST
                [ ]     Grab each answer 
                        -> Number each one
                [ ]     Call on the relevant method to store these answers as 1 entry
                [ ]     redirect to interview_preparation.html         

        [ ]     Create form:
                [ ]     Top 10 Interview Q's 
                        [ ] With text boxes for user to give their answer
                [ ]     Add option to get advice on how to answer these Q's
                        [ ]     Link to Indeed's Q behind the Q (Indeed)
                [ ]     Add button -> To save the user's answers
                        

#: [ ] Calendar page
        [ ]     Add link to calendar.html on layout.html (top bar)
        [ ]     Create calendar
        [ ]     Create a route & function on applications.html
        [ ]     Add Calendar functionality
                [ ]     Add to calendar button
                [ ]     Delete option
                [ ]     Update option
                [ ]     Option to select a date to see the events added

#: [ ] User Profile
        [ ]     Add option for user to add more details: 
                [ ]     Create form: add_extra_user_details.html
                        [ ]     Industry of preference
                        [ ]     Job title
                        [ ]     Companies of interest (10)
                        [ ]     Country -> For currency
        [ ]     Change password -> redirect user to change_password.html
                [ ]     create change_password.html
        [ ]     Delete account -> Redirect user to delete_account.html
                [ ]     create delete_account.html

#: [ ]  Add Search functionality:
        [ ]     Update the class for each of the follow to include a search "company" functionality
                [ ]     Applications.html
                [ ]     Interviews.html
                [ ]     JobOffers.html
                [ ]     Interview_prep.html


  ------------------------------------------------------------------------------ 

#: [ ] Potential extra features
        [ ]     Add Option to postpone an interview
        [ ]     Add Option to Add technical testing Interview (prior to actual Interview)
        [ ]     Add Option to Add research for a company
                [ ]     Add to: Company Directory table
                        [ ]     Main HR person TEXT (From research)
                        [ ]     Company Core values (from research)
                        [ ]     GlassDoor review url ( TEXT ) (from research)
                        [ ]     Website url TEXT (From research)
                [ ]     Display this directory to the Home page (in table)
                [ ]     Add column to ApplicationHistory: 
                        -> Website URL
        [ ]     User account 
                [ ]     Option to deactivate certain features
                [ ]     dark / light colour scheme
        [ ]     Add top 10 companies user would love to work for
        [ ]     Job board
                [ ]     Displays jobs available by:
                        [ ]     Preferred companies
                        [ ]     Job role
                        [ ]     Specific job portals
        [ ]     Tips & advise (Resources board)
                ->      Recommend people to add on LI
                ->      Interview Advise sites 
                        [ ]     LI
                        [ ]     Becky Webber
                        [ ]     Indeed
                ->      CV writing sites
                ->      LI Networking 
                        ->      advise sites
                        ->      Recommendations on who to follow on LI
        [ ]     Progress bar for user profile 
                EG You have completed x% of your user profile 
                [ ]     Displayed on Home page
                [ ]     Give option to update user profile details -> refer user to add_extra_user_details.html (form)
        [ ]     Add 'Interests' to add_extra_user_details.html form

        [ ]     Add advertising
                [ ]     Customize to user's industry or even job title 
                        -> Based on what user provides in user profile
                [ ]     If user doesn't provide Industry or Job role or Interests
                        -> General advertising

        [ ]     Preparing a Cover letter
        [ ]     Add option to allow user to plan contents of their CV section by section
                [ ]     Allow user to customize CV per application   

        [ ]     Offer user option to save their top 10 favourite businesses
                [ ]     Display job offers from these companies
                [ ]     Display news on that company

        [ ]     Add option for user to contact the HR recruiter at the company they've just had an interview at
                -> Via email / LI
        