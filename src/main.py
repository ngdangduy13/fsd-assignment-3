
from controllers.UniversityController import UniversityController
import tkinter as tk
from views.StudentView import LoginView

if __name__ == '__main__':
    # university_controller = UniversityController()
    # university_controller.main()

    root = tk.Tk()
    app = LoginView(root)
    root.mainloop()

