from flask import Flask, render_template, session, request, redirect, flash


def delete_all_applications_for_user(user_id, userRepo, applicationsRepo, userNotesRepo, interviewPrepRepo, interviewsRepo, jobOffersRepo):
    applicationsRepo.deleteByUserID(user_id)
    interviewsRepo.deleteByUserID(user_id)
    interviewPrepRepo.deleteByUserID(user_id)
    userNotesRepo.deleteByUserID(user_id)
    jobOffersRepo.deleteByUserID(user_id)

    flash("All Your Job Applications have been deleted.")
    return redirect("/dashboard")
    
