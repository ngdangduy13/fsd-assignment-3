from controllers.StudentController import StudentController


class UniversityController:
    def main(self):
        print("THE UNIVERSITY SYSTEM")
        while (True):
            print("=====================================")
            print("(A) Admin")
            print("(S) Student")
            print("(X) Exit")
            option = input("Choose an option: ")
            print("=====================================")
            if option == "a":
                continue
            elif option == "s":
                student_controller = StudentController()
                student_controller.main()
            elif option == "x":
                break
            else:
                print("Invalid option")