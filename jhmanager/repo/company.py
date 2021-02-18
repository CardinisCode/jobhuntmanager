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

    def create(self, name, description, location, industry, user_id):
        data = {
            'name': name,
            'description': description,
            'location': location,
            'industry': industry,
            'user_id': user_id
        }

        return self.sql.insert('company', data)

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