from flask import Flask, render_template, session, request, redirect


def display_all_user_notes_for_company(user_id, company_id, userNotesRepo, companyRepo):

    details = {
        "company_name": companyRepo.getCompanyById(company_id).name
    }

    return render_template("view_user_notes_for_company.html", details=details)