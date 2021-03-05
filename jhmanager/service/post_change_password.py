from flask import Flask, render_template, session, request, redirect, flash


def post_change_password(user_id, change_password_form, userRepo): 
    
    flash("Password updated!")
    return redirect("/userprofile")