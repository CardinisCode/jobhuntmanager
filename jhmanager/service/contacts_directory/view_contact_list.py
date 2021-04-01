from flask import Flask, render_template, session, request, redirect, flash


def display_contacts_for_user(user_id, contactRepo):
    contacts_list = contactRepo.getContactsByUserID(user_id)

    general_details = {
        "empty_table": True, 
        "message": "No Contacts to display."
    }

    contact_details = None
    if contacts_list:
        contact_details = {}
        contact_details["fields"] = {}
        general_details["empty_table"] = False
        general_details["message"] = "Not an empty list"

        # for contact in contact_list:
        #     contact_id = contact

    return render_template("view_contacts.html", general_details=general_details, contact_details=contact_details) 