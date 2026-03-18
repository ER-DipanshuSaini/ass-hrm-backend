-- PostgreSQL Database Schema for HRMS Lite
-- This file is for documentation and manual setup if moving away from SQLite.

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    employee_id VARCHAR(50) UNIQUE NOT NULL,
    full_name VARCHAR(150) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    department VARCHAR(100) NOT NULL
);

CREATE TYPE attendance_status AS ENUM ('Present', 'Absent');

CREATE TABLE attendance (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    status attendance_status NOT NULL,
    UNIQUE (employee_id, date)
);
