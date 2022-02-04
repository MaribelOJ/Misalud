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
''' 
class medicine(db.Model):
    __tablename__ = 'Medicine'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uniqueCode = db.Column(db.String, unique=True)
    name = db.Column(db.String)
    suplier = db.Column(db.String)
    price = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    availability = db.Column(db.String)

    def __init__(self, uniqueCode, name, suplier, price, quantity, availability):
        self.uniqueCode = uniqueCode
        self.name = name
        self.suplier = suplier
        self.price = price
        self.quantity = quantity
        self.availability = availability

class medicalAppointment(db.Model):
    __tablename__ = 'MedicalAppointment'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_id = db.Column(db.ForeignKey("patient.id"))
    medicine_name = db.Column(db.ForeignKey("medicine.name"))
    medicine_id = db.Column(db.ForeignKey("medicine.id"))
    functionary_id = db.Column(db.ForeignKey("functionary.id"))
    requestDate = db.Column(db.DateTime)
    appointmentDate = db.Column(db.Date)
    appointmentTime = db.Column(db.Time)
    observation = db.Column(db.Text)
    status = db.Column(db.String)

    def __init__(self, patient_id, medicine_name, madicine_id, functionary_id, requestDate, appointmentDate, appointmentTime, observation, status):
        self.patient_id = patient_id
        self.medicine_name = medicine_name
        self.medicine_id = madicine_id
        self.functionary_id = functionary_id
        self.requestDate = requestDate
        self.appointmentDate = appointmentDate
        self.appointmentTime = appointmentTime
        self.observation = observation
        self.status = status

class medicineControl(db.Model):
    __tablename__ = 'MedicineControl'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    medicine_id = db.Column(db.ForeignKey("medicine.id"))
    functionary_id = db.Column(db.ForeignKey("functionary.id"))
    requiredQuantity = db.Column(db.Integer)
    date = db.Column(db.Date)
    hour = db.Column(db.Time)

    def __init__(self, medicine_id, functionary_id, requiredQuantity, date, hour):
        self.medicine_id = medicine_id
        self.functionary_id = functionary_id
        self.requiredQuantity = requiredQuantity
        self.date = date
        self.hour = hour
 '''








    


    





    
