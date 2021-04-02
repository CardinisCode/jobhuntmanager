from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.address_book.cleanup_addressbook_values import cleanup_contact_fields


def display_contacts_for_user(user_id, contactRepo):
    contacts_list = contactRepo.getContactsByUserID(user_id)

    general_details = {
        "empty_list": True, 
        "add_new_contact": '/address_book/contact_list/add_contact'
    }

    contact_details = None
    if contacts_list:
        contact_details = {}
        contact_details["fields"] = {}
        general_details["empty_list"] = False

        for contact in contacts_list:
            contact_id = contact.contact_id
            view_contact = '/address_book/contact_list/{}/view_contact'.format(contact_id)
            contact_details["fields"][contact_id] = {
                "full_name": contact.full_name,
                "job_title": contact.job_title, 
                "company_name": contact.company_name,
                "view_contact": view_contact
            }
            cleanup_contact_fields(contact_details, contact_id)

    return render_template("view_contacts.html", general_details=general_details, contact_details=contact_details) 