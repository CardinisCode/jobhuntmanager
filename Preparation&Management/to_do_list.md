Project Management

#1: [ ] Setup:
        [X] Connect directory to Github
        [X] Create repo directory
        [X] Create service directory
        [X] Create style directory

        [ ] Set up SQLite3 database
                [X]     Create db
                [ ]     Create connection to db

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

#3: [ ] Login
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


#5: [ ] Home page
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


        [ ]     Come back to this after completing:
                [X]     Job applications
                [X]     Job interviews
                [ ]     Job offers
        

------------------------------------------------------------------------------

#6: Job Applications:
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

#7: [ ] Add Interview
        [x]     Add route & function for "/add_interview"
        [x]     Create InterviewHistoryRepo
                [x]     Create a method to grab details and add to repo:
                        [ ]     Unique identifier
                        [ ]     Date
                        [ ]     Company name
                        [ ]     Interviewer/s names
                        [ ]     Q's asked (optional)
                        [ ]     Take aways (notes)
                        [ ]     Room for improvement

        [ ]     GET
                [ ]     Create form:
                        [ ]     Date
                        [ ]     Company name
                        [ ]     Interviewer/s names
                        [ ]     Take aways (notes)
                        [ ]     Room for improvement
                        [ ]     Q's asked (optional)
                [ ]     renders_template for add_interview.html

        [ ]     POST
                [ ]     Grab details from form
                [ ]     call on relevant method to add details to repo
                [ ]     User will be given the option to add item to the in-app calendar
                [ ]     Display message to user to confirm the interview has been added
                [ ]     Redirect user to Interviews.html

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
#11: [ ] Display Applications & Interviews:
        [ ]     Applications page
                [ ]     Make sure all applications display as expected on Applications.html
                [ ]     Check that all entries are in order of the most recent application first
        [ ]     Interviews page
                [ ]     Make sure all interviews display as expected on Applications.html
                [ ]     Check that all entries are in order of the most recent interview first
        [ ]     Index page
                [x]     Top 5 Applications: 
                        [x]     Check that it displays the latest 5 application entries
                        [x]     Check that all entries are in order 
                                of the most recent application first (By Date)
                [ ]     Top 5 Interviews:
                        [ ]     Create a SQL query to grab last 5 interviews for this user
                                (ORDER BY: First: Date, Second: Time)
                        [ ]     Update function homepage.create_homepage_content():
                                [ ]     Call on relevant SQL query to grab top_five_interview details
                                [ ]     Add fields to variables & add to dict
                                [ ]     render dict to index.html 
                                
                        [ ]     Customise the table on index.html:
                                [ ]     Recreate the table to receive top5interviews
                        [ ]     Test that it displays the top 5 interviews as expected

------------------------------------------------------------------------------
#12: [ ] Redo Login & Register using WTForms 
        [ ]     Research how to add a login / register using WTForm   


------------------------------------------------------------------------------
#13: [ ]     Index page: 
        [ ]     Update to Display Last 7 days Applications
                [ ]     Create SQL Query
                [ ]     Pull that data in homepage.py
                [ ]     Calculate interview count
                [ ]     Update Index.html
        [ ]     Update to Display Last 7 days Interviews
                [ ]     Create SQL Query
                [ ]     Pull that data in homepage.py
                [ ]     Calculate interview count
                [ ]     Update Index.html

------------------------------------------------------------------------------                

#: Bugs to be fixed later:
        [x]     Details received from 'add_interview.html' display on interview_details.html' 
                as text boxes that can be edited. 
                [x]     Figure out solution to adjust the values for each field so they display as plain text.

        [ ]     There's a huge gap at the top of each page, due to the side bar.

------------------------------------------------------------------------------   

#: [ ] Nav bar 
        [ ]     import relevant library for icons
        [x]     import libraries for css styles
        [x]     Create structure for Nav bar:
        
 -----------------------------------------------------------------------------

#: [ ] Updating details 
        ->      User will be instructed to provide the company name
                ->      User will be shown (in table format) all applications made to that company
                ->      User can select an application 
                        ->      User will be given the options to:
                                ->      Add / view Interviews 
                                ->      add / view Communication received
                                ->      Add / view notes made

  ------------------------------------------------------------------------------ 

#13: [ ] interview_preparation
        [ ]     Create a router & function
        [ ]     Create template: interview_preparation.html
        [ ]     Create repo: InterviewPrepRepository

        [ ]     GET:
                [ ]     Add option to add Interview prep -> Button / box
                        [ ]     redirect to add_interview_prep.html
                [ ]     Add option to view interview prep -> Button / box
                        [ ]     redirect to view_interview_prep.html
                [ ]     Add option to get advice on how to answer these Q's
                        [ ]     Link to Indeed's Q behind the Q (Indeed)
                [ ]     General page design

  ------------------------------------------------------------------------------ 

#14: [ ] Add Interview prep
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

  ------------------------------------------------------------------------------ 

#15: [ ] View interview prep
        [ ]     Create method to call on an entry from InterviewPrepRepository
        [ ]     Create a view_interview_prep.html 
        [ ]     add route & function in application.py
        [ ]     GET
                [ ]     Render template for view_interview_prep.html
        [ ]     POST
                [ ]     Grab detail from Search bar
                [ ]     Search for interview details by company name
                [ ]     If company name not found in db:
                        [ ]     Display error  to user: "Company name not recognised. Try again"
                [ ]     If company name found in db
                        [ ]     grab relevant details from db for that company name
                [ ]     Structure the relevant info for the table in a dict
                [ ]     Render template to view_interview_prep.html 
                        

        [ ]     Create form on view_interview_prep.html
                [ ]     Search bar for company name 
                [ ]     Search button
                [ ]     Create Table
                        [ ] Display all interviews for that company 

  ------------------------------------------------------------------------------                                                  

#16: [ ] Calendar page
        [ ]     Create calendar
        [ ]     Adding to calendar
        [ ]     Figure out what gets displayed to user
                [ ]     Calendar
                [ ]     Add to calendar button
                [ ]     Delete option
                [ ]     Update option
                [ ]     Option to select a date to see the events added

  ------------------------------------------------------------------------------ 

#17: [ ] User Profile
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
        

  ------------------------------------------------------------------------------ 

#18: [ ] Calendar
        [ ]     Create route & function in application.py
        [ ]     GET
                [ ]     Display the calendar [ figure out how to do this!]
                        [ ]     Add option to Add interview 
                        [ ]     Option to select date 'blocks' on calendar
                        [ ]     option to delete interview
        [ ]     POST
                [ ]     Process:
                        [ ]     Requests to add interview to calendar
                        [ ]     Request to select a date / block on calendar
                        [ ]     request to delete interview

  ------------------------------------------------------------------------------ 
        
#19: [ ] Figure out how to add a side bar "default" layout structure to layout.html
        [ ]     Add side bars to 
                [ ]     Homepage
                [ ]     Applications
                [ ]     Interviews
                [ ]     User Account
        [ ]     For each page
                [ ]     customize the side bar options

  ------------------------------------------------------------------------------ 

#20: [ ] Error handling page
        [ ]     Create apology.html page
        [ ]     Create route & function in application.py
        [ ]     GET
                ->   Render template to apology.html
        [ ]     Create design for page
                -> image? 
                -> way to allow input of error message & code

  ------------------------------------------------------------------------------ 

#21: [ ] Styling
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

  ------------------------------------------------------------------------------ 

#22: [ ] Potential extra features
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
        