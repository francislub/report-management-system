from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter as tk
import mysql.connector
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
        self.var_mark1=StringVar()
        self.var_mark2=StringVar()
        self.var_grade1=StringVar()
        self.var_comm1=StringVar()
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
        #====================labels and entrys=========================================
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
        
        #==========================Select Class ========================================
        self.var_=StringVar()
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
        
        def get_selected_class():
            # Replace this function with your code to fetch the user's name from the database
            return "S.1"  
        
        # Retrieve user information from the database
        selected_cl = get_selected_class()

        # Label to display the user's name
        label_selected_class = Label(labelframeleft, text=f"SET GRADING SYSTEM FOR {selected_cl}", padx=5,font=("times new roman",16,"bold"))
        label_selected_class.place(x=0,y=100,width=600,height=20)
        
        #================btn===========================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=400,y=10,width=250,height=80)
        
        btnAdd=Button(btn_frame,text="Add",font=("arial",11,"bold"),bg="black",fg="gold",width=8)
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
        lbl_subject1_ref=Label(labelframeright,text="From",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_subject1_ref.grid(row=0,column=1,sticky=W ,padx=40)
        
        teacher1=Label(labelframeright,text="To",font=("times new roman",12,"bold"),padx=2,pady=6)
        teacher1.grid(row=0,column=3,sticky=W,padx=40)
        
        lbl_subject2_ref=Label(labelframeright,text="Grade",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_subject2_ref.grid(row=0,column=5,sticky=W ,padx=40)
        
        teacher2=Label(labelframeright,text="Comment",font=("times new roman",12,"bold"),padx=2,pady=6)
        teacher2.grid(row=0,column=7,sticky=W,padx=40)
        
        #=========================Entries=====================================
        entry_mark1=ttk.Entry(labelframeright,textvariable=self.var_mark1,width=16,font=("times new roman",13,"bold"))
        entry_mark1.grid(row=1,column=1,padx=40,pady=5)
        
        entry_mark2=ttk.Entry(labelframeright,textvariable=self.var_mark2,width=16,font=("times new roman",13,"bold"))
        entry_mark2.grid(row=1,column=3,padx=40,pady=5)
        
        entry_grade1=ttk.Entry(labelframeright,textvariable=self.var_grade1,width=16,font=("times new roman",13,"bold"))
        entry_grade1.grid(row=1,column=5,padx=40,pady=5)
        
        entry_comm1=ttk.Entry(labelframeright,textvariable=self.var_comm1,width=16,font=("times new roman",13,"bold"))
        entry_comm1.grid(row=1,column=7,padx=40,pady=5)
        
        entry_mark1_1=ttk.Entry(labelframeright,textvariable=self.var_mark1_1,width=16,font=("times new roman",13,"bold"))
        entry_mark1_1.grid(row=2,column=1,padx=40,pady=5)
        
        entry_mark2_1=ttk.Entry(labelframeright,textvariable=self.var_mark2_1,width=16,font=("times new roman",13,"bold"))
        entry_mark2_1.grid(row=2,column=3,padx=40,pady=5)
        
        entry_grade1_1=ttk.Entry(labelframeright,textvariable=self.var_grade1_1,width=16,font=("times new roman",13,"bold"))
        entry_grade1_1.grid(row=2,column=5,padx=40,pady=5)
        
        entry_comm1_1=ttk.Entry(labelframeright,textvariable=self.var_comm1_1,width=16,font=("times new roman",13,"bold"))
        entry_comm1_1.grid(row=2,column=7,padx=40,pady=5)

        entry_mark1_2=ttk.Entry(labelframeright,textvariable=self.var_mark1_2,width=16,font=("times new roman",13,"bold"))
        entry_mark1_2.grid(row=3,column=1,padx=40,pady=5)
        
        entry_mark2_2=ttk.Entry(labelframeright,textvariable=self.var_mark2_2,width=16,font=("times new roman",13,"bold"))
        entry_mark2_2.grid(row=3,column=3,padx=40,pady=5)
        
        entry_grade1_2=ttk.Entry(labelframeright,textvariable=self.var_grade1_2,width=16,font=("times new roman",13,"bold"))
        entry_grade1_2.grid(row=3,column=5,padx=40,pady=5)
        
        entry_comm1_2=ttk.Entry(labelframeright,textvariable=self.var_comm1_2,width=16,font=("times new roman",13,"bold"))
        entry_comm1_2.grid(row=3,column=7,padx=40,pady=5)

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
        entry_grade1_11.grid(row=11,column=5,padx=40,pady=5)
        
        entry_comm1_11=ttk.Entry(labelframeright,textvariable=self.var_comm1_11,width=16,font=("times new roman",13,"bold"))
        entry_comm1_11.grid(row=11,column=7,padx=40,pady=5)
        
        #========================================================================================
        
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
    obj=Grade(root)
    root.mainloop()