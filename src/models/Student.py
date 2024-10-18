from models.Database import Database
from models.Validator import Validator


class Student:
    @staticmethod
    def register(email, password, name):

        db = Database()
        if (email in [student['email'] for student in db.students]):
            raise Exception("Student already exists")

        return db.write_student(email, password, name)

    @staticmethod
    def login(email, password):
        db = Database()
        student = db.get_student_by_email_and_password(email, password)
        if student:
            return Student(student['id'], student['email'], student['password'], student['name'])

        raise Exception("Invalid email or password")

    def __init__(self, id, email, password, name):
        self.id = id
        self.email = email
        self.password = password
        self.name = name
        self.subjects = []

    def __str__(self):
        return f"Email: {self.email}"

    def __to_dict(self):
        return {'id': self.id, 'email': self.email, 'password': self.password, 'name': self.name}

    def change_password(self, new_password):
        validator = Validator()
        is_valid_password = validator.validate_password(new_password)
        if (not is_valid_password):
            raise Exception("Invalid password")

        self.password = new_password
        db = Database()
        db.update_student(self.__to_dict())
        return True
