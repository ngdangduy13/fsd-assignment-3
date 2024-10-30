import random as r

class Subject:
    # Creates a Subject instance from a dictionary of attributes.
    @staticmethod
    def from_dict(dict):
        return Subject(id=dict['id'], mark=dict['mark'])

    # Initializes the Subject class with id, mark, and grade attributes.
    def __init__(self, id=None, mark=None):
        # Generates a random 3-digit ID if none is provided.
        self.id = id or f'{r.randint(1,999):03}'
        # Assigns a mark between 25 and 100 if none is provided.
        self.mark = mark or r.randint(25, 100)
        # Calculates and assigns the grade based on the mark.
        self.grade = self.calculate_grade()

    # Determines and returns the grade based on the subject mark.
    def calculate_grade(self):
        if self.mark >= 85:
            return "HD"  # High Distinction
        elif self.mark >= 75:
            return "D"  # Distinction
        elif self.mark >= 65:
            return "C"  # Credit
        elif self.mark >= 50:
            return "P"  # Pass
        else:
            return "F"  # Fail

    # Provides a string representation of the subject with ID, mark, and grade.
    def __str__(self):
        return f"[ Subject::{self.id} -- mark = {self.mark} -- grade = {self.grade} ]"

    # Converts the Subject object into a dictionary for easy storage and retrieval.
    def to_dict(self):
        return {
            'id': self.id,
            'mark': self.mark,
            'grade': self.grade
        }
