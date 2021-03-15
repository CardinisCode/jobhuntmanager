from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, time


def display_add_job_offer_form(user_id, add_job_offer, companyRepo):
    all_companies_for_user = companyRepo.getAllCompanyEntriesForUser(user_id)
    company_names = []
    for company in all_companies_for_user:
        company_names.append(company.name)
    add_job_offer.company_list.choices = company_names


    return render_template("add_job_offer.html", add_job_offer=add_job_offer)