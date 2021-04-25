# import numpy as np
import curses
#curses
print("preparing to initialize screen...")
screen = curses.initscr()
print("Screen initialized.")
screen.refresh()
curses.napms(2000)
curses.endwin()
import math
student_list = []
course_list = []
mark_list = []


class Student:
    def __init__(self, sname, sid, dob, gpa):
        self._sid = sid
        self._sname = sname
        self._dob = dob
        self._gpa = gpa

    def getsid(self):
        return self._sid

    def getsname(self):
        return self._sname

    def getdob(self):
        return self._dob

    def getgpa(self):
        return self._gpa

    def setgpa(self, gpa):
        self._gpa = gpa

    def input_sinfo(self):
        self._sid = input("Enter student ID: ")
        self._sname = input("Enter student name: ")
        self._dob = input("Enter student DOB: ")

    def __str__(self):
        return f'Student name is: {self._sname}, with ID: {self._sid}, dob is: {self._dob}'

    def show_student(self):
        print(self.__str__())


nstu = int(input("Enter number of students: "))
for i in range(0, nstu):
    s = Student("", "", "", "")
    s.input_sinfo()
    student_list.append(s)


class Course:
    def __init__(self, cname, cid, credits):
        self._cid = cid
        self._cname = cname
        self._credits = credits

    def getcid(self):
        return self._cid

    def getcname(self):
        return self._cname

    def getcredits(self):
        return int(self._credits)

    def input_cinfo(self):
        self._cid = input("Enter course ID: ")
        self._cname = input("Enter course name: ")
        self._credits = input("Enter number of credits: ")

    def __str__(self):
        return f'Course name is: {self._cname}, with course ID: {self._cid}, {self._credits} credits'

    def show_course(self):
        print(self.__str__())


ncourse = int(input("Enter number of courses: "))
for i in range(0, ncourse):
    c = Course("", "", "")
    c.input_cinfo()
    course_list.append(c)

mark_list = []


class Mark:
    def __init__(self, sname, cname, value):
        self._student = sname
        self._course = cname
        self._value = value

    def getstudent(self):
        return self._student

    def getcourse(self):
        return self._course

    def getmark(self):
        return int(self._value)

    def inputmark(self):
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
        mark.inputmark()
        mark_list += [mark]


def calculate_gpa(sname):
    total = 0
    total_credits = 0
    for mark in mark_list:
        if mark.getstudent().getsname() == sname:
            for course in course_list:
                if course.getcname() == mark.getcourse().getcname():
                    total += int(mark.getmark()) * int(course.getcredits())
                    total_credits += int(course.getcredits())
    for student in student_list:
        if student.getsname() == sname:
            student.setgpa(math.floor(total / total_credits))

class Display:
        while True:
            main = int(input("Choose options you want: \n"
                             "1: Student_info \n"
                             "2: Course info \n"
                             "3: Show mark \n"
                             "4: Calculate gpa \n"))

            if main == 1:
                for student in student_list:
                    student.show_student()
            elif main == 2:
                for course in course_list:
                    course.show_course()
            elif main == 3:
                for mark in mark_list:
                    mark.show_mark()
            elif main == 4:
                for student in student_list:
                    calculate_gpa(student.getsname())
                    print(f"{student.getsname()} got  {student.getgpa()} in gpa")
            else:
                break
            print("window ended.")
    # print(*map(lambda m: m.getcname(), course_list), sep='\n')
# course_list[0].getcname() == mark_list[0].getcourse().getcname()
# mark_list[0].getstudent().getsname()
