class ApplicationsHistoryRepository:
    def __init__(self, db):
        self.db = db

    def addApplicationToHistory(self, arguments):
        cursor = self.db.cursor()
        result = cursor.execute("INSERT INTO applications (company_name, job_role, date, time, employment_type, job_ref, company_descrip, job_description, tech_stack, job_perks, platform, location, salary, user_notes, job_url, user_id, company_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (arguments))
        self.db.commit()

        return result

    def grabTodaysApplicationCount(self, todays_date, user_id):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT * FROM applications WHERE date = ? AND user_id = ?", (todays_date, user_id,))
        self.db.commit()

        return result

    def grabApplicationHistory(self, user_id):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT date, job_ref, company_name, job_role, salary, platform, employment_type, interview_stage, contact_received FROM applications WHERE user_id = ? ORDER BY date DESC", (user_id,))
        self.db.commit()

        return result

    def grabTop5ApplicationsFromHistory(self, user_id):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT date, job_ref, company_name, job_role, platform, employment_type, interview_stage, contact_received, salary FROM applications WHERE user_id = ? ORDER BY date DESC LIMIT 5", (user_id,))
        self.db.commit()

        return result

    def grabTop10ApplicationsFromHistory(self, user_id):
        cursor = self.db.cursor()
        result = cursor.execute("SELECT application_id, date, company_name, job_role, employment_type, salary, platform, interview_stage, job_ref, contact_received FROM applications WHERE user_id = ? ORDER BY date DESC LIMIT 10", (user_id,))
        self.db.commit()

        return result

    def insertInterviewDetailsToApplicationHistory(self, arguments):
        cursor = self.db.cursor()
        result = cursor.execute("INSERT INTO applications (user_id, date, time, employment_type, location, job_description, user_notes, job_role, company_name, platform, job_perks, company_descrip, tech_stack, job_url, interview_stage, contact_received, job_ref, salary) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (arguments))
        self.db.commit()

        return result

    def insertApplicationDetailsFromNewInterviewForNewCompany(self, user_id, current_date, company_name, job_role, interview_stage):
        cursor = self.db.cursor()
        result = cursor.execute("INSERT INTO applications (user_id, date, company_name, job_role, interview_stage) VALUES (?, ?, ?, ?, ?)", (user_id, current_date, company_name, job_role, interview_stage))
        self.db.commit()

        return result.lastrowid        

    def checkCompanyNameInApplicationHistoryForUser(self, arguments, user_name):
        cursor = self.db.cursor()
        result = cursor.execute(
            "SELECT EXISTS(SELECT company_name FROM applications WHERE company_name LIKE ? and user_id = ?)", (arguments, user_name,)
        )
        self.db.commit()

        return result

    def checkCompanyNameInApplicationHistoryByUserID(self, company_name, user_id,):
        cursor = self.db.cursor()
        result = cursor.execute(
            "SELECT EXISTS(SELECT company_name FROM applications WHERE company_name LIKE ? and user_id = ?)", (company_name, user_id,)
        )
        self.db.commit()

        return result


    def updateApplicationEntryByCompanyName(self, fields, user_id):
        cursor = self.db.cursor()
        result = cursor.execute()
        self.db.commit()

        return result

    def grabApplicationStageForCompanyNameForActiveUser(self, arguments):
        cursor = self.db.cursor()
        result = cursor.execute(
            "SELECT interview_stage FROM applications WHERE user_id = ? AND company_name LIKE ?", (arguments)
            )
        self.db.commit()

        return result


    def updateInterviewStageAfterAddingNewInterview(self, details):
        cursor = self.db.cursor()
        cursor.execute("UPDATE applications SET interview_stage = ? WHERE user_id = ? AND company_name LIKE ?", (details))
        self.db.commit()

        return 0        
