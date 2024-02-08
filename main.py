from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
from customtkinter import *
from tkinter import *
from tkinter import messagebox
import pymysql
#from dashboard import IMS
from teacherDash import Teacher

def userLoggedIn():
    app.destroy()

    root = ctk.CTk()
    root.geometry("1450x730+0+0")
    root.overrideredirect(True)
    #root.overrideredirect(True)
    root.title("LARKS TECH HUB ADMIN PANEL")

    ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
    ctk.set_appearance_mode("dark")

    #logo1 = PhotoImage(file="logo.png")
    #logo_label1 = ctk.CTkLabel(root, image=logo1)
    #logo_label1.place(x=500, y=0)

    title_label1 = ctk.CTkLabel(
        root,
        text="LARKS TECH HUB ADMIN LOGIN",
        font=CTkFont(
            size=40,
            weight="bold",
            family="Microsoft YaHei UI Light"))
    title_label1.place(x=360, y=300)

    main_frame1 = ctk.CTkFrame(master=root, width=500, height=200)
    main_frame1.place(x=430, y=400)

    user_label1 = ctk.CTkLabel(main_frame1,
                              text="ADMIN",
                              font=ctk.CTkFont(
                                  size=20,
                                  weight="bold",
                                  family="Microsoft YaHei UI Light"))
    user_label1.grid(row=0, column=1, pady=20)

    password_label1 = ctk.CTkLabel(main_frame1,
                                  text="Password",
                                  font=ctk.CTkFont(
                                      size=15,
                                      weight="bold",
                                      family="Microsoft YaHei UI Light"))
    password_label1.grid(row=4, column=1)

    password_entry1 = ctk.CTkEntry(main_frame1, width=300)
    password_entry1.grid(row=5, column=1, padx=100, pady=(0, 10))

    login_button1 = ctk.CTkButton(main_frame1, text="LOGIN")
    login_button1.grid(row=6, column=1, pady=10)

    root.mainloop()
def validate_login(username, password):
    conn = pymysql.connect(host="localhost", user="root", database="report")
    my_cursor = conn.cursor()
    my_cursor.execute("SELECT * FROM user WHERE username = %s AND password1 = %s", (username, password))
    user = my_cursor.fetchone()

    if user:
        #messagebox.showinfo("Success", "Login successful")
        open_teacher_window()
        # Add code to open a new window here
    elif username == "" and password == "":
        messagebox.showerror("Error", "Please Enter username or password")
    else:
        messagebox.showerror("Error", "Invalid username or password")

    conn.close()

def open_teacher_window():
    new_window=Toplevel()
    app=Teacher(new_window)
    
def userLogin():
    selected_role = role_menu.get()
    if selected_role == "Select Role":
        messagebox.showinfo("Error", "Please select a role")
    else:
        select_label.destroy()
        role_menu.destroy()
        enter_button.destroy()
        
        user_label = ctk.CTkLabel(mainFrame,
                                text=f"SELECTED ROLE: {selected_role}",
                                font=ctk.CTkFont(size=20, weight="bold", family="Microsoft YaHei UI Light"))
        user_label.grid(row=0, column=1, pady=20)

        username_label = ctk.CTkLabel(mainFrame,
                                    text="Username/Email",
                                    font=ctk.CTkFont(size=15, weight="bold", family="Microsoft YaHei UI Light"))
        username_label.grid(row=1, column=1)

        var_username = ctk.StringVar()
        username_entry = ctk.CTkEntry(mainFrame, textvariable=var_username, width=300)
        username_entry.grid(row=2, column=1, padx=100, pady=(0, 20))
        
        password_label = ctk.CTkLabel(mainFrame,
                                    text="Password",
                                    font=ctk.CTkFont(size=15, weight="bold", family="Microsoft YaHei UI Light"))
        password_label.grid(row=3, column=1)

        var_password = ctk.StringVar()
        password_entry = ctk.CTkEntry(mainFrame, textvariable=var_password, show="*", width=300)
        password_entry.grid(row=4, column=1, padx=100, pady=(0, 10))

        login_button = ctk.CTkButton(mainFrame, text="LOGIN", command=lambda: validate_login(var_username.get(), var_password.get()))
        login_button.grid(row=5, column=1, pady=10)
        
    admin_button = ctk.CTkButton(app, text="", command=userLoggedIn, fg_color="black",bg_color="black")
    admin_button.grid(row=0, column=0)

    
def Exit():
           Exit= messagebox.askyesno("Report Management System","confirm if you want to exit",parent=app)
           if Exit>0:
               app.destroy()

app = ctk.CTk()
#app.geometry("1400x900")
app.geometry("1450x730+0+0")
app.overrideredirect(True)
app.title("STUDENT REPORT GENERATING SYSTEM")

ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
ctk.set_appearance_mode("dark")

title_label = ctk.CTkLabel(
    app,
    text="STUDENT REPORT MANAGEMENT SYSTEM",
    font=CTkFont(
        size=40,
        weight="bold",
        family="Microsoft YaHei UI Light"))
title_label.place(x=280, y=150)

mainFrame = ctk.CTkFrame(master=app, width=500, height=200)
mainFrame.place(x=400, y=300)

select_label = ctk.CTkLabel(mainFrame,
                        text="Select Role",
                        font=CTkFont(
                            size=20,
                            weight="bold",
                            family="Microsoft YaHei UI Light"))
select_label.grid(row=0, column=2, pady=20)

roles_list = ["Select Role","Director Of Studies (DOS)", "Secretary/Teacher", "Admin"]

role_menu = ctk.CTkComboBox(mainFrame, values=roles_list, width=400)
role_menu.grab_current()
role_menu.grid(row=1, column=2, padx=100, pady=10)

enter_button = ctk.CTkButton(mainFrame, text="ENTER",command=userLogin)
enter_button.grid(row=2, column=2, pady=40)

exit_button = ctk.CTkButton(app, text="Exit",command=Exit)
exit_button.grid(row=3, column=2, pady=40)

app.mainloop()

