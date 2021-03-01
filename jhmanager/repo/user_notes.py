from jhmanager.repo.database import SqlDatabase
from datetime import date, time
from flask import flash
import sqlite3


class Notes:
    def __init__(self, db_fields):
        self.description = db_fields[0]
        self.user_notes = db_fields[1]


class UserNotesRepository:
    def __init__(self, db):
        self.db = db
        self.sql = SqlDatabase(db=db)

    def insertNewNotes(self, fields): 
        cursor = self.db.cursor()
        command = """ 
        INSERT INTO user_notes (user_id, application_id, description, notes_text)
        VALUES (?, ?, ?, ?)
        """
        result = cursor.execute(command, tuple(fields.values()))

        self.db.commit()

        return result.lastrowid
