from flask import Flask, render_template, session, flash
from datetime import datetime, date


def create_userprofile_content(session, userRepo, user_id):
    user_details = userRepo.getByUserID(user_id)
    username = user_details.username
    email_address = user_details.email

    details = {
        "change_password_url": '/userprofile/{}/change_password'.format(user_id),
        "delete_account_url": '/userprofile/{}/delete_account'.format(user_id)
    }

    user_details = {
        "username": {
            "heading": "User Name", 
            "data": username
        },
        "user_email": {
            "heading": "Email Address", 
            "data": email_address, 
            "update_url": '/userprofile/{}/update_email'.format(user_id)
        }, 
    }
    
    return render_template("userprofile.html", user_details=user_details, details=details)