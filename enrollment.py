import random as r

class Subject:
    def __init__(self):
        self.id = f'{r.randint(1,999):03}'
        self.mark = r.randint(25,100)
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.mark >= 85:
            return "HD"
        elif self.mark >= 75:
            return "D"
        elif self.mark >= 65:
            return "C"
        elif self.mark >= 50:
            return "P"
        else:
            return "F"
        
    def __str__(self):
        return f"[ Subject::{self.id} -- mark = {self.mark} -- grade = {self.grade} ]"
    
class SubjectEnrollment:
    def __init__(self):
        self.enrolled_subjects = {}
        self.max_subjects = 4
        self.password = "default_password"

    def enrol_subject(self):
        if len(self.enrolled_subjects) < self.max_subjects:
            subject = Subject()
            self.enrolled_subjects[subject.id] = subject
            print(f"Enrolling in Subject-{subject.id}")
            print(f"You are not enrolled in {len(self.enrolled_subjects)} out of {self.max_subjects} subjects")
        else:
            print("Students are allowed to enrol in 4 subjects only")

    def remove_subject(self, subject_id):
        if subject_id in self.enrolled_subjects:
            del self.enrolled_subjects[subject_id]
            print(f"Dropping Subject - {subject_id}")
        else:
            print(f"Subject - {subject_id} not found!")

    
    def show_enrolled_subjects(self):
        if not self.enrolled_subjects:
            print("Showing 0 subjects")
        else:
            print(f"Showing {len(self.enrolled_subjects)} subjects")
            for subject in self.enrolled_subjects.values():
                print(subject)
    
    def change_password(self):
        print("Updating password")
        new_password = input("New Password: ")
        confirm_password = input("Confirm Password: ")
        if new_password == confirm_password:
            self.password = new_password
            print("Password updated successfully")
        else:
            print("Password does not match - try again")

    def course_menu(self):
        while True:
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

        
def main():
    subject_enrollment = SubjectEnrollment()
    subject_enrollment.course_menu()

if __name__ == "__main__":
    main() 