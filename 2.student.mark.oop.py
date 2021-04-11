student_list = []
course_list = []
mark_list = []
nstu = int(input("Enter number of students: "))
class Student:
    def __init__(self, sname, sid, dob):
        self._sid = sid
        self._sname = sname
        self._dob = dob

    def getsid(self):
        return self._sid

    def getsname(self):
        return self._sname

    def getdob(self):
        return self._dob

    def input_sinfo(self):
        self._sid = input("Enter student ID: ")
        self._sname = input("Enter student name: ")
        self._dob = input("Enter student DOB: ")

    def __str__(self):
        return f'Student name is: {self._sname}, ' \
               f'with ID: {self._sid}' \
               f' dob is: {self._dob}'

    def show_student(self):
        print(self.__str__())

for i in range(0, nstu):
    s = Student("", "", "")
    s.input_sinfo()
    student_list.append(s)
for student in student_list:
    print(student)


ncourse = int(input("Enter number of courses: "))
class Course:
    def __init__(self, cname, cid):
        self._cid = cid
        self._cname = cname

    def getcid(self):
        return self._cid

    def getcname(self):
        return self._cname

    def input_cinfo(self):
        self._cid = input("Enter course ID: ")
        self._cname = input("Enter course name: ")

    def __str__(self):
        return f'Course name is: {self._cname}, with course ID: {self._cid}'

    def show_course(self):
        print(self.__str__())

for i in range(0, ncourse):
    c = Course("", "")
    c.input_cinfo()
    course_list.append(c)
for course in course_list:
    print(course)


class Mark:
    def __init__(self, sname, cname, value):
        self._student = sname
        self._course = cname
        self._value = value

    def input(self):
        self._value = input(f"Enter mark for student {self._student.getsname()}:")

    def __str__(self):
        return f'{self._student.getsname()} got {self._value} in course: {self._course.getcname()}'

    def show_mark(self):
        print(self.__str__())

print("____________Input mark for each course______________ ")

for j in range(len(course_list)):
    print('{}: '.format(course_list[j]))
    for i in range(len(student_list)):
        mark = Mark(student_list[i], course_list[j], "")
        mark.input()
        mark_list.append(mark)
for mark in mark_list:
    print(mark)