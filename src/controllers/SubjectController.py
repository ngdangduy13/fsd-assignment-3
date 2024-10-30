from utils.Logger import Logger
from models.Subject import Subject
from models.Validator import Validator
from models.Database import Database

class SubjectEnrollment:
    def __init__(self,student):
        self.student = student

    def enrol_subject(self):
        subject = Subject()
        self.student.enroll_subject(subject)
        db = Database()
        db.update_student(self.student)

    def remove_subject(self, subject_id):
        self.student.remove_subject(subject_id)
        db = Database()
        db.update_student(self.student)
    
    def show_enrolled_subjects(self):
        self.student.show_enrolled_subjects()
    
    def change_password(self):
        print("Updating password")
        new_password = input("New Password: ")
        confirm_password = input("Confirm Password: ")
        self.student.change_password(new_password, confirm_password)
        db = Database()
        db.update_student(self.student)
        print("Password updated successfully")

    def course_menu(self):
        while True:
            try: 
                user_input = input("Student Course Menu (c/e/r/s/x): ").lower()
                if user_input == 'e':
                    self.enrol_subject()
                elif user_input == 'r':
                    subject_id = input("Remove Subject by ID: ")
                    self.remove_subject(subject_id)
                elif user_input == 's':
                    self.show_enrolled_subjects()
                elif user_input == 'c':
                    self.change_password()
                elif user_input == 'x':
                    print("Exiting.")
                    break
                else:
                    print("Invalid input, try again.")
            except Exception as e:
                Logger.log_red(e) 

   
