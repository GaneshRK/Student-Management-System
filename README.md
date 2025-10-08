Student Management System (SMS)

This is a Python-based Student Management System (SMS) built using Tkinter for the GUI and text file storage for data management. It allows users to manage student records by adding, updating, deleting, searching, and viewing student details. The system is designed with simplicity in mind and provides an intuitive interface for handling student data.

Features:

Add Student: Input student details (Name, ID, Age, Course) and save them.

Update Student: Modify existing student records using the student ID.

Delete Student: Remove student records by ID.

Search Student: Find students by either ID or Name.

View All Students: Display a list of all stored students.

Clear Fields: Easily clear the input fields for fresh entries.

Key Components:

Tkinter GUI: A simple and interactive graphical interface.

Student Data Storage: Student details are stored in a plain text file (students.txt) and separated by a delimiter (|).

File Operations: The system supports adding, updating, deleting, and viewing records from the file.

Input Validation: Checks are in place to ensure that all fields are filled and that no duplicate student IDs are entered.

How It Works:

Student Data: All student records are stored in a text file (students.txt), and the system loads and saves this data every time a modification is made.

Add/Update/Delete: The system ensures that no duplicate student IDs are created and allows easy editing or removal of records.

Search: Users can search for students by ID or Name, and matching results are displayed.

Sort Data: Student records are automatically sorted by their ID for easy viewing.

This repository is ideal for anyone looking for a basic student management system with a GUI for educational purposes or small-scale projects.

Requirements:

Python 3.x

Tkinter (comes pre-installed with Python)

Setup:

Clone the repository.

Run the SMS.py file to launch the application.
