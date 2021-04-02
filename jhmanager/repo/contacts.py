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

    def getContactByContactID(self, contact_id):
        cursor = self.db.cursor()
        command = "SELECT * FROM indiv_contacts WHERE contact_id = {}".format(contact_id)
        result = cursor.execute(command)
        self.db.commit()

        if not result:
            return None

        data = [x for x in result][0]
        contact_details = Contact(data)

        return contact_details

    def updateByContactID(self, fields):
        cursor = self.db.cursor()

        command = """
        UPDATE indiv_contacts 
        SET full_name = ?,
            job_title = ?,
            contact_number = ?,
            company_name = ?, 
            email_address = ?, 
            linkedin_profile = ?
        WHERE contact_id = ?"""

        cursor.execute(command, tuple(fields.values()))

        self.db.commit()

    def deleteByContactID(self, contact_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM indiv_contacts WHERE contact_id = {}".format(contact_id)
            cursor.execute(command)
            self.db.commit()
            message = "Contact has been deleted successfully."

        except sqlite3.Error as error:
            message = "Contact has failed to delete. " + error
        finally:
            return message

    def deleteByUserID(self, user_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM indiv_contacts WHERE user_id = {}".format(user_id)
            cursor.execute(command)
            self.db.commit()
            message = "Contact has been deleted successfully."

        except sqlite3.Error as error:
            message = "Contact has failed to delete. " + error
        finally:
            return message