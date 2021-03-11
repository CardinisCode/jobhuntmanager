from flask import Flask, render_template, session, request, redirect, flash


def display_all_company_notes(company_id, user_id, companyRepo, companyNotesRepo):
    company = companyRepo.getCompanyById(company_id)
    
    general_details = { 
        "add_note_url": '/company/{}/add_company_note'.format(company_id),
        "company_name": company.name,
        "empty_table": True
    }



    return render_template("view_company_notes.html", general_details=general_details)