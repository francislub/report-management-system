from tkinter import*
from PIL import Image,ImageTk
from tkcalendar import DateEntry
from datetime import datetime
from tkinter import ttk
import tkinter as tk
#import mysql.connector
import pymysql
import random
import tkinter.messagebox
from tkinter import messagebox

class remark:
    def __init__(self,root):
        self.root=root
        self.root.title("Report Management System")
        self.root.geometry("1550x800+0+0")
        self.root.overrideredirect(True)
        #========================variables=======================
        self.var_gradeID=StringVar()
        x=random.randint(1000,9999)
        self.var_gradeID.set(str(x))
        
        self.var_class=StringVar()
        self.var_termbegins=StringVar()
        self.var_termends=StringVar()
        self.var_mark1_1=StringVar()
        self.var_mark2_1=StringVar()
        self.var_tcomm1=StringVar()
        self.var_hcomm1=StringVar()
        self.var_mark1_2=StringVar()
        self.var_mark2_2=StringVar()
        self.var_tcomm2=StringVar()
        self.var_hcomm2=StringVar()
        self.var_mark1_3=StringVar()
        self.var_mark2_3=StringVar()
        self.var_tcomm3=StringVar()
        self.var_hcomm3=StringVar()
        self.var_mark1_4=StringVar()
        self.var_mark2_4=StringVar()
        self.var_tcomm4=StringVar()
        self.var_hcomm4=StringVar()
        self.var_mark1_5=StringVar()
        self.var_mark2_5=StringVar()
        self.var_tcomm5=StringVar()
        self.var_hcomm5=StringVar()
        self.var_mark1_6=StringVar()
        self.var_mark2_6=StringVar()
        self.var_tcomm6=StringVar()
        self.var_hcomm6=StringVar()
        self.var_mark1_7=StringVar()
        self.var_mark2_7=StringVar()
        self.var_tcomm7=StringVar()
        self.var_hcomm7=StringVar()
        self.var_mark1_8=StringVar()
        self.var_mark2_8=StringVar()
        self.var_tcomm8=StringVar()
        self.var_hcomm8=StringVar()
        self.var_mark1_9=StringVar()
        self.var_mark2_9=StringVar()
        self.var_tcomm9=StringVar()
        self.var_hcomm9=StringVar()
        self.var_mark1_10=StringVar()
        self.var_mark2_10=StringVar()
        self.var_tcomm10=StringVar()
        self.var_hcomm10=StringVar()
        
        #=====================title=======================================================
        lbl_title=Label(self.root,text="REPORT REMARK'S FOR BOTH O AND A'LEVEL",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1355,height=50)
        #===================2st Image===log======================================================
        Image2=Image.open(r"C:\Users\ENG. FRANCIS\Desktop\summer\PYTHON PROJECTS TKINTER\REPT\images\logo.PNG")
        Image2=Image2.resize((100,40),Image.LANCZOS)
        self.photoImage2=ImageTk.PhotoImage(Image2)
        
        lblimg=Label(self.root,image=self.photoImage2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)
        #===================labelframe====================================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Select Class",font=("times new roman",18,"bold"),padx=2)
        labelframeleft.place(x=400,y=50,width=755,height=120)
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
        combo_class.bind("<<ComboboxSelected>>", self.update_txtclass)
        
        classL=Label(labelframeleft,text="Class",font=("times new roman",12,"bold"),padx=2,pady=6)
        classL.grid(row=1,column=0,sticky=W)
        
        def get_selected_class():
            # Replace this function with your code to fetch the user's name from the database
            return self.var_class.get()
        
        #========================================================================================================================
        #========================================================================================================================
        
        #================btn===========================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=400,y=10,width=250,height=80)
        
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)
        
        viewgrade=Button(btn_frame,text="View Comments",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=12)
        viewgrade.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.delete_data,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnReset=Button(btn_frame,text="Reset",command=self.fetch_data1,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnReset.grid(row=1,column=0,padx=1)
        
        btnExit=Button(btn_frame,text="Exit",command=self.Exit,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnExit.grid(row=1,column=1,padx=1)
        #============================================
        #================DATA ENTRY FRAME===========================================
        data_frame=Frame(self.root,bd=2,relief=RIDGE)
        data_frame.place(x=2,y=190,width=1350,height=570)
        
        lblclass=Label(data_frame,text="Form/Class",font=("times new roman",18,"bold"),padx=40,pady=30)
        lblclass.grid(row=0,column=0)
        self.txtclass=ttk.Entry(data_frame,width=29,font=("times new roman",15,"bold"),state="readonly")
        self.txtclass.grid(row=0,column=1)
        
        lblbegin=Label(data_frame,text="Next Term Begins",font=("times new roman",18,"bold"),padx=40,pady=30)
        lblbegin.grid(row=1,column=0)
        txtbegin = DateEntry(data_frame,textvariable=self.var_termbegins, width=29, font=("times new roman", 15, "bold"), background='darkblue', foreground='white', borderwidth=2)
        txtbegin.grid(row=1, column=1)

        # Bind click event to the entry widget
        txtbegin.bind("<<DateEntrySelected>>", self.update_begin)
        
        lblend=Label(data_frame,text="Next Term Ends",font=("times new roman",18,"bold"),padx=40,pady=30)
        lblend.grid(row=1,column=2)
        txtend=DateEntry(data_frame,textvariable=self.var_termends,width=29,font=("times new roman",15,"bold"))
        txtend.grid(row=1,column=3)
        # Bind click event to the entry widget
        txtbegin.bind("<<DateEntrySelected>>", self.update_end)
        #====================================================
        
        #==========================Labels =======================================
        lbl_from=Label(data_frame,text="From",font=("times new roman",17,"bold"),padx=2,pady=6)
        lbl_from.grid(row=2,column=0,sticky=W ,padx=40)
        
        lbl_to=Label(data_frame,text="To",font=("times new roman",17,"bold"),padx=2,pady=6)
        lbl_to.grid(row=2,column=1,sticky=W,padx=40)
        
        lbl_comment1=Label(data_frame,text="Class Teacher's Comment",font=("times new roman",17,"bold"),padx=2,pady=6)
        lbl_comment1.grid(row=2,column=2,sticky=W ,padx=40)
        
        lbl_comment2=Label(data_frame,text="Headteacher's Comment",font=("times new roman",17,"bold"),padx=2,pady=6)
        lbl_comment2.grid(row=2,column=3,sticky=W,padx=40)
        
        #=========================Entries=====================================
        #=========================row1=====================================
        entry_mark1_1=ttk.Entry(data_frame,textvariable=self.var_mark1_1,width=16,font=("times new roman",13,"bold"))
        entry_mark1_1.grid(row=3,column=0,padx=40,pady=5)
        
        entry_mark2_1=ttk.Entry(data_frame,textvariable=self.var_mark2_1,width=16,font=("times new roman",13,"bold"))
        entry_mark2_1.grid(row=3,column=1,padx=40,pady=5)
        
        entry_comm1_1=ttk.Entry(data_frame,textvariable=self.var_tcomm1,width=36,font=("times new roman",13,"bold"))
        entry_comm1_1.grid(row=3,column=2,padx=40,pady=5)
        
        entry_comm2_1=ttk.Entry(data_frame,textvariable=self.var_hcomm1,width=36,font=("times new roman",13,"bold"))
        entry_comm2_1.grid(row=3,column=3,padx=40,pady=5)
        
        #=========================row2=====================================
        entry_mark1_2=ttk.Entry(data_frame,textvariable=self.var_mark1_2,width=16,font=("times new roman",13,"bold"))
        entry_mark1_2.grid(row=4,column=0,padx=40,pady=5)
        
        entry_mark2_2=ttk.Entry(data_frame,textvariable=self.var_mark2_2,width=16,font=("times new roman",13,"bold"))
        entry_mark2_2.grid(row=4,column=1,padx=40,pady=5)
        
        entry_comm1_2=ttk.Entry(data_frame,textvariable=self.var_tcomm2,width=36,font=("times new roman",13,"bold"))
        entry_comm1_2.grid(row=4,column=2,padx=40,pady=5)
        
        entry_comm2_2=ttk.Entry(data_frame,textvariable=self.var_hcomm2,width=36,font=("times new roman",13,"bold"))
        entry_comm2_2.grid(row=4,column=3,padx=40,pady=5)
        
        #=========================row3=====================================
        entry_mark1_3=ttk.Entry(data_frame,textvariable=self.var_mark1_3,width=16,font=("times new roman",13,"bold"))
        entry_mark1_3.grid(row=5,column=0,padx=40,pady=5)
        
        entry_mark2_3=ttk.Entry(data_frame,textvariable=self.var_mark2_3,width=16,font=("times new roman",13,"bold"))
        entry_mark2_3.grid(row=5,column=1,padx=40,pady=5)
        
        entry_comm1_3=ttk.Entry(data_frame,textvariable=self.var_tcomm3,width=36,font=("times new roman",13,"bold"))
        entry_comm1_3.grid(row=5,column=2,padx=40,pady=5)
        
        entry_comm2_3=ttk.Entry(data_frame,textvariable=self.var_hcomm3,width=36,font=("times new roman",13,"bold"))
        entry_comm2_3.grid(row=5,column=3,padx=40,pady=5)
        
        #=========================row4=====================================
        entry_mark1_4=ttk.Entry(data_frame,textvariable=self.var_mark1_4,width=16,font=("times new roman",13,"bold"))
        entry_mark1_4.grid(row=6,column=0,padx=40,pady=5)
        
        entry_mark2_4=ttk.Entry(data_frame,textvariable=self.var_mark2_4,width=16,font=("times new roman",13,"bold"))
        entry_mark2_4.grid(row=6,column=1,padx=40,pady=5)
        
        entry_comm1_4=ttk.Entry(data_frame,textvariable=self.var_tcomm4,width=36,font=("times new roman",13,"bold"))
        entry_comm1_4.grid(row=6,column=2,padx=40,pady=5)
        
        entry_comm2_4=ttk.Entry(data_frame,textvariable=self.var_hcomm4,width=36,font=("times new roman",13,"bold"))
        entry_comm2_4.grid(row=6,column=3,padx=40,pady=5)
        
        #=========================row5=====================================
        entry_mark1_5=ttk.Entry(data_frame,textvariable=self.var_mark1_5,width=16,font=("times new roman",13,"bold"))
        entry_mark1_5.grid(row=7,column=0,padx=40,pady=5)
        
        entry_mark2_5=ttk.Entry(data_frame,textvariable=self.var_mark2_5,width=16,font=("times new roman",13,"bold"))
        entry_mark2_5.grid(row=7,column=1,padx=40,pady=5)
        
        entry_comm1_5=ttk.Entry(data_frame,textvariable=self.var_tcomm5,width=36,font=("times new roman",13,"bold"))
        entry_comm1_5.grid(row=7,column=2,padx=40,pady=5)
        
        entry_comm2_5=ttk.Entry(data_frame,textvariable=self.var_hcomm5,width=36,font=("times new roman",13,"bold"))
        entry_comm2_5.grid(row=7,column=3,padx=40,pady=5)
        
        #=========================row6=====================================
        entry_mark1_6=ttk.Entry(data_frame,textvariable=self.var_mark1_6,width=16,font=("times new roman",13,"bold"))
        entry_mark1_6.grid(row=8,column=0,padx=40,pady=5)
        
        entry_mark2_6=ttk.Entry(data_frame,textvariable=self.var_mark2_6,width=16,font=("times new roman",13,"bold"))
        entry_mark2_6.grid(row=8,column=1,padx=40,pady=5)
        
        entry_comm1_6=ttk.Entry(data_frame,textvariable=self.var_tcomm6,width=36,font=("times new roman",13,"bold"))
        entry_comm1_6.grid(row=8,column=2,padx=40,pady=5)
        
        entry_comm2_6=ttk.Entry(data_frame,textvariable=self.var_hcomm6,width=36,font=("times new roman",13,"bold"))
        entry_comm2_6.grid(row=8,column=3,padx=40,pady=5)
        
        #=========================row7=====================================
        entry_mark1_7=ttk.Entry(data_frame,textvariable=self.var_mark1_7,width=16,font=("times new roman",13,"bold"))
        entry_mark1_7.grid(row=9,column=0,padx=40,pady=5)
        
        entry_mark2_7=ttk.Entry(data_frame,textvariable=self.var_mark2_7,width=16,font=("times new roman",13,"bold"))
        entry_mark2_7.grid(row=9,column=1,padx=40,pady=5)
        
        entry_comm1_7=ttk.Entry(data_frame,textvariable=self.var_tcomm7,width=36,font=("times new roman",13,"bold"))
        entry_comm1_7.grid(row=9,column=2,padx=40,pady=5)
        
        entry_comm2_7=ttk.Entry(data_frame,textvariable=self.var_hcomm7,width=36,font=("times new roman",13,"bold"))
        entry_comm2_7.grid(row=9,column=3,padx=40,pady=5)
        
        #=========================row8=====================================
        entry_mark1_8=ttk.Entry(data_frame,textvariable=self.var_mark1_8,width=16,font=("times new roman",13,"bold"))
        entry_mark1_8.grid(row=10,column=0,padx=40,pady=5)
        
        entry_mark2_8=ttk.Entry(data_frame,textvariable=self.var_mark2_8,width=16,font=("times new roman",13,"bold"))
        entry_mark2_8.grid(row=10,column=1,padx=40,pady=5)
        
        entry_comm1_8=ttk.Entry(data_frame,textvariable=self.var_tcomm8,width=36,font=("times new roman",13,"bold"))
        entry_comm1_8.grid(row=10,column=2,padx=40,pady=5)
        
        entry_comm2_8=ttk.Entry(data_frame,textvariable=self.var_hcomm8,width=36,font=("times new roman",13,"bold"))
        entry_comm2_8.grid(row=10,column=3,padx=40,pady=5)
        
        #=========================row9=====================================
        entry_mark1_9=ttk.Entry(data_frame,textvariable=self.var_mark1_9,width=16,font=("times new roman",13,"bold"))
        entry_mark1_9.grid(row=11,column=0,padx=40,pady=5)
        
        entry_mark2_9=ttk.Entry(data_frame,textvariable=self.var_mark2_9,width=16,font=("times new roman",13,"bold"))
        entry_mark2_9.grid(row=11,column=1,padx=40,pady=5)
        
        entry_comm1_9=ttk.Entry(data_frame,textvariable=self.var_tcomm9,width=36,font=("times new roman",13,"bold"))
        entry_comm1_9.grid(row=11,column=2,padx=40,pady=5)
        
        entry_comm2_9=ttk.Entry(data_frame,textvariable=self.var_hcomm9,width=36,font=("times new roman",13,"bold"))
        entry_comm2_9.grid(row=11,column=3,padx=40,pady=5)
        
        #=========================row10=====================================
        entry_mark1_10=ttk.Entry(data_frame,textvariable=self.var_mark1_10,width=16,font=("times new roman",13,"bold"))
        entry_mark1_10.grid(row=12,column=0,padx=40,pady=5)
        
        entry_mark2_10=ttk.Entry(data_frame,textvariable=self.var_mark2_10,width=16,font=("times new roman",13,"bold"))
        entry_mark2_10.grid(row=12,column=1,padx=40,pady=5)
        
        entry_comm1_10=ttk.Entry(data_frame,textvariable=self.var_tcomm10,width=36,font=("times new roman",13,"bold"))
        entry_comm1_10.grid(row=12,column=2,padx=40,pady=5)
        
        entry_comm2_10=ttk.Entry(data_frame,textvariable=self.var_hcomm10,width=36,font=("times new roman",13,"bold"))
        entry_comm2_10.grid(row=12,column=3,padx=40,pady=5)
        
    def update_txtclass(self, event):
        selected_class = self.var_class.get()

        # Check if the selected class is not "Select"
        if selected_class != "Select":
            self.txtclass.config(state=NORMAL)  # Allow modification
            self.txtclass.delete(0, END)  # Clear the current content
            self.txtclass.insert(0, selected_class)  # Insert the selected class
            self.txtclass.config(state="readonly")  # Set back to readonly
        else:
            self.txtclass.config(state=NORMAL)  # Allow modification
            self.txtclass.delete(0, END)  # Clear the current content
            self.txtclass.config(state="readonly")  # Set back to readonly  
          
    def update_begin(self, event):
        selected_date = self.var_termbegins.get()

        datetime_obj = datetime.strptime(selected_date, "%d/%m/%yyy")
    def update_end(self, event):
        selected_date = self.var_termends.get()

        datetime_obj = datetime.strptime(selected_date, "%dd/%mmm/%yyy")
        
             
        #========================================================================================
    def add_data(self):
        if self.var_class.get() == "Select":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            #try:
                conn = pymysql.connect(host="localhost", user="root", database="report")
                my_cursor = conn.cursor()
                
                # Use the last reference to generate the next gradeID
                last_reference = self.get_last_reference()
                next_reference = str(int(last_reference) + 1) if last_reference else "1001"
                self.var_gradeID.set(next_reference)

                # Check if the record with gradeID and class already exists
                #gradeID = self.var_gradeID.get()
                selected_class = self.var_class.get()
                my_cursor.execute("SELECT class FROM remarks WHERE class= %s", (selected_class))
                existing_record = my_cursor.fetchone()

                if existing_record:
                    # Update the existing record
                    my_cursor.execute("""
                    UPDATE remarks
                    SET termbegins=%s, termends=%s,
                        mark1_1=%s, mark2_1=%s, tcomm1=%s, hcomm1=%s,
                        mark1_2=%s, mark2_2=%s, tcomm2=%s, hcomm2=%s,
                        mark1_3=%s, mark2_3=%s, tcomm3=%s, hcomm3=%s,
                        mark1_4=%s, mark2_4=%s, tcomm4=%s, hcomm4=%s,
                        mark1_5=%s, mark2_5=%s, tcomm5=%s, hcomm5=%s,
                        mark1_6=%s, mark2_6=%s, tcomm6=%s, hcomm6=%s,
                        mark1_7=%s, mark2_7=%s, tcomm7=%s, hcomm7=%s,
                        mark1_8=%s, mark2_8=%s, tcomm8=%s, hcomm8=%s,
                        mark1_9=%s, mark2_9=%s, tcomm9=%s, hcomm9=%s,
                        mark1_10=%s, mark2_10=%s, tcomm10=%s, hcomm10=%s
                    WHERE  class=%s
                    """, (self.var_termbegins.get(),
                        self.var_termends.get(),
                        self.var_mark1_1.get(),
                        self.var_mark2_1.get(),
                        self.var_tcomm1.get(),
                        self.var_hcomm1.get(),
                        self.var_mark1_2.get(),
                        self.var_mark2_2.get(),
                        self.var_tcomm2.get(),
                        self.var_hcomm2.get(),
                        self.var_mark1_3.get(),
                        self.var_mark2_3.get(),
                        self.var_tcomm3.get(),
                        self.var_hcomm3.get(),
                        self.var_mark1_4.get(),
                        self.var_mark2_4.get(),
                        self.var_tcomm4.get(),
                        self.var_hcomm4.get(),
                        self.var_mark1_5.get(),
                        self.var_mark2_5.get(),
                        self.var_tcomm5.get(),
                        self.var_hcomm5.get(),
                        self.var_mark1_6.get(),
                        self.var_mark2_6.get(),
                        self.var_tcomm6.get(),
                        self.var_hcomm6.get(),
                        self.var_mark1_7.get(),
                        self.var_mark2_7.get(),
                        self.var_tcomm7.get(),
                        self.var_hcomm7.get(),
                        self.var_mark1_8.get(),
                        self.var_mark2_8.get(),
                        self.var_tcomm8.get(),
                        self.var_hcomm8.get(),
                        self.var_mark1_9.get(),
                        self.var_mark2_9.get(),
                        self.var_tcomm9.get(),
                        self.var_hcomm9.get(),
                        self.var_mark1_10.get(),
                        self.var_mark2_10.get(),
                        self.var_tcomm10.get(),
                        self.var_hcomm10.get(),
                        selected_class))
                else:
                    # Insert a new record
                    my_cursor.execute("""
                    INSERT INTO remarks (gradeID, class , termbegins, termends ,mark1_1 , mark2_1 , tcomm1 , hcomm1 , mark1_2 , mark2_2, tcomm2 , hcomm2 , mark1_3, mark2_3 ,tcomm3 , hcomm3 , mark1_4 , mark2_4,tcomm4 ,hcomm4 , mark1_5 , mark2_5 , tcomm5 ,hcomm5 ,mark1_6 , mark2_6 , tcomm6 , hcomm6 , mark1_7 , mark2_7, tcomm7 , hcomm7 , mark1_8, mark2_8 ,tcomm8 , hcomm8 , mark1_9, mark2_9,tcomm9 ,hcomm9, mark1_10, mark2_10, tcomm10,hcomm10)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (self.var_gradeID.get(), selected_class, 
                        self.var_termbegins.get(),
                        self.var_termends.get(),
                        self.var_mark1_1.get(),
                        self.var_mark2_1.get(),
                        self.var_tcomm1.get(),
                        self.var_hcomm1.get(),
                        self.var_mark1_2.get(),
                        self.var_mark2_2.get(),
                        self.var_tcomm2.get(),
                        self.var_hcomm2.get(),
                        self.var_mark1_3.get(),
                        self.var_mark2_3.get(),
                        self.var_tcomm3.get(),
                        self.var_hcomm3.get(),
                        self.var_mark1_4.get(),
                        self.var_mark2_4.get(),
                        self.var_tcomm4.get(),
                        self.var_hcomm4.get(),
                        self.var_mark1_5.get(),
                        self.var_mark2_5.get(),
                        self.var_tcomm5.get(),
                        self.var_hcomm5.get(),
                        self.var_mark1_6.get(),
                        self.var_mark2_6.get(),
                        self.var_tcomm6.get(),
                        self.var_hcomm6.get(),
                        self.var_mark1_7.get(),
                        self.var_mark2_7.get(),
                        self.var_tcomm7.get(),
                        self.var_hcomm7.get(),
                        self.var_mark1_8.get(),
                        self.var_mark2_8.get(),
                        self.var_tcomm8.get(),
                        self.var_hcomm8.get(),
                        self.var_mark1_9.get(),
                        self.var_mark2_9.get(),
                        self.var_tcomm9.get(),
                        self.var_hcomm9.get(),
                        self.var_mark1_10.get(),
                        self.var_mark2_10.get(),
                        self.var_tcomm10.get(),
                        self.var_hcomm10.get(),))
                
                conn.commit()
                self.fetch_data1()
                conn.close()
                messagebox.showinfo("Success", "Remarks added/updated successfully", parent=self.root)
            #except Exception as e:
            #    messagebox.showerror("Error", f"Error due to: {str(e)}", parent=self.root)    
    
    def fetch_data(self):
        selected_class = self.var_class.get()
        if selected_class != "":
            try:
                conn = pymysql.connect(host="localhost", user="root", database="report")
                my_cursor = conn.cursor()
    
                # Fetch data for the selected class
                my_cursor.execute("SELECT * FROM remarks WHERE class = %s", (selected_class,))
                rows = my_cursor.fetchall()

                # Display data in textboxes
                if rows:
                    row = rows[0]  # Assuming only one record for a class for simplicity
                    self.var_gradeID.set(row[0])
                    self.var_class.set(row[1])
                    self.var_termbegins.set(row[2])
                    self.var_termends.set(row[3])
                    self.var_mark1_1.set(row[4])
                    self.var_mark2_1.set(row[5])
                    self.var_tcomm1.set(row[6])
                    self.var_hcomm1.set(row[7])
                    self.var_mark1_2.set(row[8])
                    self.var_mark2_2.set(row[9])
                    self.var_tcomm2.set(row[10])
                    self.var_hcomm2.set(row[11])
                    self.var_mark1_3.set(row[12])
                    self.var_mark2_3.set(row[13])
                    self.var_tcomm3.set(row[14])
                    self.var_hcomm3.set(row[15])
                    self.var_mark1_4.set(row[16])
                    self.var_mark2_4.set(row[17])
                    self.var_tcomm4.set(row[18])
                    self.var_hcomm4.set(row[19])
                    self.var_mark1_5.set(row[20])
                    self.var_mark2_5.set(row[21])
                    self.var_tcomm5.set(row[22])
                    self.var_hcomm5.set(row[23])
                    self.var_mark1_6.set(row[24])
                    self.var_mark2_6.set(row[25])
                    self.var_tcomm6.set(row[26])
                    self.var_hcomm6.set(row[27])
                    self.var_mark1_7.set(row[28])
                    self.var_mark2_7.set(row[29])
                    self.var_tcomm7.set(row[30])
                    self.var_hcomm7.set(row[31])
                    self.var_mark1_8.set(row[32])
                    self.var_mark2_8.set(row[33])
                    self.var_tcomm8.set(row[34])
                    self.var_hcomm8.set(row[35])
                    self.var_mark1_9.set(row[36])
                    self.var_mark2_9.set(row[37])
                    self.var_tcomm9.set(row[38])
                    self.var_hcomm9.set(row[39])
                    self.var_mark1_10.set(row[40])
                    self.var_mark2_10.set(row[41])
                    self.var_tcomm10.set(row[42])
                    self.var_hcomm10.set(row[43])
                        
            except Exception as e:
                messagebox.showwarning("Warning", f"Error fetching data: {str(e)}", parent=self.root)
            
        conn.close()
    
    def fetch_data1(self):
        self.var_mark1_1.set("")
        self.var_mark2_1.set("")
        self.var_tcomm1.set("")
        self.var_hcomm1.set("")
        self.var_mark1_2.set("")
        self.var_mark2_2.set("")
        self.var_tcomm2.set("")
        self.var_hcomm2.set("")
        self.var_mark1_3.set("")
        self.var_mark2_3.set("")
        self.var_tcomm3.set("")
        self.var_hcomm3.set("")
        self.var_mark1_4.set("")
        self.var_mark2_4.set("")
        self.var_tcomm4.set("")
        self.var_hcomm4.set("")
        self.var_mark1_5.set("")
        self.var_mark2_5.set("")
        self.var_tcomm5.set("")
        self.var_hcomm5.set("")
        self.var_mark1_6.set("")
        self.var_mark2_6.set("")
        self.var_tcomm6.set("")
        self.var_hcomm6.set("")
        self.var_mark1_7.set("")
        self.var_mark2_7.set("")
        self.var_tcomm7.set("")
        self.var_hcomm7.set("")
        self.var_mark1_8.set("")
        self.var_mark2_8.set("")
        self.var_tcomm8.set("")
        self.var_hcomm8.set("")
        self.var_mark1_9.set("")
        self.var_mark2_9.set("")
        self.var_tcomm9.set("")
        self.var_hcomm9.set("")
        self.var_mark1_10.set("")
        self.var_mark2_10.set("")
        self.var_tcomm10.set("")
        self.var_hcomm10.set("")
    
    def delete_data(self):
        if self.var_class.get() == "Select":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            conn = pymysql.connect(host="localhost", user="root", database="report")
            my_cursor = conn.cursor()

            selected_class = self.var_class.get()
            
            # Check if the record with the specified class exists
            my_cursor.execute("SELECT class FROM remarks WHERE class = %s", (selected_class,))
            existing_record = my_cursor.fetchone()

            if existing_record:
                # Delete the record with the specified class
                my_cursor.execute("DELETE FROM remarks WHERE class = %s", (selected_class,))
                
                conn.commit()
                self.fetch_data1()
                conn.close()
                messagebox.showinfo("Success", "Record deleted successfully", parent=self.root)
            else:
                messagebox.showinfo("Error", "No record found with the specified class", parent=self.root)


    def get_last_reference(self):
        try:
            conn = pymysql.connect(host="localhost", user="root", database="report")
            cursor = conn.cursor()

            # Execute a query to get the maximum gradeID value from the database
            cursor.execute("SELECT MAX(gradeID) FROM remarks")  # Replace with your actual table name
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
        
    def Exit(self):
           self.Exit= tkinter.messagebox.askyesno("Report Management System","confirm if you want to exit",parent=self.root)
           if self.Exit>0:
               self.root.destroy()
               return
                    
if __name__=="__main__":
    root=Tk()
    obj=remark(root)
    root.mainloop()