from utils.Logger import Logger
from models.Student import Student
from models.Validator import Validator


class StudentController:
    def register(self):
        email = input("Enter email: ")
        password = input("Enter password: ")

        validator = Validator()
        is_valid_email = validator.validate_email(email)
        is_valid_password = validator.validate_password(password)

        if (is_valid_email is False or is_valid_password is False):
            Logger.error("Incorrect email or password format")
            return

        Logger.success("Email and password formats accepted")
        name = input("Enter name: ")

        try:
            Student.register(email, password, name)
            Logger.success(f"Enrolling student: {name}")
        except Exception as e:
            Logger.error(e)

    def login(self):
        email = input("Enter email: ")
        password = input("Enter password: ")
        try:
            student = Student.login(email, password)
            Logger.success(f"Student logged in successfully: {student.name}")
        except Exception as e:
            Logger.error(e)

    def main(self):
        print("THE STUDENT SYSTEM")
        while (True):
            print("=====================================")
            print("(L) Login")
            print("(R) Register")
            print("(X) Exit")
            option = input("Choose an option: ")
            print("=====================================")
            if option == "r":
                self.register()
            elif option == "l":
                self.login()
            elif option == "x":
                break
            else:
                print("Invalid option")
