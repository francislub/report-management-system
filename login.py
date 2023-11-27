import customtkinter as ctk
import tkinter as tk

def Login():
    username = entry_username.get()
    password = entry_password.get()
    # Perform login logic using username and password
    pass

app = ctk.CTk()

app.title("Login")

app.geometry("500x450+390+170")

lblWelcome = ctk.CTkLabel(master=app, text="Larks ReportSystem", font=('Helvetica', 20, 'bold'))
lblWelcome.place(relx=0.4, rely=0.2, anchor=tk.CENTER)

label_username = ctk.CTkLabel(master=app, text="Username:")
label_username.place(relx=0.2, rely=0.45, anchor=tk.CENTER)

entry_username = ctk.CTkEntry(master=app, width=200)
entry_username.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

label_password = ctk.CTkLabel(master=app, text="Password:")
label_password.place(relx=0.2, rely=0.6, anchor=tk.CENTER)

entry_password = ctk.CTkEntry(master=app, width=200, show="*")
entry_password.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

btnLogin = ctk.CTkButton(master=app, text="Login", command=Login)
btnLogin.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

app.mainloop()
