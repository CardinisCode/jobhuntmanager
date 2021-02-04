from flask import Flask, render_template, session, flash
from datetime import datetime, date


def combine_date_and_time_into_1_string(interview_date, interview_time): 
    # I want to format the datetime format to be "%Y-%m-%d %H:%M"
    # 1) I will take the str values for Date and Time, & combine them into 1 datetime string 
    date_time_str = interview_date + " " + interview_time

    #2) Now I will convert this datetime string into its datetime object:
    date_time_format = '%Y-%m-%d %H:%M:%S'
    date_and_time_obj = datetime.strptime(date_time_str, date_time_format)

    # 3) Now I can convert this datetime_obj into a string & simultaneously get the format I want:
    updated_date_time = date_and_time_obj.strftime("%m/%d/%Y, %H:%M")

    return updated_date_time


def grab_values_from_top_5_interviews_SQLquery_and_return_top_5_interviews_dict(interviewsRepo, user_id):
    top_5_interviews_dict = {}
    query_results = interviewsRepo.grabTop5InterviewsForUser(user_id)

    if not query_results:
        flash("top_5_interviews_query didn't return any data. Please review!")

    id_count = 1
    for interview in query_results: 
        # company_name = interview[1]
        interview_date = interview[2]
        interview_time = interview[3]
        # job_role = interview[4]
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
            "date_&_Time": updated_date_time,
            "company_name": interview[1], 
            "job_role": interview[4],
            "interview_type": interview_type,
            "interview_Location": location,
            "video_medium": medium,
            "other_medium": other_medium, 
            "contact_number": contact_number,
            "status": status,
            "interviewer_names": interviewer_names, 
        } 

        # Just so that we grab an unique ID for every application on this list:
        id_count += 1
    
    # In order to use a for loop to display the headings in our table on Index
    # without using a for loop within a for loop as this would print the headings far more times than we need it to
    # (To get technical this would print n*n headings where n = the no. of headings)
    top_5_interviews_dict["headings"] = ["Id#", "Date & Time", "Company Name", "Job Role", "Interview Type", "Location", "Video Medium", "Other Medium", "Contact No.", "Status", "Interviewer Names"]

    return top_5_interviews_dict


def create_homepage_content(session, user_id, applicationsRepo, interviewsRepo):
    # Let's grab today's date as this will help us when we're grabbing interviews & applications for the current date:
    current_date = date.today()

    # Now to grab the values from the relevant SQL queries:
    applications_today = applicationsRepo.grabTodaysApplicationCount(current_date, user_id)
    top_5_applications = applicationsRepo.grabTop5ApplicationsFromHistory(user_id)
    interviews_today = interviewsRepo.grabTodaysInterviewCount(str(current_date), user_id)
    
    # Now to review the SQL query results and create a Dictionary to display to the screen:
    top_5_interviews_dict = grab_values_from_top_5_interviews_SQLquery_and_return_top_5_interviews_dict(interviewsRepo, user_id)

    interviews_today_count = 0
    for interview in interviews_today:
        interviews_today_count += 1

    message = "All good!"

    if applications_today == None:
        message = "Not successful"

    display = {
        'current_date': current_date,
        "applications_today": applications_today,
        "interviews_today": interviews_today_count,
        "message": message,
        "top_5_applications": top_5_applications,
        "top_5_interviews": top_5_interviews_dict,
    }

    return render_template("index.html", display=display)