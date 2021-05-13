from flask import Flask, render_template, session, request, redirect, flash


def display_delete_company_form(company_id, delete_company_form, companyRepo):
    display = {
        "action_url": '/company/{}/delete_company'.format(company_id), 
        "company_name": companyRepo.getCompanyById(company_id).name
    }

    select_list = [
        (0, "Yes, please delete this company profile."), 
        (1, "No, take me back to the company profile.")
    ]

    delete_company_form.confirm_choice.choices = select_list
    delete_company_form.confirm_choice.default = delete_company_form.confirm_choice.choices[1][0]

    return render_template("delete_company_profile.html", display=display, delete_company_form=delete_company_form)


def delete_company_from_db(company_id, delete_company_form, companyRepo, applicationsRepo, interviewsRepo, interviewPrepRepo, companyNotesRepo, jobOffersRepo, appNotesRepo):
    # Let's review the user's selection:
    customer_choice = delete_company_form.confirm_choice.data
    if customer_choice == 1:
        flash("No changes made.")
        return redirect("/address_book")

    else:
        # Knowing they selected 'yes', we can now delete the company profile:

        # When deleting a company, we're also deleting everything connected to that company ID:
        companyRepo.deleteCompanyByID(company_id)
        companyNotesRepo.deleteCompanyNotesByCompanyID(company_id)
        jobOffersRepo.deleteByCompanyID(company_id)

        # Lets grab all the applications linked to this company's ID:
        applications = applicationsRepo.getApplicationsByCompanyID(company_id)
        if applications:
            for application in applications:
                application_id = application.app_id
                interviewsRepo.deleteByApplicationID(application_id)
                interviewPrepRepo.deleteByApplicationID(application_id)
                appNotesRepo.deleteNoteByApplicationID(application_id)

        # Now we can delete all applications & Notes linked to this Company Id:
        applicationsRepo.deleteApplicationByCompanyID(company_id)

        flash("All Applications, Notes, Interviews & Prep related to this company have been deleted.")

        return redirect("/address_book")
