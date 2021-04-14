from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_time_format
from jhmanager.service.cleanup_files.cleanup_datetime_display import past_dated
from datetime import datetime, time


def cleanup_interview_type(interview_type):
    updated_interview_type = ""
    if interview_type == "video_or_online":
        updated_interview_type = "Video / Online"
    elif interview_type == "in_person":
        updated_interview_type = "In Person / On Site"
    else:
        updated_interview_type = "Phone Call"
    
    return updated_interview_type


def cleanup_interview_status(status):
    updated_status = ""
    if status == "upcoming":
        updated_status = 'Upcoming Interview'
    elif status == "done":
        updated_status = 'Interview Done'
    elif status == "cancelled":
        updated_status = 'The interview has been cancelled'
    else:
        updated_status = 'Interview has been post-poned'

    return updated_status


def cleanup_medium(medium, other_medium):
    # Lets cleaned up the display of 'Medium':
    if other_medium == "N/A":
        other_medium = "Not provided"
        
    updated_medium = ""
    if medium == "google_chat":
        updated_medium = "Google Chat"
    elif medium == "meet_jit_si":
        updated_medium = "Meet.Jit.Si"
    elif medium == "ms_teams":
        updated_medium = "Microsoft Teams"
    elif medium == "other":
        updated_medium = other_medium
    else: 
        updated_medium = medium.capitalize()

    return updated_medium


def check_interview_is_today(interview_date):
    interview_is_today = False 
    current_date = datetime.now().date()
    if interview_date == current_date:
        interview_is_today = True
    
    return interview_is_today


def cleanup_upcoming_interview_fields(upcoming_interviews, interview_id):
    interview_date = upcoming_interviews["fields"][interview_id]["date"] 
    upcoming_interviews["fields"][interview_id]["interview_today"] = check_interview_is_today(interview_date)
    interview_date_str = cleanup_date_format(interview_date)

    interview_time = upcoming_interviews["fields"][interview_id]["time"] 
    interview_time_str = cleanup_time_format(interview_time)
    
    interview_status = upcoming_interviews["fields"][interview_id]["status"] 
    upcoming_interviews["fields"][interview_id]["status"] = cleanup_interview_status(interview_status)
    
    interview_string = ""
    interview_string += interview_date_str + " @ " + interview_time_str + ", "

    job_role = upcoming_interviews["fields"][interview_id]["job_role"]
    interview_string += job_role.capitalize() + ", "

    company_name = upcoming_interviews["fields"][interview_id]["company_name"]
    interview_string += company_name.capitalize()

    medium = upcoming_interviews["fields"][interview_id]["interview_medium"]
    other_medium = upcoming_interviews["fields"][interview_id]["other_medium"]
    updated_medium = cleanup_medium(medium, other_medium)

    interview_type = cleanup_interview_type(upcoming_interviews["fields"][interview_id]["interview_type"])
    location = upcoming_interviews["fields"][interview_id]["location"] 
    if location == "N/A" or location == "Remote":
        location = None 
        upcoming_interviews["fields"][interview_id]["location"] = location

    contact_number = upcoming_interviews["fields"][interview_id]["contact_number"]
    if contact_number == "N/A":
        contact_number = None 
        upcoming_interviews["fields"][interview_id]["contact_number"] = contact_number

    if interview_type == "Video / Online": 
        interview_string += ", " + updated_medium

    elif interview_type == "In Person / On Site" and location:
        interview_string += ", " + location

    elif interview_type == "Phone Call" and contact_number:
        interview_string += ", " + contact_number

    upcoming_interviews["fields"][interview_id]["interview_medium"] = updated_medium
    upcoming_interviews["fields"][interview_id]["date"] = interview_date_str
    upcoming_interviews["fields"][interview_id]["time"] = interview_time_str
    upcoming_interviews["fields"][interview_id]["interview_string"] = interview_string









def cleanup_interview_fields(interview_fields, interview_id):
    # Lets start by grabbing the fields we want from the dict:
    interview_type = interview_fields["fields"][interview_id]["interview_type"]
    interview_fields["fields"][interview_id]["interview_type"] = cleanup_interview_type(interview_type)

    status = interview_fields["fields"][interview_id]["status"]
    interview_fields["fields"][interview_id]["status"] = cleanup_interview_status(status)

    location = interview_fields["fields"][interview_id]["location"]
    if location == "N/A" or location == "Remote":
        interview_fields["fields"][interview_id]["location"] = None

    interview_date = interview_fields["fields"][interview_id]["date"]
    interview_fields["fields"][interview_id]["date"] = cleanup_date_format(interview_date)

    interview_time = interview_fields["fields"][interview_id]["time"]
    interview_fields["fields"][interview_id]["time"] = cleanup_time_format(interview_time)
    interview_fields["fields"][interview_id]["past_dated"] = past_dated(interview_date, interview_time)

    contact_number = interview_fields["fields"][interview_id]["contact_number"]
    if contact_number == "N/A":
        interview_fields["fields"][interview_id]["contact_number"] = "Not Provided"

    medium = interview_fields["fields"][interview_id]["interview_medium"]
    other_medium = interview_fields["fields"][interview_id]["other_medium"]
    interview_fields["fields"][interview_id]["interview_medium"] = cleanup_medium(medium, other_medium)






def cleanup_fields_for_single_interview(interview_details, other_medium):
    # random_list = []
    for heading, value in interview_details["fields"].items():
        if value == "N/A":
            interview_details["fields"][heading] = None

    # I want to clean up a few fields to improve how they're displayed:
    interview_type = interview_details["fields"]["interview_type"]
    interview_medium = interview_details["fields"]["medium"]
    interview_date = interview_details["fields"]["date"]
    interview_time = interview_details["fields"]["time"]
    contact_number = interview_details["fields"]["contact_number"]
    video_link = interview_details["fields"]["video_link"]
    display_video_link = interview_details["fields"]["display_video_link"]
    interview_details["fields"]["status"] = cleanup_interview_status(interview_details["fields"]["status"])

    interview_details["fields"]["medium"] = cleanup_medium(interview_medium, other_medium)
    interview_details["fields"]["interview_type"] = cleanup_interview_type(interview_type)

    interview_details["fields"]["past_dated"] = past_dated(interview_date, interview_time)
    interview_details["fields"]["time"] = cleanup_time_format(interview_time)
    interview_details["fields"]["date"] = cleanup_date_format(interview_date)

    if not contact_number:
        interview_details["fields"]["contact_number"] = "Not Provided"

    if not video_link:
        interview_details["fields"]["video_link"] = "Not Provided"

    if not interview_details["fields"]["past_dated"] and interview_details["fields"]["interview_type"] == 'Video / Online': 
        # Now we can check if the interview matches the current date and the user actually provided a video link:
        if check_interview_is_today(interview_date) and interview_details["fields"]["video_link"]: 
            # The interview is today, so we can display the link to the user:
            interview_details["fields"]["display_video_link"] = True

