import json
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
                student_file.write('{}')

        student_file = pd.read_csv(student_filepath, dtype=str)
        student_dict = student_file.astype(str).to_dict(orient='records')
        self.students = [Student(item['id'], item['email'], str(item['password']), item['name'], json.loads(item['enrolled_subjects'])) for item in student_dict] 

    def __student_filepath(self):
        scriptpath = os.path.abspath(sys.argv[0])
        scriptdir = os.path.dirname(scriptpath)
        return scriptdir + "/students.data"

    def __subject_filepath(self):
        scriptpath = os.path.abspath(sys.argv[0])
        scriptdir = os.path.dirname(scriptpath)
        return scriptdir + "/subjects.data"

    def __save_current_state(self):
        filepath = self.__student_filepath()
        if (len(self.students) == 0):
            os.remove(self.__student_filepath())
        else:
            df = pd.DataFrame([student.to_dict() for student in self.students])
            df.to_csv(filepath, index=False)

    def __generate_student_id(self):
        num = random.randint(1, 999999)
        id = f"{(6 - len(str(num))) * '0'}{num}"

        # Check if the generated id is already in the database
        if (id in [student.id for student in self.students]):
            return self.__generate_student_id()

        return id

    def __is_student_exists(self, email=None, id=None):
        return email in [student.email for student in self.students] or id in [student.id for student in self.students]

    def get_student_by_email_and_password(self, email, password):
        for student in self.students:
            if student.email == email and student.password == str(password):
                return student

        raise Exception("Student does not exist")

    def insert_student(self, email, password, name):
        if (self.__is_student_exists(email=email)):
            raise Exception("Student have already existed")

        id = self.__generate_student_id()
            
        self.students.append(Student(id, email, password, name, {}))

        self.__save_current_state()
        return True

    def update_student(self, student):
        self.students = [student if s.id ==
                         student.id else s for s in self.students]

        self.__save_current_state()
        return True

    def remove_student(self, id):
        if (self.__is_student_exists(id=id) is False):
            raise Exception(f"Student {id} does not exist")
        self.students = [
            student for student in self.students if student.id != id]

        self.__save_current_state()
        return True

    def get_all_students(self):
        return [student for student in self.students]

    def clear_database(self):
        self.students = []
        self.__save_current_state()
        return True

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
                       
