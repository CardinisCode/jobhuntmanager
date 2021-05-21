from flask import Flask, render_template, session, flash
from datetime import datetime, date


def display_user_profile(user_id, userRepo):
    user = userRepo.getUserByID(user_id)

    links = {
        "change_password": '/userprofile/{}/change_password'.format(user_id),
        "delete_account": '/userprofile/{}/delete_account'.format(user_id),
        "update_email": '/userprofile/{}/update_email'.format(user_id)
    }

    user_details = {
        "username": user.username, 
        "user_email": user.email,
    }

    general_details = {
        "links": links, 
        "user_details": user_details
    }
    
    return render_template("userprofile.html", general_details=general_details)