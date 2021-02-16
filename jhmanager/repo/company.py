from jhmanager.repo.database import SqlDatabase

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

    def grab_company_name(self, user_id, company_id):
        cursor = self.db.cursor()
        command = "SELECT name FROM company WHERE company_id = {} AND user_id = {}".format(company_id, user_id)
        result = cursor.execute(command)
        self.db.commit()

        return [x for x in result][0][0]
