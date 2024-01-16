from tkinter import *
import tkinter.messagebox
from tkinter import messagebox
from tkinter import ttk
from tkinter import Tk, Button, ttk, Label, Toplevel
from PIL import Image,ImageTk
#import mysql.connector
import pymysql
import random
from time import strftime
from sheet import MarkEntry
from subject import Subject
from classL import cL


class Markss:
    def __init__(self,root,selected_class="Select Class"):
        self.root = root
        self.root.geometry("1450x730+0+0")
        self.root.overrideredirect(True)
        self.root.configure(bg="black")
        self.root .title("Report Management System | Developed by LarksTeckHub")
        
        #====================title================
        self.icon_title = PhotoImage(file="images/logo.png")
        desired_width = 100
        desired_height = 50
        self.icon_title = self.icon_title.subsample(int(self.icon_title.width() / desired_width), int(self.icon_title.height() / desired_height)) 
        title= Label(self.root, text="Build Terminal Report",image=self.icon_title,compound=LEFT, font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
                # Assuming functions to retrieve user information from the database
                
        def get_user_name():
            # Replace this function with your code to fetch the user's name from the database
            return "Francis"  # Example user name

        def get_user_role():
            # Replace this function with your code to fetch the user's role from the database
            return "DOS"  # Example user role

        # Retrieve user information from the database
        user_name = get_user_name()
        user_role = get_user_role()

        # Label to display the user's name
        label_user_name = Label(self.root, text=f"Userlogin: {user_name}",bg="#010c48",fg="white",anchor="w", padx=5,font=("times new roman",17,"bold"))
        label_user_name.place(x=750,y=25)

        # Label to display the user's role
        label_user_role = Label(self.root, text=f"UserRole: {user_role}",bg="#010c48",fg="white",anchor="w", padx=5,font=("times new roman",17,"bold"))
        label_user_role.place(x=1000,y=25)
        #========clock================
        # Function to display time on the label
        def time():
            string = f"Welcome to Report Management System\t\t Date: {strftime('%d-%m-%Y')}\t\t Time: {strftime('%H:%M:%S')}"  # Format the time string
            self.lbl_clock.config(text=string)  # Update the label with the current time
            self.lbl_clock.after(1000, time)  # Call the time function after 1000ms (1 second)

        # Create a label for the clock
        self.lbl_clock = Label(self.root, text="", font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # Call the time function to start displaying the time
        time()
        ########################Buttons#############################################
        self.icon_side = PhotoImage(file="images/side.png")
        new_width, new_height = 25, 25  # Set the new dimensions
        self.icon_side = self.icon_side.subsample(self.icon_side.width()// new_width, self.icon_side.height() // new_height)
        
        #===========Class Menu==============
        ClassMenu = Frame(self.root,bd=2,relief=RIDGE, bg="white")
        ClassMenu.place(x=0,y=100,width=1400,height=60)
        
        self.lbl_select = Label(ClassMenu, text="Select Class", font=("times new roman", 17,"bold"),image=self.icon_side,compound=RIGHT,bg="white")
        self.lbl_select.place(x=150, y=8)
        
        self.conn = pymysql.connect(host="localhost",user="root",database="report")
        
        # Retrieve values from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT class FROM subject")  # Modify with your database column and table names
        classs = [classs[0] for classs in cursor.fetchall()]

        self.combo_class = ttk.Combobox(ClassMenu, width=20, font=("times new roman", 16, "bold"), state="readonly")
        self.combo_class["values"] = tuple(["Select Class"] + classs)
        self.combo_class.current(0)
        self.combo_class.place(x=330, y=13)
        # Bind the function to update the label when the combobox selection changes
        self.combo_class.bind("<<ComboboxSelected>>", self.update_selected_class_label)
        #=====================================================================================================
        
        #=====================title=======================================================
        lbl_title=Label(self.root,text="MARKS ENTRY FORM",font=("times new roman",18,"bold"),bg="black",fg="white",bd=4)
        lbl_title.place(x=200,y=160,width=1160,height=40)
       
        self.label_class = Label(self.root, text=f"Class: {selected_class}", bg="black", fg="white", anchor="w",
                                 padx=5, font=("times new roman", 20, "bold"))
        self.label_class.place(x=270, y=160)
        
        #===========Left Menu==============
        LeftMenu = Frame(self.root,bd=2,relief=RIDGE, bg="white")
        LeftMenu.place(x=0,y=160,width=200,height=530)
        
        ################## Buttons####################################################
        #self.subject_buttons = []  # List to store subject buttons
        btn_subject = Button(LeftMenu,text="Subject\nEntry",command=self.show_loading_subject,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",17,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_terminalRe = Button(LeftMenu,text="Terminal\nReports",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",17,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_classList = Button(LeftMenu,text="Class\nList",command= self.show_loading_class,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",18,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_broadSheet = Button(LeftMenu,text="Broad\nSheet",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",18,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_teachDash = Button(LeftMenu,text="MOCK",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",18,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_teachDash = Button(LeftMenu,text="Attendance",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",18,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_teachDash = Button(LeftMenu,text="Remarks",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",18,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_settings = Button(LeftMenu,text="Settings",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",19,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit = Button(LeftMenu,text="Exit",command=self.logout,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",18,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        
        lbl_footer = Label(self.root,text="Report Management System | Developed by LarksTeckHub \nFor any Technical Issue Contact: 0741789121",font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM, fill=X)
        #===============Button==================
        #===================labelframe====================================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="",font=("times new roman",18,"bold"),padx=2)
        labelframeleft.place(x=200,y=200,width=1160,height=485)
        
        #================btn===========================================
        self.btn_subject1 = Button(labelframeleft, text="", font=("times new roman", 15, "bold"), cursor="hand2", command=self.show_subject)
        self.btn_subject1.place(x=20, y=10, height=40, width=200)
        
        self.btn_subject2 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2")
        self.btn_subject2.place(x=250,y=10,height=40,width=200)
        
        self.btn_subject3 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2")
        self.btn_subject3.place(x=20,y=60,height=40,width=200)
        
        self.btn_subject4 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2")
        self.btn_subject4.place(x=250,y=60,height=40,width=200)
        
        self.btn_subject5 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2")
        self.btn_subject5.place(x=20,y=110,height=40,width=200)
        
        self.btn_subject6 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2")
        self.btn_subject6.place(x=250,y=110,height=40,width=200)
        
        self.btn_subject7 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2")
        self.btn_subject7.place(x=20,y=160,height=40,width=200)
        
        self.btn_subject8 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2")
        self.btn_subject8.place(x=250,y=160,height=40,width=200)
        
        self.btn_subject9 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2")
        self.btn_subject9.place(x=20,y=210,height=40,width=200)
        
        self.btn_subject10 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2")
        self.btn_subject10.place(x=250,y=210,height=40,width=200)
        
        self.btn_subject11 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2")
        self.btn_subject11.place(x=20,y=260,height=40,width=200)
        
        self.btn_subject12 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2")
        self.btn_subject12.place(x=250,y=260,height=40,width=200)
        
        self.btn_subject13 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2")
        self.btn_subject13.place(x=20,y=310,height=40,width=200)
        
        self.btn_subject14 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2")
        self.btn_subject14.place(x=250,y=310,height=40,width=200)
        
        self.btn_subject15 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2")
        self.btn_subject15.place(x=20,y=360,height=40,width=200)
        
        self.btn_subject16 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2")
        self.btn_subject16.place(x=250,y=360,height=40,width=200)
        #########################################
            
        self.subject_buttons = []

        for i in range(1, 17):
            btn_subject = Button(labelframeleft, text="", font=("times new roman", 15, "bold"), cursor="hand2", command=lambda i=i: self.show_subject(i))
            row = (i - 1) // 2
            col = (i - 1) % 2
            btn_subject.place(x=20 + col * 230, y=10 + row * 50, height=40, width=200)
            self.subject_buttons.append(btn_subject)
        
    def show_selected_class(self):
        selected_class = self.combo_class.get()
        # Now, you can pass the selected_class value to sheet.py or update the label directly
        # In this example, we will use a simple print statement
        print("Selected Class:", selected_class)
              
    def update_selected_class_label(self, event):
        selected_class = self.combo_class.get()
        
        # Fetch subjects for the selected class from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT subject1, subject2, subject3, subject4, subject5, subject6, subject7, subject8, subject9, subject10, subject11, subject12, subject13, subject14, subject15, subject16 FROM subject WHERE class = %s", (selected_class,))
        subjects = cursor.fetchone()

        for i, subject in enumerate(subjects):
            # If subject is not empty, update button text
            if subject:
                self.subject_buttons[i]["text"] = subject
            else:
                # If subject is empty, display "Empty" on the button
                self.subject_buttons[i]["text"] = "Empty"
  
    def show_subject(self, subject_number):
        # Check if a class is selected
        selected_class = self.combo_class.get()
        if selected_class == "Select Class":
            messagebox.showinfo("Error", "Please select a class first.")
            return

        # Fetch students for the selected class from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT ref  FROM student WHERE class = %s", (selected_class,))
        students = [student[0] for student in cursor.fetchall()]
        #students = cursor.fetchall()
        
        # Fetch students for the selected class from the database
        #cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM student WHERE class = %s", (selected_class,))
        name = [student[0] for student in cursor.fetchall()]
        
        # Fetch marks for the selected subject from the database
        cursor.execute(f"SELECT * FROM result{subject_number} WHERE class = %s", (selected_class,))
        marks = cursor.fetchall()
        
        cursor.execute(f"SELECT subject{subject_number} FROM subject WHERE class = %s", (selected_class,))
        selected_subject = cursor.fetchone()[0]

        # Continue with the intended behavior
        self.new_window = Toplevel(self.root)
        self.app = MarkEntry(self.new_window, rows=10, columns=5, name=name, students=students, selected_class= selected_class, selected_subject=selected_subject, subject_number=subject_number)
        #self.app = MarkEntry(self.new_window, selected_class, selected_subject, students)

    #########################################  
    def show_loading_subject(self):
        self.loading_label = Label(self.root, text="Loading...", font=("times new roman", 20, "bold"))
        self.loading_label.pack()
        self.root.after(1000, self.subject_details)  # After 30 seconds, show another window
        
    def subject_details(self):
        self.loading_label.destroy()
        self.new_window=Toplevel(self.root)
        self.app=Subject(self.new_window)
    #########################################  
    def show_loading_class(self):
        self.loading_label = Label(self.root, text="Loading...", font=("times new roman", 20, "bold"))
        self.loading_label.pack()
        self.root.after(1000, self.class_details)  # After 30 seconds, show another window
    def class_details(self):
        self.loading_label.destroy()
        self.new_window=Toplevel(self.root)
        self.app=cL(self.new_window)
         # Create the UI components
       
    def logout(self):
        logout = tkinter.messagebox.askyesno("Report Management System", "Confirm if you want to log out", parent=self.root)
        if logout:
            # Perform logout actions here (e.g., closing the window, resetting variables, etc.)
            self.root.destroy()
    
root=Tk()
ob = Markss(root)
root.mainloop()