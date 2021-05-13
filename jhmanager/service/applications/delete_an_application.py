from flask import Flask, render_template, session, request, redirect, flash


def delete_application(application_id, applicationsRepo, interviewsRepo, interviewPrepRepo, appNotesRepo, jobOffersRepo):
    # To delete an application, I simply the relevant SQL query in applicationsRepo, using the application_id.
    applicationsRepo.deleteApplicationByID(application_id)
    interviewsRepo.deleteByApplicationID(application_id)
    appNotesRepo.deleteNoteByApplicationID(application_id)
    jobOffersRepo.deleteByApplicationID(application_id)

    # Once the application is deleted, the user will be redirected the 'Applications' page:
    return redirect('/applications')