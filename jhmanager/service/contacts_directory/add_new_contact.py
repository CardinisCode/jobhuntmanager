from flask import Flask, render_template, session, request, redirect, flash


def display_add_new_contact_form(new_contact_form):
    details = {
        "action_url": '/address_book/contact_list/add_contact'
    }


    return render_template("add_new_contact.html", new_contact_form=new_contact_form, details=details)