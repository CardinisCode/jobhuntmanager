from flask import Flask, render_template, session, request, redirect, flash


def cleanup_full_name(full_name):
    updated_full_name = (" ".join([x.capitalize() for x in full_name.split(' ')]))
    return updated_full_name


def cleanup_company_name(company_name):
    if company_name:
        company_name = (" ".join([x.capitalize() for x in company_name.split(' ')]))
    return company_name


def cleanup_field_value(field_value):
    if field_value:
        field_value = (" ".join([x.capitalize() for x in field_value.split(' ')]))
    return field_value


# This takes a dictionary for a specific contact and cleans up the presentation of each of its fields:
def cleanup_specific_contact_entry(contact_details):
    for heading, value in contact_details["fields"].items():
        if value == "N/A":
            contact_details["fields"][heading] = None

    contact_details["fields"]["company_name"] = cleanup_field_value(contact_details["fields"]["company_name"])
    contact_details["fields"]["full_name"] = cleanup_full_name(contact_details["fields"]["full_name"])
    contact_details["fields"]["job_title"] = cleanup_field_value(contact_details["fields"]["job_title"])

# This takes a dictionary of various contacts, and cleans up the presentation of the data for a specific contact entry:
def cleanup_each_contact_entry(contacts_details, contact_id):
    for heading, value in contacts_details["fields"][contact_id].items():
        if value == "N/A":
            contacts_details["fields"][contact_id][heading] = None

    # Need to make sure the user has capitalised the first letter of every name they've provided:
    contacts_details["fields"][contact_id]["full_name"] = cleanup_full_name(contacts_details["fields"][contact_id]["full_name"] )

    # Now to do the same for the company name the user provided:
    contacts_details["fields"][contact_id]["company_name"] = cleanup_field_value(contacts_details["fields"][contact_id]["company_name"])
    contacts_details["fields"][contact_id]["job_title"] = cleanup_field_value(contacts_details["fields"][contact_id]["job_title"])

