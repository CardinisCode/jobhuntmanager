from flask import Flask, render_template, session, request, redirect, flash


def display_update_email_form(user_id, userRepo, update_email_form):
    details = {
        "update_url": '/userprofile/{}/update_email'.format(user_id),
    }

    return render_template("update_email.html", details=details, update_email_form=update_email_form)


def post_update_email_address(update_email_form, userRepo, user_id):
    details = {
        "email": update_email_form.email.data, 
        "user_id": user_id
    }

    userRepo.updateUserEmailByID(details)


    flash("Email Updated.")
    return redirect("/userprofile")