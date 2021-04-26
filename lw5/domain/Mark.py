import curses
screen = curses.initscr()
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
        screen.addstr(f"Enter mark for student {self._student.getsname()}:")
        self._value = int(screen.getstr())

    def __str__(self):
        return f""" {self._student.getsname()} 
                got {self._value} 
                in course: {self._course.getcname()}"""

    def show_mark(self):
        screen.addstr(self.__str__())