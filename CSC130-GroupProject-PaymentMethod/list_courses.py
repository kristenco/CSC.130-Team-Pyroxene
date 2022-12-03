import pandas as pd
def display_courses():
    classes = {'Class': ['CSC_120', 'CSC_121', 'CSC_130', 'CTI_120', 'CTI_110'], 'Price': [300, 300, 300, 300, 300]}
    df = pd.DataFrame.from_records(classes)
    print(df)
display_courses()


def list_courses():
    courses = {'CSC.120': 300, 'CSC.121': 300, 'CSC.130': 300, 'CTI.120': 300, 'CTI.110': 300}
    print(list(courses.keys()))
    course_input = [item for item in input("Enter courses you would like to add(enter q to quit): ").split()]
    print(course_input)
list_courses()