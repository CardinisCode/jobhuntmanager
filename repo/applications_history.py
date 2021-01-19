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

    def insertApplicationDetailsToApplicationHistory(self, user_id, date, employment_type, location, job_description, notes, role, company_name, platform, perks, company_description, tech_stack, url, stage, contact_received):
        cursor = self.db.cursor()
        result = cursor.execute("INSERT INTO application_history (user_id, date, employment_type, location, job_description, user_notes, job_role, company_name, platform, job_perks, company_description_on_spec, tech_stack, job_url, interview_stage, contact_received) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (user_id, date, employment_type, location, job_description, notes, role, company_name, platform, perks, company_description, tech_stack, url, stage, contact_received))
        self.db.commit()

        return result.lastrowid
