from jhmanager.repo.database import SqlDatabase
from datetime import date, time
from flask import flash
import sqlite3


class Notes:
    def __init__(self, db_fields):
        self.notes_id = db_fields[0]
        self.user_id = db_fields[1]
        self.application_id = db_fields[2]
        self.company_id = db_fields[3]
        self.entry_date = db_fields[4]
        self.description = db_fields[5]
        self.user_notes = db_fields[6]


class UserNotesRepository:
    def __init__(self, db):
        self.db = db
        self.sql = SqlDatabase(db=db)

    def insertNewNotes(self, fields): 
        cursor = self.db.cursor()
        command = """ 
        INSERT INTO user_notes (user_id, application_id, company_id, date, description, notes_text)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        result = cursor.execute(command, tuple(fields.values()))

        self.db.commit()

        return result.lastrowid

    def getNoteByID(self, notes_id):
        cursor = self.db.cursor()
        command = "SELECT * FROM user_notes WHERE notes_id = {}".format(notes_id)
        result = cursor.execute(command)
        self.db.commit()

        if not result:
            return None

        data = [x for x in result][0]
        note_details = Notes(data)

        return note_details

    def getUserNotesForCompany(self, company_id, user_id):
        cursor = self.db.cursor()
        command = "SELECT * FROM user_notes WHERE user_id = {} and company_id = {} ORDER BY date DESC".format(user_id, company_id)
        result = cursor.execute(command)
        self.db.commit()

        if not result:
            return None
        
        notes_list = []
        for note in result:
            user_notes_entry = Notes(note)
            notes_list.append(user_notes_entry)

        if notes_list == []:
            return None

        return notes_list


    def getUserNotesForApplication(self, application_id, user_id):
        cursor = self.db.cursor()
        command = "SELECT * FROM user_notes WHERE user_id = {} and application_id = {} ORDER BY date DESC".format(user_id, application_id)
        result = cursor.execute(command)
        self.db.commit()

        if not result:
            return None
        
        notes_list = []
        for note in result:
            user_notes_entry = Notes(note)
            notes_list.append(user_notes_entry)

        if notes_list == []:
            return None

        return notes_list


    def getUserNotesByUserId(self, user_id):
        cursor = self.db.cursor()
        command = "SELECT * FROM user_notes WHERE user_id = {}".format(user_id)
        result = cursor.execute(command)
        self.db.commit()

        if not result:
            return None

        notes_list = []
        for note in result:
            note_result = Notes(note)
            notes_list.append(note_result)

        if notes_list == []:
            return None

        return notes_list    


    def getUserNotesByID(self, application_id, notes_id):
        cursor = self.db.cursor()
        command = "SELECT * FROM user_notes WHERE application_id = {} and notes_id = {}".format(application_id, notes_id)
        result = cursor.execute(command)
        self.db.commit()

        if not result:
            return None

        data = [x for x in result][0]
        note_details = Notes(data)

        return note_details  

    def deleteByNoteID(self, notes_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM user_notes WHERE notes_id = {}".format(notes_id)
            cursor.execute(command)
            self.db.commit()
            message = "Note successfully deleted."

        except sqlite3.Error as error:
            message = "Note failed to delete. " + error
        finally:
            return message 

    def deleteByApplicationID(self, application_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM user_notes WHERE application_id = {}".format(application_id)
            cursor.execute(command)
            self.db.commit()
            message = "Note successfully deleted."

        except sqlite3.Error as error:
            message = "Note failed to delete. " + error
        finally:
            return message  


    def deleteByUserID(self, user_id): 
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM user_notes WHERE user_id = {}".format(user_id)
            cursor.execute(command)
            self.db.commit()
            message = "Note successfully deleted."

        except sqlite3.Error as error:
            message = "Note failed to delete. " + error
        finally:
            return message                          

    def updateByID(self, fields):
        message = ""

        try: 
            cursor = self.db.cursor()
            command = """
            UPDATE user_notes
            SET description = ?, 
            notes_text = ?
            WHERE notes_id = ?
            """
            cursor.execute(command, tuple(fields.values()))
            self.db.commit()
            message = "Note successfully updated"

        except sqlite3.Error as error:
            message = "Note failed to update. " + error
        finally:
            return message