from utils.Logger import Logger
from models.Subject import Subject
from models.Validator import Validator
from models.Database import Database
from utils.String import StringUtils

class SubjectEnrollment:
    # Initializes the SubjectEnrollment class with a student instance.
    def __init__(self, student):
        self.student = student

    # Enrolls the student in a new subject by creating a Subject instance and adding it to the student's enrolled subjects.
    def enrol_subject(self):
        subject = Subject()  # Creates a new subject instance.
        self.student.enroll_subject(subject)  # Adds subject to the student's enrolled subjects.
        Logger.log_yellow(f"Enrolling in Subject-{subject.id}")  # Logs enrollment status.
        db = Database()  # Creates a database instance.
        db.update_student(self.student)  # Updates the student data in the database.
        Logger.log_yellow(f"You are enrolled in {len(self.student.enrolled_subjects)} out of {self.student.max_subjects} subjects")

    # Removes a subject from the student's enrollment list by subject ID.
    def remove_subject(self, subject_id):
        self.student.remove_subject(subject_id)  # Removes the specified subject.
        db = Database()  # Creates a database instance.
        db.update_student(self.student)  # Updates the student data in the database.

    # Displays the subjects the student is currently enrolled in.
    def show_enrolled_subjects(self):
        if not self.student.enrolled_subjects:
            Logger.log_yellow("Showing 0 subjects")  # Logs if no subjects are enrolled.
        else:
            Logger.log_yellow(f"Showing {len(self.student.enrolled_subjects)} subjects")  # Logs the count of enrolled subjects.
            for subject in self.student.enrolled_subjects:  # Iterates and prints each enrolled subject.
                print(subject)

    # Allows the student to change their password after confirming it.
    def change_password(self):
        Logger.log_yellow("Updating password")  # Logs the action of updating password.
        new_password = input("New Password: ")  # Prompts for new password input.
        confirm_password = input("Confirm Password: ")  # Prompts to confirm the new password.
        self.student.change_password(new_password, confirm_password)  # Changes the password in the student instance.
        db = Database()  # Creates a database instance.
        db.update_student(self.student)  # Updates the student data in the database.

    # Provides a course menu for the student to manage subjects and other actions.
    def course_menu(self):
        while True:
            try:
                # Prompts user to select an action in the course menu.
                user_input = input(StringUtils.to_cyan_string("Student Course Menu (c/e/r/s/x): ")).lower()
                if user_input == 'e':
                    self.enrol_subject()  # Calls enrol_subject if 'e' is selected.
                elif user_input == 'r':
                    subject_id = input("Remove Subject by ID: ")  # Prompts for subject ID to remove.
                    self.remove_subject(subject_id)  # Calls remove_subject with the provided ID.
                elif user_input == 's':
                    self.show_enrolled_subjects()  # Calls show_enrolled_subjects if 's' is selected.
                elif user_input == 'c':
                    self.change_password()  # Calls change_password if 'c' is selected.
                elif user_input == 'x':
                    print("Exiting.")  # Exits the menu if 'x' is selected.
                    break
                else:
                    print("Invalid input, try again.")  # Prompts user for valid input if entry is invalid.
            except Exception as e:
                Logger.log_red(e)  # Logs any exceptions encountered.
