from jhmanager.repo.database import SqlDatabase
from datetime import date, time
from flask import flash
import sqlite3


class Interview:
    def __init__(self, db_fields):
        self.interview_id = db_fields[0]
        self.application_id = db_fields[1]
        self.interview_date = date.fromisoformat(db_fields[2])
        self.interview_time = time.fromisoformat(db_fields[3])
        self.interview_type = db_fields[4]
        self.location = db_fields[5]
        self.medium = db_fields[6]
        self.other_medium = db_fields[7]
        self.contact_number = db_fields[8]
        self.status = db_fields[9]
        self.interviewer_names = db_fields[10]


class InterviewsHistoryRepository:
    def __init__(self, db):
        self.db = db
        self.sql = SqlDatabase(db=db)

    def grabTodaysInterviewCount(self, todays_date, user_id):
        cursor = self.db.cursor()

        command = "SELECT * FROM applications as A INNER JOIN interviews as I on A.application_id = I.application_id WHERE A.user_id = ? and I.date = ?"

        result = cursor.execute(command, (user_id,todays_date,))
        self.db.commit()

        return result


    def InsertNewInterviewDetails(self, arguments):
        cursor = self.db.cursor()
        # application_id, app_date_str, app_time_str, interview_type, location, medium, other_medium, contact_number, status, interviewers
        command = "INSERT INTO interviews (user_id, application_id, date, time, interview_type, interview_location, interview_medium, other_medium, contact_number, status, interviewer_names) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        result = cursor.execute(command, (arguments))
        self.db.commit()

        return result.lastrowid

    def grabTop5InterviewsForUser(self, user_id):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT * FROM interviews WHERE user_id = ? ORDER BY date DESC, time DESC LIMIT 5;", (user_id,))
        self.db.commit()

        return result

    
    def grabAllInterviewsForApplicationID(self, application_id):
        cursor = self.db.cursor()
        command = "SELECT * FROM interviews WHERE application_id={}".format(application_id)
        result = cursor.execute(command)
        self.db.commit()

        data = [x for x in result]
        if len(data) < 1:
            return None

        return data


    def grabInterviewByID(self, interview_ID):
        result = self.sql.getByField('interviews', 'interview_id', interview_ID)

        interview_result = Interview(result)

        return interview_result


    def updateInterview(self, fields):
        cursor = self.db.cursor()

        command = """
        UPDATE interviews 
        SET date = ?,
            time = ?,
            interviewer_names = ?,
            interview_type = ?,
            interview_location = ?,
            interview_medium = ?,
            other_medium = ?,
            contact_number = ?,
            status = ?
        WHERE interview_id = ? AND application_id = ?"""

        cursor.execute(command, tuple(fields.values()))

        self.db.commit()

    def deleteInterviewByID(self, interview_id):
        try: 
            cursor = self.db.cursor()
            command = "DELETE FROM interviews WHERE interview_id = {}".format(interview_id)
            cursor.execute(command)
            self.db.commit()

        except sqlite3.Error as error:
            flash("Interview failed to delete.", error)
