from flask import Flask, render_template, session, request, redirect
from datetime import datetime, time


def improve_display_values(details_dict, interview_id, other_medium):
    interview_type = details_dict[interview_id]["interview_type"]
    medium = details_dict[interview_id]["medium"]
    interview_status = details_dict[interview_id]["interview_status"]
    interviewers = details_dict[interview_id]["interviewers"]
    contact_number = details_dict[interview_id]["contact_number"]
    location = details_dict[interview_id]["location"]

    #1: Lets set a condition: 
    # If interview_type == "video_or_online": Display medium's value, Else: medium = "N/A"
    if interview_type == 'video_or_online':
        # Firstly we improve how the value gets displayed:
        interview_type = "Video / Online"

        # Secondly let's improve the values' appearance for video medium:
        if medium == "google_chat":
            medium = "Google Chat"
        elif medium == "meet_jit_si":
            medium = "Meet.Jit.Si"
        elif medium == "other" or medium == "Other":
            medium = other_medium
        else:
            medium = medium.capitalize()
        details_dict[interview_id]["medium"] = medium


    else: 
        # If interview_type == "in_person" or "phone_call"
        details_dict[interview_id]["medium"] = ""

        if interview_type == 'in_person':
            interview_type = "In Person"

        if interview_type == "phone_call":
            interview_type = "Telephonic call"

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

    # Now to finalise I can update the value of interview_status in our dictionary: 
    details_dict[interview_id]["interview_status"] = interview_status

    # 3: If interviewer_names == "Unknown at present", then the field should be blank:
    if interviewers == "Unknown at present":
        details_dict[interview_id]["interviewers"] = ""

    # 4: If contact_number is "N/A", lets rather display a blank field:
    if contact_number == "N/A":
        details_dict[interview_id]["contact_number"] = ""

    if location == "Remote" or location == "N/A":
        details_dict[interview_id]["location"] = ""




def display_top_10_interviews_to_interviews_html(session, user_id, interviewsRepo):
    interviews = interviewsRepo.grabTopTenInterviewsForUser(user_id)

    details_dict = {}
    interview_id = 1

    # Let's take the details from "interviews" and restructure the data for our html page:
    for interview in interviews:
        details_list = []
        for details in interview:
            details_list.append(details)

        # Now that we have grabbed the fields for this current interview
        # lets store these values in a dictionary to be displayed on the html page:

        # interview_id = details_list[0]
        medium = details_list[9]
        other_medium = details_list[10]
        interview_type = details_list[7]
        interview_status = details_list[12]
        interviewers = details_list[6]
        contact_number = details_list[11]
        app_date = details_list[2]
        app_time = details_list[3]

        # We need to merge the date & time into 1 value to be displayed:
        app_datetime = app_date + " " + app_time

        details_dict[interview_id] = {
            "date&time": app_datetime, 
            "company_name": details_list[1], 
            "job_role": details_list[4], 
            "interview_type": interview_type,
            "medium": medium,
            "interview_status": interview_status,
            "location": details_list[8], 
            "contact_number": contact_number, 
            "interviewers": interviewers, 
        }
        improve_display_values(details_dict, interview_id, other_medium)
        interview_id += 1

    headings = ["ID#", "Date & Time", "Company Name", "Role", "Type", "Medium", "Status", "Location", "Contact No.", "Interviewers' Name/s"]
    details_dict["headings"] = headings

    return render_template("interviews.html", details=details_dict)