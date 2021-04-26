from domain.Student import *
from domain.Course import *
from domain.Mark import *
screen = curses.initscr()
screen.addstr("Enter number of students: ")
nstu = int(screen.getstr())
for i in range(0, nstu):
    s = Student("", "", "", "")
    s.input_sinfo()
    student_list.append(s)

screen.addstr("Enter number of courses: ")
ncourse = int(screen.getstr())
for i in range(0, ncourse):
    c = Course("", "", "")
    c.input_cinfo()
    course_list.append(c)

screen.addstr("__________Input mark for each course____________ ")

for j in range(len(course_list)):
    for i in range(len(student_list)):
        mark = Mark(student_list[i], course_list[j], "")
        mark.inputmark()
        mark_list += [mark]