#Student Management System
import tkinter as tk
from tkinter import messagebox
import os
import definition as D
# GUI
root = tk.Tk()
root.geometry('850x900')
root.title("Student Management System")

tk.Label(root, text="Name:").grid(row=0, column=0)
tk.Label(root, text="ID:").grid(row=1, column=0)
tk.Label(root, text="Age:").grid(row=2, column=0)
tk.Label(root, text="Course:").grid(row=3, column=0)
tk.Label(root, text="Delete by Id or Name:").grid(row=5, column=0)
tk.Label(root, text="Veiw all Details:").grid(row=6, column=0)
tk.Label(root, text="Search by ID or Name:").grid(row=7, column=0)

global id_entry,name_entry,age_entry,course_entry,text_area,search_entry

name_entry = tk.Entry(root,text="Enter the ID",font=("Times New Roman",16),fg='red',bd=5)
id_entry = tk.Entry(root,text="Enter the Name",font=("Times New Roman",16),fg='red',bd=5)
age_entry = tk.Entry(root,text="Enter the Age",font=("Times New Roman",16),fg='red',bd=5)
search_entry = tk.Entry(root,text="Search by ID or Name:",bd=5,font=("Times New Roman",16),fg='red')
course_entry = tk.Entry(root,text="Enter the Course",font=("Times New Roman",16),fg='red',bd=5)

id_entry.grid(row=1, column=1)
name_entry.grid(row=0, column=1)
age_entry.grid(row=2, column=1)
course_entry.grid(row=3, column=1)
search_entry.grid(row=7, column=1)

tk.Button(root, text="Add Student", command=lambda: D.add_student(name_entry, id_entry, age_entry, course_entry), padx=10).grid(row=4, column=0)
tk.Button(root, text="Update Student", command=lambda: D.update_student(name_entry, id_entry, age_entry, course_entry), padx=10).grid(row=4, column=1)
tk.Button(root, text="Delete Student", command=lambda: D.delete_student(name_entry, id_entry, age_entry, course_entry), padx=10).grid(row=5, column=1)
tk.Button(root, text="View All", command=lambda: D.view_all_students(text_area), padx=10).grid(row=6, column=1)
tk.Button(root, text="Search", command=lambda: D.search_student(search_entry,name_entry, id_entry, age_entry, course_entry,text_area), padx=10).grid(row=8, column=1)
tk.Button(root, text="Clear", command=lambda: D.clear_student(search_entry,name_entry, id_entry, age_entry, course_entry), padx=10).grid(row=8,column=0)

text_area = tk.Text(root, height=80, width=80,bd=5,font=("Times New Roman",16),fg='red')
text_area.grid(row=9, column=0, columnspan=2, pady=10)

root.mainloop()
