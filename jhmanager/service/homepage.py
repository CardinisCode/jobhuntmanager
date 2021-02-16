from flask import Flask, render_template, session, flash
from datetime import datetime, date


def for_andis_eyes_only():
    return {}


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




def grab_values_from_top5applications_SQLquery_and_return_dict(applicationsRepo, user_id):
    top_5_applications = {}
    query_results = applicationsRepo.grabTop5ApplicationsFromHistory(user_id)

    if not query_results:
        flash("top_5_applications_query didn't return any data. Please review!")

    top_5_applications["headings"] = ["Id#", "Date", "Company Name", "Job Role", "Employment Type", "Interview Stage", "Received Contact?", "Salary", "Platform / Job Board"]
    id_count = 1
    for application in query_results:
        app_date = application[0]
        company_name = application[2]
        job_role = application[3]
        platform = application[4]
        emp_type =  application[5]
        interview_stage = application[6]
        contact_received = application[7]
        salary = application[8]

        if interview_stage == "N/A":
            interview_stage = 0

        top_5_applications[id_count] = {
            "ID#": id_count,
            "date": app_date, 
            "company_name": company_name,
            "job_role": job_role,
            "emp_type": emp_type, 
            "interview_stage": interview_stage,
            "contact_received": contact_received.capitalize(),
            "salary": salary,
            "platform": platform,
        }

        cleanup_fields_for_better_display_top5applications(top_5_applications, id_count, interview_stage)
        id_count += 1

    return top_5_applications

# def combine_date_and_time_into_1_string(interview_date, interview_time): 
#     # I want to format the datetime format to be "%Y-%m-%d %H:%M"
#     # 1) I will take the str values for Date and Time, & combine them into 1 datetime string 
#     date_time_str = interview_date + " " + interview_time

#     #2) Now I will convert this datetime string into its datetime object:
#     date_time_format = '%Y-%m-%d %H:%M'
#     date_and_time_obj = datetime.strptime(date_time_str, date_time_format)

#     # 3) Now I can convert this datetime_obj into a string & simultaneously get the format I want:
#     updated_date_time = date_and_time_obj.strftime("%m/%d/%Y, %H:%M")

#     return updated_date_time




def create_homepage_content(session, user_id, applicationsRepo, interviewsRepo, userRepo):
    #1: Let's grab today's date as this will help us when we're grabbing interviews & applications for the current date:
    current_date = date.today()
    date_format = "%Y-%m-%d"
    date_str = current_date.strftime(date_format)

    # Now to grab the values for the Applications & Interviews added on the current date (from the perspective SQL queries):
    # Firstly: applications
    applications_today = applicationsRepo.grabTodaysApplicationCount(date_str, user_id)
    interviews_today = interviewsRepo.grabTodaysInterviewCount(date_str, user_id)
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
    top_5_applications_dict = grab_values_from_top5applications_SQLquery_and_return_dict(applicationsRepo, user_id)

    message = "All good!"

    display = {
        'current_date': current_date,
        "applications_today": app_today_count,
        "interviews_today": interviews_today_count,
        "message": message,
        "top_5_applications": top_5_applications_dict,
        "username": username,
    }

    return render_template("index.html", display=display)