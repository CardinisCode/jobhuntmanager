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

#2: [ ] Registration   
        [X]     Create registration.py
        [ ]     Add registration router & function
                [ ]     GET 
                [ ]     POST
        [ ]     Verify user details dont already exist
                [ ]     username
                [ ]     email address
        [ ]     Create rules for password 
                [ ]     Add these requirements on the html page
                [ ]     Verify that the password provided meets those requirements

        [ ]     Add user to user table (sqlite3 database)
                [ ]     username ??
                [ ]     hash password
                [ ]     email address
                [ ]     date & time account was created

------------------------------------------------------------------------------

#3: [ ] Login
        [ ]     Verify email address against db
                [ ]     search db for email address provided
                [ ]     hash login password provided
                [ ]     check hashed 

        [ ]     If valid: login in user
                [ ]     Take user to home page
        [ ]     If invalid:
                [ ]     username doesn't exist:
                        [ ]     provide error message to login page
                [ ]     password doesn't match password on system for that user
                        [ ]     provide error message to login page

------------------------------------------------------------------------------

#4: [ ] Logout




------------------------------------------------------------------------------

#5: [ ] Layout.html
        [ ]     Create a root templates folder
        [ ]     Create the Layout template 
        [ ]     Add the necessary libraries
        [ ]     Include a banner to display notifications to user
        [ ]     Include a footer 

------------------------------------------------------------------------------


#6: [ ] Home page
        [ ]     Create homepage.html
        [ ]     Create route for homepage.html 
                [ ]     include the @login decorator
                [ ]     Create create_homepage function
        [ ]     Applications
                [ ]     View applications -> redirects user to view_applications.html
                        [ ]     Create view_applications.html
                [ ]     Add application -> redirects user to add_application.html
                        [ ]     Create add_application.html
        [ ]     Interviews 
                [ ]     Interview history -> redirects user to interview_history.html
                        [ ]     Create interview_history.html
                [ ]     Add interview   -> redirects user to add_interview.html
                        [ ]     Create add_interview.html
        [ ]     Update details on an interview 
                [ ]     Redirects user to update_interview_details.html page
                        [ ]     Create update_interview_details.html
        [ ]     Calendar
                [ ]     Create calendar file/page
                [ ]     Display calendar / button for calendar

------------------------------------------------------------------------------

#7: [ ] Nav bar 
        [ ]     import relevant library for icons
        [ ]     import libraries for css styles
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
        [ ]     Display user achievements
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
        [ ] Change password -> redirect user to change_password.html
                [ ]     create change_password.html
        [ ] Delete account -> Redirect user to delete_account.html
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

        