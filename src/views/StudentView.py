import tkinter as tk
from tkinter import messagebox
from controllers.StudentController import StudentController
from models.Subject import Subject
from models.Database import Database


class EnrollmentWindow(tk.Toplevel):
    def __init__(self, master, student):
        super().__init__(master=master)
        self.student = student
        
        self.geometry("400x300")
        self.title("Enrollment System")
        self.configure(bg='#607b8d')
        self.resizable(False, False)


        subjects = student.enrolled_subjects
        self.listVar = tk.Variable(value=subjects)
        self.subject_list = tk.Listbox(self, listvariable=self.listVar).pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        
        self.enrollBtn = tk.Button(self, text="Enroll", command=lambda: self.enroll(master),
                                  bg='#252525', fg='#ffc107',
                                  font='Helvetica 10 bold',
                  ).pack(pady=20)


    def enroll(self, master):
        try:
            subject = Subject()
            self.student.enroll_subject(subject)
            db = Database()
            db.update_student(self.student)

            self.listVar.set(self.student.enrolled_subjects)
        except Exception as e:
            messagebox.showerror("Enrollment", str(e))
       
        


class LoginView(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        master.geometry("400x300")
        master.title("University System")
        master.configure(bg='#607b8d')
        master.resizable(False, False)
        box = tk.LabelFrame(master, text='Sign In', bg='#607b8d', fg='white',
                            padx=20, pady=20, font='Helvetica 10 bold')
        box.columnconfigure(0, weight=1)
        box.columnconfigure(1, weight=3)
        box.place(rely=0.5, relx=0.5, anchor='center')

        self.emailLbl = tk.Label(box, text="Email:", justify='left', fg='#ffc107',
                                 font='Helvetica 12 bold', bg='#607b8d')
        self.emailLbl.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)

        passwordLbl = tk.Label(box, text="Password:", fg='#ffc107',
                               font='Helvetica 12 bold', bg='#607b8d')
        passwordLbl.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)

        self.emailText = tk.StringVar()
        self.emailField = tk.Entry(box, textvariable=self.emailText)
        self.emailField.grid(column=1, row=0, padx=5, pady=5)
        self.emailField.focus()

        self.passwordTxt = tk.StringVar()
        self.passwordField = tk.Entry(
            box, textvariable=self.passwordTxt, show="*")
        self.passwordField.grid(column=1, row=1, padx=5, pady=5)
        
        self.loginBtn = tk.Button(box, text="Login",
                                  bg='#252525', fg='#ffc107',
                                  font='Helvetica 10 bold',
                                  command= lambda: self.login(master))
        self.loginBtn.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

        self.cancelBtn = tk.Button(box,
                                   bg='#252525', fg='#ffc107',
                                   font='Helvetica 10 bold',
                                   text="Cancel", command=lambda: master.quit())
        self.cancelBtn.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

    def login(self, master):
        try:
            student_controller = StudentController()
            student = student_controller.login(self.emailText.get(), self.passwordTxt.get())
            master.withdraw()
            EnrollmentWindow(master, student)
        except Exception as e:
            messagebox.showerror("Login", str(e))
        
