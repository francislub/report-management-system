from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter as tk
#import mysql.connector
import pymysql
import random
import tkinter.messagebox
from tkinter import messagebox

class Grade:
    def __init__(self,root):
        self.root=root
        self.root.title("Report Management System")
        self.root.geometry("1550x800+0+0")
        #self.root.overrideredirect(True)
        #========================variables=======================
        self.var_gradeID=StringVar()
        x=random.randint(1000,9999)
        self.var_gradeID.set(str(x))
        
        self.var_class=StringVar()
        self.var_mark1_1=StringVar()
        self.var_mark2_1=StringVar()
        self.var_grade1_1=StringVar()
        self.var_comm1_1=StringVar()
        self.var_mark1_2=StringVar()
        self.var_mark2_2=StringVar()
        self.var_grade1_2=StringVar()
        self.var_comm1_2=StringVar()
        self.var_mark1_3=StringVar()
        self.var_mark2_3=StringVar()
        self.var_grade1_3=StringVar()
        self.var_comm1_3=StringVar()
        self.var_mark1_4=StringVar()
        self.var_mark2_4=StringVar()
        self.var_grade1_4=StringVar()
        self.var_comm1_4=StringVar()
        self.var_mark1_5=StringVar()
        self.var_mark2_5=StringVar()
        self.var_grade1_5=StringVar()
        self.var_comm1_5=StringVar()
        self.var_mark1_6=StringVar()
        self.var_mark2_6=StringVar()
        self.var_grade1_6=StringVar()
        self.var_comm1_6=StringVar()
        self.var_mark1_7=StringVar()
        self.var_mark2_7=StringVar()
        self.var_grade1_7=StringVar()
        self.var_comm1_7=StringVar()
        self.var_mark1_8=StringVar()
        self.var_mark2_8=StringVar()
        self.var_grade1_8=StringVar()
        self.var_comm1_8=StringVar()
        self.var_mark1_9=StringVar()
        self.var_mark2_9=StringVar()
        self.var_grade1_9=StringVar()
        self.var_comm1_9=StringVar()
        self.var_mark1_10=StringVar()
        self.var_mark2_10=StringVar()
        self.var_grade1_10=StringVar()
        self.var_comm1_10=StringVar()
        self.var_mark1_11=StringVar()
        self.var_mark2_11=StringVar()
        self.var_grade1_11=StringVar()
        self.var_comm1_11=StringVar()
        
        #=====================title=======================================================
        lbl_title=Label(self.root,text="GRADE SETTINGS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1355,height=50)
        #===================2st Image===log======================================================
        Image2=Image.open(r"C:\Users\USER\Desktop\summer\PYTHON PROJECTS TKINTER\REPT\images\logo.PNG")
        Image2=Image2.resize((100,40),Image.LANCZOS)
        self.photoImage2=ImageTk.PhotoImage(Image2)
        
        lblimg=Label(self.root,image=self.photoImage2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)
        #===================labelframe====================================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Select Class",font=("times new roman",18,"bold"),padx=2)
        labelframeleft.place(x=400,y=50,width=755,height=200)
        #====================labels and entrys==================================================================================
        #===========================================================================================================================
        lbl_grade_ref=Label(labelframeleft,text="Grade ID",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_grade_ref.grid(row=0,column=0,sticky=W)
        entry_gradeID=ttk.Entry(labelframeleft,textvariable=self.var_gradeID,width=22,font=("times new roman",13,"bold"),state="readonly")
        entry_gradeID.grid(row=0,column=1)
        last_reference = self.get_last_reference()  # Function to get the last reference
        
        if last_reference is not None:
            next_reference = str(int(last_reference) + 1)
        else:
            next_reference = "1001"  # Initial reference
        
        self.var_gradeID.set(next_reference)
        #===========================================================================================================================
        #==========================Select Class ========================================
        self.var_=StringVar()
        self.conn = pymysql.connect(host="localhost",user="root",database="report")

        # Retrieve values from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT class FROM class")  # Modify with your database column and table names
        classs = [classs[0] for classs in cursor.fetchall()]

        combo_class = ttk.Combobox(labelframeleft, textvariable=self.var_class, width=20, font=("times new roman", 13, "bold"), state="readonly")
        combo_class["values"] = tuple(["Select"] + classs)
        combo_class.current(0)
        combo_class.grid(row=1, column=1)
        combo_class.bind("<<ComboboxSelected>>", self.fetch_data)
        
        classL=Label(labelframeleft,text="Class",font=("times new roman",12,"bold"),padx=2,pady=6)
        classL.grid(row=1,column=0,sticky=W)
        
        def get_selected_class():
            # Replace this function with your code to fetch the user's name from the database
            return self.var_class.get()
        # Retrieve user information from the database
        selected_cl = get_selected_class()

        # Label to display the user's name
        label_selected_class = Label(labelframeleft, text=f"SET GRADING SYSTEM FOR {selected_cl}", padx=5,font=("times new roman",16,"bold"))
        label_selected_class.place(x=0,y=100,width=600,height=20)

        # Function to update the label when the class is selected
        def update_selected_class_label():
            selected_class = get_selected_class()
            label_selected_class.config(text=f"SET GRADING SYSTEM FOR {selected_class}")

        # Bind the function to the Combobox event
        combo_class.bind("<<ComboboxSelected>>", lambda event: update_selected_class_label())
        #========================================================================================================================
        #========================================================================================================================
        
        #================btn===========================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=400,y=10,width=250,height=80)
        
        btnAdd=Button(btn_frame,text="Add", command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame,text="View",font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="Delete",font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnReset=Button(btn_frame,text="Reset",font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnReset.grid(row=1,column=0,padx=1)
        
        btnExit=Button(btn_frame,text="Exit",font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnExit.grid(row=1,column=1,padx=1)
        
        #===========================Right Frame ==================================
        labelframeright=LabelFrame(self.root,bd=2,relief=RIDGE,text="",font=("arial",12,"bold"))
        labelframeright.place(x=200,y=250,width=1020,height=430)
        #==================================================================================
        #==========================Labels =======================================
        lbl_from=Label(labelframeright,text="From",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_from.grid(row=0,column=1,sticky=W ,padx=40)
        
        lbl_to=Label(labelframeright,text="To",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_to.grid(row=0,column=3,sticky=W,padx=40)
        
        lbl_grade=Label(labelframeright,text="Grade",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_grade.grid(row=0,column=5,sticky=W ,padx=40)
        
        lbl_comment=Label(labelframeright,text="Comment",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_comment.grid(row=0,column=7,sticky=W,padx=40)
        
        #=========================Entries=====================================
        entry_mark1_1=ttk.Entry(labelframeright,textvariable=self.var_mark1_1,width=16,font=("times new roman",13,"bold"))
        entry_mark1_1.grid(row=1,column=1,padx=40,pady=5)
        
        entry_mark2_1=ttk.Entry(labelframeright,textvariable=self.var_mark2_1,width=16,font=("times new roman",13,"bold"))
        entry_mark2_1.grid(row=1,column=3,padx=40,pady=5)
        
        entry_grade1_1=ttk.Entry(labelframeright,textvariable=self.var_grade1_1,width=16,font=("times new roman",13,"bold"))
        entry_grade1_1.grid(row=1,column=5,padx=40,pady=5)
        
        entry_comm1_1=ttk.Entry(labelframeright,textvariable=self.var_comm1_1,width=16,font=("times new roman",13,"bold"))
        entry_comm1_1.grid(row=1,column=7,padx=40,pady=5)

        entry_mark1_2=ttk.Entry(labelframeright,textvariable=self.var_mark1_2,width=16,font=("times new roman",13,"bold"))
        entry_mark1_2.grid(row=2,column=1,padx=40,pady=5)
        
        entry_mark2_2=ttk.Entry(labelframeright,textvariable=self.var_mark2_2,width=16,font=("times new roman",13,"bold"))
        entry_mark2_2.grid(row=2,column=3,padx=40,pady=5)
        
        entry_grade1_2=ttk.Entry(labelframeright,textvariable=self.var_grade1_2,width=16,font=("times new roman",13,"bold"))
        entry_grade1_2.grid(row=2,column=5,padx=40,pady=5)
        
        entry_comm1_2=ttk.Entry(labelframeright,textvariable=self.var_comm1_2,width=16,font=("times new roman",13,"bold"))
        entry_comm1_2.grid(row=2,column=7,padx=40,pady=5)

        entry_mark1_3=ttk.Entry(labelframeright,textvariable=self.var_mark1_3,width=16,font=("times new roman",13,"bold"))
        entry_mark1_3.grid(row=3,column=1,padx=40,pady=5)
        
        entry_mark2_3=ttk.Entry(labelframeright,textvariable=self.var_mark2_3,width=16,font=("times new roman",13,"bold"))
        entry_mark2_3.grid(row=3,column=3,padx=40,pady=5)
        
        entry_grade1_3=ttk.Entry(labelframeright,textvariable=self.var_grade1_3,width=16,font=("times new roman",13,"bold"))
        entry_grade1_3.grid(row=3,column=5,padx=40,pady=5)
        
        entry_comm1_3=ttk.Entry(labelframeright,textvariable=self.var_comm1_3,width=16,font=("times new roman",13,"bold"))
        entry_comm1_3.grid(row=3,column=7,padx=40,pady=5)

        entry_mark1_4=ttk.Entry(labelframeright,textvariable=self.var_mark1_4,width=16,font=("times new roman",13,"bold"))
        entry_mark1_4.grid(row=4,column=1,padx=40,pady=5)
        
        entry_mark2_4=ttk.Entry(labelframeright,textvariable=self.var_mark2_4,width=16,font=("times new roman",13,"bold"))
        entry_mark2_4.grid(row=4,column=3,padx=40,pady=5)
        
        entry_grade1_4=ttk.Entry(labelframeright,textvariable=self.var_grade1_4,width=16,font=("times new roman",13,"bold"))
        entry_grade1_4.grid(row=4,column=5,padx=40,pady=5)
        
        entry_comm1_4=ttk.Entry(labelframeright,textvariable=self.var_comm1_4,width=16,font=("times new roman",13,"bold"))
        entry_comm1_4.grid(row=4,column=7,padx=40,pady=5)

        entry_mark1_5=ttk.Entry(labelframeright,textvariable=self.var_mark1_5,width=16,font=("times new roman",13,"bold"))
        entry_mark1_5.grid(row=5,column=1,padx=40,pady=5)
        
        entry_mark2_5=ttk.Entry(labelframeright,textvariable=self.var_mark2_5,width=16,font=("times new roman",13,"bold"))
        entry_mark2_5.grid(row=5,column=3,padx=40,pady=5)
        
        entry_grade1_5=ttk.Entry(labelframeright,textvariable=self.var_grade1_5,width=16,font=("times new roman",13,"bold"))
        entry_grade1_5.grid(row=5,column=5,padx=40,pady=5)
        
        entry_comm1_5=ttk.Entry(labelframeright,textvariable=self.var_comm1_5,width=16,font=("times new roman",13,"bold"))
        entry_comm1_5.grid(row=5,column=7,padx=40,pady=5)

        entry_mark1_6=ttk.Entry(labelframeright,textvariable=self.var_mark1_6,width=16,font=("times new roman",13,"bold"))
        entry_mark1_6.grid(row=6,column=1,padx=40,pady=5)
        
        entry_mark2_6=ttk.Entry(labelframeright,textvariable=self.var_mark2_6,width=16,font=("times new roman",13,"bold"))
        entry_mark2_6.grid(row=6,column=3,padx=40,pady=5)
        
        entry_grade1_6=ttk.Entry(labelframeright,textvariable=self.var_grade1_6,width=16,font=("times new roman",13,"bold"))
        entry_grade1_6.grid(row=6,column=5,padx=40,pady=5)
        
        entry_comm1_6=ttk.Entry(labelframeright,textvariable=self.var_comm1_6,width=16,font=("times new roman",13,"bold"))
        entry_comm1_6.grid(row=6,column=7,padx=40,pady=5)

        entry_mark1_7=ttk.Entry(labelframeright,textvariable=self.var_mark1_7,width=16,font=("times new roman",13,"bold"))
        entry_mark1_7.grid(row=7,column=1,padx=40,pady=5)
        
        entry_mark2_7=ttk.Entry(labelframeright,textvariable=self.var_mark2_7,width=16,font=("times new roman",13,"bold"))
        entry_mark2_7.grid(row=7,column=3,padx=40,pady=5)
        
        entry_grade1_7=ttk.Entry(labelframeright,textvariable=self.var_grade1_7,width=16,font=("times new roman",13,"bold"))
        entry_grade1_7.grid(row=7,column=5,padx=40,pady=5)
        
        entry_comm1_7=ttk.Entry(labelframeright,textvariable=self.var_comm1_7,width=16,font=("times new roman",13,"bold"))
        entry_comm1_7.grid(row=7,column=7,padx=40,pady=5)

        entry_mark1_8=ttk.Entry(labelframeright,textvariable=self.var_mark1_8,width=16,font=("times new roman",13,"bold"))
        entry_mark1_8.grid(row=8,column=1,padx=40,pady=5)
        
        entry_mark2_8=ttk.Entry(labelframeright,textvariable=self.var_mark2_8,width=16,font=("times new roman",13,"bold"))
        entry_mark2_8.grid(row=8,column=3,padx=40,pady=5)
        
        entry_grade1_8=ttk.Entry(labelframeright,textvariable=self.var_grade1_8,width=16,font=("times new roman",13,"bold"))
        entry_grade1_8.grid(row=8,column=5,padx=40,pady=5)
        
        entry_comm1_8=ttk.Entry(labelframeright,textvariable=self.var_comm1_8,width=16,font=("times new roman",13,"bold"))
        entry_comm1_8.grid(row=8,column=7,padx=40,pady=5)

        entry_mark1_9=ttk.Entry(labelframeright,textvariable=self.var_mark1_9,width=16,font=("times new roman",13,"bold"))
        entry_mark1_9.grid(row=9,column=1,padx=40,pady=5)
        
        entry_mark2_9=ttk.Entry(labelframeright,textvariable=self.var_mark2_9,width=16,font=("times new roman",13,"bold"))
        entry_mark2_9.grid(row=9,column=3,padx=40,pady=5)
        
        entry_grade1_9=ttk.Entry(labelframeright,textvariable=self.var_grade1_9,width=16,font=("times new roman",13,"bold"))
        entry_grade1_9.grid(row=9,column=5,padx=40,pady=5)
        
        entry_comm1_9=ttk.Entry(labelframeright,textvariable=self.var_comm1_9,width=16,font=("times new roman",13,"bold"))
        entry_comm1_9.grid(row=9,column=7,padx=40,pady=5)

        entry_mark1_10=ttk.Entry(labelframeright,textvariable=self.var_mark1_10,width=16,font=("times new roman",13,"bold"))
        entry_mark1_10.grid(row=10,column=1,padx=40,pady=5)
        
        entry_mark2_10=ttk.Entry(labelframeright,textvariable=self.var_mark2_10,width=16,font=("times new roman",13,"bold"))
        entry_mark2_10.grid(row=10,column=3,padx=40,pady=5)
        
        entry_grade1_10=ttk.Entry(labelframeright,textvariable=self.var_grade1_10,width=16,font=("times new roman",13,"bold"))
        entry_grade1_10.grid(row=10,column=5,padx=40,pady=5)
        
        entry_comm1_10=ttk.Entry(labelframeright,textvariable=self.var_comm1_10,width=16,font=("times new roman",13,"bold"))
        entry_comm1_10.grid(row=10,column=7,padx=40,pady=5)
        
        entry_mark1_11=ttk.Entry(labelframeright,textvariable=self.var_mark1_11,width=16,font=("times new roman",13,"bold"))
        entry_mark1_11.grid(row=11,column=1,padx=40,pady=5)
        
        entry_mark2_11=ttk.Entry(labelframeright,textvariable=self.var_mark1_11,width=16,font=("times new roman",13,"bold"))
        entry_mark2_11.grid(row=11,column=3,padx=40,pady=5)
        
        entry_grade1_11=ttk.Entry(labelframeright,textvariable=self.var_grade1_11,width=16,font=("times new roman",13,"bold"))
        entry_grade1_11.grid(row=11, column=5, padx=40, pady=5)
        
        entry_comm1_11=ttk.Entry(labelframeright,textvariable=self.var_comm1_11,width=16,font=("times new roman",13,"bold"))
        entry_comm1_11.grid(row=11,column=7,padx=40,pady=5)

        
        #========================================================================================
    def add_data(self):
        if self.var_class.get() == "Select":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", database="report")
                my_cursor = conn.cursor()

                # Use the last reference to generate the next gradeID
                last_reference = self.get_last_reference()
                next_reference = str(int(last_reference) + 1) if last_reference else "1001"
                self.var_gradeID.set(next_reference)

                # Check if gradeID already exists
                my_cursor.execute("SELECT * FROM grade WHERE gradeID = %s", (self.var_gradeID.get(),))
                existing_record = my_cursor.fetchone()

                # Define the values for the query
                values = (
                    self.var_gradeID.get(),
                    self.var_class.get(),
                    self.var_mark1_1.get(), self.var_mark2_1.get(), self.var_grade1_1.get(), self.var_comm1_1.get(),
                    self.var_mark1_2.get(), self.var_mark2_2.get(), self.var_grade1_2.get(), self.var_comm1_2.get(),
                    self.var_mark1_3.get(), self.var_mark2_3.get(), self.var_grade1_3.get(), self.var_comm1_3.get(),
                    self.var_mark1_4.get(), self.var_mark2_4.get(), self.var_grade1_4.get(), self.var_comm1_4.get(),
                    self.var_mark1_5.get(), self.var_mark2_5.get(), self.var_grade1_5.get(), self.var_comm1_5.get(),
                    self.var_mark1_6.get(), self.var_mark2_6.get(), self.var_grade1_6.get(), self.var_comm1_6.get(),
                    self.var_mark1_7.get(), self.var_mark2_7.get(), self.var_grade1_7.get(), self.var_comm1_7.get(),
                    self.var_mark1_8.get(), self.var_mark2_8.get(), self.var_grade1_8.get(), self.var_comm1_8.get(),
                    self.var_mark1_9.get(), self.var_mark2_9.get(), self.var_grade1_9.get(), self.var_comm1_9.get(),
                    self.var_mark1_10.get(), self.var_mark2_10.get(), self.var_grade1_10.get(), self.var_comm1_10.get(),
                    self.var_mark1_11.get(), self.var_mark2_11.get(), self.var_grade1_11.get(), self.var_comm1_11.get()
                )

                if existing_record:
                    # Update the existing record
                    my_cursor.execute("""
                        UPDATE grade SET
                        class = %s,
                        mark1 = %s, mark1_1 = %s, grade1 = %s, comment1 = %s,
                        mark2 = %s, mark2_2 = %s, grade2 = %s, comment2 = %s,
                        mark3 = %s, mark3_3 = %s, grade3 = %s, comment3 = %s,
                        mark4 = %s, mark4_4 = %s, grade4 = %s, comment4 = %s,
                        mark5 = %s, mark5_5 = %s, grade5 = %s, comment5 = %s,
                        mark6 = %s, mark6_6 = %s, grade6 = %s, comment6 = %s,
                        mark7 = %s, mark7_7 = %s, grade7 = %s, comment7 = %s,
                        mark8 = %s, mark8_8 = %s, grade8 = %s, comment8 = %s,
                        mark9 = %s, mark9_9 = %s, grade9 = %s, comment9 = %s,
                        mark10 = %s, mark10_10 = %s, grade10 = %s, comment10 = %s,
                        mark11 = %s, mark11_11 = %s, grade11 = %s, comment11 = %s
                        WHERE gradeID = %s
                    """, values)
                else:
                    # Insert a new record
                    my_cursor.execute("""
                    INSERT INTO grade (gradeID, class, mark1, mark1_1, grade1, comment1, mark2, mark2_2, grade2, comment2,
                                    mark3, mark3_3, grade3, comment3, mark4, mark4_4, grade4, comment4, mark5, mark5_5,
                                    grade5, comment5, mark6, mark6_6, grade6, comment6, mark7, mark7_7, grade7, comment7,
                                    mark8, mark8_8, grade8, comment8, mark9, mark9_9, grade9, comment9, mark10, mark10_10,
                                    grade10, comment10, mark11, mark11_11, grade11, comment11)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, values)

                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Grade has been added/updated successfully", parent=self.root)

            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
    
    def fetch_data(self):
        conn = pymysql.connect(host="localhost", user="root", database="report")
        my_cursor = conn.cursor()

        # Fetch data for the selected class
        class_selected = self.var_class.get()
        my_cursor.execute("SELECT * FROM grade WHERE class = %s", (class_selected,))
        rows = my_cursor.fetchall()

        # Display data in textboxes
        if rows:
            row = rows[0]  # Assuming only one record for a class for simplicity
            self.var_gradeID.set(row[0])
            self.var_class.set(row[1])
            self.var_mark1_1.set(row[2])
            self.var_mark2_1.set(row[3])
            self.var_grade1_1.set(row[4])
            self.var_comm1_1.set(row[5])
            self.var_mark1_2.set(row[6])
            self.var_mark2_2.set(row[7])
            self.var_grade1_2.set(row[8])
            self.var_comm1_2.set(row[9])
            self.var_mark1_3.set(row[10])
            self.var_mark2_3.set(row[11])
            self.var_grade1_3.set(row[12])
            self.var_comm1_3.set(row[13])
            self.var_mark1_4.set(row[14])
            self.var_mark2_4.set(row[15])
            self.var_grade1_4.set(row[16])
            self.var_comm1_4.set(row[17])
            self.var_mark1_5.set(row[18])
            self.var_mark2_5.set(row[19])
            self.var_grade1_5.set(row[20])
            self.var_comm1_5.set(row[21])
            self.var_mark1_6.set(row[22])
            self.var_mark2_6.set(row[23])
            self.var_grade1_6.set(row[24])
            self.var_comm1_6.set(row[25])
            self.var_mark1_7.set(row[26])
            self.var_mark2_7.set(row[27])
            self.var_grade1_7.set(row[28])
            self.var_comm1_7.set(row[29])
            self.var_mark1_8.set(row[30])
            self.var_mark2_8.set(row[31])
            self.var_grade1_8.set(row[32])
            self.var_comm1_8.set(row[33])
            self.var_mark1_9.set(row[34])
            self.var_mark2_9.set(row[35])
            self.var_grade1_9.set(row[36])
            self.var_comm1_9.set(row[37])
            self.var_mark1_10.set(row[38])
            self.var_mark2_10.set(row[39])
            self.var_grade1_10.set(row[40])
            self.var_comm1_10.set(row[41])
            self.var_mark1_11.set(row[42])
            self.var_mark2_11.set(row[43])
            self.var_grade1_11.set(row[44])
            self.var_comm1_11.set(row[45])

        conn.close()

    
    def get_selected_class(self):
        try:
            conn = pymysql.connect(host="localhost", user="root", database="report")
            my_cursor = conn.cursor()

            # Fetch data for the selected class
            class_selected = self.var_class.get()
            my_cursor.execute("SELECT * FROM grade WHERE class = %s", (class_selected,))
            row = my_cursor.fetchone()

            conn.close()

            return row  # Returns a tuple containing the grade information for the selected class

        except Exception as e:
            messagebox.showwarning("Warning", f"Error fetching data: {str(e)}", parent=self.root)
            return None
    
    def get_last_reference(self):
        try:
            conn = pymysql.connect(host="localhost", user="root", database="report")
            cursor = conn.cursor()

            # Execute a query to get the maximum gradeID value from the database
            cursor.execute("SELECT MAX(gradeID) FROM grade")  # Replace with your actual table name
            result = cursor.fetchone()

            # Close the database connection
            conn.close()

            # If there are no existing gradeIDs, return None
            if result[0] is not None:
                return str(result[0])
            else:
                return None

        except Exception as e:
            print(f"Error: {e}")
            return None
        
    def Delete(self):
       Delete=messagebox.askyesno("Report Management System","Do you want to delete this class details",parent=self.root)
       if Delete>0:
           conn=pymysql.connect(host="localhost",user="root",database="report")
           my_cursor=conn.cursor()
           query="delete from subject where subjectID=%s"
           value=(self.var_subjectID.get(),)
           my_cursor.execute(query,value)
       else:
           if not Delete:
               return
       conn.commit()
       self.fetch_data()
       conn.close()
       self.reset()
    
    def Exit(self):
           self.Exit= tkinter.messagebox.askyesno("Report Management System","confirm if you want to exit",parent=self.root)
           if self.Exit>0:
               self.root.destroy()
               return

                    
if __name__=="__main__":
    root=Tk()
    obj=Grade(root)
    root.mainloop()