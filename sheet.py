from tkinter import *
from time import strftime
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
class MarkEntry:
    def __init__(self, root, rows , columns,students=None):
        self.root = root
        self.root.geometry("1450x730+0+0")
        self.root.configure(bg="black")
        #self.root.overrideredirect(True)
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
        self.rows = rows
        self.columns = columns
        self.students = students
        
        self.create_table(rows, columns)

        # Initialize the UI components and create the table
        #====================title================
        title= Label(self.root, text="Marks Entry For Each Subject",compound=LEFT, font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        
                # Assuming functions to retrieve user information from the database
                
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
          
        #===========Class Menu==============
        ClassLbl = Frame(self.root,relief=RIDGE, bg="#4d636d")
        ClassLbl.place(x=0,y=100,width=350,height=40)
        
        lblNo = Label(ClassLbl, text="Total Students:", font=('Arial', 12,'bold'),fg="white", bg="#4d636d")
        lblNo.grid(row=0, column=0, padx=0, pady=3)
        
        ClassMenu = Frame(self.root,bd=2,relief=RIDGE, bg="white")
        ClassMenu.place(x=350,y=100,width=1020,height=40)
        
        btnAdd=Button(ClassMenu,text="Save",font=("arial",11,"bold"),bg="black",fg="gold",width=12)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnExit=Button(ClassMenu,text="Exit",command=self.Exit,font=("arial",11,"bold"),bg="black",fg="gold",width=12)
        btnExit.grid(row=0,column=1,padx=1)
        
        # Create buttons for adding rows and columns
        add_row_button = Button(ClassMenu, text="Add Row", command=self.add_row,font=("arial",11,"bold"),bg="black",fg="gold",width=12)
        add_row_button.grid(row=0,column=2,padx=1)

        add_column_button = Button(ClassMenu, text="Add Column", command=self.add_column,font=("arial",11,"bold"),bg="black",fg="gold",width=12)
        add_column_button.grid(row=0,column=3,padx=1)

        delete_row_button = Button(ClassMenu, text="Delete Row", command=self.delete_row,font=("arial",11,"bold"),bg="black",fg="gold",width=12)
        delete_row_button.grid(row=0,column=4,padx=1)

        delete_column_button = Button(ClassMenu, text="Delete Column", command=self.delete_column,font=("arial",11,"bold"),bg="black",fg="gold",width=12)
        delete_column_button.grid(row=0,column=5,padx=1)
        
        btnPrint=Button(ClassMenu,text="Print Preview",font=("arial",11,"bold"),bg="black",fg="gold",width=12)
        btnPrint.grid(row=0,column=6,padx=1)
        
        btnPrintPDF=Button(ClassMenu,text="Print AS PDF",font=("arial",11,"bold"),bg="black",fg="gold",width=12)
        btnPrintPDF.grid(row=0,column=7,padx=1)
        
        labelMenu = Frame(self.root,bd=2, bg="#4d636d")
        labelMenu.place(x=0,y=140,width=1400,height=30)
        
        # Create title for first column
        titleUs = Label(labelMenu, text="Student Names", font=('Arial', 12,'bold'), bg="#4d636d",fg="white")
        titleUs.grid(row=0, column=0, padx=90, pady=3)
        
        title1 = Label(labelMenu, text="Test 1", font=('Arial', 12,'bold'), bg="#4d636d",fg="white")
        title1.grid(row=0, column=1, padx=70, pady=3)
        
        title2 = Label(labelMenu, text="Test 2", font=('Arial', 12,'bold'), bg="#4d636d",fg="white")
        title2.grid(row=0, column=2, padx=1, pady=3)
        
        title3 = Label(labelMenu, text="Test 3", font=('Arial', 12,'bold'), bg="#4d636d",fg="white")
        title3.grid(row=0, column=3, padx=15, pady=3)
        
        title4 = Label(labelMenu, text="Test 4", font=('Arial', 12,'bold'), bg="#4d636d",fg="white")
        title4.grid(row=0, column=4, padx=15, pady=3)
        
        title5 = Label(labelMenu, text="Test 5", font=('Arial', 12,'bold'), bg="#4d636d",fg="white")
        title5.grid(row=0, column=5, padx=15, pady=3)
        
        title6 = Label(labelMenu, text="Test 6", font=('Arial', 12,'bold'), bg="#4d636d",fg="white")
        title6.grid(row=0, column=6, padx=15, pady=3)
        
        title7 = Label(labelMenu, text="Test 7", font=('Arial', 12,'bold'), bg="#4d636d",fg="white")
        title7.grid(row=0, column=7, padx=15, pady=3)
    
        title8 = Label(labelMenu, text="Test 8", font=('Arial', 12,'bold'), bg="#4d636d",fg="white")
        title8.grid(row=0, column=8, padx=15, pady=3)
        
        title9 = Label(labelMenu, text="Test 9", font=('Arial', 12,'bold'), bg="#4d636d",fg="white")
        title9.grid(row=0, column=9, padx=15, pady=3)
        
        title10 = Label(labelMenu, text="Test10", font=('Arial', 12,'bold'), bg="#4d636d",fg="white")
        title10.grid(row=0, column=10, padx=15, pady=3)
        
        # Create a frame for the table
        self.table_frame = Frame(root)
        self.table_frame.pack(pady=85)

        # Create a 2D list to store entries
        self.entries = []
        # Create vertical scrollbar
        vscrollbar = Scrollbar(self.root, orient=VERTICAL)
        vscrollbar.pack(side=RIGHT, fill=Y)

        # Create horizontal scrollbar
        hscrollbar = Scrollbar(self.root, orient=HORIZONTAL)
        hscrollbar.pack(side=BOTTOM, fill=X)
        
        # Create a canvas to hold the table and attach scrollbars
        self.canvas = Canvas(self.root, yscrollcommand=vscrollbar.set, xscrollcommand=hscrollbar.set)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        vscrollbar.config(command=self.canvas.yview)
        hscrollbar.config(command=self.canvas.xview)
        
        # Create a frame inside the canvas for the table
        self.table_frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.table_frame, anchor=NW)

        # Initially, create a 3x3 table
        self.create_table(20, 5)

        # Configure the canvas to update scroll region when the frame size changes
        self.table_frame.bind("<Configure>", self.update_scrollregion)
                 
    def create_table(self,rows,columns):
        # self.entries = []
        for row in range(rows):
            row_entries = []
            for col in range(columns):
                if col == 0:
                    entry = Entry(self.table_frame, width=40, font=('Arial', 12))
                    if row < len(self.students):
                        entry.insert(0, self.students[row])
                else:
                    entry = Entry(self.table_frame, width=10, font=('Arial', 10))
                entry.grid(row=row, column=col, padx=5, pady=5)
                row_entries.append(entry)
            self.entries.append(row_entries)

    def add_row(self):
        # Add a new row to the table
        columns = len(self.entries[0])
        new_row_entries = []
        for col in range(columns):
            if col == 0:
                entry = Entry(self.table_frame, width=40, font=('Arial', 12))
            else:
                entry = Entry(self.table_frame, width=10, font=('Arial', 10))
            entry.grid(row=len(self.entries), column=col, padx=5, pady=5)
            new_row_entries.append(entry)
        self.entries.append(new_row_entries)
        self.update_scrollregion(None)
    #def add_row(self):
    #    for col in range(self.columns):
    #        if col == 0:
    #            entry = Entry(self.table_frame, width=40, font=('Arial', 12))
    #        else:
    #            entry = Entry(self.table_frame, width=10, font=('Arial', 10))
    #        entry.grid(row=len(self.entries), column=col, padx=5, pady=5)
    #        self.entries[-1].append(entry)
    #    self.update_scrollregion(None)

    def add_column(self):
        # Add a new column to the table
        rows = len(self.entries)
        columns = len(self.entries[0])
        for row in range(rows):
            entry = Entry(self.table_frame, width=10, font=('Arial', 10))
            entry.grid(row=row, column=columns, padx=5, pady=5)
            self.entries[row].append(entry)
        self.update_scrollregion(None)
    #def add_column(self):
    #    for row in self.entries:
    #        entry = Entry(self.table_frame, width=10, font=('Arial', 10))
    #        entry.grid(row=len(row), column=self.columns, padx=5, pady=5)
    #        row.append(entry)
    #    self.columns += 1
    #    self.update_scrollregion(None)
        
    def delete_row(self):
        # Delete the last row from the table
        if len(self.entries) > 1:
            for entry in self.entries[-1]:
                entry.destroy()
            self.entries.pop()
            self.update_scrollregion(None)

    #def delete_column(self):
        # Delete the last column from the table
    #    if len(self.entries[0]) > 1:
    #        for row in self.entries:
    #            row[-1].destroy()
    #            row.pop()
    #        self.update_scrollregion(None)
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
    ob = MarkEntry(root,3,3)
    root.mainloop()
