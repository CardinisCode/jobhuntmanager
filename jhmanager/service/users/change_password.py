from flask import Flask, render_template, session, request, redirect, flash
from passlib.hash import sha256_crypt


def display_change_password_form(user_id, change_password_form):
    details = {
        "change_password_url": '/userprofile/{}/change_password'.format(user_id)
    }

    return render_template("change_password.html", change_password_form=change_password_form, details=details)


def post_change_password(change_password_form, user_id, userRepo): 
    password = change_password_form.password.data

    # Lets ensure this password is not the same password we currently have stored for this user:
    current_user_hash = userRepo.getUserByID(user_id).hash

    match = sha256_crypt.verify(password, current_user_hash)
    if match: 
        flash("This password matches the current password.")
        redirect_url = '/userprofile/{}/change_password'.format(user_id)
        return redirect(redirect_url)
    
    # Now to hash and update the password:
    hashed_password = sha256_crypt.encrypt(str(password))
    fields = {
        "hash": hashed_password, 
        "user_id": user_id
    }
    userRepo.updateUserHashByID(fields)

    flash("Password updated!")
    return redirect("/userprofile")