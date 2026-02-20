import tkinter as tk
from tkinter import ttk

student_records =[]

def remove_student():
    selected = student_listbox.curselection()
    if selected:
        index = selected[0]
        student_listbox.delete(index)
        student_records.pop(index)
        status_label.config(text="Record removed successfully", fg="green")
    else:
        status_label.config(text="Please choose a record to remove", fg="red")

def insert_student():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    course = course_var.get()
    gender = gender_var.get()

    if name == "" or age == "" or course == "Choose Course" or gender == "":
        status_label.config(text="All details are required", fg="red")
        return

    if not age.isdigit():
        status_label.config(text="Age should be numeric", fg="red")
        return

    student_info = {"name": name,"age": age,"course": course,"gender": gender
    }
    student_records.append(student_info)
    display_text = f"{len(student_records)}. Name: {name} | Age: {age} | Dept: {course} | Gender: {gender}"
    student_listbox.insert(tk.END, display_text)
    status_label.config(text="Student added successfully", fg="green")
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    course_var.set("Choose Course")
    gender_var.set("")
root = tk.Tk()
root.title("Student Management System")
root.geometry("400x600")
header_label = tk.Label(root, text="Student Record Manager",font=("Arial", 16, "bold"))
header_label.pack(pady=10)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Student Name").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(input_frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Age").grid(row=1, column=0, padx=10, pady=5)
age_entry = tk.Entry(input_frame)
age_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Course").grid(row=2, column=0, padx=10, pady=5)
course_var = tk.StringVar()
course_box = ttk.Combobox(input_frame, textvariable=course_var,
                          values=["IT", "CSE", "ECE", "MECH", "CIVIL"],
                          state="readonly", width=18)
course_box.set("Select your Course")
course_box.grid(row=2, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Select Gender").grid(row=3, column=0, padx=10, pady=5)
gender_var = tk.StringVar()
male_radio = tk.Radiobutton(input_frame, text="Male", variable=gender_var, value="Male")
female_radio = tk.Radiobutton(input_frame, text="Female", variable=gender_var, value="Female")
male_radio.grid(row=3, column=1, sticky="w")
female_radio.grid(row=3, column=1, padx=80, sticky="w")

add_btn = tk.Button(root, text="Add Record", command=insert_student)
add_btn.pack(pady=10)

status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.pack()

student_listbox = tk.Listbox(root, width=80, height=12)
student_listbox.pack(pady=10)

delete_btn = tk.Button(root, text="Remove Selected", command=remove_student)
delete_btn.pack(pady=10)
root.mainloop()
