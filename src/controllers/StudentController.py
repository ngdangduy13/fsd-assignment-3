from models.Database import Database
from utils.Logger import Logger
from models.Student import Student
from models.Validator import Validator
from controllers.SubjectController import SubjectEnrollment
from utils.String import StringUtils

class StudentController:
    # Initializes the StudentController class with a None student attribute.
    def __init__(self):
        self.student = None

    # Registers a new student if email and password formats are valid.
    def register(self, email, password):
        is_valid_email = Validator.validate_email(email)  # Validates the email format.
        is_valid_password = Validator.validate_password(password)  # Validates the password format.

        if not is_valid_email or not is_valid_password:  # Checks if either validation fails.
            Logger.log_red("Incorrect email or password format")  # Logs validation failure.
        else:
            Logger.log_yellow("Email and password formats accepted")  # Logs successful validation.
            name = input("Name: ")  # Prompts for the student's name.

            Logger.log_yellow(f"Enrolling Student {name}")  # Logs student enrollment message.
            db = Database()  # Creates a database instance.
            db.insert_student(email, password, name)  # Inserts the student details into the database.

    # Authenticates a student login if email and password formats are valid.
    def login(self, email, password):
        is_valid_email = Validator.validate_email(email)  # Validates the email format.
        is_valid_password = Validator.validate_password(password)  # Validates the password format.

        if not is_valid_email or not is_valid_password:  # Checks if either validation fails.
            raise Exception("Incorrect email or password format")  # Raises an exception if validation fails.
        else:
            Logger.log_yellow("Email and password formats accepted")  # Logs successful validation.
            db = Database()  # Creates a database instance.
            return db.get_student_by_email_and_password(email, password)  # Retrieves student if email/password match.

    # Provides a main menu for user registration, login, or exit.
    def main(self):
        while True:
            try:
                # Prompts the user to select an option in the student system menu.
                option = input(StringUtils.to_cyan_string("Student System (l/r/x): "))
                if option == "r":
                    Logger.log_green("Student Sign Up")  # Logs sign-up initiation.
                    email = input("Email: ")  # Prompts for email input.
                    password = input("Password: ")  # Prompts for password input.
                    self.register(email, password)  # Calls register with provided email and password.
                elif option == "l":
                    Logger.log_green("Student Sign In")  # Logs sign-in initiation.
                    email = input("Email: ")  # Prompts for email input.
                    password = input("Password: ")  # Prompts for password input.
                    student = self.login(email, password)  # Calls login and retrieves student data.
                    if student is not None:
                        self.student = student  # Sets the retrieved student instance.
                        subject_enrollment = SubjectEnrollment(self.student)  # Initiates subject enrollment for the student.
                        subject_enrollment.course_menu()  # Opens the course menu for subject management.
                elif option == "x":
                    break  # Exits the loop if "x" is selected.
                else:
                    print("Invalid option")  # Notifies the user of an invalid option.
            except Exception as e:
                Logger.log_red(e)  # Logs any exceptions encountered.
