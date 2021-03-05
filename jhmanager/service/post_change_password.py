from flask import Flask, render_template, session, request, redirect, flash
from passlib.hash import sha256_crypt


def post_change_password(user_id, change_password_form, userRepo): 
    password = change_password_form.password.data

    # Lets ensure this password is not the same password we currently have stored for this user:
    current_user_hash = userRepo.getByUserID(user_id).hash

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
    userRepo.updateHash(fields)

    flash("Password updated!")
    return redirect("/userprofile")