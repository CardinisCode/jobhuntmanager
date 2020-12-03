class ApplicationsHistoryRepository:
    def __init__(self, db):
        self.db = db

    def addApplicationToHistory(self, company_name, date, job_role, platform, interview_stage, contact_received):
        cursor = self.db.cursor()
        result = cursor.execute("INSERT INTO application_history (company_name, date, job_role, platform, interview_stage, contact_received) VALUES (?, ?, ?, ?, ?, ?)", (company_name, date, job_role, platform, interview_stage, contact_received,))
        self.db.commit()

        return result.lastrowid


    # def createUser(self, username, hashed_password, email, date):
    #     cursor = self.db.cursor()
    #     result = cursor.execute("INSERT INTO users (username, hash, email, date) VALUES (?, ?, ?, ?)", (username, hashed_password, email, date,))
    #     # this was needed. It is a modification to the database and the way that sql works it needs to commit those changes (transaction)
    #     # which means it saves it to the database. otherwise it forgets the change. This is done to protect the database from corrupting
    #     # changes
    #     self.db.commit()

    #     return result.lastrowid