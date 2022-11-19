from course_functions import Courses

if __name__ == "__main__":
    # Continue offering selection menu until user exits.
    courses = Courses()
    menu = input('Course Menu\n1 - Add a course.\n2 - Add student to a wait list.\n3 - Remove a course.\n'
                 '4 - List the courses.\n5 - Pay for the courses.\n0 - To exit.\nEnter your choice: ')
    while menu != '0':
        if menu == '1':
            courses.add_course()
        elif menu == '2':
            courses.wait_list_student()
        elif menu == '3':
            courses.remove_course()
        elif menu == '4':
            courses.list_courses()
        elif menu == '5':
            courses.pay_for_courses()
        else:
            print('Invalid Choice.')
        menu = input('Course Menu\n1 - Add a course.\n2 - Add student to a wait list.\n3 - Remove a course.\n'
                     '4 - List the courses.\n5 - Pay for the courses.\n0 - To exit.\nEnter your choice: ')
