from output import *
from input import *
import time
import zipfile
import pickle


menu = ['Student', 'Course', 'Mark list', 'GPA', 'Compression', 'Extract', 'Test pickle', 'End']


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
    text3 = "Have a good day"

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
        elif key == curses.KEY_ENTER or key in [10, 13] and current_row_idx == 4:
            with zipfile.ZipFile('students.dat', 'w', compression=zipfile.ZIP_DEFLATED) as file_name:
                file_name.write('students.txt')
                file_name.write('courses.txt')
                file_name.write('marks.txt')
                stdscr.addstr('Compressed')
            stdscr.refresh()
            stdscr.getch()
        elif key == curses.KEY_ENTER or key in [10, 13] and current_row_idx == 5:
            with zipfile.ZipFile('students.dat', 'r') as my_zip:
                my_zip.extractall('Students')
                stdscr.addstr('Extracted')
            stdscr.refresh()
            stdscr.getch()
        elif key == curses.KEY_ENTER or key in [10, 13] and current_row_idx == 6:
            pickle_file = open("students.dat", "ab")
            for student in student_list:
                pickle.dump(student, pickle_file)
            for course in course_list:
                pickle.dump(course, pickle_file)
            for mark in mark_list:
                pickle.dump(mark, pickle_file)
            stdscr.refresh()
            stdscr.getch()

        elif key == curses.KEY_ENTER or key in [10, 13] and current_row_idx == 7:
            x3 = w // 2 - len(text3) // 2
            y3 = h // 2
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(y3, x3, text3)
            stdscr.refresh()
            time.sleep(2.2)
            curses.curs_set(0)
            stdscr.clear()
            break
        print_menu(stdscr, current_row_idx)
        stdscr.refresh()
curses.wrapper(main)

