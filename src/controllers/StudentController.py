from models.Database import Database
from utils.Logger import Logger
from models.Student import Student
from models.Validator import Validator
from controllers.SubjectController import SubjectEnrollment


class StudentController:
    def __init__(self):
        self.student = None

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
            db = Database()
            db.insert_student(email, password, name)
            Logger.success(f"Enrolling student: {name}")
        except Exception as e:
            Logger.error(e)

    def login(self):
        email = input("Enter email: ")
        password = input("Enter password: ")
        try:
            db = Database()
            result = db.get_student_by_email_and_password(email, password)
            return Student(
                result['id'], result['email'], result['password'], result['name'])
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
                student = self.login()
                if (student is not None):
                    self.student = student
                    subject_enrollment = SubjectEnrollment(self.student)
                    subject_enrollment.course_menu()
            elif option == "x":
                break
            else:
                print("Invalid option")
