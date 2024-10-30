from models.Database import Database
from utils.Logger import Logger
from models.Student import Student
from models.Validator import Validator
from controllers.SubjectController import SubjectEnrollment
from utils.String import StringUtils


class StudentController:
    def __init__(self):
        self.student = None

    def register(self, email, password):
        is_valid_email = Validator.validate_email(email)
        is_valid_password = Validator.validate_password(password)

        if (is_valid_email is False or is_valid_password is False):
            Logger.log_red("Incorrect email or password format")
        else:
            Logger.log_yellow("Email and password formats accepted")
            name = input("Name: ")

            Logger.log_yellow(f"Enrolling Student {name}")
            db = Database()
            db.insert_student(email, password, name)

    def login(self, email, password):
        is_valid_email = Validator.validate_email(email)
        is_valid_password = Validator.validate_password(password)

        if (is_valid_email is False or is_valid_password is False):
            raise Exception("Incorrect email or password format")
        else:
            Logger.log_yellow("Email and password formats accepted")
            db = Database()
            return db.get_student_by_email_and_password(email, password)

    def main(self):
        while (True):
            try:
                option = input(StringUtils.to_cyan_string(
                    "Student System (l/r/x): "))
                if option == "r": 
                    Logger.log_green("Student Sign Up")
                    email = input("Email: ")
                    password = input("Password: ")
                    self.register(email, password)
                elif option == "l":
                    Logger.log_green("Student Sign In")
                    email = input("Email: ")
                    password = input("Password: ")
                    student = self.login(email, password)
                    if (student is not None):
                        self.student = student
                        subject_enrollment = SubjectEnrollment(self.student)
                        subject_enrollment.course_menu()
                elif option == "x":
                    break
                else:
                    print("Invalid option")
            except Exception as e:
                Logger.log_red(e)
