from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_files.cleanup_job_offer_fields import cleanup_offer_response
from jhmanager.service.cleanup_files.cleanup_app_fields import cleanup_interview_stage
from jhmanager.service.cleanup_files.cleanup_app_fields import cleanup_application_details


def cleanup_job_offer_details(job_offer_details):
    starting_date = job_offer_details["starting_date"]
    job_offer_details["starting_date"] = cleanup_date_format(starting_date)

    offer_response = job_offer_details["offer_response"]
    job_offer_details["offer_response"] = cleanup_offer_response(offer_response)


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

    application_details = {}
    application_details["fields"] = {
        "interview_stage": application.interview_stage, 
        "job_description": application.job_description, 
        "emp_type": application.employment_type,
        "date": "N/A",
        "time": "N/A", 
        "view_application": '/applications/{}'.format(application_id)
    }
    cleanup_application_details(application_details)

    return render_template("view_job_offer.html", job_offer_details=job_offer_details, company_details=company_details, application_details=application_details)