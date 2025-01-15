from flask import Flask, request, redirect, url_for, render_template
import mysql.connector

app = Flask(__name__)

# Configure MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aadya@2003",
    database="hospital_management"
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_patient', methods=['POST'])
def add_patient():
    name = request.form['name']
    phone = request.form['phone']
    address = request.form['address']
    cursor.execute("INSERT INTO patients (name, phone, address) VALUES (%s, %s, %s)", (name, phone, address))
    db.commit()
    return redirect(url_for('index'))

@app.route('/add_doctor', methods=['POST'])
def add_doctor():
    name = request.form['name']
    phone = request.form['phone']
    address = request.form['address']
    cursor.execute("INSERT INTO doctors (name, phone, address) VALUES (%s, %s, %s)", (name, phone, address))
    db.commit()
    return redirect(url_for('index'))

@app.route('/view_patients')
def view_patients():
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()
    return render_template('view_patients.html', patients=patients)

@app.route('/view_doctors')
def view_doctors():
    cursor.execute("SELECT * FROM doctors")
    doctors = cursor.fetchall()
    return render_template('view_doctors.html', doctors=doctors)

@app.route('/delete_patient/<int:id>')
def delete_patient(id):
    cursor.execute("DELETE FROM patients WHERE id = %s", (id,))
    db.commit()
    return redirect(url_for('view_patients'))

@app.route('/delete_doctor/<int:id>')
def delete_doctor(id):
    cursor.execute("DELETE FROM doctors WHERE id = %s", (id,))
    db.commit()
    return redirect(url_for('view_doctors'))

if __name__ == '__main__':
    app.run(debug=True)
