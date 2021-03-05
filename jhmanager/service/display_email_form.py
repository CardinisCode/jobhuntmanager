from flask import Flask, render_template, session, request, redirect


def display_update_email_form(user_id, userRepo, update_email_form):
    details = {
        "update_url": '/userprofile/{}/update_email'.format(user_id),
    }

    return render_template("update_email.html", details=details, update_email_form=update_email_form)