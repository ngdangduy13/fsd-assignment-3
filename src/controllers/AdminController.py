from models.Database import Database
from utils.Logger import Logger
from utils.String import StringUtils


class AdminController:
    def remove_student(self, student_id):
        db = Database()
        db.remove_student(student_id)
        Logger.log_yellow(f"Removing Student {student_id} Account")

    def list_students(self):
        Logger.log_yellow(f"Student List")
        db = Database()
        students = db.get_all_students()
        if(len(students) == 0):
            print("Nothing to display")
        else:
            for student in students:
                print(student)

    def clear_database(self):
        Logger.log_yellow(f"Clearing students database")
        confirm = input(StringUtils.to_red_string(
            'Are you sure you want to clear the database (Y)ES (N)O: '))
        if (confirm.lower() == 'y'):
            db = Database()
            db.clear_database()
            Logger.log_yellow(f"Students data cleared")

    def main(self):
        while (True):
            try:
                option = input(StringUtils.to_cyan_string(
                    "Admin System (c/g/p/r/s/x): "))
                if option.lower() == "r":
                    student_id = input("Remove by ID: ")
                    self.remove_student(student_id)
                elif option.lower() == "s":
                    self.list_students()
                elif option.lower() == "c":
                    self.clear_database()
                elif option == "x":
                    break
                else:
                    print("Invalid option")
            except Exception as e:
                Logger.log_red(e)
