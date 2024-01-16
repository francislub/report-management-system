from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import tkinter as tk
from tkinter import messagebox
import tkinter.messagebox
#import mysql.connector
import pymysql
from time import strftime
from datetime import datetime

class cL:
    def __init__(self,root):
        self.root=root
        self.root.title("Report Management System")
        self.root.geometry("1150x550+200+100")
        self.root.wm_attributes("-toolwindow", True)
        self.root.wm_attributes("-topmost", True)
        #self.root.overrideredirect(True) 
        #self.root.geometry("1550x800+0+0")
        
        #=====================title=======================================================
        lbl_title=Label(self.root,text="Add New Class",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1150,height=50)
        #===================2st Image===log======================================================
        Image2=Image.open(r"C:\Users\USER\Desktop\summer\PYTHON PROJECTS TKINTER\REPT\images\logo.PNG")
        Image2=Image2.resize((100,40),Image.LANCZOS)
        self.photoImage2=ImageTk.PhotoImage(Image2)
        
        lblimg=Label(self.root,image=self.photoImage2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)
        #===================labelframe====================================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Add New Class",font=("times new roman",18,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=350)
        
        lbl_classID=Label(labelframeleft,text="classID",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_classID.grid(row=0,column=0,sticky=W,padx=20)
        
        self.var_classID=StringVar()
        x=random.randint(1000,9999)
        self.var_classID.set(str(x))
        entry_classID=ttk.Entry(labelframeleft,textvariable=self.var_classID,width=29,font=("times new roman",13,"bold"),state="readonly")
        entry_classID.grid(row=0,column=1,sticky=W)
        last_reference = self.get_last_reference()  # Function to get the last reference
        
        if last_reference is not None:
            next_reference = str(int(last_reference) + 1)
        else:
            next_reference = "1001"  # Initial reference
        
        self.var_classID.set(next_reference)
        
        lbl_class=Label(labelframeleft,text="Class",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_class.grid(row=1,column=0,sticky=W,padx=20)
        
        self.var_class=StringVar()
        entry_class=ttk.Entry(labelframeleft,textvariable=self.var_class,width=29,font=("times new roman",13,"bold"))
        entry_class.grid(row=1,column=1,sticky=W)
        
        #================btn===========================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)
        
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.Delete,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnReset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnReset.grid(row=0,column=3,padx=1)
        
        btnExit=Button(btn_frame,text="Exit",font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnExit.grid(row=0,column=4,padx=1)
        
        #================table frame search system===========================================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Class",font=("arial",12,"bold"))
        Table_Frame.place(x=500,y=55,width=500,height=350)
        
        Scrollbar_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        Scrollbar_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)
        
        self.class_table=ttk.Treeview(Table_Frame,columns=("classID","class"),xscrollcommand=Scrollbar_x.set,yscrollcommand=Scrollbar_y.set)
        Scrollbar_x.pack(side=BOTTOM,fill=X)
        Scrollbar_y.pack(side=RIGHT,fill=Y)
        
        Scrollbar_x.config(command=self.class_table.xview)
        Scrollbar_y.config(command=self.class_table.yview)
        
        self.class_table.heading("classID",text="Class ID",anchor=tk.CENTER)
        self.class_table.heading("class",text="Class",anchor=tk.CENTER)
        
        self.class_table["show"]="headings"
        s = ttk.Style(root)
        s.theme_use("clam")
        
        s.configure(".", font=('Helvetice',11))
        s.configure("Treeview.Heading",foreground='red',font=('Helvetica',11,"bold"))
        
        self.class_table.column("classID",width=100,anchor=tk.CENTER)
        self.class_table.column("class",width=100,anchor=tk.CENTER)
        
        self.class_table.pack(fill=BOTH,expand=1)
        self.class_table.bind("<ButtonRelease-1>",self.get_cusrsor)
        self.fetch_data()
        
        self.class_table.tag_configure("evenrow", background="#f0f0f0")
        self.class_table.tag_configure("oddrow", background="#ffffff")
        
    def add_data(self):
        if self.var_classID.get()==""or self.var_class.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=pymysql.connect(host="localhost",user="root",database="report")
                my_cursor=conn.cursor()
                # Check if term  already exists
                my_cursor.execute("SELECT * FROM class WHERE classID = %s", (self.var_classID.get(),))
                existing_record = my_cursor.fetchone()

                if existing_record:
                    messagebox.showerror("Error", "Class ID already exists. Please enter a different ID.", parent=self.root)
                else:
                    my_cursor.execute("insert into class values(%s,%s)",(
                        self.var_classID.get(),
                        self.var_class.get()
                        
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    self.reset_data()
                    messagebox.showinfo("Success","New Class Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"Something went wrong:{str(es)}",parent=self.root) 
    #fetch_data()
    def fetch_data(self):
        conn=pymysql.connect(host="localhost",user="root",database="report")
        my_cursor=conn.cursor()
        my_cursor.execute("select *from class")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.class_table.delete(*self.class_table.get_children())
            for i in rows:
                self.class_table.insert("",END,values=i)
                conn.commit()
            conn.close()
            for i, item in enumerate(self.class_table.get_children()):
                if i % 2 == 0:
                        self.class_table.item(item, tags=("oddrow",))
                else:
                        self.class_table.item(item, tags=("evenrow",))
                        
    def get_cusrsor(self,event=""):
        cusrsor_row=self.class_table.focus()
        content=self.class_table.item(cusrsor_row)
        row=content["values"]
        
        self.var_classID.set(row[0]),
        self.var_class.set(row[1])
        
    #update function
    def update(self):
        if self.var_class.get()=="":
            messagebox.showerror("Error","Please enter A Class",parent=self.root)
        else:
            conn=pymysql.connect(host="localhost",user="root",database="report")
            my_cursor=conn.cursor()
            my_cursor.execute("update  class set class=%s where classID=%s",(
                    
                    self.var_class.get(),
                    self.var_classID.get()
                    
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            self.reset_data()
            messagebox.showinfo("Update","Class has been updated sucessfully",parent=self.root)
    #delete============================================================
    def Delete(self):
        Delete=messagebox.askyesno("Report Management System","Do you want to delete this Class",parent=self.root)
        if Delete>0:
            conn=pymysql.connect(host="localhost",user="root",database="report")
            my_cursor=conn.cursor()
            query="delete from class where classID=%s"
            value=(self.var_classID.get(),)
            my_cursor.execute(query,value)
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        self.reset_data()
        messagebox.showinfo("Delete","Class has been deleted sucessfully",parent=self.root)
        
    #============================reset===================================================
    def reset_data(self):
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
            self.var_classID.set(next_reference)

        except Exception as e:
            print(f"Error fetching or incrementing reference: {e}")
        self.var_class.set("")
        #x=random.randint(1000,9999)
        #self.var_classID.set(str(x))
        
    def get_last_reference(self):
            try:
                conn = pymysql.connect(host="localhost", user="root", database="report")
                cursor = conn.cursor()

                # Execute a query to get the maximum reference value from the database
                cursor.execute("SELECT MAX(classID) FROM class")

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
    obj=cL(root)
    root.mainloop()