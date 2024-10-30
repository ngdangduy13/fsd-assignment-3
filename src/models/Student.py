import json
from models.Validator import Validator
from models.Subject import Subject


class Student:
    @staticmethod
    def from_dict(dict):
        return Student(dict['id'], dict['email'], dict['password'], dict['name'], )

    def __init__(self, id, email, password, name, subjects):
        self.id = id
        self.email = email
        self.password = password
        self.name = name
        self.enrolled_subjects = [Subject.from_dict(subject) for subject in subjects] 
        self.max_subjects = 4

    def __str__(self):
        return f"{self.name} :: {self.id} --> Email: {self.email}"

    def to_dict(self):
        return {'id': self.id, 'email': self.email, 'password': self.password, 'name': self.name, 'enrolled_subjects': json.dumps([subject.to_dict() for subject in self.enrolled_subjects])}
    
    def enroll_subject(self, subject):
        if len(self.enrolled_subjects) < self.max_subjects:
            self.enrolled_subjects.append(subject)
            print(f"Enrolling in Subject-{subject.id}")
            print(f"You are enrolled in {len(self.enrolled_subjects)} out of {self.max_subjects} subjects")
        else:
            print("Students are allowed to enrol in 4 subjects only")
    
    def show_enrolled_subjects(self):
        if not self.enrolled_subjects:
            print("Showing 0 subjects")
        else:
            print(f"Showing {len(self.enrolled_subjects)} subjects")
            for subject in self.enrolled_subjects:
                print(subject)
    
    def remove_subject(self, subject_id):
        if subject_id in [subject.id for subject in self.enrolled_subjects]:
            self.enrolled_subjects = [subject for subject in self.enrolled_subjects if subject.id != subject_id]
            print(f"Dropping Subject - {subject_id}")
        else:
            print(f"Subject - {subject_id} not found!")
    
    def change_password(self, new_password, confirm_password):
        if new_password != confirm_password:
            raise Exception("Password does not match - try again")
            
        if Validator.validate_password(new_password):
            self.password = new_password
        else:
            raise Exception("Invalid password format")

