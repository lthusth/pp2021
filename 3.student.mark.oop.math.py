import time

student_list = []
course_list = []
mark_list = []
# import numpy as np
import curses
import math

screen = curses.initscr()


# screen.addstr("Initializing screen...\n")
# screen.refresh()
# curses.napms(1000)
# screen.addstr("Screen initialized.\n")
# screen.refresh()
# screen.clear()
# curses.napms(2000)


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
        screen.clear()
        screen.addstr("Enter student ID: ")
        self._sid = screen.getstr().decode()
        screen.addstr("Enter student name: ")
        self._sname = screen.getstr().decode()
        screen.addstr("Enter student DOB: ")
        self._dob = screen.getstr().decode()
        screen.clear()
        screen.refresh()

    def __str__(self):
        return f" Student name is: {self._sname}, with ID: {self._sid}, dob is: {self._dob} \n"

    def show_student(self):
        screen.addstr(self.__str__())


screen.addstr("Enter number of students: ")
nstu = int(screen.getstr().decode())
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
        screen.clear()
        screen.addstr("Enter course ID: ")
        self._cid = screen.getstr().decode()
        screen.addstr("Enter course name: ")
        self._cname = screen.getstr().decode()
        screen.addstr("Enter number of credits: ")
        self._credits = screen.getstr().decode()
        screen.clear()

    def __str__(self):
        return f" Course name is: {self._cname}, with course ID: {self._cid}, {self._credits} credits \n"

    def show_course(self):
        screen.addstr(self.__str__())


screen.addstr("Enter number of courses: ")
ncourse = int(screen.getstr().decode())
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
        return float(self._value)

    def inputmark(self):
        screen.addstr(f"Enter mark for student {self._student.getsname()}:")
        self._value = float(screen.getstr().decode())

    def __str__(self):
        return f" {self._student.getsname()} got {self._value} in course {self._course.getcname()} \n"

    def show_mark(self):
        screen.addstr(self.__str__())


screen.addstr("__________Input mark for each course____________ \n")
for j in range(len(course_list)):
    screen.addstr("for course {} \n".format(course_list[j].getcname()))
    for i in range(len(student_list)):
        mark = Mark(student_list[i], course_list[j], "")
        mark.inputmark()
        mark_list += [mark]

    screen.clear()
    screen.refresh()


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


menu = ['Student', 'Course', 'Mark list', 'GPA']


def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w // 2 - len(row) // 2
        y = h // 2 - len(menu) // 2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    stdscr.refresh()


def main(stdscr):
    h, w = stdscr.getmaxyx()

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    text1 = "Initializing screen...."
    text2 = "WELCOME"

    x1 = w // 2 - len(text1) // 2
    y1 = h // 2
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(y1, x1, text1)
    stdscr.refresh()
    time.sleep(3)
    curses.curs_set(0)
    stdscr.clear()

    x2 = w // 2 - len(text2) // 2
    y2 = h // 2
    stdscr.attron(curses.color_pair(2))
    stdscr.addstr(y2, x2, text2)
    stdscr.refresh()
    time.sleep(2.2)
    curses.curs_set(0)
    stdscr.clear()

    current_row_idx = 0
    print_menu(stdscr, current_row_idx)
    while True:
        key = stdscr.getch()
        stdscr.clear()
        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu) - 1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13] and current_row_idx == 0:
            for student in student_list:
                student.show_student()
            stdscr.refresh()
            stdscr.getch()
        elif key == curses.KEY_ENTER or key in [10, 13] and current_row_idx == 1:
            for course in course_list:
                course.show_course()
            stdscr.refresh()
            stdscr.getch()
        elif key == curses.KEY_ENTER or key in [10, 13] and current_row_idx == 2:
            for mark in mark_list:
                mark.show_mark()
            stdscr.refresh()
            stdscr.getch()
        elif key == curses.KEY_ENTER or key in [10, 13] and current_row_idx == 3:
            for student in student_list:
                calculate_gpa(student.getsname())
                stdscr.addstr(f'{student.getsname()} got {student.getgpa()} in gpa\n')
            stdscr.refresh()
            stdscr.getch()
        print_menu(stdscr, current_row_idx)
        stdscr.refresh()
curses.wrapper(main)

# print(*map(lambda m: m.getcname(), course_list), sep='\n')
# course_list[0].getcname() == mark_list[0].getcourse().getcname()
# mark_list[0].getstudent().getsname()


