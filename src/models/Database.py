import random
import pandas as pd
import os
import sys
from pathlib import Path

from models.Student import Student


class Database:

    def __init__(self):
        # Get students
        student_filepath = self.__student_filepath()
        if (Path(student_filepath).exists() is False):
            # Create a new file with the header
            with open(student_filepath, 'x') as student_file:
                student_file.write('id,email,password,name')

        student_file = pd.read_csv(student_filepath, dtype=str)
        self.students = student_file.astype(str).to_dict(orient='records')

    def __student_filepath(self):
        scriptpath = os.path.abspath(sys.argv[0])
        scriptdir = os.path.dirname(scriptpath)
        return scriptdir + "/students.data"

    def __save_current_state(self):
        filepath = self.__student_filepath()
        if (len(self.students) == 0):
            os.remove(self.__student_filepath())
        else:
            df = pd.DataFrame(self.students)
            df.to_csv(filepath, index=False)

    def __generate_student_id(self):
        num = random.randint(1, 999999)
        id = f"{(6 - len(str(num))) * '0'}{num}"

        # Check if the generated id is already in the database
        if (id in [student['id'] for student in self.students]):
            return self.__generate_student_id()

        return id

    def __is_student_exists(self, email=None, id=None):
        return email in [student['email'] for student in self.students] or id in [student['id'] for student in self.students]

    def get_student_by_email_and_password(self, email, password):
        for student in self.students:
            if student['email'] == email and str(student['password']) == str(password):
                return Student.from_dict(student)

        raise Exception("Student does not exist")

    def insert_student(self, email, password, name):
        if (self.__is_student_exists(email=email)):
            raise Exception("Student have already existed")

        id = self.__generate_student_id()
        self.students.append(
            {'id': id, 'email': email, 'password': password, 'name': name})

        self.__save_current_state()
        return True

    def update_student(self, student):
        self.students = [student if s['id'] ==
                         student['id'] else s for s in self.students]

        self.__save_current_state()
        return True

    def remove_student(self, id):
        if (self.__is_student_exists(id=id) is False):
            raise Exception(f"Student {id} does not exist")
        self.students = [
            student for student in self.students if student["id"] != id]

        self.__save_current_state()
        return True

    def get_all_students(self):
        return [Student.from_dict(student) for student in self.students]

    def clear_database(self):
        self.students = []
        self.__save_current_state()
        return True
