from models.Validator import Validator


class Student:
    @staticmethod
    def from_dict(dict):
        return Student(dict['id'], dict['email'], dict['password'], dict['name'])

    def __init__(self, id, email, password, name):
        self.id = id
        self.email = email
        self.password = password
        self.name = name
        self.subjects = []

    def __str__(self):
        return f"{self.name} :: {self.id} --> Email: {self.email}"

    def __to_dict(self):
        return {'id': self.id, 'email': self.email, 'password': self.password, 'name': self.name}

