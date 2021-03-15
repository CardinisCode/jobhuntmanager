from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time


def display_add_job_offer_form(user_id, add_job_offer, companyRepo):
    all_companies_for_user = companyRepo.getAllCompanyEntriesForUser(user_id)
    company_names = []
    for company in all_companies_for_user:
        company_names.append(company.name)

    add_job_offer.company_list.choices = [(int(company.company_id), company.name) for company in all_companies_for_user]

    details = {
        "action_url": '/add_job_offer'
    }


    return render_template("add_job_offer.html", add_job_offer=add_job_offer, details=details)


def post_add_job_offer(user_id, add_job_offer, companyRepo):
    company_id = add_job_offer.company_list.data
    company_name = companyRepo.getCompanyById(company_id).name



    return None