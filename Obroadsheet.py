from tkinter import *
from time import strftime
from tkinter import ttk
import tkinter as tk
from tkinter import Toplevel, Label
#import mysql.connector
import pymysql
from tkinter import messagebox
class Osheet:
    def __init__(self, root,selected_class):
        self.root = root
        #self.ClassLbl = Toplevel(self.root)
        self.root.geometry("1450x730+0+0")
        self.root.configure(bg="black")
        #self.root.overrideredirect(True)
        self.selected_class =selected_class
        self.table_frame = Canvas(root)
        self.canvas = Canvas(self.table_frame, bg="white", highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.table_frame.grid_rowconfigure(0, weight=1)
        self.table_frame.grid_columnconfigure(0, weight=1)
        self.canvas.bind("<Configure>", self.update_scrollregion)
        self.entries = []
        #self.create_table(rows, columns,students)
        self.current_row = 0
        self.current_column = 0
        self.bind_arrow_keys()
        self.root.title("Report Management System | Developed by LarksTeckHub")
        #self.rows = rows
        #self.columns = columns
        
        self.create_table()

        # Initialize the UI components and create the table
        #========]'] 
        # hn============title================
        title= Label(self.root, text="ST. PETER'S SECONDARY SCHOOL KIBUZI",compound=LEFT, font=("times new roman",30,"bold"),bg="#010c48",fg="white",anchor="w" ,padx=300).place(x=0,y=0,relwidth=1)
        title2= Label(self.root, text=f"BROADSHEET FOR {selected_class}",compound=CENTER, font=("times new roman",20,"bold"),bg="#010c48",fg="white",anchor="w",padx=600).place(x=0,y=40,relwidth=3)
        title3= Label(self.root, text="SCORE AND GRADE OF STUDENTS",compound=CENTER, font=("times new roman",16,"bold"),bg="#010c48",fg="white",anchor="w",padx=550).place(x=0,y=70,relwidth=1)
        
        #self.label_subject = Label(root, text=f"Subject: {selected_subject}", font=("times new roman", 40, "bold"),
        #                           bg="#010c48", fg="white", anchor="w", padx=20)
        #self.label_subject.place(x=900, y=0, relwidth=1, height=70)
                
        #========clock================
        # Function to display time on the label
        def time():
            string = f" Date: {strftime('%d-%m-%Y')}\t Time: {strftime('%H:%M:%S')}"  # Format the time string
            self.lbl_clock.config(text=string)  # Update the label with the current time
            self.lbl_clock.after(1000, time)  # Call the time function after 1000ms (1 second)

        # Create a label for the clock
        self.lbl_clock = Label(self.root, text="", font=("times new roman", 15), bg="#010c48", fg="white")
        self.lbl_clock.place(x=1000, y=70, height=30)

        # Call the time function to start displaying the time
        time()
          
        #===========Class Menu==============
        ClassLbl = Frame(self.root,relief=RIDGE, bg="#4d636d")
        ClassLbl.place(x=0,y=100,width=350,height=40)
        
        self.lbl_total_students = Label(ClassLbl, text="Total Students: ", font=('Arial', 12, 'bold'), fg="white", bg="#4d636d")
        self.lbl_total_students.grid(row=0, column=1, padx=0, pady=3)
        
        #self.lblClass = Label(ClassLbl, text=f"Class: {selected_class}", font=('Arial', 12, 'bold'), fg="white", bg="#4d636d")
        #self.lblClass.grid(row=0, column=2, padx=75, pady=3)
        
        ClassMenu = Frame(self.root,bd=2,relief=RIDGE, bg="white")
        ClassMenu.place(x=350,y=100,width=1020,height=40)
        #================================
        #self.create_table(rows=len(students) + 1, columns=15)
        
        Unit1 = Button(ClassMenu, text="Unit 1",font=("arial",11,"bold"),bg="black",fg="gold",width=12)
        Unit1.grid(row=0,column=0,padx=1)
        
        Unit2=Button(ClassMenu,text="Unit 2",font=("arial",11,"bold"),bg="black",fg="gold",width=12)
        Unit2.grid(row=0,column=1,padx=1)

        Unit3 = Button(ClassMenu, text="Unit 3",font=("arial",11,"bold"),bg="black",fg="gold",width=12)
        Unit3.grid(row=0,column=2,padx=1)

        Unit4 = Button(ClassMenu, text="Unit 4",font=("arial",11,"bold"),bg="black",fg="gold",width=12)
        Unit4.grid(row=0,column=3,padx=1)

        Unit5 = Button(ClassMenu, text="Unit 5",font=("arial",11,"bold"),bg="black",fg="gold",width=12)
        Unit5.grid(row=0,column=4,padx=1)
        
        btnPrint=Button(ClassMenu,text="Print",font=("arial",11,"bold"),bg="black",fg="gold",width=12)
        btnPrint.grid(row=0,column=5,padx=1)
        
        btnPrintPDF=Button(ClassMenu,text="PDF",font=("arial",11,"bold"),bg="black",fg="gold",width=12)
        btnPrintPDF.grid(row=0,column=6,padx=1)
        
        btnExit=Button(ClassMenu,text="Exit",command=self.Exit,font=("arial",11,"bold"),bg="black",fg="gold",width=12)
        btnExit.grid(row=0,column=7,padx=1)
        
        # Create a frame for the table
        self.table_frame = Frame(root)
        self.table_frame.pack(pady=65)
        #==============================
         # Create vertical scrollbar
        vscrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL)
        vscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create horizontal scrollbar
        hscrollbar = tk.Scrollbar(self.root, orient=tk.HORIZONTAL)
        hscrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        # Create a canvas to hold the paper sheet and attach scrollbars
        self.canvas = tk.Canvas(self.root, yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set, bg="white")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        vscrollbar.config(command=self.canvas.yview)
        hscrollbar.config(command=self.canvas.xview)

        # Create a frame inside the canvas for the paper sheet
        self.sheet_frame = tk.Frame(self.canvas, bg="lightblue")
        self.canvas.create_window((0, 0), window=self.sheet_frame, anchor=tk.NW)

        # Configure the canvas to update scroll region when the frame size changes
        self.sheet_frame.bind("<Configure>", self.update_scrollregion)

        # Initially, create a 30x21 paper sheet with lines
        self.create_paper_sheet(100, 85, selected_class)
        
    def create_paper_sheet(self, rows, columns, selected_class):
        entry_id=Label(self.sheet_frame,text="ID",width=4,font=("times new roman",12,"bold"))
        entry_id.grid(row=0,column=0,sticky=W)
        
        entry_name=Label(self.sheet_frame,text="Student's Name",font=("times new roman",13,"bold"))
        entry_name.place(x=45,y=2,width=185,height=25)
        
        entry_subject1=Label(self.sheet_frame,font=("times new roman",13,"bold"))
        entry_subject1.place(x=240,y=2,width=160,height=25)
        
        entry_subject2=Label(self.sheet_frame,font=("times new roman",13,"bold"))
        entry_subject2.place(x=410,y=2,width=160,height=25)
        
        entry_subject3=Label(self.sheet_frame,font=("times new roman",13,"bold"))
        entry_subject3.place(x=575,y=2,width=160,height=25)
        
        entry_subject4=Label(self.sheet_frame,font=("times new roman",13,"bold"))
        entry_subject4.place(x=745,y=2,width=160,height=25)
        
        entry_subject5=Label(self.sheet_frame,font=("times new roman",13,"bold"))
        entry_subject5.place(x=915,y=2,width=160,height=25)
        
        entry_subject6=Label(self.sheet_frame,font=("times new roman",13,"bold"))
        entry_subject6.place(x=1080,y=2,width=160,height=25)
        
        entry_subject7=Label(self.sheet_frame,font=("times new roman",13,"bold"))
        entry_subject7.place(x=1250,y=2,width=160,height=25)
        
        entry_subject8=Label(self.sheet_frame,font=("times new roman",13,"bold"))
        entry_subject8.place(x=1420,y=2,width=160,height=25)
        
        entry_subject9=Label(self.sheet_frame,font=("times new roman",13,"bold"))
        entry_subject9.place(x=1590,y=2,width=160,height=25)
        
        entry_subject10=Label(self.sheet_frame,font=("times new roman",13,"bold"))
        entry_subject10.place(x=1755,y=2,width=160,height=25)
        
        entry_subject11=Label(self.sheet_frame,font=("times new roman",13,"bold"))
        entry_subject11.place(x=1925,y=2,width=160,height=25)
        
        entry_subject12=Label(self.sheet_frame,font=("times new roman",13,"bold"))
        entry_subject12.place(x=2090,y=2,width=160,height=25)
        
        entry_subject13=Label(self.sheet_frame,font=("times new roman",13,"bold"))
        entry_subject13.place(x=2260,y=2,width=160,height=25)
        
        entry_subject14=Label(self.sheet_frame,font=("times new roman",13,"bold"))
        entry_subject14.place(x=2425,y=2,width=160,height=25)
        
        entry_subject15=Label(self.sheet_frame,font=("times new roman",13,"bold"))
        entry_subject15.place(x=2595,y=2,width=160,height=25)
        
        entry_subject16=Label(self.sheet_frame,font=("times new roman",13,"bold"))
        entry_subject16.place(x=2760,y=2,width=160,height=25)
        
        entry_subject17=Label(self.sheet_frame,font=("times new roman",13,"bold"))
        entry_subject17.place(x=2930,y=2,width=160,height=25)
        
        entry_subject18=Label(self.sheet_frame,font=("times new roman",13,"bold"))
        entry_subject18.place(x=3097,y=2,width=160,height=25)
        
        entry_subject19=Label(self.sheet_frame,font=("times new roman",13,"bold"))
        entry_subject19.place(x=3266,y=2,width=160,height=25)
        
        entry_subject20=Label(self.sheet_frame,font=("times new roman",13,"bold"))
        entry_subject20.place(x=3433,y=2,width=160,height=25)
        
        entry_total=ttk.Label(self.sheet_frame,text="TOTAL POINTS",font=("times new roman",9,"bold"), state="readonly")
        entry_total.place(x=3605,y=2,width=95,height=25)
        
        entry_avg=ttk.Label(self.sheet_frame,text="OUT OF",font=("times new roman",10,"bold"), state="readonly")
        entry_avg.place(x=3708,y=2,width=95,height=25)
        
        entry_Agg=ttk.Label(self.sheet_frame,text="FINAL SCORE",font=("times new roman",10,"bold"), state="readonly")
        entry_Agg.place(x=3810,y=2,width=95,height=25)
        
        # Fetch subjects for the selected class from the database
        conn = pymysql.connect(host="localhost", user="root", database="report")
        cursor = conn.cursor()
        cursor.execute("SELECT subject1, subject2, subject3, subject4, subject5, subject6, subject7, subject8, subject9, subject10, subject11, subject12, subject13, subject14, subject15, subject16, subject17, subject18, subject19, subject20 FROM subject WHERE class = %s", (selected_class,))
        subjects = cursor.fetchone()
        
        # Fetch data from the database (replace 'your_database_table' with the actual table name)
        conn = pymysql.connect(host="localhost", user="root", database="report")
        cursor = conn.cursor()
        cursor.execute("SELECT ref, name FROM student WHERE class = %s", (selected_class,))
        student_data = cursor.fetchall()
        
        # Update the total number of students label
        total_students = len(student_data)
        self.lbl_total_students.config(text=f"Total Students: {total_students}")
        
        # List to store Entry widgets
        entry_subjects = []

        # Loop to create Entry widgets for each subject
        for i, subject in enumerate(subjects):
            entry_subject = Label(self.sheet_frame, text=subject, font=("times new roman", 13, "bold"))
            entry_subject.place(x=(240 + i * 170), y=2, width=90, height=25)
            #entry_subject.insert(0, subject)  # Insert subject into Entry widget
            entry_subjects.append(entry_subject)
                    
        # Assuming 'selected_class' is a variable holding the current selected class
        selected_class_data_query = "SELECT ref, name FROM student WHERE class = %s"
        cursor.execute(selected_class_data_query, (selected_class,))
        selected_class_data = cursor.fetchall()
        
        # Create the first row with 21 cells each of length 24
        row_entries = []
        #for row in range(1, rows):
        for row, (ref, name) in enumerate(selected_class_data, start=1):
            row_entries = []
            for col in range(columns):
                if col == 0:
                    entry = Entry(self.sheet_frame, width=4, font=('Arial', 9), relief=FLAT)
                    entry.insert(0, ref)
                elif col == 1:
                    entry = Entry(self.sheet_frame, width=26, font=('Arial', 10), relief=FLAT)       
                    entry.insert(0, name)               
                elif col == 82:
                    entry = Entry(self.sheet_frame, width=10, font=('Arial', 12), relief=FLAT)       
                elif col == 83:
                    entry = Entry(self.sheet_frame, width=10, font=('Arial', 12), relief=FLAT)       
                elif col == 84:
                    entry = Entry(self.sheet_frame, width=10, font=('Arial', 12), relief=FLAT)       
                else:
                    entry = Entry(self.sheet_frame, width=4, font=('Arial', 10), relief=FLAT)
                entry.grid(row=row, column=col, padx=5, pady=5)
                
                row_entries.append(entry)
            self.entries.append(row_entries)
        

    def update_scrollregion(self, event):
        # Update the scroll region of the canvas when the frame size changes
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
    def get_entries_data(self):
        # Get data from entries
        data = []
        for row in self.entries:
            row_data = [entry.get() for entry in row]
            data.append(row_data)
        return data
                
    def create_table(self):
        # self.entries = []
        row_entries = []
        entry = Entry(self.table_frame, width=10, font=('Arial', 10))
        entry.grid( padx=5, pady=5)
        row_entries.append(entry)
        self.entries.append(row_entries)
            
    def delete_column(self):
        if self.columns > 1:
            for row in self.entries:
                row[-1].destroy()
                row.pop()
            self.columns -= 1
            self.update_scrollregion(None)

    def update_scrollregion(self, event):
        # Update the scroll region of the canvas when the frame size changes
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def bind_arrow_keys(self):
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)

    def move_up(self, event):
        if self.current_row > 0:
            self.current_row -= 1
            self.entries[self.current_row][self.current_column].focus_set()

    def move_down(self, event):
        if self.current_row < len(self.entries) - 1:
            self.current_row += 1
            self.entries[self.current_row][self.current_column].focus_set()

    def move_left(self, event):
        if self.current_column > 0:
            self.current_column -= 1
            self.entries[self.current_row][self.current_column].focus_set()

    def move_right(self, event):
        if self.current_column < len(self.entries[0]) - 1:
            self.current_column += 1
            self.entries[self.current_row][self.current_column].focus_set()
       
    def Exit(self):
           self.Exit= messagebox.askyesno("Hotel Management System","confirm if you want to exit",parent=self.root)
           if self.Exit>0:
               self.root.destroy()
        
if __name__ == "__main__":
    root = Tk()
    ob = Osheet(root,3,3)
    root.mainloop()