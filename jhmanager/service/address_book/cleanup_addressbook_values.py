from flask import Flask, render_template, session, request, redirect, flash
from jhmanager.service.contacts_directory.cleanup_contact import cleanup_full_name
from jhmanager.service.contacts_directory.cleanup_contact import cleanup_company_name


def cleanup_contact_fields(contacts_details, contact_id):
    for heading, value in contacts_details["fields"][contact_id].items():
        if value == "N/A":
            contacts_details["fields"][contact_id][heading] = None

    # Need to make sure the user has capitalised the first letter of every name they've provided:
    contacts_details["fields"][contact_id]["full_name"] = cleanup_full_name(contacts_details["fields"][contact_id]["full_name"] )

    # Now to do the same for the company name the user provided:
    contacts_details["fields"][contact_id]["company_name"] = cleanup_company_name(contacts_details["fields"][contact_id]["company_name"])

    job_title = contacts_details["fields"][contact_id]["job_title"]
    if job_title == "N/A":
        contacts_details["fields"][contact_id]["job_title"] = None
    else:
        contacts_details["fields"][contact_id]["job_title"] = job_title.capitalize()

