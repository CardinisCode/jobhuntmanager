from jhmanager.repo.database import SqlDatabase


class Company:
    def __init__(self, db_fields):
        self.company_id = db_fields[0]
        self.user_id = db_fields[1]
        self.name = db_fields[2]
        self.description = db_fields[3]
        self.location = db_fields[4]
        self.industry = db_fields[5]
        self.url = db_fields[6]
        self.interviewers = db_fields[7]
        self.contact_number = db_fields[8]

    
class CompanyRepository:
    def __init__(self, db):
        self.sql = SqlDatabase(db=db)
        self.db = db

    # def addColumnToTable(self, name, datatype):
    #     ALTER TABLE users ADD date datetime;

    def create(self, fields):
        return self.sql.insert('company', fields)

    
    def updateUsingApplicationDetails(self, fields):
        cursor = self.db.cursor()

        command = """
        UPDATE company 
        SET name = ?,
            description = ?,
            industry = ?,
            location = ?
        WHERE user_id = ? and company_id = ?"""

        cursor.execute(command, tuple(fields.values()))

        self.db.commit()

    # def update(self, description, location, industry, url, interviewers, contact_number, company_id, user_id):
    #     data = {
    #         "description": description,
    #         "location": location,
    #         "industry": industry,
    #         "url": url, 
    #         "interviewers": interviewers, 
    #         "contact_number": contact_number,
    #     }



    def getCompanyById(self, company_id):
        result = self.sql.getByField('company', 'company_id', company_id)

        company = Company(result)

        return company

    def grab_company_name(self, user_id, company_id):
        cursor = self.db.cursor()
        command = "SELECT name FROM company WHERE company_id = {} AND user_id = {}".format(company_id, user_id)
        result = cursor.execute(command)
        self.db.commit()

        return [x for x in result][0][0]

    def grabCompanyByNameAndUserID(self, company_name, user_id) -> Company:
        result = self.sql.getByName('company', 'name', company_name, 'user_id', user_id)

        if not result:
            return None

        company = Company(result)

        return company

