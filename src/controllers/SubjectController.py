from models.Subject import Subject

class SubjectEnrollment:
    def __init__(self,student):
        self.student = student
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

    def save_to_file(self, filename):
        with open(filename, 'students.data') as file:
            for subject in self.enrolled_subejcts.value():
                file.write(f'{subject.id},{subject.mark},{subject.grade}\n')
        print(f'Enrolled subjects saved to {filename}')

    def load_from_file(self, filename):
        try:
            with open(filename, 'students.data') as file:
                for line in file:
                    subject_id, mark, grade = line .strip().split(',')
                    self.enrolled_subjects[subject_id] = Subject(subject_id, grade, mark)
            print(f'Enrolled subjects loaded from {filename}')
        except FileNotFoundError:
            print(f'No filename named {filename} found')
