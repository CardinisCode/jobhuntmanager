from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time


def display_update_job_offer_form(application_id, job_offer_id, update_job_offer, jobOffersRepo, companyRepo):
    job_offer = jobOffersRepo.getJobOfferByID(job_offer_id)
    company = companyRepo.getCompanyById(job_offer.company_id)
    details = {
        "action_url": '/applications/{}/job_offers/{}/update_job_offer'.format(application_id, job_offer_id), 
        "company_name": company.name,
    }

    return render_template("update_job_offer.html", update_job_offer=update_job_offer, details=details)


def post_update_job_offer(application_id, job_offer_id, update_job_offer_form, jobOffersRepo):
    fields = {
        "job_role": update_job_offer_form.job_role.data,
        "starting_date": update_job_offer_form.starting_date.data, 
        "salary_offered": update_job_offer_form.salary_offered.data,
        "perks_offered": update_job_offer_form.perks_offered.data,
        "offer_response": update_job_offer_form.offer_response.data, 
        "job_offer_id": job_offer_id
    }

    jobOffersRepo.updateJobOfferByID(fields)
    flash("Job offer details updated.")
    redirect_url = '/applications/{}/job_offers/{}'.format(application_id, job_offer_id)

    return redirect(redirect_url)