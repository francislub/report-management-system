from tkinter import *
import tkinter.messagebox
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
import random
from time import strftime
import openpyxl
import os
class Marks:
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
        
        self.conn = mysql.connector.connect(host="localhost",user="root",password="francis121",database="report")
        
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

        
        #=====================title=======================================================
        lbl_title=Label(self.root,text="MARKS ENTRY FORM",font=("times new roman",18,"bold"),bg="black",fg="white",bd=4)
        lbl_title.place(x=200,y=160,width=1160,height=40)
       
        self.label_class = Label(self.root, text=f"Class: {selected_class}", bg="black", fg="white", anchor="w",
                                 padx=5, font=("times new roman", 20, "bold"))
        self.label_class.place(x=270, y=160)
        
        #===========Left Menu==============
        LeftMenu = Frame(self.root,bd=2,relief=RIDGE, bg="white")
        LeftMenu.place(x=0,y=160,width=200,height=520)
        
        ################## Buttons####################################################
        #self.subject_buttons = []  # List to store subject buttons
        btn_subject = Button(LeftMenu,text="Subject\nEntry",command=self.show_subject1,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",17,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_terminalRe = Button(LeftMenu,text="Terminal\nReports",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",17,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_classList = Button(LeftMenu,text="Class List",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",18,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_reportGeneration = Button(LeftMenu,text="",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",18,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_teachDash = Button(LeftMenu,text="",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",18,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_teachDash = Button(LeftMenu,text="",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",18,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_teachDash = Button(LeftMenu,text="",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",18,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_settings = Button(LeftMenu,text="Settings",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",19,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit = Button(LeftMenu,text="Exit",command=self.logout,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",18,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        
        lbl_footer = Label(self.root,text="Report Management System | Developed by LarksTeckHub \nFor any Technical Issue Contact: 0741789121",font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM, fill=X)
   
        #===============Button==================
        #===================labelframe====================================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="",font=("times new roman",18,"bold"),padx=2)
        labelframeleft.place(x=200,y=200,width=1160,height=485)
        
        #================btn===========================================
        self.btn_subject1 = Button(labelframeleft, text="", font=("times new roman", 15, "bold"), cursor="hand2", command=self.show_subject1)
        self.btn_subject1.place(x=20, y=10, height=40, width=200)
        
        self.btn_subject2 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2",command=self.show_subject2)
        self.btn_subject2.place(x=250,y=10,height=40,width=200)
        
        self.btn_subject3 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2",command=self.show_subject3)
        self.btn_subject3.place(x=20,y=60,height=40,width=200)
        
        self.btn_subject4 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2",command=self.show_subject4)
        self.btn_subject4.place(x=250,y=60,height=40,width=200)
        
        self.btn_subject5 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2",command=self.show_subject5)
        self.btn_subject5.place(x=20,y=110,height=40,width=200)
        
        self.btn_subject6 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2",command=self.show_subject6)
        self.btn_subject6.place(x=250,y=110,height=40,width=200)
        
        self.btn_subject7 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2",command=self.show_subject7)
        self.btn_subject7.place(x=20,y=160,height=40,width=200)
        
        self.btn_subject8 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2",command=self.show_subject8)
        self.btn_subject8.place(x=250,y=160,height=40,width=200)
        
        self.btn_subject9 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2",command=self.show_subject9)
        self.btn_subject9.place(x=20,y=210,height=40,width=200)
        
        self.btn_subject10 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2",command=self.show_subject10)
        self.btn_subject10.place(x=250,y=210,height=40,width=200)
        
        self.btn_subject11 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2",command=self.show_subject11)
        self.btn_subject11.place(x=20,y=260,height=40,width=200)
        
        self.btn_subject12 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2",command=self.show_subject12)
        self.btn_subject12.place(x=250,y=260,height=40,width=200)
        
        self.btn_subject13 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2",command=self.show_subject13)
        self.btn_subject13.place(x=20,y=310,height=40,width=200)
        
        self.btn_subject14 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2",command=self.show_subject14)
        self.btn_subject14.place(x=250,y=310,height=40,width=200)
        
        self.btn_subject15 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2",command=self.show_subject15)
        self.btn_subject15.place(x=20,y=360,height=40,width=200)
        
        self.btn_subject16 = Button(labelframeleft,text="",font=("times new roman",15,"bold"),cursor="hand2",command=self.show_subject16)
        self.btn_subject16.place(x=250,y=360,height=40,width=200)
        #########################################
             
    def update_selected_class_label(self, event):
        selected_class = self.combo_class.get()
        if selected_class != "Select Class":
            self.label_class.config(text=f"Class: {selected_class}")

    def show_subject1(self):
        selected_class = self.combo_class.get()
        if selected_class != "Select Class":
            # Fetch subjects related to the selected class from the database
            conn = mysql.connector.connect(host="localhost", user="root", password="francis121", database="report")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT subject1 FROM subject WHERE class = %s", (selected_class,))
            subjects = [subject[0] for subject in my_cursor.fetchall()]

            if subjects:
                subject_text = "\n".join(subjects)
                self.btn_subject1.config(text=subject_text)
            else:
                messagebox.showinfo("No Subjects", "No subjects available for the selected class.", parent=self.root)
        else:
            messagebox.showwarning("Warning", "Please select a class.")
            
    def show_subject2(self):
        selected_class = self.combo_class.get()
        if selected_class != "Select Class":
            # Fetch subjects related to the selected class from the database
            conn = mysql.connector.connect(host="localhost", user="root", password="francis121", database="report")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT subject2 FROM subject WHERE class = %s", (selected_class,))
            subjects = [subject[0] for subject in my_cursor.fetchall()]

            if subjects:
                subject_text = "\n".join(subjects)
                self.btn_subject2.config(text=subject_text)
            else:
                messagebox.showinfo("No Subjects", "No subjects available for the selected class.", parent=self.root)
        else:
            messagebox.showwarning("Warning", "Please select a class.")
            
    def show_subject3(self):
        selected_class = self.combo_class.get()
        if selected_class != "Select Class":
            # Fetch subjects related to the selected class from the database
            conn = mysql.connector.connect(host="localhost", user="root", password="francis121", database="report")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT subject3 FROM subject WHERE class = %s", (selected_class,))
            subjects = [subject[0] for subject in my_cursor.fetchall()]

            if subjects:
                subject_text = "\n".join(subjects)
                self.btn_subject3.config(text=subject_text)
            else:
                messagebox.showinfo("No Subjects", "No subjects available for the selected class.", parent=self.root)
        else:
            messagebox.showwarning("Warning", "Please select a class.")
            
    def show_subject4(self):
        selected_class = self.combo_class.get()
        if selected_class != "Select Class":
            # Fetch subjects related to the selected class from the database
            conn = mysql.connector.connect(host="localhost", user="root", password="francis121", database="report")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT subject4 FROM subject WHERE class = %s", (selected_class,))
            subjects = [subject[0] for subject in my_cursor.fetchall()]

            if subjects:
                subject_text = "\n".join(subjects)
                self.btn_subject4.config(text=subject_text)
            else:
                messagebox.showinfo("No Subjects", "No subjects available for the selected class.", parent=self.root)
        else:
            messagebox.showwarning("Warning", "Please select a class.")
        
    def show_subject5(self):
        selected_class = self.combo_class.get()
        if selected_class != "Select Class":
            # Fetch subjects related to the selected class from the database
            conn = mysql.connector.connect(host="localhost", user="root", password="francis121", database="report")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT subject5 FROM subject WHERE class = %s", (selected_class,))
            subjects = [subject[0] for subject in my_cursor.fetchall()]

            if subjects:
                subject_text = "\n".join(subjects)
                self.btn_subject5.config(text=subject_text)
            else:
                messagebox.showinfo("No Subjects", "No subjects available for the selected class.", parent=self.root)
        else:
            messagebox.showwarning("Warning", "Please select a class.")
            
    def show_subject6(self):
        selected_class = self.combo_class.get()
        if selected_class != "Select Class":
            # Fetch subjects related to the selected class from the database
            conn = mysql.connector.connect(host="localhost", user="root", password="francis121", database="report")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT subject6 FROM subject WHERE class = %s", (selected_class,))
            subjects = [subject[0] for subject in my_cursor.fetchall()]

            if subjects:
                subject_text = "\n".join(subjects)
                self.btn_subject6.config(text=subject_text)
            else:
                messagebox.showinfo("No Subjects", "No subjects available for the selected class.", parent=self.root)
        else:
            messagebox.showwarning("Warning", "Please select a class.")
    def show_subject7(self):
        selected_class = self.combo_class.get()
        if selected_class != "Select Class":
            # Fetch subjects related to the selected class from the database
            conn = mysql.connector.connect(host="localhost", user="root", password="francis121", database="report")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT subject7 FROM subject WHERE class = %s", (selected_class,))
            subjects = [subject[0] for subject in my_cursor.fetchall()]

            if subjects:
                subject_text = "\n".join(subjects)
                self.btn_subject7.config(text=subject_text)
            else:
                messagebox.showinfo("No Subjects", "No subjects available for the selected class.", parent=self.root)
        else:
            messagebox.showwarning("Warning", "Please select a class.")
    def show_subject8(self):
        selected_class = self.combo_class.get()
        if selected_class != "Select Class":
            # Fetch subjects related to the selected class from the database
            conn = mysql.connector.connect(host="localhost", user="root", password="francis121", database="report")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT subject8 FROM subject WHERE class = %s", (selected_class,))
            subjects = [subject[0] for subject in my_cursor.fetchall()]

            if subjects:
                subject_text = "\n".join(subjects)
                self.btn_subject8.config(text=subject_text)
            else:
                messagebox.showinfo("No Subjects", "No subjects available for the selected class.", parent=self.root)
        else:
            messagebox.showwarning("Warning", "Please select a class.")
    def show_subject9(self):
        selected_class = self.combo_class.get()
        if selected_class != "Select Class":
            # Fetch subjects related to the selected class from the database
            conn = mysql.connector.connect(host="localhost", user="root", password="francis121", database="report")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT subject9 FROM subject WHERE class = %s", (selected_class,))
            subjects = [subject[0] for subject in my_cursor.fetchall()]

            if subjects:
                subject_text = "\n".join(subjects)
                self.btn_subject9.config(text=subject_text)
            else:
                messagebox.showinfo("No Subjects", "No subjects available for the selected class.", parent=self.root)
        else:
            messagebox.showwarning("Warning", "Please select a class.")
    def show_subject10(self):
        selected_class = self.combo_class.get()
        if selected_class != "Select Class":
            # Fetch subjects related to the selected class from the database
            conn = mysql.connector.connect(host="localhost", user="root", password="francis121", database="report")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT subject10 FROM subject WHERE class = %s", (selected_class,))
            subjects = [subject[0] for subject in my_cursor.fetchall()]

            if subjects:
                subject_text = "\n".join(subjects)
                self.btn_subject10.config(text=subject_text)
            else:
                messagebox.showinfo("No Subjects", "No subjects available for the selected class.", parent=self.root)
        else:
            messagebox.showwarning("Warning", "Please select a class.")
    def show_subject11(self):
        selected_class = self.combo_class.get()
        if selected_class != "Select Class":
            # Fetch subjects related to the selected class from the database
            conn = mysql.connector.connect(host="localhost", user="root", password="francis121", database="report")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT subject11 FROM subject WHERE class = %s", (selected_class,))
            subjects = [subject[0] for subject in my_cursor.fetchall()]

            if subjects:
                subject_text = "\n".join(subjects)
                self.btn_subject11.config(text=subject_text)
            else:
                messagebox.showinfo("No Subjects", "No subjects available for the selected class.", parent=self.root)
        else:
            messagebox.showwarning("Warning", "Please select a class.")
    def show_subject12(self):
        selected_class = self.combo_class.get()
        if selected_class != "Select Class":
            # Fetch subjects related to the selected class from the database
            conn = mysql.connector.connect(host="localhost", user="root", password="francis121", database="report")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT subject12 FROM subject WHERE class = %s", (selected_class,))
            subjects = [subject[0] for subject in my_cursor.fetchall()]

            if subjects:
                subject_text = "\n".join(subjects)
                self.btn_subject12.config(text=subject_text)
            else:
                messagebox.showinfo("No Subjects", "No subjects available for the selected class.", parent=self.root)
        else:
            messagebox.showwarning("Warning", "Please select a class.")
    def show_subject13(self):
        selected_class = self.combo_class.get()
        if selected_class != "Select Class":
            # Fetch subjects related to the selected class from the database
            conn = mysql.connector.connect(host="localhost", user="root", password="francis121", database="report")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT subject13 FROM subject WHERE class = %s", (selected_class,))
            subjects = [subject[0] for subject in my_cursor.fetchall()]

            if subjects:
                subject_text = "\n".join(subjects)
                self.btn_subject13.config(text=subject_text)
            else:
                messagebox.showinfo("No Subjects", "No subjects available for the selected class.", parent=self.root)
        else:
            messagebox.showwarning("Warning", "Please select a class.")
    def show_subject14(self):
        selected_class = self.combo_class.get()
        if selected_class != "Select Class":
            # Fetch subjects related to the selected class from the database
            conn = mysql.connector.connect(host="localhost", user="root", password="francis121", database="report")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT subject14 FROM subject WHERE class = %s", (selected_class,))
            subjects = [subject[0] for subject in my_cursor.fetchall()]

            if subjects:
                subject_text = "\n".join(subjects)
                self.btn_subject14.config(text=subject_text)
            else:
                messagebox.showinfo("No Subjects", "No subjects available for the selected class.", parent=self.root)
        else:
            messagebox.showwarning("Warning", "Please select a class.")
    def show_subject15(self):
        selected_class = self.combo_class.get()
        if selected_class != "Select Class":
            # Fetch subjects related to the selected class from the database
            conn = mysql.connector.connect(host="localhost", user="root", password="francis121", database="report")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT subject15 FROM subject WHERE class = %s", (selected_class,))
            subjects = [subject[0] for subject in my_cursor.fetchall()]

            if subjects:
                subject_text = "\n".join(subjects)
                self.btn_subject15.config(text=subject_text)
            else:
                messagebox.showinfo("No Subjects", "No subjects available for the selected class.", parent=self.root)
        else:
            messagebox.showwarning("Warning", "Please select a class.")
    def show_subject16(self):
        selected_class = self.combo_class.get()
        if selected_class != "Select Class":
            # Fetch subjects related to the selected class from the database
            conn = mysql.connector.connect(host="localhost", user="root", password="francis121", database="report")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT subject16 FROM subject WHERE class = %s", (selected_class,))
            subjects = [subject[0] for subject in my_cursor.fetchall()]

            if subjects:
                subject_text = "\n".join(subjects)
                self.btn_subject16.config(text=subject_text)
            else:
                messagebox.showinfo("No Subjects", "No subjects available for the selected class.", parent=self.root)
        else:
            messagebox.showwarning("Warning", "Please select a class.")
                        
    #def show_loading_subject(self):
     #   self.loading_label = Label(self.root, text="Loading...", font=("times new roman", 20, "bold"))
     #   self.loading_label.pack()
     #   self.root.after(1000, self.subject_details)  # After 30 seconds, show another window
        
    #def subject_details(self):
    #    self.loading_label.destroy()
    #    self.new_window=Toplevel(self.root)
    #    self.app=MarkButton(self.new_window)

    #########################################  
    #def show_loading_term(self):
    #    self.loading_label = Label(self.root, text="Loading...", font=("times new roman", 20, "bold"))
    #    self.loading_label.pack()
    #    self.root.after(1000, self.term_details)  # After 30 seconds, show another window
        
    #def term_details(self):
    #    self.loading_label.destroy()
    #    self.new_window=Toplevel(self.root)
    #    self.app=termYear(self.new_window)
    #########################################  
    #def show_loading_year(self):
    #    self.loading_label = Label(self.root, text="Loading...", font=("times new roman", 20, "bold"))
    #    self.loading_label.pack()
    #    self.root.after(1000, self.year_details)  # After 30 seconds, show another window
    #def year_details(self):
    #    self.loading_label.destroy()
    #    self.new_window=Toplevel(self.root)
    #    self.app=Year(self.new_window)
         # Create the UI components

    #def create_widgets(self):
    #    labelframeleft = Frame(self.root)
    #    labelframeleft.place(x=20, y=100, height=200, width=250)

        # Subject display button
    #    self.btn_subject1 = Button(labelframeleft, text="", font=("times new roman", 15, "bold"), cursor="hand2")
    #    self.btn_subject1.place(x=20, y=10, height=40, width=200)

    #def update_subject_button(self, subject_text):
    #    self.btn_subject1["text"] = subject_text
       
    def logout(self):
        logout = tkinter.messagebox.askyesno("Report Management System", "Confirm if you want to log out", parent=self.root)
        if logout:
            # Perform logout actions here (e.g., closing the window, resetting variables, etc.)
            self.root.destroy()
    
root=Tk()
ob = Marks(root)
root.mainloop()