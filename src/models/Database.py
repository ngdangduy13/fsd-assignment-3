import random
import pandas as pd
import os
import sys
from pathlib import Path


class Database:

    def __init__(self):
        filepath = self.__filepath()
        if (Path(filepath).exists() is False):
            # Create a new file with the header
            with open(filepath, 'x') as file:
                file.write('id,email,password,name')

        file = pd.read_csv(filepath, dtype=str)
        self.students = file.astype(str).to_dict(orient='records')

    def __filepath(self):
        scriptpath = os.path.abspath(sys.argv[0])
        scriptdir = os.path.dirname(scriptpath)
        return scriptdir + "/students.data"

    def __save_current_state(self):
        df = pd.DataFrame(self.students)
        filepath = self.__filepath()
        df.to_csv(filepath, index=False)

    def __generate_student_id(self):
        num = random.randint(1, 999999)
        id = f"{(6 - len(str(num))) * '0'}{num}"

        # Check if the generated id is already in the database
        if (id in [student['id'] for student in self.students]):
            return self.__generate_student_id()

        return id

    def __is_student_exists(self, email):
        return email in [student['email'] for student in self.students]

    def get_student_by_email_and_password(self, email, password):
        for student in self.students:
            if student['email'] == email and str(student['password']) == str(password):
                return student

        raise Exception("Invalid email or password")

    def insert_student(self, email, password, name):
        if (self.__is_student_exists(email)):
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
        return False

    def enroll_students_in_subject(self, student_id, subject_id, subject_name, grade = None):
        for student in self.students:
            if student['id'] == student_id:
                if any(sub['id'] == subject_id for sub in student['enrolled_subjects']):
                    return False

                student['enrolled_subjects'].append({
                    'id': subject_id,
                    'name': subject_name,
                    'grade': grade
                })
                self.__save_current_state()
                return True
        return False

    def get_student_subjects(self, student_id):
        for student in self.students:
            if student['id'] == student_id:
                return student['enrolled_subjects']
        return None
                       
