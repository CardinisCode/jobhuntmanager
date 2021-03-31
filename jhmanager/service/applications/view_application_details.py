from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time
from jhmanager.service.cleanup_datetime_display import cleanup_time_format
from jhmanager.service.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_datetime_display import past_dated
from jhmanager.service.job_offers.cleanup_job_offer_fields import cleanup_job_offer
from jhmanager.service.applications.cleanup_app_fields import cleanup_application_details
from jhmanager.service.interviews.cleanup_interview_fields import cleanup_interview_fields
    

def grab_and_display_job_offers(application_id, jobOffersRepo, user_id, company_details, companyRepo):
    job_offers = jobOffersRepo.getJobOffersByUserId(user_id)

    job_offers_details = {
        "empty_table": True,
        "add_job_offer": '/applications/{}/add_job_offer'.format(application_id), 
    }

    if not job_offers: 
        return job_offers_details

    count = 0
    job_offers_details["details"] = {}
    for job_offer in job_offers:
        job_offers_details["empty_table"] = False
        job_offer_id = job_offer.job_offer_id
        company_id = job_offer.company_id
        application_id = job_offer.application_id
        view_url = '/applications/{}/job_offers/{}'.format(application_id, job_offer_id)
        update_url = '/applications/{}/job_offers/{}/update_job_offer'.format(application_id, job_offer_id)
        if company_id == company_details["fields"]["company_id"]:
            count += 1
            job_offers_details["details"][count] = {
                "company_name": companyRepo.getCompanyById(company_id).name,
                "offer_response": job_offer.offer_response, 
                "offer_accepted": False,
                "salary_offered": job_offer.salary_offered, 
                "starting_date": job_offer.starting_date, 
                "job_role": job_offer.job_role, 
                "perks_offered": job_offer.perks_offered,
                "update_url": update_url, 
                "view_url": view_url
            }
            cleanup_job_offer(job_offers_details, count)

    job_offers_details["count"] = count
 
    return job_offers_details


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
        "emp_type" : application.employment_type, 
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
    count = 0

    if all_interviews_for_app_id != None:
        interview_details["empty_fields"] = False 
        interview_fields["fields"] ={}
        for interview in all_interviews_for_app_id:
            count += 1
            interview_id = interview.interview_id
            status = interview.status
            view_more_url = "/applications/{}/interview/{}".format(application_id, interview_id)
            delete_url = '/applications/{}/interview/{}/delete_interview'.format(application_id, interview_id)
            update_url = '/applications/{}/interview/{}/update_interview'.format(application_id, interview_id)
            prepare_url = '/applications/{}/interview/{}/interview_preparation'.format(application_id, interview_id)
            location = interview.location
            
            interview_fields["fields"][count] = {
                "ID#": interview_id, 
                "date": interview.interview_date, 
                "time": interview.interview_time,
                "interview_type": interview.interview_type, 
                "interview_medium": interview.medium, 
                "other_medium": interview.other_medium,
                "contact_number": interview.contact_number,
                "status": status,
                "location": location,
                "view_more": view_more_url,
                "delete_url": delete_url,
                "update_url": update_url,
                "prepare_url": prepare_url,
                "past_dated": False,
            }
            cleanup_interview_fields(interview_fields, count)

    interview_fields["interviews_count"] = count
    job_offer_details = grab_and_display_job_offers(application_id, jobOffersRepo, user_id, company_details, companyRepo) 

    interview_fields["add_interview_url"] = '/applications/{}/add_interview'.format(application_id)

    return render_template("view_application.html", details=application_details, interview_details=interview_details, interview_fields=interview_fields, company_details=company_details, job_offer_details=job_offer_details)
