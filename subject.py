from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter as tk
import mysql.connector
import random
import tkinter.messagebox
from tkinter import messagebox

class Subject:
    def __init__(self,root):
        self.root=root
        self.root.title("Report Management System")
        self.root.geometry("1550x800+0+0")
        #self.root.overrideredirect(True)
        #========================variables=======================
        self.var_subjectID=StringVar()
        x=random.randint(1000,9999)
        self.var_subjectID.set(str(x))
        
        self.var_class=StringVar()
        self.var_classteacher=StringVar()
        self.var_subject1=StringVar()
        self.var_teacher1=StringVar()
        self.var_subject2=StringVar()
        self.var_teacher2=StringVar()
        self.var_subject3=StringVar()
        self.var_teacher3=StringVar()
        self.var_subject4=StringVar()
        self.var_teacher4=StringVar()
        self.var_subject5=StringVar()
        self.var_teacher5=StringVar()
        self.var_subject6=StringVar()
        self.var_teacher6=StringVar()
        self.var_subject7=StringVar()
        self.var_teacher7=StringVar()
        self.var_subject8=StringVar()
        self.var_teacher8=StringVar()
        self.var_subject9=StringVar()
        self.var_teacher9=StringVar()
        self.var_subject10=StringVar()
        self.var_teacher10=StringVar()
        self.var_subject11=StringVar()
        self.var_teacher11=StringVar()
        self.var_subject12=StringVar()
        self.var_teacher12=StringVar()
        self.var_subject13=StringVar()
        self.var_teacher13=StringVar()
        self.var_subject14=StringVar()
        self.var_teacher14=StringVar()
        self.var_subject15=StringVar()
        self.var_teacher15=StringVar()
        self.var_subject16=StringVar()
        self.var_teacher16=StringVar()
        
        #=====================title=======================================================
        lbl_title=Label(self.root,text="ADD SUBJECTS TO CORRESPONDING CLASS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1355,height=50)
        #===================2st Image===log======================================================
        Image2=Image.open(r"C:\Users\USER\Desktop\summer\PYTHON PROJECTS TKINTER\REPT\images\logo.PNG")
        Image2=Image2.resize((100,40),Image.LANCZOS)
        self.photoImage2=ImageTk.PhotoImage(Image2)
        
        lblimg=Label(self.root,image=self.photoImage2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)
        #===================labelframe====================================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Select Class",font=("times new roman",18,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=325,height=300)
        #====================labels and entrys=========================================
        lbl_subject_ref=Label(labelframeleft,text="Subject ID",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_subject_ref.grid(row=0,column=0,sticky=W)
        entry_subjectID=ttk.Entry(labelframeleft,textvariable=self.var_subjectID,width=22,font=("times new roman",13,"bold"),state="readonly")
        entry_subjectID.grid(row=0,column=1)
        last_reference = self.get_last_reference()  # Function to get the last reference
        
        if last_reference is not None:
            next_reference = str(int(last_reference) + 1)
        else:
            next_reference = "1001"  # Initial reference
        
        self.var_subjectID.set(next_reference)
        
        #==========================Select Class ========================================
        self.var_year=StringVar()
        self.conn = mysql.connector.connect(host="localhost",user="root",password="francis121",database="report")

        # Retrieve values from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT class FROM class")  # Modify with your database column and table names
        classs = [classs[0] for classs in cursor.fetchall()]

        combo_class = ttk.Combobox(labelframeleft, textvariable=self.var_class, width=20, font=("times new roman", 13, "bold"), state="readonly")
        combo_class["values"] = tuple(["Select"] + classs)
        combo_class.current(0)
        combo_class.grid(row=1, column=1)
        
        classL=Label(labelframeleft,text="Class",font=("times new roman",12,"bold"),padx=2,pady=6)
        classL.grid(row=1,column=0,sticky=W)
        
        #==========================Select class teacher =======================================
        self.conn = mysql.connector.connect(host="localhost",user="root",password="francis121",database="report")

        # Retrieve values from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT Name FROM teacher")  # Modify with your database column and table names
        name = [Name[0] for Name in cursor.fetchall()]

        combo_classteacher = ttk.Combobox(labelframeleft, textvariable=self.var_classteacher, width=20, font=("times new roman", 13, "bold"), state="readonly")
        combo_classteacher["values"] = tuple(["Select"] + name)
        combo_classteacher.current(0)
        combo_classteacher.grid(row=2, column=1)
        
        classteacher=Label(labelframeleft,text="Class Teacher",font=("times new roman",12,"bold"),padx=2,pady=6)
        classteacher.grid(row=2,column=0,sticky=W)
        
        #================btn===========================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=2,y=200,width=560,height=100)
        
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.Delete,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnReset.grid(row=1,column=0,padx=1)
        
        btnExit=Button(btn_frame,text="Exit",font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnExit.grid(row=1,column=1,padx=1)
        
        #===========================Right Frame ==================================
        labelframeright=LabelFrame(self.root,bd=2,relief=RIDGE,text="Enter Subjects with Teachers",font=("arial",12,"bold"))
        labelframeright.place(x=335,y=50,width=1020,height=310)
        #==================================================================================
        #=========================subject one=====================================
        lbl_subject1_ref=Label(labelframeright,text="Subject",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_subject1_ref.grid(row=0,column=0,sticky=W)
        entry_subject1=ttk.Entry(labelframeright,textvariable=self.var_subject1,width=16,font=("times new roman",13,"bold"))
        entry_subject1.grid(row=0,column=1,padx=10)
        
        #==========================Select teacher =======================================
        self.conn = mysql.connector.connect(host="localhost",user="root",password="francis121",database="report")

        # Retrieve values from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT Name FROM teacher")  # Modify with your database column and table names
        name = [Name[0] for Name in cursor.fetchall()]

        combo_teacher1 = ttk.Combobox(labelframeright, textvariable=self.var_teacher1, width=16, font=("times new roman", 13, "bold"), state="readonly")
        combo_teacher1["values"] = tuple(["Select"] + name)
        combo_teacher1.current(0)
        combo_teacher1.grid(row=0, column=3)
        
        teacher1=Label(labelframeright,text="Teacher",font=("times new roman",12,"bold"),padx=2,pady=6)
        teacher1.grid(row=0,column=2,sticky=W,padx=20)
        
        #=========================subject Two=====================================
        lbl_subject2_ref=Label(labelframeright,text="Subject",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_subject2_ref.grid(row=0,column=4,sticky=W)
        entry_subject2=ttk.Entry(labelframeright,textvariable=self.var_subject2,width=16,font=("times new roman",13,"bold"))
        entry_subject2.grid(row=0,column=5,padx=10)
        
        #==========================Select teacher =======================================
        self.conn = mysql.connector.connect(host="localhost",user="root",password="francis121",database="report")
        # Retrieve values from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT Name FROM teacher")  # Modify with your database column and table names
        name = [Name[0] for Name in cursor.fetchall()]

        combo_teacher2 = ttk.Combobox(labelframeright, textvariable=self.var_teacher2, width=16, font=("times new roman", 13, "bold"), state="readonly")
        combo_teacher2["values"] = tuple(["Select"] + name)
        combo_teacher2.current(0)
        combo_teacher2.grid(row=0, column=7)
        
        teacher2=Label(labelframeright,text="Teacher",font=("times new roman",12,"bold"),padx=2,pady=6)
        teacher2.grid(row=0,column=6,sticky=W,padx=20)
        
        #=========================subject 3=====================================
        lbl_subject3_ref=Label(labelframeright,text="Subject",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_subject3_ref.grid(row=1,column=0,sticky=W)
        entry_subject3=ttk.Entry(labelframeright,textvariable=self.var_subject3,width=16,font=("times new roman",13,"bold"))
        entry_subject3.grid(row=1,column=1)
        
        #==========================Select teacher =======================================
        self.conn = mysql.connector.connect(host="localhost",user="root",password="francis121",database="report")

        # Retrieve values from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT Name FROM teacher")  # Modify with your database column and table names
        name = [Name[0] for Name in cursor.fetchall()]

        combo_teacher3 = ttk.Combobox(labelframeright, textvariable=self.var_teacher3, width=16, font=("times new roman", 13, "bold"), state="readonly")
        combo_teacher3["values"] = tuple(["Select"] + name)
        combo_teacher3.current(0)
        combo_teacher3.grid(row=1, column=3)
        
        teacher3=Label(labelframeright,text="Teacher",font=("times new roman",12,"bold"),padx=2,pady=6)
        teacher3.grid(row=1,column=2,sticky=W,padx=20)
        
        #=========================subject 4=====================================
        lbl_subject4_ref=Label(labelframeright,text="Subject",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_subject4_ref.grid(row=1,column=4,sticky=W)
        entry_subject4=ttk.Entry(labelframeright,textvariable=self.var_subject4,width=16,font=("times new roman",13,"bold"))
        entry_subject4.grid(row=1,column=5)
        
        #==========================Select teacher =======================================
        self.conn = mysql.connector.connect(host="localhost",user="root",password="francis121",database="report")
        # Retrieve values from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT Name FROM teacher")  # Modify with your database column and table names
        name = [Name[0] for Name in cursor.fetchall()]

        combo_teacher4 = ttk.Combobox(labelframeright, textvariable=self.var_teacher4, width=16, font=("times new roman", 13, "bold"), state="readonly")
        combo_teacher4["values"] = tuple(["Select"] + name)
        combo_teacher4.current(0)
        combo_teacher4.grid(row=1, column=7)
        
        teacher4=Label(labelframeright,text="Teacher",font=("times new roman",12,"bold"),padx=2,pady=6)
        teacher4.grid(row=1,column=6,sticky=W,padx=20)
        
        #=========================subject 5=====================================
        lbl_subject5_ref=Label(labelframeright,text="Subject",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_subject5_ref.grid(row=2,column=0,sticky=W)
        entry_subject5=ttk.Entry(labelframeright,textvariable=self.var_subject5,width=16,font=("times new roman",13,"bold"))
        entry_subject5.grid(row=2,column=1)
        
        #==========================Select teacher =======================================
        self.conn = mysql.connector.connect(host="localhost",user="root",password="francis121",database="report")

        # Retrieve values from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT Name FROM teacher")  # Modify with your database column and table names
        name = [Name[0] for Name in cursor.fetchall()]

        combo_teacher5 = ttk.Combobox(labelframeright, textvariable=self.var_teacher5, width=16, font=("times new roman", 13, "bold"), state="readonly")
        combo_teacher5["values"] = tuple(["Select"] + name)
        combo_teacher5.current(0)
        combo_teacher5.grid(row=2, column=3)
        
        teacher5=Label(labelframeright,text="Teacher",font=("times new roman",12,"bold"),padx=2,pady=6)
        teacher5.grid(row=2,column=2,sticky=W,padx=20)
        
        #=========================subject six=====================================
        lbl_subject6_ref=Label(labelframeright,text="Subject",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_subject6_ref.grid(row=2,column=4,sticky=W)
        entry_subject6=ttk.Entry(labelframeright,textvariable=self.var_subject6,width=16,font=("times new roman",13,"bold"))
        entry_subject6.grid(row=2,column=5)
        
        #==========================Select teacher =======================================
        self.conn = mysql.connector.connect(host="localhost",user="root",password="francis121",database="report")
        # Retrieve values from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT Name FROM teacher")  # Modify with your database column and table names
        name = [Name[0] for Name in cursor.fetchall()]

        combo_teacher6 = ttk.Combobox(labelframeright, textvariable=self.var_teacher6, width=16, font=("times new roman", 13, "bold"), state="readonly")
        combo_teacher6["values"] = tuple(["Select"] + name)
        combo_teacher6.current(0)
        combo_teacher6.grid(row=2, column=7)
        
        teacher6=Label(labelframeright,text="Teacher",font=("times new roman",12,"bold"),padx=2,pady=6)
        teacher6.grid(row=2,column=6,sticky=W,padx=20)
        
        #=========================subject seven=====================================
        lbl_subject7_ref=Label(labelframeright,text="Subject",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_subject7_ref.grid(row=3,column=0,sticky=W)
        entry_subject7=ttk.Entry(labelframeright,textvariable=self.var_subject7,width=16,font=("times new roman",13,"bold"))
        entry_subject7.grid(row=3,column=1)
        
        #==========================Select teacher =======================================
        self.conn = mysql.connector.connect(host="localhost",user="root",password="francis121",database="report")

        # Retrieve values from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT Name FROM teacher")  # Modify with your database column and table names
        name = [Name[0] for Name in cursor.fetchall()]

        combo_teacher7 = ttk.Combobox(labelframeright, textvariable=self.var_teacher7, width=16, font=("times new roman", 13, "bold"), state="readonly")
        combo_teacher7["values"] = tuple(["Select"] + name)
        combo_teacher7.current(0)
        combo_teacher7.grid(row=3, column=3)
        
        teacher7=Label(labelframeright,text="Teacher",font=("times new roman",12,"bold"),padx=2,pady=6)
        teacher7.grid(row=3,column=2,sticky=W,padx=20)
        
        #=========================subject eight=====================================
        lbl_subject8_ref=Label(labelframeright,text="Subject",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_subject8_ref.grid(row=3,column=4,sticky=W)
        entry_subject8=ttk.Entry(labelframeright,textvariable=self.var_subject8,width=16,font=("times new roman",13,"bold"))
        entry_subject8.grid(row=3,column=5)
        
        #==========================Select teacher =======================================
        self.conn = mysql.connector.connect(host="localhost",user="root",password="francis121",database="report")
        # Retrieve values from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT Name FROM teacher")  # Modify with your database column and table names
        name = [Name[0] for Name in cursor.fetchall()]

        combo_teacher8 = ttk.Combobox(labelframeright, textvariable=self.var_teacher8, width=16, font=("times new roman", 13, "bold"), state="readonly")
        combo_teacher8["values"] = tuple(["Select"] + name)
        combo_teacher8.current(0)
        combo_teacher8.grid(row=3, column=7)
        
        teacher8=Label(labelframeright,text="Teacher",font=("times new roman",12,"bold"),padx=2,pady=6)
        teacher8.grid(row=3,column=6,sticky=W,padx=20)
        
        #=========================subject nine=====================================
        lbl_subject9_ref=Label(labelframeright,text="Subject",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_subject9_ref.grid(row=4,column=0,sticky=W)
        entry_subject9=ttk.Entry(labelframeright,textvariable=self.var_subject9,width=16,font=("times new roman",13,"bold"))
        entry_subject9.grid(row=4,column=1)
        
        #==========================Select teacher =======================================
        self.conn = mysql.connector.connect(host="localhost",user="root",password="francis121",database="report")

        # Retrieve values from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT Name FROM teacher")  # Modify with your database column and table names
        name = [Name[0] for Name in cursor.fetchall()]

        combo_teacher9 = ttk.Combobox(labelframeright, textvariable=self.var_teacher9, width=16, font=("times new roman", 13, "bold"), state="readonly")
        combo_teacher9["values"] = tuple(["Select"] + name)
        combo_teacher9.current(0)
        combo_teacher9.grid(row=4, column=3)
        
        teacher9=Label(labelframeright,text="Teacher",font=("times new roman",12,"bold"),padx=2,pady=6)
        teacher9.grid(row=4,column=2,sticky=W,padx=20)
        
        #=========================subject Ten=====================================
        lbl_subject10_ref=Label(labelframeright,text="Subject",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_subject10_ref.grid(row=4,column=4,sticky=W)
        entry_subject10=ttk.Entry(labelframeright,textvariable=self.var_subject10,width=16,font=("times new roman",13,"bold"))
        entry_subject10.grid(row=4,column=5)
        
        #==========================Select teacher =======================================
        self.conn = mysql.connector.connect(host="localhost",user="root",password="francis121",database="report")
        # Retrieve values from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT Name FROM teacher")  # Modify with your database column and table names
        name = [Name[0] for Name in cursor.fetchall()]

        combo_teacher10 = ttk.Combobox(labelframeright, textvariable=self.var_teacher10, width=16, font=("times new roman", 13, "bold"), state="readonly")
        combo_teacher10["values"] = tuple(["Select"] + name)
        combo_teacher10.current(0)
        combo_teacher10.grid(row=4, column=7)
        
        teacher10=Label(labelframeright,text="Teacher",font=("times new roman",12,"bold"),padx=2,pady=6)
        teacher10.grid(row=4,column=6,sticky=W,padx=20)
        
        #=========================subject 11=====================================
        lbl_subject11_ref=Label(labelframeright,text="Subject",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_subject11_ref.grid(row=5,column=0,sticky=W)
        entry_subject11=ttk.Entry(labelframeright,textvariable=self.var_subject11,width=16,font=("times new roman",13,"bold"))
        entry_subject11.grid(row=5,column=1)
        
        #==========================Select teacher =======================================
        self.conn = mysql.connector.connect(host="localhost",user="root",password="francis121",database="report")

        # Retrieve values from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT Name FROM teacher")  # Modify with your database column and table names
        name = [Name[0] for Name in cursor.fetchall()]

        combo_teacher11 = ttk.Combobox(labelframeright, textvariable=self.var_teacher11, width=16, font=("times new roman", 13, "bold"), state="readonly")
        combo_teacher11["values"] = tuple(["Select"] + name)
        combo_teacher11.current(0)
        combo_teacher11.grid(row=5, column=3)
        
        teacher11=Label(labelframeright,text="Teacher",font=("times new roman",12,"bold"),padx=2,pady=6)
        teacher11.grid(row=5,column=2,sticky=W,padx=20)
        
        #=========================subject 12=====================================
        lbl_subject12_ref=Label(labelframeright,text="Subject",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_subject12_ref.grid(row=5,column=4,sticky=W)
        entry_subject12=ttk.Entry(labelframeright,textvariable=self.var_subject12,width=16,font=("times new roman",13,"bold"))
        entry_subject12.grid(row=5,column=5)
        
        #==========================Select teacher =======================================
        self.conn = mysql.connector.connect(host="localhost",user="root",password="francis121",database="report")
        # Retrieve values from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT Name FROM teacher")  # Modify with your database column and table names
        name = [Name[0] for Name in cursor.fetchall()]

        combo_teacher12 = ttk.Combobox(labelframeright, textvariable=self.var_teacher12, width=16, font=("times new roman", 13, "bold"), state="readonly")
        combo_teacher12["values"] = tuple(["Select"] + name)
        combo_teacher12.current(0)
        combo_teacher12.grid(row=5, column=7)
        
        teacher12=Label(labelframeright,text="Teacher",font=("times new roman",12,"bold"),padx=2,pady=6)
        teacher12.grid(row=5,column=6,sticky=W,padx=20)
        
        #=========================subject 13=====================================
        lbl_subject13_ref=Label(labelframeright,text="Subject",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_subject13_ref.grid(row=6,column=0,sticky=W)
        entry_subject13=ttk.Entry(labelframeright,textvariable=self.var_subject13,width=16,font=("times new roman",13,"bold"))
        entry_subject13.grid(row=6,column=1)
        
        #==========================Select teacher =======================================
        self.conn = mysql.connector.connect(host="localhost",user="root",password="francis121",database="report")

        # Retrieve values from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT Name FROM teacher")  # Modify with your database column and table names
        name = [Name[0] for Name in cursor.fetchall()]

        combo_teacher13 = ttk.Combobox(labelframeright, textvariable=self.var_teacher13, width=16, font=("times new roman", 13, "bold"), state="readonly")
        combo_teacher13["values"] = tuple(["Select"] + name)
        combo_teacher13.current(0)
        combo_teacher13.grid(row=6, column=3)
        
        teacher13=Label(labelframeright,text="Teacher",font=("times new roman",12,"bold"),padx=2,pady=6)
        teacher13.grid(row=6,column=2,sticky=W,padx=20)
        
        #=========================subject 14=====================================
        lbl_subject14_ref=Label(labelframeright,text="Subject",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_subject14_ref.grid(row=6,column=4,sticky=W)
        entry_subject14=ttk.Entry(labelframeright,textvariable=self.var_subject14,width=16,font=("times new roman",13,"bold"))
        entry_subject14.grid(row=6,column=5)
        
        #==========================Select teacher =======================================
        self.conn = mysql.connector.connect(host="localhost",user="root",password="francis121",database="report")
        # Retrieve values from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT Name FROM teacher")  # Modify with your database column and table names
        name = [Name[0] for Name in cursor.fetchall()]

        combo_teacher14 = ttk.Combobox(labelframeright, textvariable=self.var_teacher14, width=16, font=("times new roman", 13, "bold"), state="readonly")
        combo_teacher14["values"] = tuple(["Select"] + name)
        combo_teacher14.current(0)
        combo_teacher14.grid(row=6, column=7)
        
        teacher14=Label(labelframeright,text="Teacher",font=("times new roman",12,"bold"),padx=2,pady=6)
        teacher14.grid(row=6,column=6,sticky=W,padx=20)
        
        #=========================subject 15=====================================
        lbl_subject15_ref=Label(labelframeright,text="Subject",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_subject15_ref.grid(row=7,column=0,sticky=W)
        entry_subject15=ttk.Entry(labelframeright,textvariable=self.var_subject15,width=16,font=("times new roman",13,"bold"))
        entry_subject15.grid(row=7,column=1)
        
        #==========================Select teacher =======================================
        self.conn = mysql.connector.connect(host="localhost",user="root",password="francis121",database="report")

        # Retrieve values from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT Name FROM teacher")  # Modify with your database column and table names
        name = [Name[0] for Name in cursor.fetchall()]

        combo_teacher15 = ttk.Combobox(labelframeright, textvariable=self.var_teacher15, width=16, font=("times new roman", 13, "bold"), state="readonly")
        combo_teacher15["values"] = tuple(["Select"] + name)
        combo_teacher15.current(0)
        combo_teacher15.grid(row=7, column=3)
        
        teacher15=Label(labelframeright,text="Teacher",font=("times new roman",12,"bold"),padx=2,pady=6)
        teacher15.grid(row=7,column=2,sticky=W,padx=20)
        
        #=========================subject 16=====================================
        lbl_subject16_ref=Label(labelframeright,text="Subject",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_subject16_ref.grid(row=7,column=4,sticky=W)
        entry_subject16=ttk.Entry(labelframeright,textvariable=self.var_subject16,width=16,font=("times new roman",13,"bold"))
        entry_subject16.grid(row=7,column=5)
        
        #==========================Select teacher =======================================
        self.conn = mysql.connector.connect(host="localhost",user="root",password="francis121",database="report")
        # Retrieve values from the database
        cursor = self.conn.cursor()
        cursor.execute("SELECT DISTINCT Name FROM teacher")  # Modify with your database column and table names
        name = [Name[0] for Name in cursor.fetchall()]

        combo_teacher16 = ttk.Combobox(labelframeright, textvariable=self.var_teacher16, width=16, font=("times new roman", 13, "bold"), state="readonly")
        combo_teacher16["values"] = tuple(["Select"] + name)
        combo_teacher16.current(0)
        combo_teacher16.grid(row=7, column=7)
        
        teacher16=Label(labelframeright,text="Teacher",font=("times new roman",12,"bold"),padx=2,pady=6)
        teacher16.grid(row=7,column=6,sticky=W,padx=20)
        #========================================================================================
        #===============table========================================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("arial",12,"bold"))
        Table_Frame.place(x=5,y=350,width=1350,height=350)
        
        lblSearchBy=Label(Table_Frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)
        
        self.serch_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.serch_var,width=20,font=("times new roman",13,"bold"),state="readonly")
        combo_Search["value"]=("SubjectID","Class")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=20,font=("times new roman",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnSearch.grid(row=0,column=3,padx=1)
        
        btnShowAll=Button(Table_Frame,command=self.show_all_data,text="Show All",font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnShowAll.grid(row=0,column=4,padx=1)
        
        #================Show data table===========================================
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=40,width=1350,height=290)
        
        Scrollbar_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scrollbar_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.Cust_Details_Table=ttk.Treeview(details_table,columns=("subjectID","class","classteacher","subject1","teacher1","subject2","teacher2","subject3","teacher3","subject4","teacher4","subject5","teacher5","subject6","teacher6","subject7","teacher7","subject8","teacher8","subject9","teacher9","subject10","teacher10","subject11","teacher11","subject12","teacher12","subject13","teacher13","subject14","teacher14","subject15","teacher15","subject16","teacher16",),xscrollcommand=Scrollbar_x.set,yscrollcommand=Scrollbar_y.set)
        Scrollbar_x.pack(side=BOTTOM,fill=X)
        Scrollbar_y.pack(side=RIGHT,fill=Y)
        
        Scrollbar_x.config(command=self.Cust_Details_Table.xview)
        Scrollbar_y.config(command=self.Cust_Details_Table.yview)
        
        self.Cust_Details_Table.heading("subjectID",text="Subject ID",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("class",text="Class")
        self.Cust_Details_Table.heading("classteacher",text="Class Teacher",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("subject1",text="Subject1",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("teacher1",text="Teacher1",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("subject2",text="Subject2",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("teacher2",text="Teacher2",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("subject3",text="Subject3",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("teacher3",text="Teacher3",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("subject4",text="Subject4",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("teacher4",text="Teacher4",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("subject5",text="Subject5",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("teacher5",text="Teacher5",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("subject6",text="Subject6",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("teacher6",text="Teacher6",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("subject7",text="Subject7",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("teacher7",text="Teacher7",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("subject8",text="Subject8",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("teacher8",text="Teacher8",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("subject9",text="Subject9",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("teacher9",text="Teacher9",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("subject10",text="Subject10",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("teacher10",text="Teacher10",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("subject11",text="Subject11",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("teacher11",text="Teacher11",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("subject12",text="Subject12",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("teacher12",text="Teacher12",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("subject13",text="Subject13",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("teacher13",text="Teacher13",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("subject14",text="Subject14",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("teacher14",text="Teacher14",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("subject15",text="Subject15",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("teacher15",text="Teacher15",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("subject16",text="Subject16",anchor=tk.CENTER)
        self.Cust_Details_Table.heading("teacher16",text="Teacher16",anchor=tk.CENTER)
        
        self.Cust_Details_Table["show"]="headings"
        self.Cust_Details_Table.column("subjectID",width=100,anchor=tk.CENTER)
        self.Cust_Details_Table.column("class",width=100,anchor=tk.CENTER)
        self.Cust_Details_Table.column("classteacher",width=100,anchor=tk.CENTER)
        self.Cust_Details_Table.column("subject1",width=100,anchor=tk.CENTER)
        self.Cust_Details_Table.column("teacher1",width=200,anchor=tk.CENTER)
        self.Cust_Details_Table.column("subject2",width=100,anchor=tk.CENTER)
        self.Cust_Details_Table.column("teacher2",width=200,anchor=tk.CENTER)
        self.Cust_Details_Table.column("subject3",width=100,anchor=tk.CENTER)
        self.Cust_Details_Table.column("teacher3",width=200,anchor=tk.CENTER)
        self.Cust_Details_Table.column("subject4",width=100,anchor=tk.CENTER)
        self.Cust_Details_Table.column("teacher4",width=200,anchor=tk.CENTER)
        self.Cust_Details_Table.column("subject5",width=100,anchor=tk.CENTER)
        self.Cust_Details_Table.column("teacher5",width=200,anchor=tk.CENTER)
        self.Cust_Details_Table.column("subject6",width=100,anchor=tk.CENTER)
        self.Cust_Details_Table.column("teacher6",width=200,anchor=tk.CENTER)
        self.Cust_Details_Table.column("subject7",width=100,anchor=tk.CENTER)
        self.Cust_Details_Table.column("teacher7",width=200,anchor=tk.CENTER)
        self.Cust_Details_Table.column("subject8",width=100,anchor=tk.CENTER)
        self.Cust_Details_Table.column("teacher8",width=200,anchor=tk.CENTER)
        self.Cust_Details_Table.column("subject9",width=100,anchor=tk.CENTER)
        self.Cust_Details_Table.column("teacher9",width=200,anchor=tk.CENTER)
        self.Cust_Details_Table.column("subject10",width=100,anchor=tk.CENTER)
        self.Cust_Details_Table.column("teacher10",width=200,anchor=tk.CENTER)
        self.Cust_Details_Table.column("subject11",width=100,anchor=tk.CENTER)
        self.Cust_Details_Table.column("teacher11",width=200,anchor=tk.CENTER)
        self.Cust_Details_Table.column("subject12",width=100,anchor=tk.CENTER)
        self.Cust_Details_Table.column("teacher12",width=200,anchor=tk.CENTER)
        self.Cust_Details_Table.column("subject13",width=100,anchor=tk.CENTER)
        self.Cust_Details_Table.column("teacher13",width=200,anchor=tk.CENTER)
        self.Cust_Details_Table.column("subject14",width=100,anchor=tk.CENTER)
        self.Cust_Details_Table.column("teacher14",width=200,anchor=tk.CENTER)
        self.Cust_Details_Table.column("subject15",width=100,anchor=tk.CENTER)
        self.Cust_Details_Table.column("teacher15",width=200,anchor=tk.CENTER)
        self.Cust_Details_Table.column("subject16",width=100,anchor=tk.CENTER)
        self.Cust_Details_Table.column("teacher16",width=200,anchor=tk.CENTER)
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cusrsor)
        self.fetch_data()
        
    def add_data(self):
        if self.var_subjectID.get() == "" or self.var_class.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="francis121", database="report")
                my_cursor = conn.cursor()
                # Check if subjectID  already exists
                my_cursor.execute("SELECT * FROM subject WHERE subjectID = %s", (self.var_subjectID.get(),))
                existing_record = my_cursor.fetchone()

                if existing_record:
                    messagebox.showerror("Error", "Subject ID already exists. Please enter a different ID.", parent=self.root)
                else:
                    my_cursor.execute("insert into subject values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_subjectID.get(),
                        self.var_class.get(),
                        self.var_classteacher.get(),
                        self.var_subject1.get(),
                        self.var_teacher1.get(),
                        self.var_subject2.get(),
                        self.var_teacher2.get(),
                        self.var_subject3.get(),
                        self.var_teacher3.get(),
                        self.var_subject4.get(),
                        self.var_teacher4.get(),
                        self.var_subject5.get(),
                        self.var_teacher5.get(),
                        self.var_subject6.get(),
                        self.var_teacher6.get(),
                        self.var_subject7.get(),
                        self.var_teacher7.get(),
                        self.var_subject8.get(),
                        self.var_teacher8.get(),
                        self.var_subject9.get(),
                        self.var_teacher9.get(),
                        self.var_subject10.get(),
                        self.var_teacher10.get(),
                        self.var_subject11.get(),
                        self.var_teacher11.get(),
                        self.var_subject12.get(),
                        self.var_teacher12.get(),
                        self.var_subject13.get(),
                        self.var_teacher13.get(),
                        self.var_subject14.get(),
                        self.var_teacher14.get(),
                        self.var_subject15.get(),
                        self.var_teacher15.get(),
                        self.var_subject16.get(),
                        self.var_teacher16.get()
                        
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    self.reset()
                    messagebox.showinfo("Success", "Subject has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)
          
    def fetch_data(self):
       conn=mysql.connector.connect(host="localhost",username="root",password="francis121",database="report")
       my_cursor=conn.cursor()
       my_cursor.execute("select *from subject")
       rows=my_cursor.fetchall()
       if len(rows)!=0:
           self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
           for i in rows:
               self.Cust_Details_Table.insert("",END,values=i)
               conn.commit()
           conn.close()
            
    def get_cusrsor(self,event=""):
       cusrsor_row=self.Cust_Details_Table.focus()
       content=self.Cust_Details_Table.item(cusrsor_row)
       row=content["values"]
        
       self.var_subjectID.set(row[0]),
       self.var_class.set(row[1]),
       self.var_classteacher.set(row[2]),
       self.var_subject1.set(row[3]),
       self.var_teacher1.set(row[4]),
       self.var_subject2.set(row[5]),
       self.var_teacher2.set(row[6]),
       self.var_subject3.set(row[7]),
       self.var_teacher3.set(row[8]),
       self.var_subject4.set(row[9]),
       self.var_teacher4.set(row[10]),
       self.var_subject5.set(row[11]),
       self.var_teacher5.set(row[12]),
       self.var_subject6.set(row[13]),
       self.var_teacher6.set(row[14]),
       self.var_subject7.set(row[15]),
       self.var_teacher7.set(row[16]),
       self.var_subject8.set(row[17]),
       self.var_teacher8.set(row[18]),
       self.var_subject9.set(row[19]),
       self.var_teacher9.set(row[20]),
       self.var_subject10.set(row[21]),
       self.var_teacher10.set(row[22]),
       self.var_subject11.set(row[23]),
       self.var_teacher11.set(row[24]),
       self.var_subject12.set(row[25]),
       self.var_teacher12.set(row[26]),
       self.var_subject13.set(row[27]),
       self.var_teacher13.set(row[28]),
       self.var_subject14.set(row[29]),
       self.var_teacher14.set(row[30]),
       self.var_subject15.set(row[31]),
       self.var_teacher15.set(row[32]),
       self.var_subject16.set(row[33]),
       self.var_teacher16.set(row[34])
        
    def update(self):
       if self.var_class.get()=="Select"and self.var_classteacher.get()=="Select":
           messagebox.showerror("Error","Please enter Class Teacher and Subjects",parent=self.root)
       else:
           conn=mysql.connector.connect(host="localhost",username="root",password="francis121",database="report")
           my_cursor=conn.cursor()
           my_cursor.execute("update subject set Class=%s,Classteacher=%s,Subject1=%s,Teacher1=%s,Subject2=%s,Teacher2=%s,Subject3=%s,Teacher3=%s,Subject4=%s,Teacher4=%s,Subject5=%s,Teacher5=%s,Subject6=%s,Teacher6=%s,Subject7=%s,Teacher7=%s,Subject8=%s,Teacher8=%s,Subject9=%s,Teacher9=%s,Subject10=%s,Teacher10=%s,Subject11=%s,Teacher11=%s,Subject12=%s,Teacher12=%s,Subject13=%s,Teacher13=%s,Subject14=%s,Teacher14=%s,Subject15=%s,Teacher15=%s,Subject16=%s,Teacher16=%s where subjectID=%s",(
                   self.var_class.get(),
                   self.var_classteacher.get(),
                   self.var_subject1.get(),
                   self.var_teacher1.get(),
                   self.var_subject2.get(),
                   self.var_teacher2.get(),
                   self.var_subject3.get(),
                   self.var_teacher3.get(),
                   self.var_subject4.get(),
                   self.var_teacher4.get(),
                   self.var_subject5.get(),
                   self.var_teacher5.get(),
                   self.var_subject6.get(),
                   self.var_teacher6.get(),
                   self.var_subject7.get(),
                   self.var_teacher7.get(),
                   self.var_subject8.get(),
                   self.var_teacher8.get(),
                   self.var_subject9.get(),
                   self.var_teacher9.get(),
                   self.var_subject10.get(),
                   self.var_teacher10.get(),
                   self.var_subject11.get(),
                   self.var_teacher11.get(),
                   self.var_subject12.get(),
                   self.var_teacher12.get(),
                   self.var_subject13.get(),
                   self.var_teacher13.get(),
                   self.var_subject14.get(),
                   self.var_teacher14.get(),
                   self.var_subject15.get(),
                   self.var_teacher15.get(),
                   self.var_subject16.get(),
                   self.var_teacher16.get(),
                   self.var_subjectID.get()         
           ))
           conn.commit()
           self.fetch_data()
           conn.close()
           self.reset()
           messagebox.showinfo("Update","Subject details has been updated sucessfully",parent=self.root)
    def Delete(self):
       Delete=messagebox.askyesno("Report Management System","Do you want to delete this class details",parent=self.root)
       if Delete>0:
           conn=mysql.connector.connect(host="localhost",username="root",password="francis121",database="report")
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
    def reset(self):
        try:
            # Fetch the last reference from the database
            last_reference = self.get_last_reference()

            if last_reference is not None:
                # Increment the last reference by 1
                next_reference = str(int(last_reference) + 1)
            else:
                # If there's no existing reference, set a default value
                next_reference = "1000"

            # Set the incremented reference to self.var_ref
            self.var_subjectID.set(next_reference)

        except Exception as e:
            print(f"Error fetching or incrementing reference: {e}")
        self.var_class.set("Select"),
        self.var_classteacher.set("Select"),
        self.var_subject1.set(""),
        self.var_teacher1.set("Select"),
        self.var_subject2.set(""),
        self.var_teacher2.set("Select"),
        self.var_subject3.set(""),
        self.var_teacher3.set("Select"),
        self.var_subject4.set(""),
        self.var_teacher4.set("Select"),
        self.var_subject5.set(""),
        self.var_teacher5.set("Select"),
        self.var_subject6.set(""),
        self.var_teacher6.set("Select"),
        self.var_subject7.set(""),
        self.var_teacher7.set("Select"),
        self.var_subject8.set(""),
        self.var_teacher8.set("Select"),
        self.var_subject9.set(""),
        self.var_teacher9.set("Select"),
        self.var_subject10.set(""),
        self.var_teacher10.set("Select"),
        self.var_subject11.set(""),
        self.var_teacher11.set("Select"),
        self.var_subject12.set(""),
        self.var_teacher12.set("Select"),
        self.var_subject13.set(""),
        self.var_teacher13.set("Select"),
        self.var_subject14.set(""),
        self.var_teacher14.set("Select"),
        self.var_subject15.set(""),
        self.var_teacher15.set("Select"),
        self.var_subject16.set(""),
        self.var_teacher16.set("Select"),
        #x=random.randint(1000,9999)
        #self.var_subjectID.set(str(x))
        
    def search(self):
       conn=mysql.connector.connect(host="localhost",user="root",password="francis121",database="report")
       my_cursor=conn.cursor()
       my_cursor.execute("SELECT * FROM subject WHERE " + str(self.serch_var.get()) + " LIKE %s", ('%' + str(self.txt_search.get()) + '%',))

       rows=my_cursor.fetchall()
       if len(rows)!=0:
           self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
           for i in rows:
               self.Cust_Details_Table.insert("",END,values=i)
           conn.commit()
       conn.close()
       
    def show_all_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="francis121", database="report")
        my_cursor = conn.cursor()

        my_cursor.execute("SELECT * FROM subject")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            # Assuming self.Cust_Details_Table is your treeview widget
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())

            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)

            conn.commit()

        conn.close()
       
    def get_last_reference(self):
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="francis121", database="report")
                cursor = conn.cursor()

                # Execute a query to get the maximum reference value from the database
                cursor.execute("SELECT MAX(subjectID) FROM subject")

                # Fetch the result
                result = cursor.fetchone()

                # Close the database connection
                conn.close()

                # If there are no existing references, return None
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
    obj=Subject(root)
    root.mainloop()