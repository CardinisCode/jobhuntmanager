from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.interviews.add_interview import update_interview_stage_in_applications_repo


def delete_interview(application_id, interview_id, interviewsRepo, interviewPrepRepo, applicationsRepo):
    interviewsRepo.deleteInterviewByID(interview_id)
    interviewPrepRepo.deleteInterviewPrepByInterviewID(interview_id)

    update_interview_stage_in_applications_repo(interviewsRepo, application_id, applicationsRepo)

    flash("Interview has been successfully deleted.")
    redirect_url = '/applications/{}'.format(application_id)
    return redirect(redirect_url)