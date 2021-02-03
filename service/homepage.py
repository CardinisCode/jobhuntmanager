from flask import Flask, render_template, session, flash
import datetime


def grab_values_from_top_5_interviews_SQLquery_and_return_top_5_interviews_dict(interviewsRepo, user_id):
    top_5_interviews_dict = {}
    query_results = interviewsRepo.grabTop5InterviewsForUser(user_id)

    if not query_results:
        flash("top_5_interviews_query didn't return any data. Please review!")

    id_count = 1
    for interview in query_results: 
        company_name = interview[1]
        interview_date = interview[2]
        interview_time = interview[3]
        job_role = interview[4]
        interviewer_names = interview[5]
        interview_type = interview[7]
        location = interview[8]
        medium = interview[9]
        other_medium = interview[10]
        contact_number = interview[11]
        status = interview[12]
    
        top_5_interviews_dict[id_count] = {
            "interview_date": interview_date, 
            "interview_time": interview_time,
            "company_name": company_name, 
            "job_role": job_role,
            "interview_type": interview_type,
            "Interview Location": location,
            "Video medium": medium,
            "other_medium": other_medium, 
            "contact_number": contact_number,
            "status": status,
            "interviewer_names": interviewer_names, 
        } 
        id_count += 1

    return top_5_interviews_dict


def create_homepage_content(session, user_id, applicationsRepo, interviewsRepo):
    # Let's grab today's date as this will help us when we're grabbing interviews & applications for the current date:
    current_date = datetime.date.today()

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