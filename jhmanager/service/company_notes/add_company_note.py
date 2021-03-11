from flask import Flask, render_template, session, request, redirect, flash
from datetime import datetime, date


def display_add_company_note_form(company_id, company_note_form, companyRepo):
    company = companyRepo.getCompanyById(company_id)
    details = {
        "company_name": company.name, 
        "company_id": company_id, 
        "action_url": '/company/{}/add_company_note'.format(company_id)
    }

    return render_template("add_company_note.html", company_note_form=company_note_form, details=details)