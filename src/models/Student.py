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
        else:
            raise Exception("Students are allowed to enrol in 4 subjects only")
    
    def remove_subject(self, subject_id):
        if subject_id in [subject.id for subject in self.enrolled_subjects]:
            self.enrolled_subjects = [subject for subject in self.enrolled_subjects if subject.id != subject_id]
            print(f"Dropping Subject - {subject_id}")
        else:
            raise Exception(f"Subject - {subject_id} not found!")
    
    def change_password(self, new_password, confirm_password):
        if new_password != confirm_password:
            raise Exception("Password does not match - try again")
            
        if Validator.validate_password(new_password):
            self.password = new_password
        else:
            raise Exception("Invalid password format")
        
    def get_avg_mark(self):
        return sum([subject.mark for subject in self.enrolled_subjects]) / len(self.enrolled_subjects)
    
    def get_grade(self):
        avg_mark = self.get_avg_mark()
        if avg_mark >= 85:
            return "HD"
        elif avg_mark >= 75:
            return "D"
        elif avg_mark >= 65:
            return "C"
        elif avg_mark >= 50:
            return "P"
        else:
            return "F"

