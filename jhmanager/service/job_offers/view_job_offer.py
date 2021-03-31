from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.job_offers.cleanup_job_offer_fields import cleanup_offer_response
from jhmanager.service.applications.cleanup_app_fields import cleanup_interview_stage


def cleanup_job_offer_details(job_offer_details):
    starting_date = job_offer_details["starting_date"]
    job_offer_details["starting_date"] = cleanup_date_format(starting_date)

    offer_response = job_offer_details["offer_response"]
    job_offer_details["offer_response"] = cleanup_offer_response(offer_response)

    
def cleanup_app_details(application_details):
    interview_stage = application_details["interview_stage"]
    application_details["interview_stage"] = cleanup_interview_stage(interview_stage)

    emp_type = application_details["emp_type"]
    job_description = application_details["job_description"] 

    if emp_type == "full_time":
        application_details["emp_type"] = "Full Time"
    elif emp_type == "part_time":
        application_details["emp_type"] = "Part Time"
    elif emp_type == "temp":
        application_details["emp_type"] = "Temporary"
    elif emp_type == "contract":
        application_details["emp_type"] = "Contract"
    else: 
        application_details["emp_type"] = "Other"

    if job_description == "N/A":
        application_details["job_description"] = "None provided."


def display_job_offer(job_offer_id, jobOffersRepo, companyRepo, applicationsRepo):
    job_offer = jobOffersRepo.getJobOfferByJobOfferID(job_offer_id)
    company = companyRepo.getCompanyById(job_offer.company_id)
    application_id = job_offer.application_id
    application = applicationsRepo.grabApplicationByID(application_id)

    update_url = '/applications/{}/job_offers/{}/update_job_offer'.format(application_id, job_offer_id)
    delete_url = '/applications/{}/job_offers/{}/delete_job_offer'.format(application_id, job_offer_id)
    company_profile_url = '/company/{}/view_company'.format(company.company_id)

    job_offer_details = {
        "job_role": job_offer.job_role, 
        "starting_date": job_offer.starting_date, 
        "salary_offered": job_offer.salary_offered, 
        "perks_offered": job_offer.perks_offered, 
        "offer_response": job_offer.offer_response, 
        "update_offer_url": update_url, 
        "delete_offer_url": delete_url, 
    }
    cleanup_job_offer_details(job_offer_details)

    company_details = {
        "name": company.name, 
        "description": company.description, 
        "industry": company.industry, 
        "profile_url": company_profile_url,
    }

    application_details = {
        "interview_stage": application.interview_stage, 
        "job_description": application.job_description, 
        "emp_type": application.employment_type,
        "view_application": '/applications/{}'.format(application_id)
    }
    cleanup_app_details(application_details)

    return render_template("view_job_offer.html", job_offer_details=job_offer_details, company_details=company_details, application_details=application_details)