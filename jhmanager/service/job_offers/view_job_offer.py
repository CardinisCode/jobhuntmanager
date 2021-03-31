from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.cleanup_datetime_display import cleanup_date_format


def cleanup_job_offer_details(job_offer_details):
    starting_date = cleanup_date_format(job_offer_details["starting_date"])
    job_offer_details["starting_date"] = starting_date

    offer_response = job_offer_details["offer_response"]

    message = ""
    if offer_response == 'user_accepted':
        message = "I've accepted the offer!"
    elif offer_response == 'user_declined':
        message = "I've declined the offer."
    elif offer_response == 'company_pulled_offer':
        message = "{} pulled the offer.".format(company_name)
    else:
        message = "Still deciding..."
    job_offer_details["offer_response"] = message

    

def display_job_offer(job_offer_id, jobOffersRepo, companyRepo):
    job_offer = jobOffersRepo.getJobOfferByJobOfferID(job_offer_id)
    company = companyRepo.getCompanyById(job_offer.company_id)
    application_id = job_offer.application_id
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

    return render_template("view_job_offer.html", job_offer_details=job_offer_details, company_details=company_details)