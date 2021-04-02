from flask import Flask, render_template, session, request, redirect, flash


def display_update_contact_form(contact_id, update_contact_form):
    action_url = '/address_book/contact_list/{}/update_contact'.format(contact_id)
    details = {
        "action_url": action_url
    }

    return render_template("update_contact_form.html", update_contact_form=update_contact_form, details=details)