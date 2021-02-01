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
        medium = details_list[9]
        other_medium = details_list[10]
        interview_type = details_list[7]
        interview_status = details_list[12]

        details_dict[interview_id] = {
            "company_name": details_list[1], 
            "date": details_list[2], 
            "time": details_list[3], 
            "job_role": details_list[4], 
            "interviewers": details_list[5], 
            "location": details_list[8], 
            "contact_number": details_list[11], 
            "interview_status": details_list[12]
        }

        # Condition: If user selects 'Other', we want their chosen medium to be displayed for 'medium'
        if medium == 'other': 
            medium = other_medium
        details_dict[interview_id]["medium"] = medium

        # Two of the fields have their data displayed like variable names
        # 

        # 1: Let's replace the current values for 'interview_type' with strings that improve the appearance of the data:
        if interview_type == 'in_person':
            interview_type = "In Person"
        elif interview_type == 'video_or_online':
            interview_type = "Video / Online"
        else:
            interview_type = "Contact Number"
        details_dict[interview_id]["interview_type"] = interview_type

        # 2: Let's adjust 'status' data so we can capitalize it before it reaches the table
        if interview_status == "upcoming":
            interview_status = "Upcoming"
        elif interview_status == "done":
            interview_status = "Done"
        elif interview_status == 'cancelled':
            interview_status = "Cancelled"
        else:
            interview_status = "Post-poned"
        details_dict[interview_id]["interview_status"] = interview_status


    return render_template("interviews.html", details=details_dict)