from flask import Flask, render_template, session, flash
from datetime import datetime, date


def create_userprofile_content(session, userRepo, user_id):
    user_details = userRepo.getByUserID(user_id)
    username = user_details.username
    email_address = user_details.email

    user_details = {
        "username": {
            "heading": "UserName", 
            "data": username
        },
        "user_email": {
            "heading": "Email Address", 
            "data": email_address
        }            
    }
    
    return render_template("userprofile.html", user_details=user_details)