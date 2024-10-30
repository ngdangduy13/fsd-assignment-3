from utils.Logger import Logger
from models.Subject import Subject
from models.Validator import Validator
from models.Database import Database
from utils.String import StringUtils

class SubjectEnrollment:
    def __init__(self,student):
        self.student = student

    def enrol_subject(self):
        subject = Subject()
        self.student.enroll_subject(subject)
        Logger.log_yellow(f"Enrolling in Subject-{subject.id}")
        db = Database()
        db.update_student(self.student)
        Logger.log_yellow(f"You are enrolled in {len(self.enrolled_subjects)} out of {self.max_subjects} subjects")

    def remove_subject(self, subject_id):
        self.student.remove_subject(subject_id)
        db = Database()
        db.update_student(self.student)
    
    def show_enrolled_subjects(self):
        if not self.student.enrolled_subjects:
            Logger.log_yellow("Showing 0 subjects")
        else:
            Logger.log_yellow(f"Showing {len(self.student.enrolled_subjects)} subjects")
            for subject in self.student.enrolled_subjects:
                print(subject)
    
    def change_password(self):
        Logger.log_yellow("Updating password")
        new_password = input("New Password: ")
        confirm_password = input("Confirm Password: ")
        self.student.change_password(new_password, confirm_password)
        db = Database()
        db.update_student(self.student)

    def course_menu(self):
        while True:
            try: 
                user_input = input(StringUtils.to_cyan_string("Student Course Menu (c/e/r/s/x): ")).lower()
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

   
