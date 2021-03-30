from jhmanager.repo.database import SqlDatabase
from datetime import date, time
from flask import flash
import sqlite3


class CompanyNotes:
    def __init__(self, db_fields):
        self.company_note_id = db_fields[0]
        self.user_id = db_fields[1]
        self.company_id = db_fields[2]
        self.entry_date = db_fields[3]
        self.subject = db_fields[4]
        self.note_text = db_fields[5]


class CompanyNotesRepository:
    def __init__(self, db):
        self.db = db
        self.sql = SqlDatabase(db=db)

    def insertNewNotes(self, fields): 
        cursor = self.db.cursor()
        command = """ 
        INSERT INTO company_notes (user_id, company_id, date, subject, note_text)
        VALUES (?, ?, ?, ?, ?)
        """
        result = cursor.execute(command, tuple(fields.values()))

        self.db.commit()

        return result.lastrowid

    # Takes a tuple containing the company_id and user_id:
    def getAllNotesByCompanyID(self, fields):
        cursor = self.db.cursor()
        command = "SELECT * FROM company_notes WHERE company_id = ? and user_id = ? ORDER BY company_note_id DESC"
        result = cursor.execute(command, (fields))
        self.db.commit()

        data = [x for x in result]
        if len(data) < 1:
            return None

        notes_list = []
        
        for note in data:
            note_result = CompanyNotes(note)
            notes_list.append(note_result)

        return notes_list

    def getCompanyNoteByID(self, note_id):
        cursor = self.db.cursor()
        command = """
        SELECT * FROM company_notes
        WHERE company_note_id = {}
        """.format(note_id)
        result = cursor.execute(command)
        self.db.commit()

        data = [x for x in result]
        if len(data) < 1:
            return None

        company_note = CompanyNotes(data[0])

        return company_note

    def getCompanyNotesByUserID(self, user_id): 
        cursor = self.db.cursor()
        command = "SELECT * FROM company_notes WHERE user_id = {} ORDER BY company_note_id DESC".format(user_id)
        result = cursor.execute(command)
        self.db.commit()

        data = [x for x in result]
        if len(data) < 1:
            return None

        notes_list = []
        
        for note in data:
            note_result = CompanyNotes(note)
            notes_list.append(note_result)

        return notes_list


    def UpdateByCompanyNoteID(self, fields):
        cursor = self.db.cursor()

        command = """
        UPDATE company_notes 
        SET date = ?,
            subject = ?,
            note_text = ?
        WHERE company_note_id = ?"""
        cursor.execute(command, tuple(fields.values()))

        self.db.commit()

    def deleteByCompanyNotesID(self, company_note_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM company_notes WHERE company_note_id = {}".format(company_note_id)
            cursor.execute(command)
            self.db.commit()
            message = "Note successfully deleted!"

        except sqlite3.Error as error:
            message = "Note failed to delete. " + error
        finally:
            return message 


    def deleteByUserID(self, user_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM company_notes WHERE user_id = {}".format(user_id)
            cursor.execute(command)
            self.db.commit()

        except sqlite3.Error as error:
            message = "Failed to delete all notes for this user. " + error
        
        finally:
            return message 

    def deleteByCompanyID(self, company_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM company_notes WHERE company_id = {}".format(company_id)
            cursor.execute(command)
            self.db.commit()

        except sqlite3.Error as error:
            message = "Failed to delete all notes for this company. " + error
        
        finally:
            return message 
