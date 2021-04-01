from jhmanager.repo.database import SqlDatabase
import sqlite3


class Contact:
    def __init__(self, db_fields):
        self.contact_id = db_fields[0]
        self.user_id = db_fields[1]
        self.full_name = db_fields[2]
        self.job_title = db_fields[3]
        self.contact_number = db_fields[4]
        self.company_name = db_fields[5]
        self.email_address = db_fields[6]
        self.linkedin_profile = db_fields[7]


class ContactRepository:
    def __init__(self, db):
        self.sql = SqlDatabase(db=db)
        self.db = db

    def create_contact(self, fields):
        cursor = self.db.cursor()
        command = """
        INSERT INTO indiv_contacts 
        (user_id, full_name, job_title, contact_number, company_name, email_address, linkedin_profile)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        result = cursor.execute(command, tuple(fields.values()))
        self.db.commit()

        return result.lastrowid

    def getContactsByUserID(self, user_id):
        cursor = self.db.cursor()
        command = """  
        SELECT * FROM indiv_contacts
        WHERE user_id = {}
        ORDER BY full_name
        """.format(user_id)

        result = cursor.execute(command)
        self.db.commit()

        contact_list = []

        if not result: 
            return None

        for contact in result:
            contact_result = Contact(contact)
            contact_list.append(contact_result)

        return contact_list