from jhmanager.repo.database import SqlDatabase
from datetime import datetime, date, time
from flask import flash
import sqlite3


class Interview:
    def __init__(self, db_fields):
        self.interview_id = db_fields[0]
        self.application_id = db_fields[1]
        self.user_id = db_fields[2]
        self.entry_date = date.fromisoformat(db_fields[3])
        self.interview_date = date.fromisoformat(db_fields[4])
        self.interview_time = time.fromisoformat(db_fields[5])
        self.interview_type = db_fields[6]
        self.location = db_fields[7]
        self.medium = db_fields[8]
        self.other_medium = db_fields[9]
        self.contact_number = db_fields[10]
        self.status = db_fields[11]
        self.interviewer_names = db_fields[12]
        self.video_link = db_fields[13]
        self.extra_notes = db_fields[14]


class InterviewsHistoryRepository:
    
    def __init__(self, db):
        self.db = db
        self.sql = SqlDatabase(db=db)

    def CreateInterview(self, fields):
        cursor = self.db.cursor()
        command = """
        INSERT INTO interviews 
            (application_id, user_id, entry_date, interview_date, interview_time, interview_type, interview_location, interview_medium, other_medium, contact_number, status, interviewer_names, video_link, extra_notes)
        VALUES 
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """ 
        result = cursor.execute(command, tuple(fields.values()))
        self.db.commit()

        return result.lastrowid

    def getInterviewByID(self, interview_ID):
        result = self.sql.getByField('interviews', 'interview_id', interview_ID)

        interview_result = Interview(result)

        return interview_result

    def getInterviewsByUserID(self, user_id):
        cursor = self.db.cursor()
        command = "SELECT * FROM interviews WHERE user_id={} ORDER BY interview_date DESC, interview_time DESC".format(user_id)
        result = cursor.execute(command)
        self.db.commit()

        interviews_list = [] 

        for interview in result:
            interview_result = Interview(interview)
            interviews_list.append(interview_result)

        if interviews_list == []:
            return None

        return interviews_list

    def getInterviewsByApplicationID(self, application_id):
        cursor = self.db.cursor()
        command = "SELECT * FROM interviews where application_id = {} ORDER BY interview_date DESC, interview_time DESC".format(application_id)
        result = cursor.execute(command)
        self.db.commit()

        interviews_list = [] 

        for interview in result:
            interview_result = Interview(interview)
            interviews_list.append(interview_result)

        if interviews_list == []:
            return None

        return interviews_list

    def getTop6InterviewsByApplicationID(self, application_id):
        cursor = self.db.cursor()
        command = "SELECT * FROM interviews where application_id = {} ORDER BY interview_date, interview_time LIMIT 6".format(application_id)
        result = cursor.execute(command)
        self.db.commit()

        interviews_list = [] 

        for interview in result:
            interview_result = Interview(interview)
            interviews_list.append(interview_result)

        if interviews_list == []:
            return None

        return interviews_list

    def updateInterviewByID(self, fields):
        cursor = self.db.cursor()

        command = """
        UPDATE interviews 
        SET interview_date = ?,
            interview_time = ?,
            interviewer_names = ?,
            interview_type = ?,
            interview_location = ?,
            interview_medium = ?,
            other_medium = ?,
            contact_number = ?,
            status = ?, 
            video_link = ?, 
            extra_notes = ?
        WHERE interview_id = ? AND application_id = ?"""

        cursor.execute(command, tuple(fields.values()))

        self.db.commit()


    def updateInterviewStatusByID(self, fields):
        cursor = self.db.cursor()

        command = """
        UPDATE interviews 
        SET status = ?
        WHERE interview_id = ?"""

        cursor.execute(command, tuple(fields.values()))

        self.db.commit()

    def deleteInterviewByID(self, interview_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM interviews WHERE interview_id = {}".format(interview_id)
            cursor.execute(command)
            self.db.commit()
            message = "Interview deleted successfully."

        except sqlite3.Error as error:
            message = "Interview failed to delete. " + error
        finally: 
            return message

    def deleteInterviewsByApplicationID(self, application_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM interviews WHERE application_id = {}".format(application_id)
            cursor.execute(command)
            self.db.commit()
            message = "Interviews deleted successfully."

        except sqlite3.Error as error:
            message = "Interviews failed to delete. " + error
        finally: 
            return message

    def deleteInterviewsByUserID(self, user_id):
        message = ""
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM interviews WHERE user_id = {}".format(user_id)
            cursor.execute(command)
            self.db.commit()
            message = "Interviews deleted successfully."

        except sqlite3.Error as error:
            message = "Interviews failed to delete. " + error
        finally: 
            return message

