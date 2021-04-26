import curses
screen = curses.initscr()

student_list = []
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
        self._sid = screen.getstr().decode()
        screen.addstr("Enter student name: ")
        self._sname = screen.getstr().decode()
        screen.addstr("Enter student DOB: ")
        self._dob = screen.getstr().decode()
        self._gpa = 0
        screen.clear()
        screen.refresh()

    def __str__(self):
        return f" Student name is: {self._sname}, with ID: {self._sid} , dob is: {self._dob}"

    def show_student(self):
        screen.addstr(self.__str__())