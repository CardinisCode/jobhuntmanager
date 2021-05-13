from jhmanager.repo.database import SqlDatabase
from datetime import date, time
from flask import flash
import sqlite3


class ApplicationNotes:
    def __init__(self, db_fields):
        self.app_notes_id = db_fields[0]
        self.user_id = db_fields[1]
        self.application_id = db_fields[2]
        self.company_id = db_fields[3]
        self.entry_date = db_fields[4]
        self.description = db_fields[5]
        self.notes_text = db_fields[6]


class ApplicationNotesRepository:
    def __init__(self, db):
        self.db = db
        self.sql = SqlDatabase(db=db)

    def insertNewNote(self, fields): 
        cursor = self.db.cursor()
        command = """ 
        INSERT INTO application_notes (user_id, application_id, company_id, entry_date, description, notes_text)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        result = cursor.execute(command, tuple(fields.values()))

        self.db.commit()

        return result.lastrowid

    def getNoteByAppNoteID(self, app_notes_id):
        cursor = self.db.cursor()
        command = "SELECT * FROM application_notes WHERE app_notes_id = {}".format(app_notes_id)
        result = cursor.execute(command)
        self.db.commit()

        if not result:
            return None

        data = [x for x in result][0]
        note_details = ApplicationNotes(data)

        return note_details

    def getAppNotesByApplicationID(self, application_id, user_id):
        cursor = self.db.cursor()
        command = "SELECT * FROM application_notes WHERE user_id = {} and application_id = {} ORDER BY entry_date DESC".format(user_id, application_id)
        result = cursor.execute(command)
        self.db.commit()

        if not result:
            return None
        
        notes_list = []
        for note in result:
            app_notes_entry = ApplicationNotes(note)
            notes_list.append(app_notes_entry)

        if notes_list == []:
            return None

        return notes_list


    def getAppNotesByUserId(self, user_id):
        cursor = self.db.cursor()
        command = "SELECT * FROM application_notes WHERE user_id = {}".format(user_id)
        result = cursor.execute(command)
        self.db.commit()

        if not result:
            return None

        notes_list = []
        for note in result:
            note_result = ApplicationNotes(note)
            notes_list.append(note_result)

        if notes_list == []:
            return None

        return notes_list    
        

    def deleteNoteByAppNoteID(self, app_notes_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM application_notes WHERE app_notes_id = {}".format(app_notes_id)
            cursor.execute(command)
            self.db.commit()
            message = "Note successfully deleted."

        except sqlite3.Error as error:
            message = "Note failed to delete. " + error
        finally:
            return message 

    def deleteNoteByApplicationID(self, application_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM application_notes WHERE application_id = {}".format(application_id)
            cursor.execute(command)
            self.db.commit()
            message = "Note successfully deleted."

        except sqlite3.Error as error:
            message = "Note failed to delete. " + error
        finally:
            return message  


    def deleteNoteByUserID(self, user_id): 
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM application_notes WHERE user_id = {}".format(user_id)
            cursor.execute(command)
            self.db.commit()
            message = "Note successfully deleted."

        except sqlite3.Error as error:
            message = "Note failed to delete. " + error
        finally:
            return message                          

    def updateNoteByID(self, fields):
        message = ""

        try: 
            cursor = self.db.cursor()
            command = """
            UPDATE application_notes
            SET description = ?, 
            notes_text = ?
            WHERE app_notes_id = ?
            """
            cursor.execute(command, tuple(fields.values()))
            self.db.commit()
            message = "Note successfully updated"

        except sqlite3.Error as error:
            message = "Note failed to update. " + error
        finally:
            return message