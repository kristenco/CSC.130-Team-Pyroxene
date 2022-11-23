"""
    Course functions:
        - Add a course function
        - Add student to a wait list (a queue) function
        - Remove a course function
        - List the classes a student is taking
        - Paying for the courses
"""


class Courses:
    def __init__(self):
        self.courses = {}

    def add_course(self):
        # TODO
        pass

    def wait_list_student(self):
        # TODO
        pass

    def remove_course(self):
        course_input = input('Enter the course you\'d like to remove or enter "All" to remove all: ').upper()
        if course_input == 'ALL':
            self.courses = {}
            print('All courses deleted.')
        elif course_input not in self.courses.keys() and course_input != 'ALL':
            print('That course does not exist.')
        else:
            del self.courses[course_input]
            print(f'Course {course_input} was removed.')

    def list_courses(self):
        # TODO
        pass

    def pay_for_courses(self):
        # TODO
        pass
