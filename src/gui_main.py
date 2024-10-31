from controllers.UniversityController import UniversityController
import tkinter as tk
from views.StudentView import LoginView

if __name__ == '__main__':
    tk = tk.Tk()
    app = LoginView(tk)
    app.mainloop()