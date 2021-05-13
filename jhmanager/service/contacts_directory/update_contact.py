from flask import Flask, render_template, session, request, redirect, flash


def display_update_contact_form(contact_id, update_contact_form):
    action_url = '/address_book/contact_list/{}/update_contact'.format(contact_id)
    details = {
        "action_url": action_url
    }

    return render_template("update_contact_form.html", update_contact_form=update_contact_form, details=details)


def post_update_contact(contact_id, user_id, update_contact_form, contactRepo):
    details = {
        "full_name": update_contact_form.full_name.data, 
        "job_title": update_contact_form.job_title.data, 
        "contact_number": update_contact_form.contact_number.data,
        "company_name": update_contact_form.company_name.data, 
        "email_address": update_contact_form.email_address.data, 
        "linkedin_profile": update_contact_form.linkedin_profile.data, 
        "contact_id": contact_id
    }

    # If the user leaves any of the optional fields open, they'll be saved in the DB as "N/A":
    for heading, value in details.items():
        if not value:
            details[heading] = "N/A"

    contactRepo.updateContactByID(details)

    redirect_url = '/address_book/contact_list/{}/view_contact'.format(contact_id)
    flash("Contact has been successfully updated!")

    return redirect(redirect_url)
