from flask import Flask, render_template, session, request, redirect, flash
from passlib.hash import sha256_crypt


def display_delete_user_form(user_id, delete_account_form):
    display = {
        "action_url": '/userprofile/{}/delete_account'.format(user_id)
    }

    return render_template("delete_account.html", delete_account_form=delete_account_form, display=display)



def post_delete_user_form(delete_account_form, user_id, userRepo): 
    password = delete_account_form.password.data

    # Lets verify the password is correct:
    current_hash = userRepo.getByUserID(user_id).hash
    match = sha256_crypt.verify(password, current_hash)
    if not match:
        flash("Incorrect password.")
        redirect_url = '/userprofile/{}/delete_account'.format(user_id)
        return redirect(redirect_url)

    userRepo.deleteByUserID(user_id)

    flash("Your account has been successfully deleted!")
    return redirect("/")