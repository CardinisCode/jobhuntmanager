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



def cleanup_contact_details(contact_details, contact_id):
    for heading, value in contact_details["fields"].items():
        if value == "N/A":
            contact_details["fields"][heading] = None

    contact_details["fields"]["company_name"] = cleanup_field_value(contact_details["fields"]["company_name"])
    contact_details["fields"]["full_name"] = cleanup_full_name(contact_details["fields"]["full_name"])
    contact_details["fields"]["job_title"] = cleanup_field_value(contact_details["fields"]["job_title"])



