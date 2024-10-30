from controllers.AdminController import AdminController
from controllers.StudentController import StudentController
from utils.String import StringUtils

class UniversityController:
    # Main method providing the main menu for choosing between Admin, Student, or Exit options.
    def main(self):
        while True:
            # Prompts the user to select an option in the university system menu.
            option = input(StringUtils.to_cyan_string("University System: (A)Admin, (S)Student, or X: "))
            if option.lower() == "a":
                admin_controller = AdminController()  # Initializes an AdminController instance.
                admin_controller.main()  # Calls the main method for admin actions.
                continue  # Returns to the main menu after admin operations.
            elif option.lower() == "s":
                student_controller = StudentController()  # Initializes a StudentController instance.
                student_controller.main()  # Calls the main method for student actions.
            elif option.lower() == "x":
                break  # Exits the loop if "x" is selected.
            else:
                print("Invalid option")  # Notifies the user of an invalid option.
