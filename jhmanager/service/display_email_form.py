from flask import Flask, render_template, session, request, redirect
from jhmanager.forms.update_user_details import UpdateEmailAddressForm


def display_update_email_form(user_id, userRepo):
    user_details = userRepo.getByUserID(user_id)
    email_address = user_details.email
    update_email_form = UpdateEmailAddressForm(obj=user_details)


    details = {
        "update_url": '/userprofile/{}/update_email'.format(user_id),
    }

    return render_template("update_email.html", details=details, update_email_form=update_email_form)