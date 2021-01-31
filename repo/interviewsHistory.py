class InterviewsHistoryRepository:
    def __init__(self, db):
        self.db = db

    def grabTodaysInterviewCount(self, todays_date, user_id):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT * FROM interview_history WHERE date = ? AND user_id = ?", (todays_date, user_id,))
        self.db.commit()

        return result.lastrowid


    def InsertNewInterviewDetails(self, user_id, company_name, date, time, job_role, interviewers, interview_type, location, medium, other_medium, contact_number, status):
        cursor = self.db.cursor()
        result = cursor.execute("INSERT INTO interview_history (user_id, company_name, date, time, job_role, interviewer_names, interview_type, interview_location, interview_medium, other_medium, contact_number, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (user_id, company_name, date, time, job_role, interviewers, interview_type, location, medium, other_medium, contact_number, status,))
        self.db.commit()

        return result.lastrowid
