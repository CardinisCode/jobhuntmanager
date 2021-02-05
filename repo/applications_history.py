class ApplicationsHistoryRepository:
    def __init__(self, db):
        self.db = db

    def addApplicationToHistory(self, company_name, job_role, date, employment_type, job_ref, company_descrip, job_description, tech_stack, job_perks, platform, location, salary, user_notes, job_url):
        cursor = self.db.cursor()
        result = cursor.execute("INSERT INTO application_history (company_name, job_role, date, employment_type, job_ref, company_descrip, job_description, tech_stack, job_perks, platform, location, salary, user_notes, job_url) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (company_name, job_role, date, employment_type, job_ref, company_descrip, job_description, tech_stack, job_perks, platform, location, salary, user_notes, job_url))
        self.db.commit()

        return result.lastrowid

    def grabTodaysApplicationCount(self, todays_date, user_id):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT * FROM application_history WHERE date = ? AND user_id = ?", (todays_date, user_id,))
        self.db.commit()

        return result.lastrowid

    def grabApplicationHistory(self, user_id):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT date, job_ref, company_name, job_role, salary, platform, employment_type, interview_stage, contact_received FROM application_history WHERE user_id = ? ORDER BY date DESC", (user_id,))
        self.db.commit()

        return result

    def grabTop5ApplicationsFromHistory(self, user_id):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT date, job_ref, company_name, job_role, platform, employment_type, interview_stage, contact_received, salary FROM application_history WHERE user_id = ? ORDER BY date DESC LIMIT 5", (user_id,))
        self.db.commit()

        return result

    def grabTop10ApplicationsFromHistory(self, user_id):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT id, date, company_name, job_role, employment_type, salary, platform, interview_stage, job_ref, contact_received FROM application_history WHERE user_id = ? ORDER BY date DESC LIMIT 10", (user_id,))
        self.db.commit()

        return result

    def insertApplicationDetailsToApplicationHistory(self, user_id, date, employment_type, location, job_description, notes, role, company_name, platform, perks, company_description, tech_stack, url, stage, contact_received, job_ref, salary):
        cursor = self.db.cursor()
        result = cursor.execute("INSERT INTO application_history (user_id, date, employment_type, location, job_description, user_notes, job_role, company_name, platform, job_perks, company_descrip, tech_stack, job_url, interview_stage, contact_received, job_ref, salary) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (user_id, date, employment_type, location, job_description, notes, role, company_name, platform, perks, company_description, tech_stack, url, stage, contact_received, job_ref, salary))
        self.db.commit()

        return result.lastrowid

    def checkCompanyNameInApplicationHistoryForUser(self, pattern, user_name):
        cursor = self.db.cursor()
        result = cursor.execute(
            "SELECT EXISTS(SELECT company_name FROM application_history WHERE company_name LIKE ? and user_id = ?)", (pattern, user_name,)
        )
        self.db.commit()

        return result
