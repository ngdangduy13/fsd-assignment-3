import json
import random
import pandas as pd
import os
import sys
from pathlib import Path

from models.Student import Student

class Database:
    # Initializes the Database class, loading student data from a file or creating a new file if none exists.
    def __init__(self):
        # Retrieves the file path for storing student data.
        student_filepath = self.__student_filepath()
        if not Path(student_filepath).exists():
            # Creates a new student data file if it doesn't exist.
            with open(student_filepath, 'x') as student_file:
                student_file.write('{}')

        # Load students if file is not empty
        if os.stat(student_filepath).st_size > 0:
            student_file = pd.read_csv(student_filepath, dtype=str)
            student_dict = student_file.astype(str).to_dict(orient='records')
            self.students = [
                Student(item['id'], item['email'], str(item['password']), item['name'], json.loads(item['enrolled_subjects']))
                for item in student_dict
            ]
        else:
            self.students = []

    # Returns the file path for the student data file.
    def __student_filepath(self):
        scriptpath = os.path.abspath(sys.argv[0])
        scriptdir = os.path.dirname(scriptpath)
        return scriptdir + "/students.data"

    # Saves the current student data to the student data file.
    def __save_current_state(self):
        # Get the file path for the student data file.
        filepath = self.__student_filepath()
        
        # If there are no students in the list, delete the data file and log the deletion.
        if len(self.students) == 0:
            os.remove(filepath)
            print("File deleted as there are no students.")
        else:
            # Convert the list of Student objects to a DataFrame for saving.
            df = pd.DataFrame([student.to_dict() for student in self.students])
            
            # Save the DataFrame to a CSV file at the specified path, without an index column.
            df.to_csv(filepath, index=False)

    # Generates a unique student ID that is not already in use.
    def __generate_student_id(self):
        num = random.randint(1, 999999)
        id = f"{(6 - len(str(num))) * '0'}{num}"  # Pads ID to be six digits.
        # Recursively generates a new ID if the generated ID already exists.
        if id in [student.id for student in self.students]:
            return self.__generate_student_id()
        return id

    # Checks if a student exists by email or ID.
    def __is_student_exists(self, email=None, id=None):
        return email in [student.email for student in self.students] or id in [student.id for student in self.students]

    # Retrieves a student based on their email and password.
    def get_student_by_email_and_password(self, email, password):
        for student in self.students:
            if student.email == email and student.password == str(password):
                return student
        raise Exception("Student does not exist")

    # Inserts a new student if they do not already exist in the database.
    def insert_student(self, email, password, name):
        if self.__is_student_exists(email=email):
            raise Exception("Student has already existed")
        id = self.__generate_student_id()  # Generates a unique ID for the student.
        self.students.append(Student(id, email, password, name, {}))  # Adds the new student to the list.
        self.__save_current_state()  # Saves the updated student list to the file.
        return True

    # Updates an existing student's information in the database.
    def update_student(self, student):
        # Replaces the student entry if the ID matches the provided student.
        self.students = [student if s.id == student.id else s for s in self.students]
        self.__save_current_state()  # Saves the updated student data.
        return True

    # Removes a student from the database by their ID.
    def remove_student(self, id):
        if not self.__is_student_exists(id=id):
            raise Exception(f"Student {id} does not exist")
        self.students = [student for student in self.students if student.id != id]  # Filters out the student.
        self.__save_current_state()  # Saves the updated student list.
        return True

    # Retrieves all students in the database.
    def get_all_students(self):
        return self.students

    # Clears all student data from the database.
    def clear_database(self):
        self.students = []  # Empties the list of students.
        self.__save_current_state()  # Saves the empty list to the file.
        return True

 
