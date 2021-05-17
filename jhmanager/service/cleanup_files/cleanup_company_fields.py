from flask import Flask, render_template, session, request, redirect
from jhmanager.service.cleanup_files.cleanup_general_fields import cleanup_field_value
from jhmanager.service.cleanup_files.cleanup_general_fields import cleanup_urls


def check_if_all_company_fields_empty(company_details):
    for heading, fields in company_details.items():
        if heading == "company_name":
            continue 

        if fields["data"]:
            return False 

        return True 

# Clean up the values for a specific company's 'company profile':
def cleanup_company_profile(company_details):
    company_details["all_fields_empty"] = check_if_all_company_fields_empty(company_details)

    for heading, fields in company_details.items():
        if heading == "company_name" or heading == "all_fields_empty":
            continue 
        
        for label, value in fields.items():
            if value == "N/A" or value == "Unknown at present" or value == "":
                company_details[heading][label] = None
            else:
                company_details[heading][label] = cleanup_field_value(value)


# Clean up the values for a specific company:
def cleanup_specific_company(company_details):
    for heading, value in company_details["fields"].items():
        if value == "N/A" or value == "Unknown at present" or value == "":
            company_details["fields"][heading] = None
        else:
            company_details["fields"][heading] = cleanup_field_value(value) 


# Clean up fields for a company, when part of a dictionary of companies:
def cleanup_company_fields(company_contacts, company_id):
    if not company_contacts["empty_list"]:
        for heading, value in company_contacts["fields"][company_id].items():
            if value == "N/A":
                # If the value is N/A it means this field was left blank. So lets replace it with 'None'
                company_contacts["fields"][company_id][heading] = None
            elif heading == "view_company":
                # If we come across the URL 'view_company', then we'd want to clean up using 'cleanup_urls'
                company_contacts["fields"][company_id][heading] = cleanup_urls(value)
            else:
                company_contacts["fields"][company_id][heading] = cleanup_field_value(value)




