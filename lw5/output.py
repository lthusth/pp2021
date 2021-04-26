from input import *
import math
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
