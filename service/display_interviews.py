from flask import Flask, render_template, session, request, redirect
from datetime import datetime, time


def display_top_10_interviews_to_interviews_html(session, user_id, interviewsRepo):
    interviews = interviewsRepo.grabTopTenInterviewsForUser(user_id)

    details_dict = {}

    # Let's take the details from "interviews" and restructure the data for our html page:
    for interview in interviews:
        details_list = []
        for details in interview:
            details_list.append(details)

        # Now that we have grabbed the fields for this current interview
        # lets store these values in a dictionary to be displayed on the html page:

        interview_id = details_list[0]

        details_dict[interview_id] = {
            "company_name": details_list[1], 
            "date": details_list[2], 
            "time": details_list[3], 
            "job_role": details_list[4], 
            "interviewers": details_list[5], 
            "interview_type": details_list[7], 
            "location": details_list[8], 
            "medium": details_list[9], 
            "other_medium": details_list[10], 
            "contact_number": details_list[11], 
            "interview_status": details_list[12]
        }

    return render_template("interviews.html", details=details_dict)