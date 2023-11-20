from tkinter import *
import customtkinter as ctk
from customtkinter import *
from tkinter import messagebox
#from PIL import ImageTk
from time import strftime
class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1450x730+0+0")
        self.root.configure(bg="black")
        #self.root.overrideredirect(True)

        self.root.title('Login System Of Student Management System')
        self.root.resizable(True, True)
        
        title= Label(self.root, text="DIRECTOR OF STUDIES LOGIN",compound=LEFT, font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=300).place(x=1,y=2,relwidth=1,height=70)
        

        loginFrame = Frame(self.root, bg='white')
        loginFrame.place(x=400, y=150)

        usernameLabel=Label(loginFrame,  text = 'Username', font=('times new roman', 20, 'bold'), bg='white')
        usernameLabel.grid(row=1, column=0, pady=10, padx=20)

        usernameEntry = Entry(loginFrame, font=('times new roman',20,'bold'),bd=2,fg='royalblue')
        usernameEntry.grid(row=1, column= 1,pady=10, padx=20)
        #========PASSWORD================================
        #passwordImage = PhotoImage(file='password.png')
        passwordLabel=Label(loginFrame,  text = 'Password', font=('times new roman', 20, 'bold'), bg='white')
        passwordLabel.grid(row=2, column=0, pady=10, padx=20)

        passwordEntry = Entry(loginFrame, font=('times new roman',20,'bold'),bd=2,fg='royalblue')
        passwordEntry.grid(row=2, column= 1,pady=10, padx=20)

        loginButton = Button(loginFrame, text='Login',font=('times new roman',15,'bold'), width=15, fg='white', bg='cornflowerblue', activebackground='cornflowerblue',activeforeground='white',cursor='hand2')
        loginButton.grid(row=3, column=1, pady=10)
        
        def login (self):
            if usernameEntry.get() == '' or passwordEntry.get() == '':
                messagebox.showerror('Error', 'Field cannot be empty')
            elif usernameEntry.get() == 'francis' and passwordEntry.get() == '123':
                messagebox.showinfo('Success','Welcome')
                self.root.destroy()

            else:
                messagebox.showerror('Error','Please enter correct credentials')


root=Tk()
ob = IMS(root)
root.mainloop()
