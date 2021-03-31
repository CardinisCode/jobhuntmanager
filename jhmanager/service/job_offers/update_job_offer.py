from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time


def display_update_job_offer_form(application_id, user_id, job_offer_id, update_job_offer, job_offer, companyRepo):
    company_id = job_offer.company_id
    action_url = '/applications/{}/job_offers/{}/update_job_offer'.format(application_id, job_offer_id)
    details = {
        "action_url": action_url, 
        "company_name": companyRepo.getCompanyById(company_id).name, 
        "job_offer_id": job_offer_id
    }

    return render_template("update_job_offer.html", update_job_offer=update_job_offer, details=details)


def post_update_job_offer(application_id, job_offer_id, user_id, update_job_offer_form, jobOffersRepo):
    fields = {
        "job_role": update_job_offer_form.job_role.data,
        "starting_date": update_job_offer_form.starting_date.data, 
        "salary_offered": update_job_offer_form.salary_offered.data,
        "perks_offered": update_job_offer_form.perks_offered.data,
        "offer_response": update_job_offer_form.offer_response.data, 
        "job_offer_id": job_offer_id
    }

    jobOffersRepo.updateByJobOfferID(fields)
    flash("Job offer details updated.")
    redirect_url = '/applications/{}/job_offers/{}'.format(application_id, job_offer_id)

    return redirect(redirect_url)