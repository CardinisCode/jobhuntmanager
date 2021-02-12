from flask import Flask, render_template, session, flash
from datetime import datetime, date


def create_userprofile_content(session, userRepo, user_id):
    username = userRepo.getUsernameByUserID(user_id)
    email_address = userRepo.getEmailAddressByUserID(user_id)

    user_details = {
        "username": username,
        "user_email": email_address
    }
    
    return render_template("userprofile.html", user_details=user_details)