# Attendance Management System 📚

This is a **Python-based Attendance Management System** that allows faculty and managers to sign up, manage student information, and mark attendance. The system stores data in CSV files and provides a tabular display of attendance records.

## Features ✨

- **Faculty/Manager Sign-up and Login**: Ensures only authorized personnel can access and modify records.
- **Student Information Management**: Easily add students with details like name, roll number, ID, phone number, and email.
- **Attendance Marking**: Mark attendance for students daily by adding new date columns dynamically to the attendance sheet.
- **CSV-Based Storage**: Data is stored in CSV format for easy export, retrieval, and analysis.
- **Tabular Display**: Attendance records are displayed in a well-formatted tabular view for clarity.

## Project Structure 🗂️

```bash
.
├── attendance.csv                  # Stores attendance records
├── student_info.csv                # Stores student information
├── mark_attendance.py              # Main script for marking attendance
├── faculty_signup.py               # Script for faculty signup/login
├── README.md                       # Project documentation
