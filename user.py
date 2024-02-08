from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter as tk
#import mysql.connector
import pymysql
import random
from tkinter import filedialog
from tkcalendar import DateEntry
from datetime import datetime
import tkinter.messagebox
from tkinter import messagebox
class User:
    def __init__(self,root):
        self.root=root
        self.root.title("Report Management System")
        self.root.geometry("1550x800+0+0")
        #self.root.overrideredirect(True)
        #========================variables=======================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_username=StringVar()
        self.var_email=StringVar()
        self.var_role=StringVar()
        self.var_password1=StringVar()
        self.var_password2=StringVar()
        self.var_image=StringVar()
        
        #=====================title=======================================================
        lbl_title=Label(self.root,text="CREATE USER'S ACCOUNTS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1355,height=50)
        #===================2st Image===log======================================================
        Image2=Image.open(r"C:\Users\ENG. FRANCIS\Desktop\summer\PYTHON PROJECTS TKINTER\REPT\images\logo.PNG")
        Image2=Image2.resize((100,40),Image.LANCZOS)
        self.photoImage2=ImageTk.PhotoImage(Image2)
        
        lblimg=Label(self.root,image=self.photoImage2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)
        
        #===========Left Menu==============
        #LeftMenu = Frame(self.root,bd=2,relief=RIDGE, bg="white")
        #LeftMenu.place(x=5,y=50,width=420,height=170)
        
        # Placeholder for user's photo (Assumed as a box)
        #user_photo_placeholder = Label(LeftMenu, text="User Photo", bg="lightgray", height=10)
        #user_photo_placeholder.pack(side="top", fill="x")
        
        #===================labelframe====================================================
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="User Details",font=("times new roman",18,"bold"),padx=2)
        labelframeleft.place(x=5,y=60,width=425,height=550)
        #====================labels and entrys=========================================
        lbl_student_ref = Label(labelframeleft, text="User Ref", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lbl_student_ref.grid(row=0, column=0, sticky=W)
        
        entry_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref, width=29, font=("times new roman", 13, "bold"), state="readonly")
        entry_ref.grid(row=0, column=1)
        
        last_reference = self.get_last_reference()  # Function to get the last reference
        
        if last_reference is not None:
            next_reference = str(int(last_reference) + 1)
        else:
            next_reference = "1001"  # Initial reference
        
        self.var_ref.set(next_reference)

            
        uname=Label(labelframeleft,text="User Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        uname.grid(row=1,column=0,sticky=W)
        txtuname=ttk.Entry(labelframeleft,textvariable=self.var_username,width=29,font=("times new roman",13,"bold"))
        txtuname.grid(row=1,column=1)
        
        label_email=Label(labelframeleft,text="email",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_email.grid(row=2,column=0,sticky=W)
        entry_email = ttk.Entry(labelframeleft, textvariable=self.var_email, width=29, font=("times new roman", 13, "bold"))
        entry_email.grid(row=2, column=1)
        
        label_role=Label(labelframeleft,text="Role",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_role.grid(row=3,column=0,sticky=W)
        combo_role=ttk.Combobox(labelframeleft,textvariable=self.var_role,width=27,font=("times new roman",13,"bold"),state="readonly")
        combo_role["value"]=("Select","DOS","Teacher","Secretory")
        combo_role.current(0)
        combo_role.grid(row=3,column=1)
        
        lblpassword1=Label(labelframeleft,text="Password",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblpassword1.grid(row=4,column=0,sticky=W)
        txtpassword1=ttk.Entry(labelframeleft,textvariable=self.var_password1,width=29,font=("times new roman",13,"bold"), show="*")
        txtpassword1.grid(row=4,column=1)
        
        lblpassword2=Label(labelframeleft,text="Confirm Password",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblpassword2.grid(row=5,column=0,sticky=W)
        txtpassword2=ttk.Entry(labelframeleft,textvariable=self.var_password2,width=29,font=("times new roman",13,"bold"), show="*")
        txtpassword2.grid(row=5,column=1)
        
        def open_image():
            file_path = filedialog.askopenfilename()
            image = Image.open(file_path)
            # Update the entry widget with the file name
            txtimage.delete(0, END)
            txtimage.insert(0, file_path)

        lblimage=Label(labelframeleft,text="Image",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblimage.grid(row=8,column=0,sticky=W)
        txtimage=ttk.Entry(labelframeleft,textvariable=self.var_image,width=29,font=("times new roman",13,"bold"))
        txtimage.grid(row=8,column=1)
        btn_open=Button(labelframeleft,text="Open Image", command=open_image,font=("times new roman",13,"bold"))
        btn_open.grid(row=9,column=0,sticky=W)
        
        #================btn===========================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=760,height=50)
        
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.Delete,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnReset.grid(row=0,column=3,padx=1)
        
        btnExit=Button(btn_frame,text="Exit",font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnExit.grid(row=0,column=4,padx=1)
        
        #===============table===============
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View User's Details",font=("arial",12,"bold"))
        Table_Frame.place(x=435,y=50,width=915,height=490)
        
        #================Show data table===========================================
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=890,height=400)
        
        Scrollbar_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scrollbar_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.Cust_Details_Table=ttk.Treeview(details_table,columns=("ref","username","email","role","password1","password2","image"),xscrollcommand=Scrollbar_x.set,yscrollcommand=Scrollbar_y.set)
        Scrollbar_x.pack(side=BOTTOM,fill=X)
        Scrollbar_y.pack(side=RIGHT,fill=Y)
        

        Scrollbar_x.config(command=self.Cust_Details_Table.xview)
        Scrollbar_y.config(command=self.Cust_Details_Table.yview)
        
        self.Cust_Details_Table.heading("ref",text="Refer No", anchor=tk.CENTER)
        self.Cust_Details_Table.heading("username",text="User Name", anchor=tk.CENTER)
        self.Cust_Details_Table.heading("email",text="Email", anchor=tk.CENTER)
        self.Cust_Details_Table.heading("role",text="Role", anchor=tk.CENTER)
        self.Cust_Details_Table.heading("password1",text="Password", anchor=tk.CENTER)
        self.Cust_Details_Table.heading("password2",text="Confirm Password", anchor=tk.CENTER)
        self.Cust_Details_Table.heading("image",text="Image", anchor=tk.CENTER)
        
        self.Cust_Details_Table["show"]="headings"
        s = ttk.Style(root)
        s.theme_use("clam")
        
        s.configure(".", font=('Helvetice',11))
        s.configure("Treeview.Heading",foreground='red',font=('Helvetica',11,"bold"))
        
        self.Cust_Details_Table.column("ref",width=100, anchor=tk.CENTER)
        self.Cust_Details_Table.column("username",width=300, anchor=tk.CENTER)
        self.Cust_Details_Table.column("email",width=300, anchor=tk.CENTER)
        self.Cust_Details_Table.column("role",width=200, anchor=tk.CENTER)
        self.Cust_Details_Table.column("password1",width=250, anchor=tk.CENTER)
        self.Cust_Details_Table.column("password2",width=250, anchor=tk.CENTER)
        self.Cust_Details_Table.column("image",width=100, anchor=tk.CENTER)
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cusrsor)
        self.fetch_data()
        
        # Define tag configuration for odd and even rows
        self.Cust_Details_Table.tag_configure("evenrow", background="#f0f0f0")
        self.Cust_Details_Table.tag_configure("oddrow", background="#ffffff")
        
    def add_data(self):
        if self.var_username.get() == "" or self.var_email.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.var_password1.get() != self.var_password2.get():
            messagebox.showerror("Error", "Passwords do not match", parent=self.root)
        else:
            try:
                conn = pymysql.connect(host="localhost", user="root", database="report")
                my_cursor = conn.cursor()
                # Check if subjectID  already exists
                my_cursor.execute("SELECT * FROM user WHERE ref = %s", (self.var_ref.get(),))
                existing_record = my_cursor.fetchone()

                if existing_record:
                    messagebox.showerror("Error", "User reference already exists. Please enter a different reference.", parent=self.root)
                else:
                    my_cursor.execute("insert into user values(%s, %s, %s, %s, %s, %s, %s)", (
                        self.var_ref.get(),
                        self.var_username.get(),
                        self.var_email.get(),
                        self.var_role.get(),
                        self.var_password1.get(),
                        self.var_password2.get(),
                        self.var_image.get(),
                    ))
                    conn.commit()
                    self.fetch_data()
                    self.reset()
                    conn.close()
                    messagebox.showinfo("Success", "User has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
       conn=pymysql.connect(host="localhost",user="root",database="report")
       my_cursor=conn.cursor()
       my_cursor.execute("select *from user")
       rows=my_cursor.fetchall()
       if len(rows)!=0:
           self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
           for i in rows:
               self.Cust_Details_Table.insert("",END,values=i)
               conn.commit()
           conn.close()
           
           for i, item in enumerate(self.Cust_Details_Table.get_children()):
                if i % 2 == 0:
                        self.Cust_Details_Table.item(item, tags=("oddrow",))
                else:
                        self.Cust_Details_Table.item(item, tags=("evenrow",))
            
    def get_cusrsor(self,event=""):
       cusrsor_row=self.Cust_Details_Table.focus()
       content=self.Cust_Details_Table.item(cusrsor_row)
       row=content["values"]
        
       self.var_ref.set(row[0]),
       self.var_username.set(row[1]),
       self.var_email.set(row[2]),
       self.var_role.set(row[3]),
       self.var_password1.set(row[4]),
       self.var_password2.set(row[5]),
       self.var_image.set(row[6])
        
    def update(self):
       if self.var_username.get()=="":
           messagebox.showerror("Error","Please enter the user details to be deleted",parent=self.root)
       elif self.var_password1.get() != self.var_password2.get():
            messagebox.showerror("Error", "Passwords do not match", parent=self.root)
       else:
           conn=pymysql.connect(host="localhost",user="root",database="report")
           my_cursor=conn.cursor()
           my_cursor.execute("update user set Username=%s,Email=%s,Role=%s,Password1=%s,Password2=%s,image=%s where Ref=%s",(
                   self.var_username.get(),
                   self.var_email.get(),
                   self.var_role.get(),
                   self.var_password1.get(),
                   self.var_password2.get(),
                   self.var_image.get(),
                   self.var_ref.get()
           ))
           conn.commit()
           self.fetch_data()
           conn.close()
           self.reset()
           messagebox.showinfo("Update","User details has been updated sucessfully",parent=self.root)
    def Delete(self):
       Delete=messagebox.askyesno("Report Management System","Do you want to delete this User",parent=self.root)
       if Delete>0:
           conn=pymysql.connect(host="localhost",user="root",database="report")
           my_cursor=conn.cursor()
           query="delete from user where Ref=%s"
           value=(self.var_ref.get(),)
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
            self.var_ref.set(next_reference)

        except Exception as e:
            print(f"Error fetching or incrementing reference: {e}")

        # Reset other variables
        self.var_username.set("")
        self.var_email.set("")
        self.var_role.set("Select")
        self.var_password1.set("")
        self.var_password2.set("")
        self.var_image.set("")
       
    def get_last_reference(self):
            try:
                conn = pymysql.connect(host="localhost", user="root", database="report")
                cursor = conn.cursor()

                # Execute a query to get the maximum reference value from the database
                cursor.execute("SELECT MAX(ref) FROM user")

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

    #def Exit(self):
    #       self.Exit= tkinter.messagebox.askyesno("Hotel Management System","confirm if you want to exit",parent=self.root)
    #       if self.Exit>0:
    #           self.root.destroy()
    #           show_dashboard()

                    
if __name__=="__main__":
    root=Tk()
    obj=User(root)
    root.mainloop()