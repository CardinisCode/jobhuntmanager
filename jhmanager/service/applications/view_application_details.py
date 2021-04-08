from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_time_format
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_files.cleanup_datetime_display import past_dated
from jhmanager.service.cleanup_files.cleanup_job_offer_fields import cleanup_job_offer
from jhmanager.service.cleanup_files.cleanup_app_fields import cleanup_details_for_specific_application
from jhmanager.service.cleanup_files.cleanup_app_fields import cleanup_urls
from jhmanager.service.cleanup_files.cleanup_interview_fields import cleanup_interview_fields
from jhmanager.service.cleanup_files.cleanup_company_fields import prepare_company_website_url
from jhmanager.service.cleanup_files.cleanup_general_fields import replace_na_value_with_none
    

def grab_and_display_job_offers(application_id, user_id, company, jobOffersRepo):
    job_offers = jobOffersRepo.getJobOffersByUserId(user_id)

    job_offers_details = {
        "empty_table": True,
        "fields": None, 
    }

    if not job_offers: 
        return job_offers_details

    count = 0
    
    if job_offers: 
        job_offers_details["fields"] = {}
        job_offers_details["empty_table"] = False
        for job_offer in job_offers:
            job_offer_id = job_offer.job_offer_id
            company_id = job_offer.company_id
            application_id = job_offer.application_id
            if company_id == company.company_id:
                count += 1
                job_offers_details["fields"][job_offer_id] = {
                    "company_name": company.name,
                    "offer_response": job_offer.offer_response, 
                    "offer_accepted": False,
                    "salary_offered": job_offer.salary_offered, 
                    "starting_date": job_offer.starting_date, 
                    "job_role": job_offer.job_role, 
                    "perks_offered": job_offer.perks_offered,
                    "update_url": '/applications/{}/job_offers/{}/update_job_offer'.format(application_id, job_offer_id), 
                    "view_url": '/applications/{}/job_offers/{}'.format(application_id, job_offer_id), 
                    "delete_url": '/applications/{}/job_offers/{}/delete_job_offer'.format(application_id, job_offer_id)
                }
                cleanup_job_offer(job_offers_details, job_offer_id)

    job_offers_details["count"] = count
 
    return job_offers_details


def display_application_details(session, user_id, applicationsRepo, application_id, companyRepo, interviewsRepo, jobOffersRepo):
    application = applicationsRepo.grabApplicationByID(application_id)
    app_date = application.app_date
    app_time = application.app_time
    company_id = application.company_id
    company = companyRepo.getCompanyById(company_id)

    general_details = {
        "links": {}, 
        "company_details": {}, 
        "interview_details": {},
        "user_notes": replace_na_value_with_none(application.user_notes)
    }

    application_details = {}
    application_details["fields"] = {
        "app_id": application.app_id,
        "job_ref" : application.job_ref,
        "date": app_date, 
        "time": app_time, 
        "job_role" : application.job_role, 
        "job_description" : application.job_description,
        "perks" : application.job_perks,
        "technology_stack" : application.tech_stack,
        "salary" : application.salary,
        "platform": application.platform, 
        "interview_stage" : application.interview_stage,
        "emp_type" : application.employment_type, 
        "contact_received?" : application.contact_received, 
    }
    cleanup_details_for_specific_application(application_details)

    # Lets grab some company details:
    general_details["company_details"] = {
        "company_id": company.company_id,
        "company_name": company.name,
        "description": company.description,
    }

    # Now I want to display all the interviews for this application_id:
    all_interviews_for_app_id = interviewsRepo.getTop6InterviewsByApplicationID(application_id)

    # Lets build the interview dict to be displayed to the user.
    general_details["interview_details"] = {
        "empty_fields" : True,
        "interviews_count": 0
    }
    
    # In the case that there are actually interviews for this application, 
    # we want to grab those details & update the "fields" value to contain these values.
    # These values will be displayed to the user, in a table format. 
    interview_fields = None
    count = 0

    if all_interviews_for_app_id != None:
        general_details["interview_details"]["empty_fields"] = False 
        interview_fields = {}
        interview_fields["fields"] = {}

        for interview in all_interviews_for_app_id:
            count += 1
            interview_id = interview.interview_id
            interview_fields["fields"][interview_id] = {
                "number": count, 
                "date": interview.interview_date, 
                "time": interview.interview_time,
                "interview_type": interview.interview_type, 
                "interview_medium": interview.medium, 
                "other_medium": interview.other_medium,
                "contact_number": interview.contact_number,
                "status": interview.status,
                "location": interview.location,
                "past_dated": False,
                "view_more": "/applications/{}/interview/{}".format(application_id, interview_id),
            }
            cleanup_interview_fields(interview_fields, interview_id)

    general_details["links"] = {
        "update_application": '/applications/{}/update_application'.format(application_id), 
        "delete_application": '/applications/{}/delete'.format(application_id), 
        "add_note": '/applications/{}/app_notes/add_note'.format(application_id), 
        "view_notes": '/applications/{}/view_application_notes'.format(application_id), 
        "add_interview": '/applications/{}/add_interview'.format(application_id), 
        "view_interviews": '/applications/{}/view_all_interviews'.format(application_id), 
        "company_profile": '/company/{}/view_company'.format(company.company_id), 
        "company_website": prepare_company_website_url(company.url), 
        "update_company": '/company/{}/update_company'.format(company.company_id),
        "view_job_posting": cleanup_urls(application.job_url),
        "add_job_offer": '/applications/{}/add_job_offer'.format(application_id), 
    }

    interview_fields["interviews_count"] = count
    job_offer_details = grab_and_display_job_offers(application_id, user_id, company, jobOffersRepo) 

    return render_template("view_application.html", application_details=application_details, interview_fields=interview_fields, job_offer_details=job_offer_details, general_details=general_details)
