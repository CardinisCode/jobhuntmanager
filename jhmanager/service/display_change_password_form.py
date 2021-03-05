from flask import Flask, render_template, session, request, redirect, flash


def display_change_password_form_details(user_id, change_password_form, userRepo):
    details = {
        "change_password_url": '/userprofile/{}/change_password'.format(user_id)
    }

    return render_template("change_password.html", change_password_form=change_password_form, details=details)

