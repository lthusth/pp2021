from output import *

screen = curses.initscr()
screen.addstr("preparing to initialize screen...\n"
              "Screen initialized.")
screen.refresh()
curses.napms(2000)
screen.clear()

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