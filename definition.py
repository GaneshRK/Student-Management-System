#Definition
import os
import tkinter as tk
from tkinter import messagebox 


FILE_NAME = "students.txt"
DELIMITER = "|"

global id_entry,name_entry,age_entry,course_entry,text_area

def load_students():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
        return [line.strip().split(DELIMITER) for line in lines if line.strip()]

def save_students(students):
    with open(FILE_NAME, "w") as file:
        for student in students:
            file.write(DELIMITER.join(student) + "\n")

def add_student(name_entry, id_entry, age_entry, course_entry):
    student = [name_entry.get(),id_entry.get(), age_entry.get(), course_entry.get()]
    if not all(student):
        messagebox.showwarning("Input Error", "All fields are required.")
        return
    students = load_students()
    temp=student[0]
    student[0]=student[1]
    student[1]=temp
    for s in students:
        if s[0] == student[0]:
            messagebox.showerror("Duplicate ID", "Student ID already exists.")
            return
    students.append(student)
    students.sort(key=lambda x:x[0])
    save_students(students)
    messagebox.showinfo("Success", "Student added successfully.")
    clear_entries(id_entry, name_entry, age_entry, course_entry)

def view_all_students(text_area):
    students = load_students()
    text_area.delete("1.0", tk.END)
    for s in students:
        text_area.insert(tk.END, f"ID: {s[0]}, Name: {s[1]}, Age: {s[2]}, Course: {s[3]}\n")

def update_student(name_entry, id_entry, age_entry, course_entry):
    student_id = id_entry.get()
    students = load_students()
    found = False
    for i, student in enumerate(students):
        if student[0] == student_id:
            students[i] = [student_id, name_entry.get(), age_entry.get(), course_entry.get()]
            found = True
            break

    if not found:
        messagebox.showerror("Not Found", "Student ID not found.")
        return

    students.sort(key=lambda x:x[0])
    save_students(students)
    messagebox.showinfo("Success", "Student updated successfully.")
    clear_entries(name_entry, id_entry, age_entry, course_entry)

def delete_student(name_entry, id_entry, age_entry, course_entry):
    student_id = id_entry.get()
    students = load_students()
    new_students = [s for s in students if s[0] != student_id]

    if len(new_students) == len(students):
        messagebox.showerror("Not Found", "Student ID not found.")
        return

    save_students(new_students)
    messagebox.showinfo("Deleted", "Student deleted successfully.")
    clear_entries(name_entry, id_entry, age_entry, course_entry)

def search_student(search_entry,name_entry, id_entry, age_entry, course_entry,text_area):
    keyword = search_entry.get().strip().lower()
    students = load_students()
    results = [s for s in students if keyword in s[0].lower() or keyword in s[1].lower()]
    text_area.delete("1.0", tk.END)
    for s in results:
        text_area.insert(tk.END, f"ID: {s[0]},Name: {s[1]}, Age: {s[2]}, Course: {s[3]}\n")
    if not results:
        text_area.insert(tk.END, "No matching student found.\n")

def clear_entries(name_entry, id_entry, age_entry, course_entry):
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)


def clear_student(search_entry,name_entry, id_entry, age_entry, course_entry):
    id_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    
    





