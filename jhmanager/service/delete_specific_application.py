from flask import Flask, render_template, session, request, redirect, flash


def delete_application(application_id, applicationsRepo):
    # To delete an application, I simply the relevant SQL query in applicationsRepo, using the application_id.
    applicationsRepo.deleteEntryByApplicationID(application_id)

    # Once the application is deleted, I'll redirect the user to all their applications:
    return redirect('/applications')