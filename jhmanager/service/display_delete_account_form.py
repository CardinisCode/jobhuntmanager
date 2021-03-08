from flask import Flask, render_template, session, request, redirect, flash


def display_details_for_delete_user_form(user_id, delete_account_form):
    display = {
        "action_url": '/userprofile/{}/delete_account'.format(user_id)
    }

    return render_template("delete_account.html", delete_account_form=delete_account_form, display=display)