from flask import Flask, render_template, session, request, redirect, flash


def display_add_new_contact_form(new_contact_form):
    details = {
        "action_url": '/address_book/contact_list/add_contact'
    }

    return render_template("add_new_contact.html", new_contact_form=new_contact_form, details=details)


def post_add_new_contact(new_contact_form, user_id, contactRepo):
    details = {
        "user_id": user_id, 
        "full_name": new_contact_form.full_name.data, 
        "job_title": new_contact_form.job_title.data, 
        "contact_number": new_contact_form.contact_number.data, 
        "company_name": new_contact_form.company_name.data, 
        "email_address": new_contact_form.email_address.data,
        "linkedin_profile": new_contact_form.linkedin_profile.data
    }

    # If the user leaves any of the optional fields open, they'll be saved in the DB as "N/A":
    for heading, value in details.items():
        if not value:
            details[heading] = "N/A"

    contactRepo.create_contact(details)
    flash("New Contact saved successfully.")

    return redirect('/address_book/contact_list')