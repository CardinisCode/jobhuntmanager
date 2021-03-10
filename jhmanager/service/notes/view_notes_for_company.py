from flask import Flask, render_template, session, request, redirect


# def display_all_user_notes_for_company(user_id, application_id, userNotesRepo, companyRepo):
    
#     general_details = {
#         "company_name": companyRepo.getCompanyById(company_id).name, 
#         "company_id": company_id, 
#         "message": ""
#     }

#     user_notes_details = None
#     company_notes = userNotesRepo.getUserNotesForCompany(company_id, user_id)
#     if not company_notes:
#         general_details["empty_table"] = True
#         general_details["message"] = "Start Adding notes now..."

#     else:
#         note_count = 0
#         user_notes_details = {}
#         for note in company_notes:
#             note_count += 1
#             user_notes_details[note_count] = {
#                 "entry_date": note.entry_date,
#                 "subject": note.description,
#                 "note_text": note.user_notes, 
#             }

#     return render_template("view_user_notes_for_company.html", general_details=general_details, user_notes_details=user_notes_details)