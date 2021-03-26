student_list = []
course_list = []
mark_value = []


def student_info():
    nstu = int(input('Enter student numbers: '))
    for i in range(nstu):
        info = {
            'id': str(input('Enter student id: ')),
            'name': str(input('Enter student name: ')),
            'dob': str(input('Enter student dob: '))
        }
        student_list.append(info)


def course_info():
    ncourse = int(input('Enter course numbers: '))
    for i in range(ncourse):
        course = {
            'id': str(input('Enter course ID: ')),
            'name': str(input('Enter course name: '))
        }
        course_list.append(course)


def printStudents():
    print('---------Student details----------')
    for student in student_list:
        print(' Student ID: ' + student['id'] + ' - ' + ' Student name: ' + student['name'] + ' - ' + ' Student DOB: ' + student['dob'])

def printCourses():
    print('----------Course available details-----------')
    for course in course_list:
        print(' Course ID: ' + course['id'] + ' - ' + ' Course name: ' + course['name'])

def inputMark():
    print('Input mark for each course: ')
    for course in course_list:
        print('- Course {}: '.format(course['name']))
        for student in student_list:
            value = input('+ Input mark for the student {}: '.format(student['name']))
            mark_value.append(
                {' Student name: ': student['name'], ' Course name: ': course['name'], ' Mark value: ': value, })

def printMark():
    for value in mark_value:
        print(value)

student_info()
course_info()
printStudents()
printCourses()
inputMark()
printMark()
