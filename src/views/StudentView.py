import tkinter as tk
from tkinter import messagebox


class StudentView:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Window")
        self.master.geometry("300x150+100+100")
        self.master.update_idletasks()

        # Create and place the username label and entry
        self.label_username = tk.Label(master, text="Username:")
        self.label_username.pack(pady=5)

        self.entry_username = tk.Entry(master)
        self.entry_username.pack(pady=5)

        # Create and place the password label and entry
        self.label_password = tk.Label(master, text="Password:")
        self.label_password.pack(pady=5)

        self.entry_password = tk.Entry(master, show="*")
        self.entry_password.pack(pady=5)

        # Create and place the login button
        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack(pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Check if the credentials match (for demo purposes)
        if username == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

