from flask import Flask, render_template, session, request, redirect, flash


def delete_contact_details(contact_id, contactRepo):
    

    flash("Contact has been successfully deleted.")
    return redirect('/address_book')