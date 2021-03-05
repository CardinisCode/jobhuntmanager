from flask import Flask, render_template, session, request, redirect, flash


def post_update_email_address(update_email_form, userRepo, user_id):
    

    flash("Email Updated.")
    return redirect("/userprofile")
