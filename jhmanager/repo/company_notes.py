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