from controllers.AdminController import AdminController
from controllers.StudentController import StudentController
from utils.String import StringUtils


class UniversityController:
    def main(self):
        while (True):
            option = input(StringUtils.to_cyan_string("University System: (A)Admin, (S)Student, or X: "))
            if option.lower()  == "a":
                admin_controller = AdminController()
                admin_controller.main()
                continue
            elif option.lower() == "s":
                student_controller = StudentController()
                student_controller.main()
            elif option.lower() == "x":
                break
            else:
                print("Invalid option")