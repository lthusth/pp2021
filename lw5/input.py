from domain.Student import *
from domain.Course import *
from domain.Mark import *
screen = curses.initscr()
screen.addstr("Enter number of students: ")
nstu = int(screen.getstr().decode())
for i in range(0, nstu):
    s = Student("", "", "", "")
    s.input_sinfo()
    student_list.append(s)
    if len(student_list) == 0:
        f = open("students.txt", "w")
    else:
        f = open("students.txt", "a")
    f.write(s.getsid() + "\n" + s.getsname() + "\n" + s.getdob() + "\n" + str(s.getgpa()) + "\n")
    f.close()

screen.addstr("Enter number of courses: ")
ncourse = int(screen.getstr().decode())
for i in range(0, ncourse):
    c = Course("", "", "")
    c.input_cinfo()
    course_list.append(c)
    if len(course_list) == 0:
        f = open("courses.txt", "w")
    else:
        f = open("courses.txt", "a")
    f.write(c.getcid() + "\n" + c.getcname() + "\n" + str(c.getcredits()) + "\n")
    f.close()

screen.addstr("__________Input mark for each course____________ \n")

for j in range(len(course_list)):
    screen.addstr("for course {} \n".format(course_list[j].getcname()))
    for i in range(len(student_list)):
        mark = Mark(student_list[i], course_list[j], "")
        mark.inputmark()
        mark_list += [mark]
        if len(mark_list) == 0:
            f = open("marks.txt", "w")
        else:
            f = open("marks.txt", "a")
        f.write(mark.getstudent().getsname() + "\n" + mark.getcourse().getcname() + "\n" + str(mark.getmark()) + "\n")
        f.close()