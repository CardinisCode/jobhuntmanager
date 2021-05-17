from flask import Flask, render_template, session, request, redirect, flash


def delete_all_applications_for_user(user_id, applicationsRepo, appNotesRepo, interviewPrepRepo, interviewsRepo, jobOffersRepo):
    applicationsRepo.deleteApplicationsByUserID(user_id)
    interviewsRepo.deleteInterviewsByUserID(user_id)
    interviewPrepRepo.deleteInterviewPrepByUserID(user_id)
    appNotesRepo.deleteNoteByUserID(user_id)
    jobOffersRepo.deleteJobOfferByUserID(user_id)

    flash("All Your Job Applications have been deleted.")
    return redirect("/dashboard")
    
