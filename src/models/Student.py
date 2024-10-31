import json
from models.Validator import Validator
from models.Subject import Subject

class Student:
    # Creates a Student instance from a dictionary of attributes.
    @staticmethod
    def from_dict(dict):
        return Student(dict['id'], dict['email'], dict['password'], dict['name'])

    # Initializes the Student class with id, email, password, name, and enrolled subjects.
    def __init__(self, id, email, password, name, subjects):
        self.id = id  # Unique identifier for the student.
        self.email = email  # Email address of the student.
        self.password = password  # Password for student authentication.
        self.name = name  # Name of the student.
        # List of subjects the student is enrolled in, created from the subject data.
        self.enrolled_subjects = [Subject.from_dict(subject) for subject in subjects]
        self.max_subjects = 4  # Maximum number of subjects a student can enroll in.

    # Returns a string representation of the student, showing name, ID, and email.
    def __str__(self):
        return f"{self.name} :: {self.id} --> Email: {self.email}"

    # Converts the Student object into a dictionary for easy storage and retrieval.
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'name': self.name,
            # Serializes the list of enrolled subjects.
            'enrolled_subjects': json.dumps([subject.to_dict() for subject in self.enrolled_subjects])
        }

    # Enrolls the student in a new subject if they are below the max subject limit.
    def enroll_subject(self, subject):
        if len(self.enrolled_subjects) < self.max_subjects:
            self.enrolled_subjects.append(subject)
        else:
            raise Exception("Students are allowed to enroll in 4 subjects only")

    # Removes a subject from the student's enrolled subjects by subject ID.
    def remove_subject(self, subject_id):
        # Checks if the subject exists in the enrolled subjects list.
        if subject_id in [subject.id for subject in self.enrolled_subjects]:
            self.enrolled_subjects = [subject for subject in self.enrolled_subjects if subject.id != subject_id]
            print(f"Dropping Subject - {subject_id}")
        else:
            raise Exception(f"Subject - {subject_id} not found!")

    # Changes the student's password if the new password is valid and matches the confirmation.
    def change_password(self, new_password, confirm_password):
        if new_password != confirm_password:
            raise Exception("Password does not match - try again")
        # Validates the password format before updating it.
        if Validator.validate_password(new_password):
            self.password = new_password
        else:
            raise Exception("Invalid password format")

    # Calculates and returns the student's average mark across all enrolled subjects.
    def get_avg_mark(self):
        if (len(self.enrolled_subjects) == 0):
            return 0
        return sum([subject.mark for subject in self.enrolled_subjects]) / len(self.enrolled_subjects)

    # Determines and returns the student's grade based on their average mark.
    def get_grade(self):
        avg_mark = self.get_avg_mark()
        if avg_mark >= 85:
            return "HD"  # High Distinction
        elif avg_mark >= 75:
            return "D"  # Distinction
        elif avg_mark >= 65:
            return "C"  # Credit
        elif avg_mark >= 50:
            return "P"  # Pass
        else:
            return "F"  # Fail
