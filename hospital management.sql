CREATE DATABASE hospital_db;

USE hospital_db;

CREATE TABLE Patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    address VARCHAR(255),
    phone VARCHAR(15)
);

CREATE TABLE Doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    specialization VARCHAR(100),
    phone VARCHAR(15)
);

CREATE TABLE Appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    appointment_date DATE,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);

INSERT INTO Patients (name, age, gender, address, phone)
VALUES ('Aditi', 30, 'Male', '123 Main St', '555-1234'),
       ('Smita', 25, 'Female', '456 5th cross', '555-5678'),
       ('Rakesh', 40, 'Female', '789 Park Street', '555-9012');
       
       INSERT INTO Doctors (name, specialization, phone) VALUES
('Dr. Greasha J', 'Diagnostic Medicine', '555-1111'),
('Dr. Mira Anand', 'General Surgery', '555-2222'),
('Dr. Deeksha Khare', 'Neurosurgery', '555-3333');

INSERT INTO Appointments (patient_id, doctor_id, appointment_date) VALUES
(1, 1, '2024-07-01'),
(2, 2, '2024-07-02'),
(3, 3, '2024-07-03');

select * from Patients;
