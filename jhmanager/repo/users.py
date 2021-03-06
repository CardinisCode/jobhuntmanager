from jhmanager.repo.database import SqlDatabase
from datetime import date, time
from flask import flash
import sqlite3


class User:
    def __init__(self, db_fields):
        self.user_id = db_fields[0]
        self.username = db_fields[1]
        self.hash = db_fields[2]
        self.email = db_fields[3]
        self.date = db_fields[4]


class UserRepository:
    def __init__(self, db):
        self.db = db

    def createUser(self, fields):
        cursor = self.db.cursor()
        command = """ 
            INSERT INTO users 
                (username, hash, email, date) 
            VALUES (?, ?, ?, ?)
        """
        result = cursor.execute(command, tuple(fields.values()))
        self.db.commit()

        return result.lastrowid
    
    def getUserByID(self, user_id): 
        cursor = self.db.cursor()
        result = cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
        self.db.commit()

        user_result = User(result.fetchone()) 

        return user_result
    
    def getUserByUsername(self, username):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        self.db.commit()        

        return result.fetchone()

    def getUserByEmail(self, email):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        self.db.commit()

        return result.fetchone()

    def updateUserEmailByID(self, fields): 
        cursor = self.db.cursor()
        command = """ 
        UPDATE users 
        SET email = ?
        WHERE user_id = ?
        """
        cursor.execute(command, tuple(fields.values()))
        self.db.commit()


    def updateUserHashByID(self, fields):
        cursor = self.db.cursor()
        command = """ 
        UPDATE users 
        SET hash = ?
        WHERE user_id = ?
        """
        cursor.execute(command, tuple(fields.values()))
        self.db.commit()        

    def deleteUserByID(self, user_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM users WHERE user_id = {}".format(user_id)
            cursor.execute(command)
            self.db.commit()
            message = "User details deleted successfully."

        except sqlite3.Error as error:
            message = "User details failed to delete. " + error
        finally: 
            return message