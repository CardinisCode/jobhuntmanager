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

    def createUser(self, username, hashed_password, email, date):
        cursor = self.db.cursor()
        result = cursor.execute("INSERT INTO users (username, hash, email, date) VALUES (?, ?, ?, ?)", (username, hashed_password, email, date,))
        # this was needed. It is a modification to the database and the way that sql works it needs to commit those changes (transaction)
        # which means it saves it to the database. otherwise it forgets the change. This is done to protect the database from corrupting
        # changes
        self.db.commit()

        return result.lastrowid

    # def getById(self, user_id):
    #     return self.db.execute("SELECT * FROM users WHERE id = :user_id", user_id=user_id)

    
    def getByUserID(self, user_id): 
        cursor = self.db.cursor()
        result = cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
        self.db.commit()

        user_result = User(result.fetchone()) 

        return user_result

    
    def getByUserName(self, username):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        self.db.commit()        

        return result.fetchone()

    def getByUserEmail(self, email):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT * FROM users WHERE email=?", (email,))

        return result.fetchone()

    def getUsernameByUserID(self, user_id):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT username FROM users WHERE user_id=?", (user_id,))

        return result.fetchone()[0]

    def getEmailAddressByUserID(self, user_id):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT email FROM users WHERE user_id=?", (user_id,))

        return result.fetchone()[0]

    def deleteByUserID(self, user_id):
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

    