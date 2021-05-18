from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_time_format
from jhmanager.service.cleanup_files.cleanup_datetime_display import present_dated
from jhmanager.service.cleanup_files.cleanup_datetime_display import past_dated
from jhmanager.service.cleanup_files.cleanup_general_fields import cleanup_field_value
from jhmanager.service.cleanup_files.cleanup_general_fields import cleanup_urls
from datetime import datetime, time


def cleanup_interview_type(interview_type):
    if interview_type == "video_or_online":
        return "Video / Online"
    elif interview_type == "in_person":
        return "In Person / On Site"
    elif interview_type == "phone_call":
        return "Phone Call"
    else:
        return interview_type

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


def cleanup_interview_fields(interview_details, interview_id, other_medium): 
    for heading, value in interview_details["fields"][interview_id].items():
        if value == "N/A":
            interview_details["fields"][interview_id][heading] = None
        elif heading == "status":
            interview_details["fields"][interview_id][heading] = cleanup_interview_status(value)
        elif heading == "medium" or heading == "interview_medium":
            interview_details["fields"][interview_id][heading] = cleanup_medium(value, other_medium)
        elif heading == "interview_type":
            interview_details["fields"][interview_id][heading] = cleanup_interview_type(value)
        elif heading == "time":
            interview_details["fields"][interview_id][heading] = cleanup_time_format(value)
        elif heading == "date":
            interview_details["fields"][interview_id][heading] = cleanup_date_format(value)
        elif heading == "contact_number" or heading == "video_link":
            if value:
                continue
            else:
                interview_details["fields"][interview_id][heading] = "Not Provided"
        elif heading == "number" or heading == "past_dated" or heading == "view_more":
            continue
        else:
            interview_details["fields"][interview_id][heading] = cleanup_field_value(value)


def cleanup_specific_interview(interview_details, other_medium):
    for heading, value in interview_details["fields"].items():
        if value == "N/A":
            interview_details["fields"][heading] = None
        elif heading == "status":
            interview_details["fields"][heading] = cleanup_interview_status(value)
        elif heading == "medium":
            interview_details["fields"][heading] = cleanup_medium(value, other_medium)
        elif heading == "interview_type":
            interview_details["fields"][heading] = cleanup_interview_type(value)
        elif heading == "time":
            interview_details["fields"][heading] = cleanup_time_format(value)
        elif heading == "date":
            interview_details["fields"][heading] = cleanup_date_format(value)
        elif heading == "contact_number" or heading == "video_link":
            if not value:
                interview_details["fields"][heading] = "Not Provided"
        else:
            interview_details["fields"][heading] = cleanup_field_value(value)

    interview_date = interview_details["fields"]["date"]
    interview_time = interview_details["fields"]["time"]
    interview_details["fields"]["past_dated"] = past_dated(interview_date, interview_time)
    if not interview_details["fields"]["past_dated"] and interview_details["fields"]["interview_type"] == 'Video / Online': 
        # Now we can check if the interview matches the current date and the user actually provided a video link:
        if present_dated(interview_date) and interview_details["fields"]["video_link"]: 
            # The interview is today, so we can display the link to the user:
            interview_details["fields"]["display_video_link"] = True


