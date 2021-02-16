class InterviewsHistoryRepository:
    def __init__(self, db):
        self.db = db

    def grabTodaysInterviewCount(self, todays_date, user_id):
        cursor = self.db.cursor()

        command = "SELECT * FROM applications as A INNER JOIN interviews as I on A.application_id = I.application_id WHERE A.user_id = ? and I.date = ?"

        result = cursor.execute(command, (user_id,todays_date,))
        self.db.commit()

        return result


    def InsertNewInterviewDetails(self, arguments):
        cursor = self.db.cursor()
        result = cursor.execute("INSERT INTO interviews (user_id, company_name, date, time, job_role, interviewer_names, interview_type, location, interview_medium, other_medium, contact_number, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (arguments))
        self.db.commit()

        return result.lastrowid

    def grabTop5InterviewsForUser(self, user_id):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT * FROM interviews WHERE user_id = ? ORDER BY date DESC, time DESC LIMIT 5;", (user_id,))
        self.db.commit()

        return result


    # def grabTopTenInterviewsForUser(self, application_id):
    #     cursor = self.db.cursor()
    #     result = cursor.execute("SELECT * FROM interviews WHERE application_id = ? ORDER BY date DESC, time DESC LIMIT 10;", (application_id,))
    #     self.db.commit()

    #     return result
