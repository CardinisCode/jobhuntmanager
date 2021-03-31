from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time


def display_add_job_offer_form(application_id, user_id, add_job_offer, companyRepo):
    all_companies_for_user = companyRepo.getAllCompanyEntriesForUser(user_id)
    company_names = []
    for company in all_companies_for_user:
        company_names.append(company.name)

    add_job_offer.company_list.choices = [(int(company.company_id), company.name) for company in all_companies_for_user]
    action_url = '/applications/{}/add_job_offer'.format(application_id)

    details = {
        "action_url": action_url
    }

    return render_template("add_job_offer.html", add_job_offer=add_job_offer, details=details)


def post_add_job_offer(user_id, add_job_offer, companyRepo, applicationsRepo, jobOffersRepo):
    company_id = add_job_offer.company_list.data
    company_name = companyRepo.getCompanyById(company_id).name

    fields = {
        "user_id": user_id,
        "company_id": company_id,
        "job_role": add_job_offer.job_role.data,
        "starting_date": add_job_offer.starting_date.data, 
        "salary_offered": add_job_offer.salary_offered.data,
        "perks_offered": add_job_offer.perks_offered.data,
        "offer_response": add_job_offer.offer_response.data
    }

    jobOffersRepo.addJobOfferToHistory(fields)
    flash("Job offer saved in the DB.")

    return redirect('/dashboard')