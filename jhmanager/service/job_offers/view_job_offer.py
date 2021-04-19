from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_files.cleanup_datetime_display import cleanup_date_format
from jhmanager.service.cleanup_files.cleanup_job_offer_fields import cleanup_offer_response
from jhmanager.service.cleanup_files.cleanup_app_fields import cleanup_interview_stage
from jhmanager.service.cleanup_files.cleanup_app_fields import cleanup_details_for_specific_application


def cleanup_job_offer_details(job_offer_details):
    starting_date = job_offer_details["starting_date"]
    job_offer_details["starting_date"] = cleanup_date_format(starting_date)

    company_name = job_offer_details["company_name"]
    offer_response = job_offer_details["offer_response"]
    job_offer_details["offer_response"] = cleanup_offer_response(offer_response, company_name)


def display_job_offer(job_offer_id, jobOffersRepo, companyRepo, applicationsRepo):
    job_offer = jobOffersRepo.getJobOfferByJobOfferID(job_offer_id)
    company = companyRepo.getCompanyById(job_offer.company_id)
    application = applicationsRepo.grabApplicationByID(job_offer.application_id)

    job_offer_details = {
        "job_role": job_offer.job_role, 
        "starting_date": job_offer.starting_date, 
        "salary_offered": job_offer.salary_offered, 
        "perks_offered": job_offer.perks_offered, 
        "offer_response": job_offer.offer_response, 
        "company_name": company.name
    }
    cleanup_job_offer_details(job_offer_details)

    company_details = {
        "name": company.name, 
        "description": company.description, 
        "industry": company.industry, 
    }

    application_details = {}
    application_details["fields"] = {
        "interview_stage": application.interview_stage, 
        "job_description": application.job_description, 
        "emp_type": application.employment_type,
        "date": "N/A",
        "time": "N/A", 
    }
    cleanup_details_for_specific_application(application_details)

    links = {
        "update_offer": '/applications/{}/job_offers/{}/update_job_offer'.format(application.app_id, job_offer_id), 
        "delete_offer": '/applications/{}/job_offers/{}/delete_job_offer'.format(application.app_id, job_offer_id), 
        "company_profile": '/company/{}/view_company'.format(company.company_id),
        "view_application": '/applications/{}'.format(application.app_id)
    }

    general_details = {
        "job_offer_details": job_offer_details, 
        "company_details": company_details, 
        "application_details": application_details, 
        "links": links
    }

    return render_template("view_job_offer.html", general_details=general_details)