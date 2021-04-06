from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_time_format
from jhmanager.service.cleanup_files.cleanup_datetime_display import past_dated


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
    updated_medium = ""
    if medium == "google_chat":
        updated_medium = "Google Chat"
    elif medium == "meet_jit_si":
        updated_medium = "Meet.Jit.Si"
    elif medium == "other":
        updated_medium = other_medium
    else: 
        updated_medium = medium.capitalize()


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


