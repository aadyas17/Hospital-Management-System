from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aadya@2003",
    database="hospital_db"
)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        address = request.form['address']
        phone = request.form['phone']
        cursor.execute("INSERT INTO Patients (name, age, gender, address, phone) VALUES (%s, %s, %s, %s, %s)",
                       (name, age, gender, address, phone))
        db.commit()
        return redirect(url_for('index'))
    return render_template('add_patient.html')

@app.route('/view_patients')
def view_patients():
    cursor.execute("SELECT * FROM Patients")
    patients = cursor.fetchall()
    return render_template('view_patients.html', patients=patients)

if __name__ == '__main__':
    app.run(debug=True)
