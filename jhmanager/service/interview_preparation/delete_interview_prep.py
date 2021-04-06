from flask import Flask, render_template, session, request, redirect, flash


def delete_interview_prep_details(application_id, interview_id, interview_prep_id, interviewPrepRepo):
    interview_prep = interviewPrepRepo.getEntryByInterviewPrepID(interview_prep_id)
    subject = interview_prep.question

    interviewPrepRepo.deleteByInterviewPrepID(interview_prep_id)

    redirect_url = '/applications/{}/interview/{}/interview_preparation'.format(application_id, interview_id)
    flash("Interview preparation for subject: {} has been deleted.".format(subject))
    return redirect(redirect_url)