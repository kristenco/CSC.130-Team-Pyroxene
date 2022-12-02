"""
    Course functions:
        - Add a course function
        - Add student to a wait list (a queue) function
        - Remove a course function
        - List the classes a student is taking
        - Paying for the courses
"""

"""
    class ListQueue(object):
        def __init__(self, sourceCollection=None):
            self.items = []
            self.size = 0
            if sourceCollection:
                self.add(sourceCollection)

        def __len__(self):
            return self.size

        def __iter__(self):
            for i in self.items:
                yield i

        def __str__(self):
            return "{" + ",".join(map(str, self)) + "}"

        def __add__(self, other):
            ret_val = ListQueue(self)
            for item in other:
                ret_val.add(item)
            return ret_val

        def add(self, item):
            self.items.append(item)
            self.size += 1

        def pop(self):
            if self.isEmpty():
                raise IndexError("Queue is empty")
            else:
                val = self.items[0]
                del self.items[0]
                return val
"""

class ListQueue(object):
    """A list-based stack implementation."""

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = []
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

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

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        for i in self.items:
            if len(self.items) != len(other):
                return False
        return True

    def peek(self):
        """Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises IndexError if queue is empty."""
        if self.isEmpty():
            raise IndexError("Index is empty")
        else:
            for i in self.items:
                if i == self.items[0]:
                    return i

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.items.clear()

    def add(self, item):
        """Inserts item at rear of the queue."""
        self.items.append(item)
        self.size += 1

    def pop(self):
        """Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises IndexError if queue is not empty.
        Postcondition: the front item is removed from the queue."""
        if self.isEmpty():
            raise IndexError("Queue is empty")
        else:
            val = self.items[0]
            del self.items[0]
            return val
class Courses:
    def __init__(self):
        self.courses = []



    def add_course(self):
        seats = 0
        course_input = (input('Enter the course you\'d like to add: ')).upper()
        if course_input in self.courses:
            print('You\'ve already registered for this class.')
        elif seats <= 0:
            waitlist = ListQueue(self)
            print(str(waitlist))
            print(f"\n\nThis class registration is currently full. You've been added to the waitlist.\n"
            f"The number of students in the current waitlist: {len(waitlist)}")
        else:
            self.courses.append(course_input)
            seats -= 1
            print(f'Course {course_input} was added.')

    def remove_course(self):
        course_input = input('Enter the course you\'d like to remove or enter "All" to remove all: ').upper()
        if course_input == 'ALL':
            self.courses.clear()
            print('All courses deleted.')
        elif course_input not in self.courses and course_input != 'ALL':
            print('That course does not exist.')
        else:
            self.courses.remove(f'{course_input}')
            print(f'Course {course_input} was removed.')

    def list_courses(self):
        # TODO
        pass

    def pay_for_courses(self):
        # TODO
        pass
