from flask import Flask, render_template, session, request, redirect, flash


def delete_interview(application_id, interview_id, interviewsRepo):
    interviewsRepo.deleteByInterviewID(interview_id)

    flash("Interview has been successfully deleted.")
    redirect_url = '/applications/{}'.format(application_id)
    return redirect(redirect_url)