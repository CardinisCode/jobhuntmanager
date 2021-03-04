from flask import Flask, render_template, session, flash
from datetime import datetime, date


def for_andis_eyes_only():
    return {}


def past_dated_interview(interview_date, interview_time):
    past_dated = False 

    return past_dated


def cleanup_interview_details(interview_details, other_medium, company_name, interview_id):
    medium = interview_details[company_name][interview_id]["interview_medium"]
    interviewers = interview_details[company_name][interview_id]["interviewers"]

    # Lets cleaned up the display of 'Medium':
    if medium == "google_chat":
        interview_details[company_name][interview_id]["interview_medium"] = "Google Chat"
    elif medium == "meet_jit_si":
        interview_details[company_name][interview_id]["interview_medium"] = "Meet.Jit.Si"
    elif medium == "other":
        interview_details[company_name][interview_id]["interview_medium"] = other_medium
    else: 
        interview_details[company_name][interview_id]["interview_medium"] = medium.capitalize()

    if interviewers == "Unknown at present":
        interview_details[company_name][interview_id]["interviewers"] = None

    return "Done"


def extract_and_display_interviews(all_interviews, applicationsRepo, companyRepo): 
    if not all_interviews: 
        interview_details = None
    else: 
        interview_details = {}
        for interview in all_interviews:
            interview_id = interview.interview_id
            application_id = interview.application_id
            company_id = applicationsRepo.grabApplicationByID(application_id).company_id
            company_name = companyRepo.getCompanyById(company_id).name
            view_more_url = '/applications/{}/interview/{}'.format(application_id, interview_id)
            update_url = '/applications/{}/interview/{}/update_interview'.format(application_id, interview_id)
            other_medium = interview.other_medium
            
            interview_details[company_name] = {} 
            interview_details[company_name][interview_id] = {
                "Date": interview.interview_date, 
                "Time": interview.interview_time,
                "Location": interview.location,
                "View_More": view_more_url, 
                "status": interview.status,
                "interview_type": interview.interview_type,
                "interview_medium": interview.medium, 
                "contact_number": interview.contact_number,
                "interviewers": interview.interviewer_names,
                "past_dated": False, 
                "update_url": update_url
            }
            cleanup_interview_details(interview_details, other_medium, company_name, interview_id)


    return interview_details


def cleanup_fields_for_better_display_top5applications(top_5_applications, id_count, interview_stage):
    emp_type = top_5_applications[id_count]["emp_type"]
    salary = top_5_applications[id_count]["salary"]
    platform = top_5_applications[id_count]["platform"]

    # Lets improve how the data for "Employment Type" is displayed to the user in the table:
    if emp_type == "full_time":
        top_5_applications[id_count]["emp_type"] = "Full Time"
    elif emp_type == "part_time":
        top_5_applications[id_count]["emp_type"] = "Part Time"
    elif emp_type == "temp":
        top_5_applications[id_count]["emp_type"] = "Temporary"
    elif emp_type == "contract":
        top_5_applications[id_count]["emp_type"] = "Contract"
    else:
        top_5_applications[id_count]["emp_type"] = "Other"

    # Let's format how interview_stage is presented to the user:
    if interview_stage == 0:
        interview_stage_str = "No interview lined up yet."
    else:
        interview_stage_str = "Interview #{interview_stage} lined up.".format(interview_stage = str(interview_stage))
    top_5_applications[id_count]["interview_stage"] = interview_stage_str

    # If these fields values == "N/A", we'll just display a blank field to user:
    if salary == "N/A":
        salary = ""
    top_5_applications[id_count]["salary"] = salary

    if platform == "N/A":
        platform = ""
    top_5_applications[id_count]["platform"] = platform




def grab_values_from_top5applications_SQLquery_and_return_dict(applicationsRepo, user_id, companyRepo):
    top_5_applications = {}
    application_query_results = applicationsRepo.grabTop5ApplicationsByUserID(user_id)

    if not application_query_results: 
        top_5_applications["fields"] = None

    else:
        top_5_applications["fields"] = {}
        top_5_applications["headings"] = ["Id#", "Date", "Time", "Company Name", "Job Role", "Employment Type", "Interview Stage", "Received Contact?", "Salary", "Platform / Job Board", "View More"]
        id_count = 1

        for application in application_query_results:
            application_id = application.app_id
            company_id = application.company_id
            company_name = companyRepo.getCompanyById(company_id).name
            app_date = application.app_date
            app_time = application.app_time
            job_role = application.job_role
            platform = application.platform
            emp_type = application.employment_type
            interview_stage = application.interview_stage
            contact_received = application.contact_received
            salary = application.salary
            # delete_url = 
            view_more_url = "/applications/{}".format(application_id)

            top_5_applications[id_count] = {
                "ID#": id_count,
                "date": app_date, 
                "Time": app_time,
                "company_name": company_name,
                "job_role": job_role,
                "emp_type": emp_type, 
                "interview_stage": interview_stage,
                "contact_received": contact_received.capitalize(),
                "salary": salary,
                "platform": platform,
                "View More": view_more_url
            }
        
            cleanup_fields_for_better_display_top5applications(top_5_applications, id_count, interview_stage)
            id_count += 1

    return top_5_applications


def create_homepage_content(session, user_id, applicationsRepo, interviewsRepo, userRepo, companyRepo):
    #1: Let's grab today's date as this will help us when we're grabbing interviews & applications for the current date:
    current_date = date.today()
    date_format = "%Y-%m-%d"
    date_str = current_date.strftime(date_format)

    # Now to grab the values for the Applications & Interviews added on the current date (from the perspective SQL queries):
    # Firstly: applications
    applications_today = applicationsRepo.grabTodaysApplicationCount(date_str, user_id)
    interviews_today = interviewsRepo.grabTodaysInterviewCount(date_str, user_id)
    # all_interviews = interviewsRepo.grabAllInterviewsForUserID(user_id)
    all_interviews = interviewsRepo.grabUpcomingInterviewsByUserID(user_id)
    interview_details = extract_and_display_interviews(all_interviews, applicationsRepo, companyRepo)
    username = userRepo.getUsernameByUserID(user_id)

    # Sadly SQLite doesn't have the functionality to return COUNT(*) from SQLite to Python
    # So we'll have manually count the number of rows returned from the SQL query:
    app_today_count = 0
    for app in applications_today:
        app_today_count += 1

    interviews_today_count = 0
    for interview in interviews_today:
        interviews_today_count += 1

    # Now to grab the values from our SQL queries for the top 5 applications & interviews & create a dictionary for each:
    top_5_applications_dict = grab_values_from_top5applications_SQLquery_and_return_dict(applicationsRepo, user_id, companyRepo)

    message = "All good!"

    display = {
        'current_date': current_date,
        "applications_today": app_today_count,
        "interviews_today": interviews_today_count,
        "message": message,
        "top_5_applications": top_5_applications_dict,
        "username": username,
        "interview_details": interview_details
    }

    return render_template("index.html", display=display)