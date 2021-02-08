class CompanyRepository:
    def __init__(self, db):
        self.db = db

    # def addColumnToTable(self, name, datatype):
    #     ALTER TABLE users ADD date datetime;

    def createCompany(self, name):
        cursor = self.db.cursor()
        result = cursor.execute("INSERT INTO company_directory (company_name) VALUES (?)", (name,))
        self.db.commit()
        return result.lastrowid
