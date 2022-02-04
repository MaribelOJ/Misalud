from asyncio.windows_events import NULL
from cgitb import text
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/misaluddb"
app.config['SQLALCHEMY_DATABASE_URL'] =  "postgresql://itbhznlmjvxpho:207139a015697300f6a516a2440fc6a6c1aed80d2857235f514be7075e374c3d@ec2-54-157-15-228.compute-1.amazonaws.com:5432/deee8u79387j9s"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'some-secret-key'

db = SQLAlchemy(app)

from tables import patient, functionary


db.create_all()
db.session.commit()


@app.route('/')
def front_page():
    return render_template("home.html")

@app.route('/patientLogIn')
def patientAccount():
    return render_template("loginpatient.html") 

@app.route('/functionaryLogIn')
def functionaryAccount():
    return render_template("loginfunctionary.html") 

@app.route('/useraccount', methods=['GET', 'POST'])
def userOptions():
    if (request.form["user"] == 'Patient'):
        return redirect(url_for('patientAccount'))
    if (request.form["user"] == 'Functionary'):
        return redirect(url_for('functionaryAccount'))


@app.route('/signup', methods=['GET','POST'])
def signUp():
    if (request.method == 'GET'):
        return render_template("signupform.html")

    elif (request.method == 'POST'):
    
        request_data = request.form

        full_name = request_data["fullName"]
        identification = request_data["identification"] 
        phone = request_data["phone"]
        age = request_data["age"]
        birthdate = request_data["birthdate"]
        blood_type = request_data["blood_type"]
        department = request_data["department"]
        district = request_data["district"]
        email = request_data["email"]
        password = request_data["password"]
        status = ""
        
        if(request.form["status"] == ' '):
            status = NULL

        elif(request.form["status"] == '1 - 2'):
            status = "1 - 2"

        elif(request.form["status"] == '3 - 4'):
            status = "3 - 4"

        elif(request.form["status"] == '5 - 6'):
            status = "5 - 6"
        
        newPatient = patient(identification, email, password, full_name, phone, department, district, birthdate, age, blood_type, status)
        db.session.add(newPatient)
        db.session.commit()

        return "your account has been created successfully"

@app.route('/loginPatient', methods=['POST'])
def loginP():

    request_data = request.form
    email = request_data["email"]
    password = request_data["password"]

    emails = patient.query.filter(patient.email == email)
    passwords = patient.query.filter(patient.password == password)
    #user = patient.query.filter(patient.email == email, patient.password == password)
    #user = patient.query.filter(patient.email == email).first()

    try:
        if (emails[0] is not None and passwords[0] is not None):
            return redirect(url_for('accountP', nombre = emails[0].full_name))  
    except:
        return "Wrong email or password entered" 


@app.route('/loginFunctionary', methods=['POST'])
def loginF():
    request_data = request.form
    id = request_data["id"]
    password = request_data["password"]

    ids = functionary.query.filter(functionary.identification == id)
    passwords = functionary.query.filter(functionary.password == password)

    try:
        if (ids[0] is not None and passwords[0] is not None):
            return redirect(url_for('accountF', nombre = ids[0].full_name))  
    except:
        return "Wrong email or password entered" 
   
@app.route('/accountP/<nombre>')   
def accountP(nombre):
    return render_template("patienthome.html", nombre = nombre)

@app.route('/accountF/<nombre>')   
def accountF(nombre):
    return render_template("functionaryhome.html", nombre = nombre)


if __name__ == "__main__":
    app.run()


