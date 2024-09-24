import tkinter as tk 
from tkinter import messagebox 
import json 
import os 
 
 
DataFile = "Project.json" 
 
 
def readData(): 
    if os.path.exists(DataFile): 
        with open(DataFile, "r") as file: 
            try: 
                return json.load(file) 
            except json.JSONDecodeError: 
                return {} 
    else: 
        return {} 
 
 
def writeData(data): 
    with open(DataFile, "w") as file: 
        json.dump(data, file, indent=4) 
 
 
 
def addStudent(): 
    global student_ID, name, subject, grade 
 
 
    data = readData() 
  
    add_window = tk.Toplevel(root) 
    add_window.geometry("200x150") 
    add_window.title("Check Student") 
 
 
    tk.Label(add_window, text="Student ID").pack(pady=5) 
    student_id_entry = tk.Entry(add_window) 
    student_id_entry.pack(pady=5) 
 
 
    tk.Button(add_window, text="Enter", command= lambda: [input_id()]).pack(pady=10) 
 
 
 
 
    def input_id(): 
        global win2, name_entry, subject_entry, grade_entry 
        student_ID = student_id_entry.get() 
 
 
        if not student_ID : 
            messagebox.showerror("Input Error", "Input Student id.") 
            return 
        
        if student_ID in data: 
            messagebox.showerror("Duplicate ID", f"{student_ID} already exists. Use update option.") 
            return 
        
        data[student_ID]= {} 
        writeData(data) 
 
 
 
        if student_ID : 
 
 
            win2= tk.Toplevel(add_window) 
            win2.title("Add Student") 
            win2.geometry("500x400+50+50") 
            win2.config(bg="#f2e5ff") 
 
 
            tk.Label(win2, text="Name").pack(pady=5) 
            name_entry = tk.Entry(win2) 
            name_entry.pack(pady=5) 
 
 
            tk.Label(win2, text="Subject").pack(pady=5) 
            subject_entry = tk.Entry(win2) 
            subject_entry.pack(pady=5) 
 
 
            tk.Label(win2, text="Grade").pack(pady=5) 
            grade_entry = tk.Entry(win2) 
            grade_entry.pack(pady=5) 
 
 
            tk.Button(win2, text="Submit", command=lambda: [add(),finish()]).pack(pady=20) 
 
 
            tk.Button(win2, text="Add subjects" ,command= lambda: [add()]).pack(pady=5) 
 
 
            tk.Button(win2, text="End", command=lambda: [end()]).pack(pady=20) 
 
 
 
 
    
    def add(): 
        global student_ID 
        student_ID = student_id_entry.get() 
        name = name_entry.get() 
        subject = subject_entry.get() 
        grade_2= grade_entry.get() 
        grade=float(grade_2) 
     
 
        if not name or not subject or not grade: 
            messagebox.showerror("Input Error", "All information required.") 
            return 
        if "subjects" not in data[student_ID]: 
                data[student_ID]["name"] = name 
                data[student_ID]["subjects"] = {} 
 
        # Add new subjects or append grades to the subject if it already exists 
        data[student_ID]["subjects"][subject] = grade 
        
        writeData(data) 
        subject_entry.delete(0, tk.END) 
        grade_entry.delete(0,tk.END) 
 
    def finish(): 
         
 
        messagebox.showinfo("Success", f"Student added successfully.\n{data[student_ID]}") 
        win2.destroy() 
 
 
 
     
         
 
    def end(): 
        win2.destroy() 
        add_window.destroy() 
 
 
 
def updateData(): 
    global name_entry 
    update_window = tk.Toplevel(root) 
    update_window.title("Update Student") 
    update_window.geometry("200x150+200+200") 
 
 
    tk.Label(update_window, text="Student ID").pack(pady=5) 
    student_id_entry = tk.Entry(update_window) 
    student_id_entry.pack(pady=5) 
 
 
    tk.Button(update_window, text="Enter", command= lambda: submit_update()).pack(pady=10) 
 
 
    def submit_update(): 
        student_ID = student_id_entry.get() 
        data = readData() 
 
 
        if student_ID not in data: 
            messagebox.showerror("Not Found", f"Student ID {student_ID} not found.") 
            update_window.destroy() 
            return 
 
 
        if student_ID :
            win=tk.Toplevel(update_window) 
            win.title("Update Student") 
            win.geometry("500x400+50+50") 
            win.config(bg="#f2e5ff") 
 
 
            tk.Label(win, text="New Name (Leave empty if no change)").pack(pady=5) 
            name_entry = tk.Entry(win) 
            name_entry.pack(pady=5) 
 
 
            tk.Label(win, text="Subject").pack(pady=5) 
            subject_entry = tk.Entry(win) 
            subject_entry.pack(pady=5) 
 
 
            tk.Label(win, text="New Grade").pack(pady=5) 
            grade_entry = tk.Entry(win) 
            grade_entry.pack(pady=5) 
 
 
            tk.Button(win, text="Submit", command=lambda: [update(),more()]).pack(pady=20) 
 
 
            tk.Button(win, text="Add subjects" ,command= lambda:[update(),more()]).pack(pady=5) 
 
 
            tk.Button(win, text="End", command=lambda:finish()).pack(pady=20) 
 
 
 
 
        def update(): 
            name = name_entry.get() 
            subject = subject_entry.get() 
            grade_1= grade_entry.get() 
            grade=float(grade_1) 
 
            info=data[student_ID] 
 
            if not info: 
                data[student_ID]["name"] = name 
                data[student_ID]["subjects"] = {} 
 
            if name: 
                data[student_ID]["name"] = name 
                messagebox.showinfo("Success", f"Name updated for student {student_ID}.") 
 
     
            if subject and grade: 
                data[student_ID]["subjects"][subject] = grade 
                messagebox.showinfo("Success", f"Updated student {student_ID}.") 
            else: 
                messagebox.showerror("Input Error", "Subject and grade are required for update.") 
                return 
        
             
 
            writeData(data) 
 
 
        def more(): 
            subject_entry.delete(0,tk.END) 
            grade_entry.delete(0,tk.END) 
 
 
        def finish(): 
            win.destroy() 
            update_window.destroy() 
  
 
 
# View Student Function with GUI Integration 
def viewData(): 
    def submit_view(): 
        student_ID = student_id_entry.get() 
        data = readData() 
 
 
        if student_ID in data: 
            student = data[student_ID] 
            subjects_info = "\n".join([f"{subject}: {grades}" for subject, grades in student["subjects"].items()]) 
            messagebox.showinfo(f"Student Info", f"Name: {student['name']}\nSubjects:\n{subjects_info}") 
        else: 
            messagebox.showerror("Not Found", f"Student ID {student_ID} not found.") 
        view_window.destroy() 
 
 
    view_window = tk.Toplevel(root) 
    view_window.title("View Student") 
 
 
    tk.Label(view_window, text="Student ID").pack(pady=5) 
    student_id_entry = tk.Entry(view_window) 
    student_id_entry.pack(pady=5) 
 
 
    tk.Button(view_window, text="View", command=submit_view).pack(pady=10) 
 
 
# Remove Student Function with GUI Integration 
def removeData(): 
    def submit_remove(): 
        student_ID = student_id_entry.get() 
        data = readData() 
 
 
        if student_ID in data: 
            del data[student_ID] 
            writeData(data) 
            messagebox.showinfo("Success", f"Student {student_ID} removed successfully.") 
        else: 
            messagebox.showerror("Not Found", f"Student ID {student_ID} not found.") 
        remove_window.destroy() 
 
 
    remove_window = tk.Toplevel(root) 
    remove_window.title("Remove Student") 
 
 
    tk.Label(remove_window, text="Student ID").pack(pady=5) 
    student_id_entry = tk.Entry(remove_window) 
    student_id_entry.pack(pady=5) 
 
 
    tk.Button(remove_window, text="Remove", command=submit_remove).pack(pady=10) 
 
 
def calculate(): 
    data=readData() 
 
 
    calc = tk.Toplevel(root) 
    calc.geometry("200x150+300+300") 
    calc.title("Check Average Grade") 
 
 
    tk.Label(calc, text="Student ID").pack(pady=5) 
    student_id_entry = tk.Entry(calc) 
    student_id_entry.pack(pady=5) 
 
 
 
 
    def do(): 
        student_ID = student_id_entry.get() 
        if student_ID not in data: 
            messagebox.showerror("Not Found", f"Student ID {student_ID} not found.") 
            student_id_entry.destroy() 
            return 
 
        sum=0 
        b= len(data[student_ID]["subjects"]) 
        di  = data[student_ID]["subjects"] 
        for key,value in di.items(): 
            sum+=value 
 
 
        avg= sum/b 
        messagebox.showinfo("Average Grade", f"Average grade of {data[student_ID]["name"]} is CGPA: {avg}") 
 
 
 
 
    tk.Button(calc,text="Calculate", command=do).pack(pady=10) 
 
 
 
 
# Main GUI function (remains the same as before) 
def main_gui(): 
    global root  #to use it in outer functions 
    root = tk.Tk() 
    root.title("Student Grade Management System") 
    root.geometry("800x600+70+70") 
    root.resizable(False,False) 
    root.config(bg="#C8A2C8") 
 
 
    # Buttons to trigger different functions 
    tk.Button(root, text="Add Student",bg="#E8FAEA", command=addStudent, width=100, height=5).pack(padx=5,pady=5) 
    tk.Button(root, text="Update Student",bg="#E8FAEA", command=updateData, width=100, height=5).pack(padx=5,pady=5) 
    tk.Button(root, text="View Student",bg="#E8FAEA", command=viewData, width=100, height=5).pack(padx=5,pady=5) 
    tk.Button(root, text="Remove Student",bg="#E8FAEA", command=removeData, width=100, height=5).pack(padx=5,pady=5) 
    tk.Button(root, text="Average Grade Calculate",bg="#E8FAEA",command=calculate, width=100, height=5).pack(padx=5,pady=5) 
    tk.Button(root, text="Exit",bg="#E8FAEA", command=root.quit, width=100, height=5).pack(padx=5,pady=5) 
 
 
    root.mainloop() 
 
 
main_gui()
            