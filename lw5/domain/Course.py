import curses
screen = curses.initscr()
course_list = []
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