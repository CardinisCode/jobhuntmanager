from flask import Flask, render_template, session, request, redirect, flash


def cleanup_contact_details(contact_details, contact_id):
    update_contact = None
    contact_details["fields"][contact_id]

    for contact_id, field in contact_details.fields.items():
        raise ValueError(contact_id, field)



    return update_contact


def cleanup_full_name(full_name):
    updated_full_name = (" ".join([x.capitalize() for x in full_name.split(' ')]))
    return updated_full_name


def cleanup_company_name(company_name):
    updated_company_name = (" ".join([x.capitalize() for x in company_name.split(' ')]))
    return updated_company_name
