from tkinter import *
import tkinter as tk
import tkinter.messagebox
from PIL import Image,ImageTk
#import mysql.connector
import pymysql
import random
from time import strftime
from teacher import Teacher_win
from teacherDash import Teacher
import colorsys
from classL import cL
from subject import Subject
from grade import Grade 
from remarks import remark
from itertools import cycle
#=====================Graph===============
from tkinter import Frame, RIDGE
import matplotlib.pyplot as plt
import numpy as np
#import os
#os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
#import matplotlib
#matplotlib.rcParams['font.sans-serif'] = 'Arial'
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1450x730+0+0")
        self.root.overrideredirect(True)
        self.root.title('Color Changer') 
        # Other initialization code...
        self.classes = []  # List to store available classes
        self.current_class_index = 0

        # Fetch available classes from the database
        self.fetch_classes()
        self.selected_class = None
        self.current_class = 1

        # Set initial class for display
        self.selected_class = self.classes[self.current_class_index]
        self.display_graph()
        
        #List of colors
        colors = ["#000000","#000426","#000848","#000C6A","#00108C","#0014AE","#0018D0"]
        #colors = ["#010c48","#ff5733", "#33ff57", "#3357ff", "#ff33a6", "#a633ff"]

        # Function to change the background color
        def change_color():
            color = random.choice(colors)  # Select a random color from the list
            self.root.configure(bg=color)  # Change the background color of the window
            self.root.after(10000, change_color)  # Call the change_color function after 300000ms (5 minutes)

        # Call the change_color function to start changing the color
        change_color()
        self.root .title("Report Management System | Developed by LarksTeckHub")
        
        
        #====================title================
        self.icon_title = PhotoImage(file="images/logo.png")
        desired_width = 100
        desired_height = 50
        self.icon_title = self.icon_title.subsample(int(self.icon_title.width() / desired_width), int(self.icon_title.height() / desired_height)) 
        title= Label(self.root, text="DIRECTOR OF STUDIES DASHBOARD",image=self.icon_title,compound=LEFT, font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
        #============btn_logout=====
        btn_history = Button(self.root,text="History",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)
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
        
        #btn_termYear = Button(LeftMenu,text="Term & Year",command=self.term_details,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",16,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
                ################## Class####################################################
        btn_class = Button(LeftMenu,text="Add Class",command=self.show_loading_class,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",16,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        btn_subject = Button(LeftMenu,text="Subject",command=self.show_loading_subject,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",16,"bold"),bg="white",bd=3,cursor="hand2")
        btn_subject.pack(side=TOP,fill=X)
        
        btn_reportgrade = Button(LeftMenu,text="Grading",command=self.show_loading_grade,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",16,"bold"),bg="white",bd=3,cursor="hand2")
        btn_reportgrade.pack(side=TOP,fill=X)
        
        btn_reportRemarks = Button(LeftMenu,text="Report Remarks",command=self.show_loading_remark,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",13,"bold"),bg="white",bd=3,cursor="hand2")
        btn_reportRemarks.pack(side=TOP,fill=X)
        
        #==================================
        btn_reportGeneration = Button(LeftMenu,text="Report Generation",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",14,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_teachDash = Button(LeftMenu,text="Teacher's Dash",command=self.show_loading_teacher,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",16,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
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
        #========footer================
        
        lbl_footer = Label(self.root,text="Report Management System | Developed by LarksTeckHub \nFor any Technical Issue Contact: 0741789121",font=("times new roman",12),bg="#4d636d",fg="white").pack(side=BOTTOM, fill=X)
   
        #===============content==================
        ###############################################################
        # Display total students
        self.lbl_student = Label(self.root, text="", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_student.place(x=250, y=120, height=100, width=200)
        
        # Connect to the MySQL database
        self.mydb = pymysql.connect(host="localhost", user="root", database="report")

        # Create a cursor object to execute SQL queries
        self.mycursor = self.mydb.cursor()

        # Initialize the slide index
        self.slide_index = 0

        # Schedule the slide show
        self.update_slideshowStudent()

    def update_slideshowStudent(self):
        # Execute queries to get relevant information
        queries = [
            "SELECT COUNT(*) FROM student",
            "SELECT COUNT(*) FROM student WHERE gender = 'Female'",
            "SELECT COUNT(*) FROM student WHERE gender = 'Male'",
            "SELECT class, COUNT(*) FROM student GROUP BY class"
        ]

        self.mycursor.execute(queries[self.slide_index])

        if self.slide_index == 0:
            result = self.mycursor.fetchone()
            total_students = result[0]
            self.lbl_student.config(text=f"Total Students\n{total_students}")

        elif self.slide_index == 1:
            result = self.mycursor.fetchone()
            total_girls = result[0]
            self.lbl_student.config(text=f"Total Girls\n{total_girls}")

        elif self.slide_index == 2:
            result = self.mycursor.fetchone()
            total_boys = result[0]
            self.lbl_student.config(text=f"Total Boys\n{total_boys}")

        elif self.slide_index == 3:
            results = self.mycursor.fetchall()
            class_info = "\n".join([f"{row[0]}: {row[1]}" for row in results])
            self.lbl_student.config(text=f"Total Students in Each Class\n{class_info}")

        # Increment the slide index
        self.slide_index = (self.slide_index + 1) % 4

        # Schedule the next update after 3000 milliseconds (3 seconds)
        self.root.after(3000, self.update_slideshowStudent)
        ##################################################### START ######################
               # Connect to the MySQL database
        mydb = pymysql.connect(host="localhost",user="root",database="report")

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # Execute an SQL query to get the total number of stuff
        mycursor.execute("SELECT COUNT(*) FROM teacher")

        # Fetch the result of the query
        result = mycursor.fetchone()

        # Get the total number of stuff from the result
        total_stuff = result[0]
        ###################################################################===================
    
        # Display the total number of stuff
        self.lbl_stuff = Label(self.root, text=f"Total Stuff\n{total_stuff}", bd=5, relief=RIDGE, bg="#ff5722", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_stuff.place(x=450, y=120, height=100, width=200)
        # Connect to the MySQL database
        #self.mydb = mysql.connector.connect(host="localhost", user="root", password="francis121", database="report")

        # Create a cursor object to execute SQL queries
        #self.mycursor = self.mydb.cursor()

        # Create labels to display total information
        #self.labels = [
        #    Label(self.root, bd=5, relief=RIDGE, bg="#ff5722", fg="white", font=("goudy old style", 20, "bold"))
        #    for _ in range(3)
        #]

        # Display the labels
        #for idx, label in enumerate(self.labels):
        #    label.place(x=450, y=120, height=100, width=200)

        # Create a slideshow iterator
        #self.slide_show = cycle(self.update_labels)
        #self.root.after(0, self.update_slideshow)

    #def execute_query(self, query):
    #    self.mycursor.execute(query)
    #    result = self.mycursor.fetchone()
    #    return result[0]

    #def update_labels(self):
        # Execute SQL queries to get total count for different categories
    #    total_stuff = self.execute_query("SELECT COUNT(*) FROM teacher")
    #    total_males = self.execute_query("SELECT COUNT(*) FROM teacher WHERE gender = 'Male'")
    #    total_females = self.execute_query("SELECT COUNT(*) FROM teacher WHERE gender = 'Female'")

        # Display the total information on labels
    #    self.labels[0]['text'] = f"Total Stuff\n{total_stuff}"
    #    self.labels[1]['text'] = f"Total Males\n{total_males}"
    #    self.labels[2]['text'] = f"Total Females\n{total_females}"

    #def update_slideshow(self):
        # Update labels with the next set of information
    #    next_slide = next(self.slide_show)
    #    next_slide()

        # Schedule the next update after 10 seconds
    #    self.root.after(10000, self.update_slideshow)
        ##################################################################===================================
        # Connect to the MySQL database
        mydb = pymysql.connect(host="localhost",user="root",database="report")

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
        mydb = pymysql.connect(host="localhost",user="root",database="report")

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
       # Connect to the MySQL database
        mydb = pymysql.connect(host="localhost",user="root",database="report")

        # Create a cursor object to execute SQL queries
        mycursor = mydb.cursor()

        # Execute an SQL query to get the total number of user
        mycursor.execute("SELECT COUNT(*) FROM user")

        # Fetch the result of the query
        result = mycursor.fetchone()

        # Get the total number of user from the result
        total_term = result[0]

        # Display the total number of user
        self.lbl_sales = Label(self.root, text=f"Total Users\n{total_term}", bd=5, relief=RIDGE, bg="#ffc107", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=1050, y=120, height=100, width=200)
        #######################################################################################################################
        #===========Graph Menu==============
        self.GraphMenu1 = Frame(self.root,bd=2,relief=RIDGE, bg="white")
        self.GraphMenu1.place(x=390,y=230,width=965,height=455)
        
        # Add class navigation buttons
        self.next_button = Button(self.GraphMenu1, text="Next", command=self.next_class, font=("arial", 11, "bold"), bg="black", fg="gold", width=12)
        self.next_button.place(x=890,y=5,width=50,height=25)

        self.prev_button = Button(self.GraphMenu1, text="Previous", command=self.previous_class, font=("arial", 11, "bold"), bg="black", fg="gold", width=12)
        self.prev_button.place(x=10,y=5,width=70,height=25)
        
        self.title = Label(self.GraphMenu1, text=f'PERFORMANCE FOR {self.selected_class}', font=("goudy old style", 20, "bold"))
        self.title.place(x=300, y=5, height=25)
        
        #############################################################################################################
        self.GraphMenu = Frame(self.GraphMenu1,bd=1,relief=RIDGE, bg="white")
        self.GraphMenu.place(x=0,y=30,width=960,height=424)
        # Display the initial graph
        self.display_graph()

    
    def display_graph(self):
    
        # Clear the GraphMenu frame before displaying the graph
        if hasattr(self, 'GraphMenu'):
            for widget in self.GraphMenu.winfo_children():
                widget.destroy()

            # Create a Matplotlib figure
            fig ,ax = plt.subplots(figsize=(8,4))
            
            conn = pymysql.connect(host="localhost", user="root", database="report")
            my_cursor = conn.cursor()
            
            # Fetch subjects for the selected class
            subjects_query = f"SELECT subject1, subject2, subject3, subject4, subject5, subject6, subject7, subject8, subject9, subject10, subject11, subject12, subject13, subject14, subject15, subject16 FROM subject WHERE class='{self.selected_class}'"
            my_cursor.execute(subjects_query)
            subjects_result = my_cursor.fetchone()

            # Filter out null or empty and non-existing subjects
            filtered_subjects = [subject for subject in subjects_result if subject != ""]

            # Create concatenated string without null or empty subjects
            subjects = ','.join(filtered_subjects)

            # Bar width for better visualization
            bar_width = 100
            index = np.arange(len(filtered_subjects))
            
            fig, ax = plt.subplots()
            # Plotting the bar graph for girls
            ax.bar(index, np.random.randint(50, 100), label='Girls',edgecolor='grey', color='pink')  # Replace with your data

            # Plotting the bar graph for boys
            ax.bar(index + bar_width, np.random.randint(60, 100), label='Boys',edgecolor='grey', color='blue')  # Replace with your data

            # Set labels and title
            ax.set_xlabel("SUBJECTS")
            ax.set_ylabel("TOTAL SCORE")
            ax.set_xticks(index + bar_width / 2)
            ax.set_xticklabels([subj[:4] for subj in filtered_subjects])
            ax.legend()

            # Embed the Matplotlib figure in the Tkinter window
            canvas = FigureCanvasTkAgg(fig, master=self.GraphMenu)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            canvas.draw()
            plt.close()
            
            #######################################################################################################################
        
    def fetch_classes(self):
        # Fetch available classes from the database
        conn = pymysql.connect(host="localhost", user="root", database="report")
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT class FROM subject")  
        self.classes = [cls[0] for cls in cursor.fetchall()]

    def next_class(self):
        # Update to the next class in the list
        self.current_class_index = (self.current_class_index + 1) % len(self.classes)
        self.selected_class = self.classes[self.current_class_index]
        self.current_class += 1
        self.display_graph()

    def previous_class(self):
        # Update to the previous class in the list
        self.current_class_index = (self.current_class_index - 1) % len(self.classes)
        self.selected_class = self.classes[self.current_class_index]
        if self.current_class > 1:
            self.current_class -= 1
            self.display_graph()

        #########################################  
    def show_loading_message(self):
        self.loading_label = Label(self.root, text="Loading...", font=("times new roman", 20, "bold"))
        self.loading_label.pack()
        self.root.after(1000, self.cust_details)  # After 30 seconds, show another window
        
    def cust_details(self):
        self.loading_label.destroy()
        self.new_window=Toplevel(self.root)
        self.app=Teacher_win(self.new_window)
    
    #########################################  
    def show_loading_class(self):
        self.loading_label = Label(self.root, text="Loading...", font=("times new roman", 20, "bold"))
        self.loading_label.pack()
        self.root.after(1000, self.class_details)  # After 30 seconds, show another window
        
    def class_details(self):
        self.loading_label.destroy()
        self.new_window=Toplevel(self.root)
        self.app=cL(self.new_window)
        
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
    def show_loading_grade(self):
        self.loading_label = Label(self.root, text="Loading...", font=("times new roman", 20, "bold"))
        self.loading_label.pack()
        self.root.after(1000, self.grade_details)  # After 30 seconds, show another window
    def grade_details(self):
        self.loading_label.destroy()
        self.new_window=Toplevel(self.root)
        self.app=Grade(self.new_window)

        
    #########################################  
    def show_loading_remark(self):
        self.loading_label = Label(self.root, text="Loading...", font=("times new roman", 20, "bold"))
        self.loading_label.pack()
        self.root.after(1000, self.remark_details)  # After 30 seconds, show another window
    def remark_details(self):
        self.loading_label.destroy()
        self.new_window=Toplevel(self.root)
        self.app=remark(self.new_window)
        
    #########################################  
    #########################################  
    def show_loading_teacher(self):
        self.loading_label = Label(self.root, text="Loading...", font=("times new roman", 20, "bold"))
        self.loading_label.pack()
        self.root.after(1000, self.teacher_details)  # After 30 seconds, show another window
    def teacher_details(self):
        self.loading_label.destroy()
        self.new_window=Toplevel(self.root)
        self.app=Teacher(self.new_window)
        
    def logout(self):
        logout = tkinter.messagebox.askyesno("Report Management System", "Confirm if you want to log out", parent=self.root)
        if logout:
            # Perform logout actions here (e.g., closing the window, resetting variables, etc.)
            self.root.destroy()
    
if __name__=="__main__":
    root=Tk()
    ob = IMS(root)
    root.mainloop()
