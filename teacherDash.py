from tkinter import *
import tkinter.messagebox
import mysql.connector
import random
from time import strftime
from PIL import Image,ImageTk

class Teacher:
    def __init__(self,root):
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
        title= Label(self.root, text="TEACHERS AND SECRETORY DASHBOARD",image=self.icon_title,compound=LEFT, font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        #============btn_logout=====
        #btn_history = Button(self.root,text="History",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)
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
        
        #===========Left Menu==============
        LeftMenu = Frame(self.root,bd=2,relief=RIDGE, bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=600)
        
                # Assuming functions to retrieve user information from the database
        def get_user_name():
            # Replace this function with your code to fetch the user's name from the database
            return "Francis"  # Example user name

        def get_user_role():
            # Replace this function with your code to fetch the user's role from the database
            return "DOS"  # Example user role

        # Placeholder for user's photo (Assumed as a box)
        user_photo_placeholder = Label(LeftMenu, text="User Photo", bg="lightgray", height=10)
        user_photo_placeholder.pack(side="top", fill="x")

        # Retrieve user information from the database
        user_name = get_user_name()
        user_role = get_user_role()

        # Label to display the user's name
        label_user_name = Label(LeftMenu, text=f"User: {user_name}",bg="#4d636d", padx=5,font=("times new roman",16,"bold"))
        label_user_name.pack(side="top", fill="x")

        # Label to display the user's role
        label_user_role = Label(LeftMenu, text=f"Role: {user_role}",bg="#4d636d", padx=5,font=("times new roman",16,"bold"))
        label_user_role.pack(side="top", fill="x")
        
        ########################Buttons#############################################
        self.icon_side = PhotoImage(file="images/side.png")
        new_width, new_height = 25, 25  # Set the new dimensions
        self.icon_side = self.icon_side.subsample(self.icon_side.width()// new_width, self.icon_side.height() // new_height)
        
        #=========================BUTTONS===============================================
        btn_students = Button(LeftMenu,text="Students",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",16,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_marks = Button(LeftMenu,text="Marks Entry",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",16,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_viewStud = Button(LeftMenu,text="View Students",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",13,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_reportGeneration = Button(LeftMenu,text="",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",14,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_reportGenerat = Button(LeftMenu,text="",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",14,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_reportGenerat = Button(LeftMenu,text="",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",14,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        ################## SETTINGS####################################################
        # Create a Menu for Settings dropdown
        self.settings_menu = Menu(root, tearoff=0)
        self.settings_menu.configure(font=("times new roman", 16, "bold"))  # Apply the same font as the Settings button
        self.settings_menu.add_command(label="Reset Password", font=("times new roman", 16, "bold"))  # Apply font to dropdown items
        self.settings_menu.add_command(label="Edit Profile", font=("times new roman", 16, "bold"))  # Apply font to dropdown items
        
        # Function to display the Settings dropdown
        def show_settings_menu():
            x = btn_settings.winfo_rootx() + btn_settings.winfo_width()  # Adjust x-coordinate to place the menu on the right
            y = btn_settings.winfo_rooty() + btn_settings.winfo_height()
            self.settings_menu.post(x, y)
        # Settings Button with dropdown
        btn_settings = Button(LeftMenu, text="Settings", image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 16, "bold"), bg="white", bd=3, cursor="hand2", command=show_settings_menu)
        btn_settings.pack(side=TOP, fill=X) 

        # Attach the dropdown menu to the Settings button
        #btn_settings['menu'] = self.settings_menu 
         
        btn_logout = Button(LeftMenu,text="Logout",command=self.logout,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",16,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        #===============content==================
        self.lbl_student=Label(self.root,text="Total Students\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_student.place(x=250,y=120,height=100,width=200)
        
        #####################################################
        # Connect to the MySQL database
        mydb = mysql.connector.connect(host="localhost",user="root",password="francis121",database="report")

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # Execute an SQL query to get the total number of stuff
        mycursor.execute("SELECT COUNT(*) FROM teacher")

        # Fetch the result of the query
        result = mycursor.fetchone()

        # Get the total number of stuff from the result
        total_stuff = result[0]

        # Display the total number of stuff
        self.lbl_stuff = Label(self.root, text=f"Total Stuff\n{total_stuff}", bd=5, relief=RIDGE, bg="#ff5722", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_stuff.place(x=450, y=120, height=100, width=200)
        ##################################################################
        # Connect to the MySQL database
        mydb = mysql.connector.connect(host="localhost",user="root",password="francis121",database="report")

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # Execute an SQL query to get the total number of stuff
        mycursor.execute("SELECT COUNT(*) FROM subject")

        # Fetch the result of the query
        result = mycursor.fetchone()

        # Get the total number of stuff from the result
        total_subject = result[0]

        # Display the total number of stuff
        self.lbl_subject = Label(self.root, text=f"Total Subject\n{total_subject}", bd=5, relief=RIDGE, bg="#009688", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_subject.place(x=650, y=120, height=100, width=200)
        #################################################################
       # Connect to the MySQL database
        mydb = mysql.connector.connect(host="localhost",user="root",password="francis121",database="report")

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # Execute an SQL query to get the total number of stuff
        mycursor.execute("SELECT COUNT(*) FROM term")

        # Fetch the result of the query
        result = mycursor.fetchone()

        # Get the total number of term from the result
        total_term = result[0]

        # Display the total number of term
        self.lbl_term = Label(self.root, text=f"Total Term\n{total_term}", bd=5, relief=RIDGE, bg="#607d8b", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_term.place(x=850, y=120, height=100, width=200)
       #########################################################
       
        self.lbl_sales=Label(self.root,text="Total User\n[0]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=1050,y=120,height=100,width=200)
       
       
        #========footer================
        lbl_footer = Label(self.root,text="Report Management System | Developed by LarksTeckHub \nFor any Technical Issue Contact: 0741789121",font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM, fill=X)
   
    def logout(self):
        logout = tkinter.messagebox.askyesno("Report Management System", "Confirm if you want to log out", parent=self.root)
        if logout:
            # Perform logout actions here (e.g., closing the window, resetting variables, etc.)
            self.root.destroy()
    
root=Tk()
ob = Teacher(root)
root.mainloop()
