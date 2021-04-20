from flask import Flask, render_template, session, request, redirect


def prepare_company_website_url(company_url): 
    if company_url == "N/A" or company_url == "n/a":
        return None

    elif company_url == "http://" or company_url == "https://":
        return None

    return company_url


def check_if_all_company_fields_empty(company_details):
    for heading, fields in company_details.items():
        if heading == "company_name":
            continue 

        if fields["data"] != None:
            return False 

        return True 


def cleanup_company_profile(company_details):
    for heading, fields in company_details.items():
        if heading == "company_name" or heading == "all_fields_empty":
            continue 
        
        for label, value in fields.items():
            if value == "N/A" or value == "Unknown at present" or value == "":
                company_details[heading][label] = None

    company_details["all_fields_empty"] = check_if_all_company_fields_empty(company_details)


def cleanup_company_website(website_url):
    if website_url == "N/A" or website_url == "http://" or website_url == "https://":
        website_url = None

    return website_url