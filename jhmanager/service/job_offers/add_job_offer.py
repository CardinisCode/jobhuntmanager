from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time


def display_add_job_offer_form(application_id, add_job_offer, companyRepo, applicationsRepo):
    application = applicationsRepo.getApplicationByID(application_id)
    company = companyRepo.getCompanyById(application.company_id)
    action_url = '/applications/{}/add_job_offer'.format(application_id)

    details = {
        "action_url": action_url, 
        "company_name": company.name
    }

    return render_template("add_job_offer.html", add_job_offer=add_job_offer, details=details)


def post_add_job_offer(application_id, user_id, add_job_offer, companyRepo, applicationsRepo, jobOffersRepo):
    application = applicationsRepo.getApplicationByID(application_id)
    company = companyRepo.getCompanyById(application.company_id)
    current_date = datetime.now().date()

    fields = {
        "user_id": user_id,
        "company_id": company.company_id,
        "application_id": application_id,
        "entry_date": current_date, 
        "job_role": add_job_offer.job_role.data,
        "starting_date": add_job_offer.starting_date.data, 
        "salary_offered": add_job_offer.salary_offered.data,
        "perks_offered": add_job_offer.perks_offered.data,
        "offer_response": add_job_offer.offer_response.data
    }

    job_offer_id = jobOffersRepo.CreateJobOffer(fields)
    flash("Job offer saved in the DB.")

    redirect_url = '/applications/{}/job_offers/{}'.format(application_id, job_offer_id)

    return redirect(redirect_url)