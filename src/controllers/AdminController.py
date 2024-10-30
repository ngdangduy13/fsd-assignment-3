from models.Database import Database
from utils.Logger import Logger
from utils.String import StringUtils

class AdminController:
    # Removes a student from the database by their student ID.
    def remove_student(self, student_id):
        db = Database()  # Creates a database instance.
        db.remove_student(student_id)  # Calls the database to remove the student.
        Logger.log_yellow(f"Removing Student {student_id} Account")  # Logs the removal action.

    # Retrieves and displays the list of all students in the database.
    def list_students(self):
        Logger.log_yellow("Student List")  # Logs the action of listing students.
        db = Database()  # Creates a database instance.
        students = db.get_all_students()  # Retrieves all students from the database.
        if len(students) == 0:
            print("< Nothing to display >")  # Notifies if no students are present.
        else:
            for student in students:  # Iterates and prints each student's information.
                print(student)

    # Clears the entire student database after user confirmation.
    def clear_database(self):
        Logger.log_yellow("Clearing students database")  # Logs the clearing action.
        confirm = input(StringUtils.to_red_string(
            'Are you sure you want to clear the database (Y)ES (N)O: '))  # Prompts for confirmation.
        if confirm.lower() == 'y':
            db = Database()  # Creates a database instance.
            db.clear_database()  # Calls the database to clear all student data.
            Logger.log_yellow("Students data cleared")  # Logs successful clearance.

    # Partitions students into pass and fail categories based on average marks.
    def partition_students(self):
        Logger.log_yellow("PASS/FAIL Partition")  # Logs the partition action.
        db = Database()  # Creates a database instance.
        students = db.get_all_students()  # Retrieves all students.
        # Divides students into fail or pass based on their average mark.
        fail_students = [student for student in students if student.get_avg_mark() < 50]
        pass_students = [student for student in students if student.get_avg_mark() >= 50]
        # Displays the students in the fail and pass lists with grade and mark.
        print(f"FAIL --> {[f'{student.name} :: {student.id} --> GRADE: {student.get_grade()} - MARK: {student.get_avg_mark():.2f}' for student in fail_students]}")
        print(f"PASS --> {[f'{student.name} :: {student.id} --> GRADE: {student.get_grade()} - MARK: {student.get_avg_mark():.2f}' for student in pass_students]}")

    # Groups students by their grade and displays each group with student information.
    def group_by_grade(self):
        Logger.log_yellow("Grade Grouping")  # Logs the grouping action.
        db = Database()  # Creates a database instance.
        students = db.get_all_students()  # Retrieves all students.
        grade_dict = {}  # Initializes a dictionary for grade-based grouping.
        # Groups students by grade, adding each student to the appropriate list.
        for student in students:
            grade_dict.setdefault(student.get_grade(), []).append(student)
        
        if len(grade_dict) == 0:
            print("< Nothing to display >")  # Notifies if no data to display.
        else:
            # Iterates through the grade dictionary and prints each group.
            for grade, students in grade_dict.items():
                print(f"{grade} --> {[f'{student.name} :: {student.id} --> MARK: {student.get_avg_mark():.2f}' for student in students]}")

    # Provides the main admin menu for different student management operations.
    def main(self):
        while True:
            try:
                # Prompts the admin for an action selection.
                option = input(StringUtils.to_cyan_string("Admin System (c/g/p/r/s/x): "))
                if option.lower() == "r":
                    student_id = input("Remove by ID: ")  # Prompts for student ID to remove.
                    self.remove_student(student_id)  # Calls remove_student with the provided ID.
                elif option.lower() == "s":
                    self.list_students()  # Lists all students if 's' is selected.
                elif option.lower() == "g":
                    self.group_by_grade()  # Groups students by grade if 'g' is selected.
                elif option.lower() == "p":
                    self.partition_students()  # Partitions students by pass/fail if 'p' is selected.
                elif option.lower() == "c":
                    self.clear_database()  # Clears the database if 'c' is selected.
                elif option == "x":
                    break  # Exits the menu if "x" is selected.
                else:
                    print("Invalid option")  # Notifies the admin of an invalid option.
            except Exception as e:
                Logger.log_red(e)  # Logs any exceptions encountered.
