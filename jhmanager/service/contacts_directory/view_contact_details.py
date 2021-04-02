from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.contacts_directory.cleanup_contact import cleanup_contact_details


def display_contact_details(contact_id, contactRepo):
    contact = contactRepo.getContactByContactID(contact_id)

    contact_details = {
        "empty_contact": True, 
        "fields": None, 
        "address_book": '/address_book', 
        "contacts_list": '/address_book/contact_list'
    }

    if contact:
        contact_details["empty_contact"] = False
        contact_details["fields"] = {}
        contact_id = contact.contact_id
        company_name = contact.company_name
        contact_details["fields"] = {
            "full_name": contact.full_name, 
            "job_title": contact.job_title, 
            "contact_number": contact.contact_number, 
            "company_name": company_name, 
            "email_address": contact.email_address, 
            "linkedin_profile": contact.linkedin_profile
        }
        # cleanup_contact_details(contact_details, contact_id)


    return render_template("view_contact_details.html", contact_details=contact_details)