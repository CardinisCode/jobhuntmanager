from flask import Flask, render_template, session, request, redirect, flash


def display_update_interview_prep_form(application_id, interview_id, interview_prep_id, update_interview_prep_form, applicationsRepo, companyRepo):
    application = applicationsRepo.grabApplicationByID(application_id)
    company = companyRepo.getCompanyById(application.company_id)

    details = {
        "company_name": company, 
        "action_url": '/applications/{}/interview/{}/interview_preparation/{}/update_interview_prep_entry'.format(application_id, interview_id, interview_prep_id)
    }

    return render_template("update_interview_prep.html", details=details, update_interview_prep_form=update_interview_prep_form)


def post_update_interview_preparation(application_id, interview_id, interview_prep_id, update_interview_prep_form, interviewPrepRepo):
    prep_fields = {
        "specific_question": update_interview_prep_form.question.data, 
        "specific_answer": update_interview_prep_form.answer.data, 
        "interview_prep_id": interview_prep_id
    }

    for heading, value in prep_fields.items():
        if value == "":
            prep_fields[heading] = "N/A"

    output = interviewPrepRepo.updateByInterviewPrepID(prep_fields)
    if not output: 
        flash("Failed to update the details. Please try again.")
        redirect_url = '/applications/{}/interview/{}/interview_preparation/{}/update_interview_prep_entry'.format(application_id, interview_id, interview_prep_id)
        return redirect(redirect_url)

    flash("Details for this interview preparation entry have been updated successfully.")

    redirect_url = '/applications/{}/interview/{}/interview_preparation'.format(application_id, interview_id)
    return redirect(redirect_url)