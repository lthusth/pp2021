student_list = []
course_list = []
mark_list = []
# import numpy as np
import curses
import math

screen = curses.initscr()
screen.addstr("preparing to initialize screen...\n"
              "Screen initialized.")
screen.refresh()
curses.napms(2000)
screen.clear()


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
        screen.addstr("Enter student ID: ")
        self._sid = screen.getstr()
        screen.addstr("Enter student name: ")
        self._sname = screen.getstr()
        screen.addstr("Enter student DOB: ")
        self._dob = screen.getstr()
        screen.clear()
        screen.refresh()

    def __str__(self):
        return f""" Student name is: {self._sname}
        with ID: {self._sid}  
        dob is: {self._dob} """

    def show_student(self):
        screen.addstr(self.__str__())


screen.addstr("Enter number of students: ")
nstu = int(screen.getstr())
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
        screen.addstr("Enter course ID: ")
        self._cid = screen.getstr()
        screen.addstr("Enter course name: ")
        self._cname = screen.getstr()
        screen.addstr("Enter number of credits: ")
        self._credits = screen.getstr()

    def __str__(self):
        return f""" Course name is: {self._cname}
        with course ID: {self._cid}
        {self._credits} credits """

    def show_course(self):
        screen.addstr(self.__str__())


screen.addstr("Enter number of courses: ")
ncourse = int(screen.getstr())
for i in range(0, ncourse):
    c = Course("", "", "")
    c.input_cinfo()
    course_list.append(c)


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
        screen.addstr(f"Enter mark for student {self._student.getsname()}:")
        self._value = int(screen.getstr())

    def __str__(self):
        return f""" {self._student.getsname()} 
                got {self._value} 
                in course: {self._course.getcname()}"""

    def show_mark(self):
        screen.addstr(self.__str__())


screen.addstr("__________Input mark for each course____________ ")

for j in range(len(course_list)):
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


while True:
    screen.addstr(
        "Choose options you want: \n"
        "1: Student_info \n"
        "2: Course info \n"
        "3: Show mark \n"
        "4: Calculate gpa \n")

    screen.refresh()
    main = int(screen.getstr())

    if main == 1:
        screen.clear()
        for student in student_list:
            student.show_student()
        screen.refresh()

    elif main == 2:
        screen.clear()
        for course in course_list:
            course.show_course()
        screen.refresh()

    elif main == 3:
        screen.clear()
        for mark in mark_list:
            mark.show_mark()
        screen.refresh()

    elif main == 4:
        screen.clear()
        for student in student_list:
            calculate_gpa(student.getsname())
            screen.addstr(f'{student.getsname()} got  {student.getgpa()} in gpa')
        screen.refresh()

    else:
        break
    screen.addstr("window ended.")

# print(*map(lambda m: m.getcname(), course_list), sep='\n')
# course_list[0].getcname() == mark_list[0].getcourse().getcname()
# mark_list[0].getstudent().getsname()
