CREATE DATABASE employee_db;
USE employee_db;


CREATE TABLE employees (
    emp_id VARCHAR(255) PRIMARY KEY,
    emp_name VARCHAR(255),
    emp_role VARCHAR(255),
    emp_pwd VARCHAR(255)
);

INSERT INTO employees VALUES ("E001", "Shubham Soni", "Python Developer", "pass123");
INSERT INTO employees VALUES ("E002", "Saksham Soni", "Data Analyst", "saksham123");
INSERT INTO employees VALUES ("E003", "Pratibha Dwivedi", "ML Engineer", "pratibha123");


CREATE TABLE managers (
    manager_id VARCHAR(255) PRIMARY KEY,
    manager_pwd VARCHAR(255)
);

INSERT INTO managers VALUES ("admin@company.com", "admin1234");


CREATE TABLE departments (
    dept_id VARCHAR(255) PRIMARY KEY,
    dept_name VARCHAR(255)
);

INSERT INTO departments VALUES ("D001", "Human Resources");
INSERT INTO departments VALUES ("D002", "Information Technology");


CREATE TABLE attendance (
    record_id VARCHAR(255) PRIMARY KEY,
    emp_id VARCHAR(255),
    dept_id VARCHAR(255)
);

INSERT INTO attendance VALUES ("2023-02-25 09:11:34.48956", "E001", "D002");


CREATE TABLE salaries (
    salary_id VARCHAR(255) PRIMARY KEY,
    emp_id VARCHAR(255),
    amount DECIMAL(10,2),
    pay_date DATE
);

INSERT INTO salaries VALUES ("S001", "E001", 55000.00, "2025-05-31");
INSERT INTO salaries VALUES ("S002", "E002", 62000.00, "2025-05-31");
INSERT INTO salaries VALUES ("S003", "E003", 58000.00, "2025-05-31");


CREATE TABLE leaves (
    leave_id VARCHAR(255) PRIMARY KEY,
    emp_id VARCHAR(255),
    from_date DATE,
    to_date DATE,
    reason VARCHAR(255),
    status VARCHAR(50)
);

INSERT INTO leaves VALUES ("L001", "E001", "2025-06-10", "2025-06-12", "Medical Leave", "Approved");
INSERT INTO leaves VALUES ("L002", "E002", "2025-06-15", "2025-06-16", "Personal Work", "Pending");
INSERT INTO leaves VALUES ("L003", "E003", "2025-06-20", "2025-06-22", "Family Function", "Rejected");