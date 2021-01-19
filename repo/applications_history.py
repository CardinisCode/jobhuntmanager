class ApplicationsHistoryRepository:
    def __init__(self, db):
        self.db = db

    def addApplicationToHistory(self, company_name, date, job_role, platform, interview_stage, contact_received):
        cursor = self.db.cursor()
        result = cursor.execute("INSERT INTO application_history (company_name, date, job_role, platform, interview_stage, contact_received) VALUES (?, ?, ?, ?, ?, ?)", (company_name, date, job_role, platform, interview_stage, contact_received,))
        self.db.commit()

        return result.lastrowid

    
    def grabTodaysApplicationCount(self, todays_date, user_id):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT * FROM application_history WHERE date = ? AND user_id = ?", (todays_date, user_id,))
        self.db.commit()

        return result.lastrowid

    def grabApplicationHistory(self, user_id):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT * FROM application_history WHERE user_id = ?", (user_id,))
        self.db.commit()

        return result.lastrowid

    
