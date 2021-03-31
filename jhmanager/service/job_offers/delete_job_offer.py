from flask import Flask, render_template, session, request, redirect, flash


def delete_job_offer_from_db(job_offer_id, jobOffersRepo):
    jobOffersRepo.deleteByJobOfferID(job_offer_id)

    flash("Job Offer successfully deleted.")
    return redirect("/dashboard")