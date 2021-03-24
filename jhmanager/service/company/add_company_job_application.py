from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime


def display_add_company_application_form(add_application_form, company_id, companyRepo):
    details = {
        "company_name": companyRepo.getCompanyById(company_id).name
    }

    return render_template('add_company_job_application.html', add_application_form=add_application_form, details=details)