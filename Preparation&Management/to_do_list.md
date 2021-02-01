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
                [ ]     Job interviews
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

        [ ]     Display Interviews
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

                [ ]     Bugs: 
                        [x]     Data displayed is ordered by Date but not by time, so all rows of a specific date are in mixed order
                                [x]     In SQL query: Sort by Date, then by time        


        [ ]     In service/homepage, update create_homepage_content (function) 
                -> All content displayed to Index.html

                [x]     Grab today's date
                [x]     Display Today's date on index.html
                For Applications:
                [ ]     Create a SQL query to pull together all applications made today / current day. 
                [ ]     Count the number of applications and save that to a variable
                        [x]     Display to page:
                                EG: "You have made {{ X }} number of applications today"
                        [ ]     If no applications made today: 
                                [ ]     Display message to user:
                                                "Have you had any applications yet?" 
                                [ ]     Add button / link: 
                                        [ ]     Add an application

                For Interviews:
                [x]     Set up a Repo for Interview History
                [x]     Connect to this new repo in your applications.py
                [ ]     Create a SQL query to pull all interviews for current date
                [ ]     Pull all the day current_day interviews to a variable
                        [ ] Save how many items were returned & display to user
                                EG: "You have {{ X }} number of Interviews today" 
                        [ ]     If interviews lined up = True
                                [ ]     Offer user option to Prepare for the interview:
                                        -> Will direct user to relevant page (interview_prep.html)

                        [ ] IF no interviews lined up today: 
                                EG: "You have {{ X }} number of Interviews today" 
                                [ ]     Add option to add lined up interview
                                        "Have a lined up Interview? Add it!"
                                [ ]     Pull interviews in the next 7 days
                                        [ ]     Display Interviews (10 items max) 
                                        [ ]     Option to "view more" -> Directs user to interviews.html  


------------------------------------------------------------------------------

#7: [ ] Nav bar 
        [ ]     import relevant library for icons
        [ ]     import libraries for css styles
        [ ]     Create structure for Nav bar:
                [ ]     Left: 
                        [ ]     Home
                                [ ]     Add house icon
                                [ ]     linked to homepage.html
                        [ ]     (Job) Applications
                                [ ]     Add applicable icon
                                [ ]     Linked to job_applications.html
                        [ ]     Interviews      
                                [ ]     Add icon
                                [ ]     linked to interviews.html
                        [ ]     Calendar
                                [ ]     Add icon
                                [ ]     linked to calendar.html
                        
                [ ]     right
                        [ ]     Before Logged in:
                                [ ]     Login   
                                        [ ]     Add icon with door
                                        [ ]     linked to login.html
                                [ ]     Register 
                                        [ ]     Add icon (pref usericon with a plus)
                                        [ ]     linked to register.html
                        
                        [ ]     After logged out
                                [ ]     User account 
                                        [ ]     add icon
                                        [ ]     linked to user_account.html
                                [ ]     Logout 
                                        [ ]     Add icon (closing door)
                                        [ ]     linked to login.html
        
 ------------------------------------------------------------------------------

#8: [ ] View job Applications page
        [x]     Create Applications table
                [x]     app_id (AUTOINCREMENT) 
                [x]     Company name -> send to company directory table
                [x]     company_id -> From company directory table
                [x]     Job role
                [x]     Job platform
                [x]     Interview Stage
                [x]     Received contact Y/N
        [ ]     set up SQL db:
                [ ]     Create an application history table
                        [ ]     Unique identifier (job_id)
                        [ ]     company name
                        [ ]     role applied for
                        [ ]     date of application
                        [ ]     platform used for application
                        [ ]     source of job -> where it was found
                        [ ]     Salary info provided
                [ ]     set up an application history repo 
                        [ ]     class ApplicationHistoryRepository -> to allow for:

        [ ]     Add option to view application history 
                [ ]     Add call to ApplicationHistoryRepository 
                        ->      in repo directory
                        [ ]     should grab all items in the history repo 
                                [ ]     where userid is the current user
                                [ ]     by Date in DESC order 
                [ ]     Display history to view_applications.html 
                        [ ]     In a table using a html table
                        [ ]     Provide user options to:
                                [ ]     Search by...
                                [ ]     delete entry
                                [ ]     Update entry -> redirect to update_interview_details.html

        [ ]     Add option to add application to the application history
                [ ]     Add button "Add application"
                [ ]     Direct user to add_application.html
 

        [ ]     Add option to Update an application 
                [ ]     Add button "Update an application"
                [ ]     direct user to update_interview_details.html
        
 ------------------------------------------------------------------------------

#9: [ ] Add Application
        [ ]   Create Add Application page  
        [ ]     Add call to ApplicationHistoryRepository 
                ->      in repo directory
                
        [ ]     Add route & function on application.py
                [ ]     GET -> render template on add_application.html
                [ ]     POST
                        [ ]     Grab details from form (in variables)
                        [ ]     Catch potential errors
                        [ ]     Add details to ApplicationHistoryRepository 
                                [ ]     Create a method in repo for adding application to 
                                        ApplicationHistoryRepository 
                        [ ]     Display notification to user to confirm application 
                                has been added
                        [ ]     redirect user back to view_applications.html

        [ ]     Create form on add_application.html:
                [ ]     company name
                [ ]     role applied for
                [ ]     date of application
                [ ]     platform used for application
                [ ]     source of job -> where it was found
                [ ]     Salary info provided  
                [ ]     Location 
                [ ]     Remote / in office 

  ------------------------------------------------------------------------------               

#10: [ ] Interviews
        [ ]     Create Interviews table
                [ ]     id (AUTOINCREMENT) 
                [ ]     Company name
                [ ]     company_id -> From company directory table
                [ ]     Status:
                        -> Lined up
                        -> Had interview
                        -> Postponed -> Add once all basic requirements met
                        -> Cancelled
        

        [ ]     Add option to view application history
                -> redirects to interview_history.html
        [ ]     Create InterviewHistoryRepository 
                [ ]     Add method to add an interview
                [ ]     add method to delete an interview
                [ ]     Add method to update an interview
        [ ]     Add option to Add interview 
                ->      Redirects user to add_interview.html
        [ ]     Add option to update Interview
                ->      Redirects user to update_interview_html
        [ ]     Add option for interview prep
                ->      redirects user to interview_preparation.html   

  ------------------------------------------------------------------------------  

#11: [ ] Add Interview
        [ ]     Add route & function for "/add_interview"
        [ ]     Create InterviewHistoryRepo
                [ ]     Create a method to grab details and add to repo:
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

#12: [ ] Updating details 
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
        