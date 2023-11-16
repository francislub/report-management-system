from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk
from customtkinter import *
from tkinter import *

def userLoggedIn():
    app.destroy()

    root = ctk.CTk()
    root.geometry("1400x900")
    root.title("LARKS TECH HUB ADMIN PANEL")

    ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
    ctk.set_appearance_mode("dark")

    logo1 = PhotoImage(file="logo.png")
    logo_label1 = ctk.CTkLabel(root, image=logo1)
    logo_label1.place(x=500, y=0)

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


def userLogin():
    select_label.destroy()
    role_menu.destroy()
    enter_button.destroy()

    user_label = ctk.CTkLabel(mainFrame,
                              text="SELECTED ROLE",
                              font=ctk.CTkFont(
                                  size=20,
                                  weight="bold",
                                  family="Microsoft YaHei UI Light"))
    user_label.grid(row=0, column=1, pady=20)

    login_label = ctk.CTkLabel(mainFrame,
                               text="LOGIN",
                               font=CTkFont(
                                   size=15,
                                   weight="bold",
                                   family="Microsoft YaHei UI Light"))
    login_label.grid(row=1, column=1)

    username_label = ctk.CTkLabel(mainFrame,
                                  text="Username/Email",
                                  font=ctk.CTkFont(
                                      size=15,
                                      weight="bold",
                                      family="Microsoft YaHei UI Light"))
    username_label.grid(row=2, column=1)

    username_entry = ctk.CTkEntry(mainFrame, width=300)
    username_entry.grid(row=3, column=1, padx=100, pady=(0, 20))

    password_label = ctk.CTkLabel(mainFrame,
                                  text="Password",
                                  font=ctk.CTkFont(
                                      size=15,
                                      weight="bold",
                                      family="Microsoft YaHei UI Light"))
    password_label.grid(row=4, column=1)

    password_entry = ctk.CTkEntry(mainFrame, width=300)
    password_entry.grid(row=5, column=1, padx=100, pady=(0, 10))

    login_button = ctk.CTkButton(mainFrame, text="LOGIN", command=userLoggedIn)
    login_button.grid(row=6, column=1, pady=10)


app = ctk.CTk()
app.geometry("1400x900")
app.title("STUDENT REPORT GENERATING SYSTEM")

ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
ctk.set_appearance_mode("dark")

logo = PhotoImage(file="logo.png")
logo_label = ctk.CTkLabel(app, image=logo)
logo_label.place(x=500, y=0)

title_label = ctk.CTkLabel(
    app,
    text="STUDENT REPORT MANAGEMENT SYSTEM",
    font=CTkFont(
        size=40,
        weight="bold",
        family="Microsoft YaHei UI Light"))
title_label.place(x=280, y=300)

mainFrame = ctk.CTkFrame(master=app, width=500, height=200)
mainFrame.place(x=430, y=400)

select_label = ctk.CTkLabel(mainFrame,
                        text="Select Role",
                        font=CTkFont(
                            size=20,
                            weight="bold",
                            family="Microsoft YaHei UI Light"))
select_label.grid(row=0, column=2, pady=20)

roles_list = ["Director Of Studies (DOS)", "Secretary/Teacher", "Admin"]

role_menu = ctk.CTkComboBox(mainFrame, values=roles_list, width=300)
role_menu.grab_current()
role_menu.grid(row=1, column=2, padx=100, pady=10)

enter_button = ctk.CTkButton(mainFrame, text="ENTER")
enter_button.grid(row=2, column=2, pady=40)

app.mainloop()

