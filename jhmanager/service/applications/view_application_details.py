from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime


def grab_and_display_job_offers(jobOffersRepo, user_id, company_details):
    job_offers = jobOffersRepo.getJobOffersByUserId(user_id)
    if not job_offers: 
        return None

    job_offers_details = {}
    for job_offer in job_offers:
        job_offer_id = job_offer.job_offer_id
        company_id = job_offer.company_id
        job_offers_details["details"] = None
        if company_id == company_details["fields"]["company_id"]:
            job_offers_details["details"] = {
                "offer_response": job_offer.offer_response, 
                "salary_offered": job_offer.salary_offered, 
                "starting_date": job_offer.starting_date, 
                "job_role": job_offer.job_role, 
                "perks_offered": job_offer.perks_offered
            }
            job_offers_details["update_url"] = '/job_offer/{}/update_job_offer'.format(job_offer_id)

    return job_offers_details


def cleanup_interview_fields(interview_fields, interview_id):

    # Lets start by grabbing the fields we want from the dict:
    interview_type = interview_fields["fields"][interview_id]["interview_type"]
    status = interview_fields["fields"][interview_id]["status"]

    # Now I can optimise the presentation of the values for these variables:
    if interview_type == "video_or_online":
        interview_fields["fields"][interview_id]["interview_type"] = "Video / Online"
    elif interview_type == "in_person":
        interview_fields["fields"][interview_id]["interview_type"] = "In Person / On Site"
    else:
        interview_fields["fields"][interview_id]["interview_type"] = "Phone Call"

    # Now to focus on 'status':
    if status == "upcoming":
        status = 'Upcoming Interview'

    elif status == "done":
        status = 'Interview Done'
    
    elif status == "cancelled":
        status = 'The interview has been cancelled'
    
    else:
        status = 'Interview has been post-poned'
    
    interview_fields["fields"][interview_id]["status"] = status


def cleanup_application_details(application_details):
    for heading, value in application_details["fields"].items():
        if value == "N/A":
            application_details["fields"][heading] = None

    interview_stage = application_details["fields"]["interview_stage"]
    if interview_stage == 0:
        application_details["fields"]["interview_stage"] = "No interview lined up yet."

    emp_type = application_details["fields"]["type"]
    if emp_type == "full_time":
        application_details["fields"]["type"] = "Full Time"
    elif emp_type == "part_time":
        application_details["fields"]["type"] = "Part Time"
    elif emp_type == "temp":
        application_details["fields"]["type"] = "Temporary"
    elif emp_type == "other_emp_type": 
        application_details["fields"]["type"] = "Other"
    else:
        application_details["fields"]["type"] = emp_type.capitalize()
    

def display_application_details(session, user_id, applicationsRepo, application_id, companyRepo, interviewsRepo, jobOffersRepo):
    application = applicationsRepo.grabApplicationByID(application_id)
    app_date = application.app_date
    app_time = application.app_time
    company_id = application.company_id
    company = companyRepo.getCompanyById(company_id)

    application_details = {}
    application_details["fields"] = {
        "job_ref" : application.job_ref,
        "date": app_date, 
        "time": app_time, 
        "job_role" : application.job_role, 
        "description" : application.job_description,
        "perks" : application.job_perks,
        "technology_stack" : application.tech_stack,
        "salary" : application.salary,
        "platform": application.platform, 
        "interview_stage" : application.interview_stage,
        "type" : application.employment_type, 
        "contact_Received?" : application.contact_received, 
        "job_url" : application.job_url,
    }
    cleanup_application_details(application_details)

    application_details["update_application_url"] = '/applications/{}/update_application'.format(application_id)
    application_details["delete_application_url"] = '/applications/{}/delete'.format(application_id)
    application_details["add_note_url"] = '/applications/{}/app_notes/add_note'.format(application_id)
    application_details["view_notes_url"] = '/applications/{}/view_application_notes'.format(application_id)
    application_details["add_interview_url"] = '/applications/{}/add_interview'.format(application_id)

    application_details["app_id"] = application_id

    user_notes = application.user_notes
    if user_notes == "N/A": 
        application_details["user_notes"] = None
    else:
        application_details["user_notes"] = user_notes

    # Lets grab some company details:
    company_details = {}
    company_id = company.company_id
    company_details["fields"] = {
        "company_id": company_id,
        "company_name": company.name,
        "view_profile": '/company/{}/view_company'.format(company_id), 
    }

    company_details["update_url"] = '/company/{}/update_company'.format(company_id)
    

    # Now I want to display all the interviews for this application_id:
    all_interviews_for_app_id = interviewsRepo.grabAllInterviewsByApplicationID(application_id)

    # Lets build the interview dict to be displayed to the user.
    # I'll set the default value for "fields" key to be None, as there are currently no values to display.
    interview_details = {
        "message": "No interviews added yet for this application.", 
        "headings": ["ID#", "Date", "Time", "Interview Type", "Status", "Location", "View", "Delete", "Prepare"], 
        "app_id": application_id, 
        "empty_fields" : True,
    }
    
    # In the case that there are actually interviews for this application, 
    # we want to grab those details & update the "fields" value to contain these values.
    # These values will be displayed to the user, in a table format. 
    interview_fields = {}
    if all_interviews_for_app_id != None:
        interview_details["empty_fields"] = False 
        for interview in all_interviews_for_app_id:
            interview_id = interview.interview_id
            status = interview.status
            view_more_url = "/applications/{}/interview/{}".format(application_id, interview_id)
            delete_url = '/applications/{}/interview/{}/delete_interview'.format(application_id, interview_id)
            prepare_url = '/applications/{}/interview/{}/interview_preparation'.format(application_id, interview_id)
            location = interview.location
            interview_fields["fields"] ={}
            interview_fields["fields"][interview_id] = {
                "ID#": interview_id, 
                "date": interview.interview_date, 
                "time": interview.interview_time,
                "interview_type": interview.interview_type, 
                "status": status,
                "location": location,
                "view_more": view_more_url,
                "delete_url": delete_url,
                "prepare_url": prepare_url
            }

            cleanup_interview_fields(interview_fields, interview_id)

    job_offer_details = grab_and_display_job_offers(jobOffersRepo, user_id, company_details) 


    return render_template("view_application.html", details=application_details, interview_details=interview_details, interview_fields=interview_fields, company_details=company_details, job_offer_details=job_offer_details)
