
import random as r

class Subject:
    @staticmethod
    def from_dict(dict):
        return Subject(id=dict['id'], mark = dict['mark'])

    def __init__(self, id= None, mark = None):
        self.id = id or f'{r.randint(1,999):03}'
        self.mark = mark or r.randint(25,100)
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

    def to_dict(self):
        return {
            'id': self.id,
            'mark': self.mark,
            'grade': self.grade 
        }