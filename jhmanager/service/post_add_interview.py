from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time


def InsertFieldsIntoInterviewHistory(interviewsRepo, user_id, company_name, interview_date, interview_time, interview_type, job_role, interviewers, interview_location, video_medium, other_medium, contact_number, status):
    company_name = company_name.data
    interview_date = str(interview_date.data)
    interview_time = str(interview_time.data)
    interview_type = interview_type.data

    job_role = job_role.data
    if not job_role: 
        job_role = "N/A"

    interviewers = interviewers.data
    if not interviewers:
        interviewers = "N/A"

    location = interview_location.data
    if not location:
        location = "N/A"

    medium = video_medium.data
    if not medium:
        medium = "N/A"

    other_medium = other_medium.data
    if not other_medium:
        other_medium = "N/A"

    contact_number = contact_number.data
    if not contact_number:
        contact_number = "N/A"

    status = status.data
    if not status: 
        status = "upcoming"

    insert_values = interviewsRepo.InsertNewInterviewDetails(user_id, company_name, interview_date, interview_time, job_role, interviewers, interview_type, location, medium, other_medium, contact_number, status)

    # For Development purposes, if this function ever fails to insert the values, we need an error message flashing to notify us:
    if not insert_values:
        flash("Failed to insert values into InterviewHistoryRepo. Please investigate!")
        return False

    # If it gets here, the new interview has been successfully added to the repo.
    return True



def gather_details_and_add_to_display_dict(company_name, interview_date, interview_time, interview_type, job_role, interviewers, interview_location, video_medium, other_medium, contact_number, status, interview_stage):
    details = {}
    
    # Gather all fields to be displayed to user as confirmation:
    details = {
        "company_name" : {
            "label": company_name.label, 
            "data": company_name.data
        }, 
        "interview_date": {
            "label": interview_date.label, 
            "data": interview_date.data
        }, 
        "interview_time": {
            "label": interview_time.label, 
            "data": interview_time.data
        }, 
        "job_role": {
            "label": job_role.label, 
            "data": job_role.data
        }
    }

    # I want to display the interview_type as text, not a drop down option
    # So I'll format out the data will be displayed to the user:

    interview_type_data = interview_type.data
    if interview_type_data == "in_person":
        interview_type_data = "In Person"
    elif interview_type_data == "video_or_online":
        interview_type_data = "Video / Online"
    elif interview_type_data == "phone_call":
        interview_type_data = "Phone call"

    details["interview_type"] = {
        "label": "Type", 
        "data": interview_type_data
    }

    if interviewers.data != "Unknown at present":
        details["interviewers"] = {
            "label": "Interviewers' names", 
            "data": interviewers.data
        }

    # Let's set a few conditions for what gets displayed to the user:
    if interview_type.data == 'in_person':
        details["interview_type"] = {
            "label": interview_type.label,
            "data": "In Person"
        }

        details["interview_location"] = {
            "label": interview_location.label, 
            "data": interview_location.data
        }

    if interview_type.data == 'phone_call': 
        details["phone_call"] = {
            "label": contact_number.label,
            "data": contact_number.data
        } 

    # Let's replace the dropdown options for video_medium with just the plain text for video_medium's data.
    video_medium_data = video_medium.data
    
    if interview_type.data == 'video_or_online':
        video_medium_data = video_medium.data

        # Let's improve the data for user presentation:
        if video_medium_data == 'skype':
            video_medium_data = "Skype"
        elif video_medium_data == 'zoom':
            video_medium_data = "Zoom"
        elif video_medium_data == 'google_chat':
            video_medium_data = "Google Chat"
        elif video_medium_data == "meet_jit_si":
            video_medium_data = "Meet.Jit.Si"
        
        # If the user selects 'other', then we want to display which medium they provided (in the 'other_medium' field)
        else:
            video_medium_data = other_medium.data

        # Now the data can be added to the dictionary in its final form
        details["video_medium"] = {
            "label": video_medium.label, 
            "data": video_medium_data
        } 

    # Let's capitalise each possible value of 'status':
    if status.data == "upcoming":
        status.data = "Upcoming"
    
    elif status.data == "done":
        status.data = "Interview Done!"

    elif status.data == 'cancelled':
        status.data = "Cancelled"

    else:
        status.data = "Post-poned"
    
    details["status"] = {
        "label": "Interview Status", 
        "data": status.data
    }

    interview_stage_text = "Interview #{interview_stage} lined up.".format(interview_stage = str(interview_stage))
    details["interview_stage"] = {
        "label": "Interview Stage", 
        "data": interview_stage_text
    }

    return details


def check_businessName_against_application_history(company_name, user_id, applicationsRepo):
    company_already_exists_in_db = False
    query_results = applicationsRepo.checkCompanyNameInApplicationHistoryForUser(str(company_name.data), user_id)
    for row in query_results:
        if row[0] == 1:
            company_already_exists_in_db = True
        
    return company_already_exists_in_db


def update_interview_stage_for_existing_application(applicationsRepo, user_id, company_name):
    # # Lets start by setting some default values:
    message = "Interview stage has not been successfully updated."
    updated_interview_stage = None

    # Lets first check what the current interview stage is for this company name:
    fields = (str(user_id), str(company_name.data))
    grab_interview_stage = applicationsRepo.grabApplicationStageForCompanyNameForActiveUser(fields)
    for item in grab_interview_stage:
        current_interview_stage = item[0]

    # Let's update the interview_stage based on interview_stage's current value:
    updated_interview_stage = int(current_interview_stage) + 1
    details = (str(updated_interview_stage), int(user_id), str(company_name.data))
    update = applicationsRepo.updateInterviewStageAfterAddingNewInterview(details)
    if update == 0:
        message = "The Interview stage for this company has been successfully updated."
        return (updated_interview_stage, message)

    return (updated_interview_stage, message)


def add_interview_details_to_application_history_for_unknown_company_name(applicationsRepo, user_id, company_name, job_role):
        # Let's add the details for this interview into application_history:
        # application_date = str(datetime.date(datetime.now()))
        application_date = str(datetime.date(datetime.now()))
        employment_type = "N/A"
        location = "Remote"
        job_description = "N/A"
        notes = "N/A"
        platform = "N/A"
        perks = "N/A"
        company_description = "N/A"
        tech_stack = "N/A"
        url = "N/A"
        stage = "N/A"
        contact_received = "yes"
        job_ref = "N/A"
        salary =  "N/A"
        company_name_value = company_name._value()
        job_role_value = job_role._value()

        applicationsRepo.insertApplicationDetailsToApplicationHistory(user_id, application_date, employment_type, location, job_description, notes, job_role_value, company_name_value, platform, perks, company_description, tech_stack, url, stage, contact_received, job_ref, salary)


def post_add_interview(session, user_id, form, interviewsRepo, applicationsRepo):
    #Grab and verify field data:
    company_name = form.company_name 
    interview_date = form.interview_date
    interview_time = form.interview_time
    interview_type = form.interview_type
    job_role = form.job_role
    interviewers = form.interviewer_names
    interview_location = form.interview_location
    video_medium = form.interview_medium
    other_medium = form.other_medium
    contact_number = form.phone_call
    status = form.status

    # Lets check if the company name already exists in our Db:
    company_already_exists_in_db = check_businessName_against_application_history(company_name, user_id, applicationsRepo)
    if company_already_exists_in_db: 
        flash("Company already exists in DB, consider updating the application details for this company.")
        # Create SQL query to update entry for this company in application_history -> update interview_stage = "Interview lined up."
        interview_stage_updated = update_interview_stage_for_existing_application(applicationsRepo, user_id, company_name)
        message = interview_stage_updated[1]
        interview_stage = interview_stage_updated[0]
        if interview_stage == None:
            flash(message)

    else:
        # The user has added an interview for company_name without adding a new application for that company first:
        flash("Use interview details to create a new application for this company.")
        interview_stage = 0

        add_interview_details_to_application_history_for_unknown_company_name(applicationsRepo, user_id, company_name, job_role)

        # # Let's add the details for this interview into application_history:
        # # application_date = str(datetime.date(datetime.now()))
        # application_date = str(datetime.date(datetime.now()))
        # employment_type = "N/A"
        # location = "Remote"
        # job_description = "N/A"
        # notes = "N/A"
        # platform = "N/A"
        # perks = "N/A"
        # company_description = "N/A"
        # tech_stack = "N/A"
        # url = "N/A"
        # stage = "N/A"
        # contact_received = "yes"
        # job_ref = "N/A"
        # salary =  "N/A"
        # company_name_value = company_name._value()
        # job_role_value = job_role._value()

        # applicationsRepo.insertApplicationDetailsToApplicationHistory(user_id, application_date, employment_type, location, job_description, notes, job_role_value, company_name_value, platform, perks, company_description, tech_stack, url, stage, contact_received, job_ref, salary)


    # Add details to application_history in SQL DB:
    InsertFieldsIntoInterviewHistory(interviewsRepo, user_id, company_name, interview_date, interview_time, interview_type, job_role, interviewers, interview_location, video_medium, other_medium, contact_number, status)

    # Add details to a dict to be displayed to the template
    details = gather_details_and_add_to_display_dict(company_name, interview_date, interview_time, interview_type, job_role, interviewers, interview_location, video_medium, other_medium, contact_number, status, interview_stage)

    return render_template("interview_details.html", details=details)


# def add_interview_details_to_interviewHistoryRepo()


