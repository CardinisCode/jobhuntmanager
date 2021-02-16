from jhmanager.repo.database import SqlDatabase

class CompanyRepository:
    def __init__(self, db):
        self.db = SqlDatabase(db=db)

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

        return self.db.insert('company', data)
