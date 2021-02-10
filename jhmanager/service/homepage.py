from flask import Flask, render_template, session, flash
from datetime import datetime, date


def for_andis_eyes_only():
    return {}


def cleanup_fields_for_better_display_top5applications(top_5_applications, id_count, interview_stage):
    emp_type = top_5_applications[id_count]["emp_type"]

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

    # Improving how the date & time values are presented
    # 1) I need to convert my date&time value to actual datetime values:
    # current_datetime_format = "%Y-%m-%d %H:%M:%S.%f"
    # date_time_obj = datetime.strptime(date_time_str, current_datetime_format)

    # # 2) To convert this datetime_obj into a string & simultaneously get the format I want:
    # desired_datetime_format = "%Y-%m-%d, %H:%M"
    # updated_date_time = date_time_obj.strftime(desired_datetime_format)

    # # 3) Finally, we can update the datetime value in our dictionary:
    # top_5_applications[id_count]["date&time"] = updated_date_time

    # Let's format how interview_stage is presented to the user:
    interview_stage_str = "Interview #{interview_stage} lined up.".format(interview_stage = str(interview_stage))
    top_5_applications[id_count]["interview_stage"] = interview_stage_str


def grab_values_from_top5applications_SQLquery_and_return_dict(applicationsRepo, user_id):
    top_5_applications = {}
    query_results = applicationsRepo.grabTop5ApplicationsFromHistory(user_id)

    if not query_results:
        flash("top_5_applications_query didn't return any data. Please review!")

    top_5_applications["headings"] = ["Id#", "Date", "Company Name", "Job Role", "Employment Type", "Salary", "Interview Stage", "Platform / Job Board", "Received Contact? Y/N", "Job Ref"]
    id_count = 1
    for application in query_results:
        app_date = application[0]
        job_ref = application[1]
        company_name = application[2]
        job_role = application[3]
        platform = application[4]
        emp_type =  application[5]
        interview_stage = application[6]
        contact_received = application[7]
        salary = application[8]

        top_5_applications[id_count] = {
            "ID#": id_count,
            "date": app_date, 
            "company_name": company_name,
            "job_role": job_role,
            "emp_type": emp_type, 
            "salary": salary,
            "interview_stage": interview_stage,
            "platform": platform,
            "contact_received": contact_received,
            "job_ref": job_ref,
        }

        cleanup_fields_for_better_display_top5applications(top_5_applications, id_count, interview_stage)
        id_count += 1

    return top_5_applications


def cleanup_fields_for_better_display(top_5_interviews_dict, id_count, other_medium):
    # Let's start by extracting the fields we want to update: 
    interview_type = top_5_interviews_dict[id_count]["interview_type"]
    status = top_5_interviews_dict[id_count]["status"]
    medium = top_5_interviews_dict[id_count]["video_medium"] 

    # Lets set a few conditions for what gets displayed to the user & clean up the presentation of the data:
    if  interview_type == "video_or_online":
        top_5_interviews_dict[id_count]["interview_type"] = "Video / Online"

        # At this point we know the user's selected "Video / Online", 
        # so we can add the medium to the fields displayed in the table to the user:
        if medium == "skype":
            medium = "Skype"
        elif medium == "zoom":
            medium = "Zoom"
        elif medium == "google_chat":
            medium = "Google Chat"
        elif medium == "meet_jit_si":
            medium = "Meet.Jit.Si"
        else: 
            medium = other_medium
        top_5_interviews_dict[id_count]["video_medium"] = medium

    elif interview_type == "phone_call": 
        top_5_interviews_dict[id_count]["interview_type"] = "Phone Call"
        top_5_interviews_dict[id_count]["video_medium"] = "N/A"

    else: 
        top_5_interviews_dict[id_count]["interview_type"] = "In Person"
        top_5_interviews_dict[id_count]["video_medium"] = "N/A"

    if status == "upcoming": 
        top_5_interviews_dict[id_count]["status"] = "Upcoming"
    elif status == "done":
        top_5_interviews_dict[id_count]["status"] = "Interview Done"
    elif status == "cancelled":
        top_5_interviews_dict[id_count]["status"] = "Cancelled"
    else: 
        top_5_interviews_dict[id_count]["status"] = "Post-poned"

    return top_5_interviews_dict


def combine_date_and_time_into_1_string(interview_date, interview_time): 
    # I want to format the datetime format to be "%Y-%m-%d %H:%M"
    # 1) I will take the str values for Date and Time, & combine them into 1 datetime string 
    date_time_str = interview_date + " " + interview_time

    #2) Now I will convert this datetime string into its datetime object:
    date_time_format = '%Y-%m-%d %H:%M'
    date_and_time_obj = datetime.strptime(date_time_str, date_time_format)

    # 3) Now I can convert this datetime_obj into a string & simultaneously get the format I want:
    updated_date_time = date_and_time_obj.strftime("%m/%d/%Y, %H:%M")

    return updated_date_time


def grab_values_from_top5interviews_SQLquery_and_return_dict(interviewsRepo, user_id):
    top_5_interviews_dict = {}
    query_results = interviewsRepo.grabTop5InterviewsForUser(user_id)

    if not query_results:
        flash("top_5_interviews_query didn't return any data. Please review!")

    # We need some headings for our fields:
    # I've chosen to use a list instead of an imbedded dict as this prevents the headings from being printed more than once each. 
    # When using a for loop on the index.html page.
    top_5_interviews_dict["headings"] = ["Id#", "Date & Time", "Company Name", "Job Role", "Interview Type", "Status", "Video Medium", "Interview Location","Contact No.", "Interviewer Names"]

    id_count = 1
    for interview in query_results: 
        interview_date = interview[2]
        interview_time = interview[3]
        interviewer_names = interview[5]
        interview_type = interview[7]
        location = interview[8]
        medium = interview[9]
        other_medium = interview[10]
        contact_number = interview[11]
        status = interview[12]

        # Let's combined our date & time values (received from the SQL query) into 1 variable
        # Using the format: "%Y-M-D, H:M":
        updated_date_time = combine_date_and_time_into_1_string(interview_date, interview_time)

        # Now I can finish by adding the updated datetime, along with all the other values, 
        # to my top_5_interviews_dict dictionary: 
        top_5_interviews_dict[id_count] = {
            "Id#": id_count,
            "date_&_time": updated_date_time,
            "company_name": interview[1], 
            "job_role": interview[4],
            "interview_type": interview_type,
            "status": status,
            "video_medium": medium,
            "location": location,
            "contact_number": contact_number,
            "interviewer_names": interviewer_names, 
        } 

        # Lets clean up how our values are displayed to the user on Index.html:
        cleanup_fields_for_better_display(top_5_interviews_dict, id_count, other_medium)

        # Just so that we grab an unique ID for every application on this list:
        id_count += 1
    
    return top_5_interviews_dict


def create_homepage_content(session, user_id, applicationsRepo, interviewsRepo):
    #1: Let's grab today's date as this will help us when we're grabbing interviews & applications for the current date:
    current_date = date.today()
    date_format = "%Y-%m-%d"
    date_str = current_date.strftime(date_format)

    # Now to grab the values for the Applications & Interviews added on the current date (from the perspective SQL queries):
    # Firstly: applications
    applications_today = applicationsRepo.grabTodaysApplicationCount(date_str, user_id)
    interviews_today = interviewsRepo.grabTodaysInterviewCount(date_str, user_id)

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
    top_5_interviews_dict = grab_values_from_top5interviews_SQLquery_and_return_dict(interviewsRepo, user_id)

    message = "All good!"

    display = {
        'current_date': current_date,
        "applications_today": app_today_count,
        "interviews_today": interviews_today_count,
        "message": message,
        "top_5_applications": top_5_applications_dict,
        "top_5_interviews": top_5_interviews_dict,
    }

    return render_template("index.html", display=display)