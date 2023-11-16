import customtkinter as ctk
from customtkinter import *
from tkinter import *

def adminLoggedIn():
    pass

app = ctk.CTk()
app.geometry("1400x900")
app.title("LARKS TECH HUB ADMIN PANEL")

ctk.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
ctk.set_appearance_mode("dark")

logo = PhotoImage(file="logo.png")
logo_label = ctk.CTkLabel(app, image=logo)
logo_label.place(x=500, y=0)

title_label = ctk.CTkLabel(
    app,
    text="LARKS TECH HUB ADMIN LOGIN",
    font=CTkFont(
        size=40,
        weight="bold",
        family="Microsoft YaHei UI Light"))
title_label.place(x=280, y=300)

mainFrame = ctk.CTkFrame(master=app, width=500, height=200)
mainFrame.place(x=430, y=400)

user_label = ctk.CTkLabel(mainFrame,
                              text="ADMIN",
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

password_label = ctk.CTkLabel(mainFrame,
                              text="Password",
                              font=ctk.CTkFont(
                                  size=15,
                                  weight="bold",
                                  family="Microsoft YaHei UI Light"))
password_label.grid(row=4, column=1)

password_entry = ctk.CTkEntry(mainFrame, width=300)
password_entry.grid(row=5, column=1, padx=100, pady=(0, 10))

login_button = ctk.CTkButton(mainFrame, text="LOGIN", command=adminLoggedIn)
login_button.grid(row=6, column=1, pady=10)

app.mainloop()
