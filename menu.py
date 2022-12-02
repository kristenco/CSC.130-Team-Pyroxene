from course_functions import Courses

if __name__ == "__main__":
    # Continue offering selection menu until user exits.
    courses = Courses()
    login = True

    while True:
        while login:
            print(f"Student Registration Login:")
            name = input("Name: ")
            id = input("Student ID: ")
            login = False
        print()
        menu = input('Course Menu\n1 - Add a course.\n2 - Remove a course.\n'
                     '3 - List the courses.\n4 - Pay for the courses.\n5 - Log in as different student\n0 - To exit.\nEnter your choice: ')
        if menu == '1':
            courses.add_course()
        elif menu == '2':
            courses.remove_course()
        elif menu == '3':
            courses.list_courses()
        elif menu == '4':
            courses.pay_for_courses()
        elif menu == '5':
            login = True
            print()
        elif menu == '0':
            print("\nExiting...")
            break
        else:
            print('Invalid Choice.')
        
