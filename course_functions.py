import pandas as pd

"""
    Course functions:
        - Add a course function
        - Add student to a wait list (a queue) function
        - Remove a course function
        - List the classes a student is taking
        - Paying for the courses
"""


class ListQueue(object):
    """A list-based stack implementation."""

    # Constructor
    def __init__(self, student=None):
        self.items = []
        self.size = 0
        if student:
            self.items.append(student)
            self.size += 1

    # Accessor methods
    def isEmpty(self):
        """Returns True if the queue is empty, or False otherwise."""
        return len(self.items) == 0

    def __len__(self):
        """Returns the number of items in the queue."""
        return self.size

    def __str__(self):
        """Returns the string representation of the queue."""
        return "{" + ",".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of the queue."""
        for i in self.items:
            yield i

    def __add__(self, other):
        """Returns a new queue containing the contents
        of self and other."""
        ret_val = ListQueue(self)
        for item in other:
            ret_val.add(item)
        return ret_val

    # Mutator methods

    def add(self, item):
        """Inserts item at rear of the queue."""
        self.items.append(item)
        self.size += 1

    def clear(self):
        """Makes self become empty."""
        self.items.clear()


def display_courses():
    classes = {'Class': ['CSC120', 'CSC121', 'CSC130', 'CTI120', 'CTI110'], 'Price': [300, 300, 300, 300, 300]}
    pd.set_option('display.colheader_justify', 'center')
    df = pd.DataFrame.from_records(classes)
    print(df.to_string(index=False))

    return classes['Class']

class Courses:
    def __init__(self):
        self.courses = []
        self.waitlist = ListQueue()
        self.seats = 2
        self.payment_owed = 0

    def add_course(self):
        course_choices = []
        print(f"The current courses available are: ")
        for i in display_courses():
            course_choices.append(i)
        course_input = (input('Enter the course you\'d like to add: ')).upper()
        if course_input in self.courses:
            print('You\'ve already registered for this class.')
        elif course_input not in course_choices:
            print("That is not a course available to take. Sending you back to the menu.")
        elif self.seats <= 0:
            self.waitlist.add(course_input)
            print(f"\n\nThis class registration is currently full. You've been added to the waitlist.\n"
                  f"The number of students in the current waitlist: {len(self.waitlist)}\n"
                  f"Current waitlist: {self.waitlist}")
        else:
            self.courses.append(course_input)
            self.seats -= 1
            print(f'Course {course_input} was added.')
        print()

    def remove_course(self):
        if not self.courses:
            print("You are currently not registered for any courses. Sending you back to the menu.")
        else:
            course_input = input('Enter the course you\'d like to remove or enter "All" to remove all: ').upper()
            if course_input == 'ALL':
                self.courses.clear()
                print('All courses deleted.')
            elif course_input not in self.courses and course_input != 'ALL':
                print('You are not currently registered for that course.')
            else:
                self.courses.remove(f'{course_input}')
                print(f'Course {course_input} was removed.')
        print()

    def list_courses(self):
        if not self.courses:
            print("You're not currently registered for any courses.")
        else:
            for i in self.courses:
                print(i)
        print()

    def pay_for_courses(self):
        courses = self.courses
        self.payment_owed = len(courses) * 300
        if not self.courses:
            print("You are currently not registered for any courses. Sending you back to the menu.")
        else:
            print("Your current registered classes are: ")
            for i in self.courses:
                print(i)
            print("You class payment is $", self.payment_owed)

            if self.payment_owed == 0:
                print("You do not currently have any courses for which you need to pay.")
            else:
                payment_method = input("Pay online or at the cashiers office. Type \"online\" or \"cash\" to proceed:")

                if payment_method == "online":
                    try:
                        card_holder_name = str(input("Please enter card holders name:"))
                        card_num = int(input("Please enter card number(no spaces):"))
                        exp_date = input("Please enter expiration date:")
                        security_code = int(input("Please enter 3 digit security code:"))
                        print("Thank you, your payment has been accepted.")
                        self.courses.clear()
                    except ValueError:
                        print("Invalid input. Sending you back to the menu.")

                elif payment_method == "cash":
                    print("""Thank you. You can pay at Scott Northern Wake Campus. 
                The address for the cashiers office is 6600 Louisburg Road Raleigh, NC 27616. 
                It is located in Building C, Office 236D.
                The phone number of the cashiers office is 919-866-5460. 
                Office hours are Monday - Friday: 8 a.m. - 5 p.m. Closed for lunch: 2 p.m. - 3 p.m.""")
                    self.courses.clear()
                else:
                    print("Invalid input. Sending you back to the menu.")
