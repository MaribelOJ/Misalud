from this import s
from routes import db

class patient(db.Model):
    __tablename__ = 'Patient'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    identification = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    full_name = db.Column(db.String)
    phone = db.Column(db.String(10))
    department = db.Column(db.String)
    district = db.Column(db.String)
    birthdate = db.Column(db.String)
    age = db.Column(db.Integer)
    blood_type = db.Column(db.String)
    status = db.Column(db.String, nullable=True)

    def __init__(self, identification, email, password, full_name, phone, department, district, birthdate, age, blood_type, status):
        self.identification = identification
        self.email = email
        self.password = password
        self.full_name = full_name
        self.phone = phone
        self.department = department
        self.district = district
        self.birthdate = birthdate
        self.age = age
        self.blood_type = blood_type
        self.status = status
    
class functionary(db.Model):
    __tablename__ = 'Functionary'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    identification = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    full_name = db.Column(db.String)
    position = db.Column(db.String)
    phone = db.Column(db.String(10), unique=True)

    def __init__(self, identification, email, password, full_name, position, phone):
        self.identification = identification
        self.email = email
        self.password = password
        self.full_name = full_name
        self.position = position
        self.phone = phone








    


    





    
