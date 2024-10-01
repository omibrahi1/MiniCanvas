"""
File Name: admin_module.py
    Purpose:  This file serves as the admin module for the program
    and defines functions of the admin.
First Create Date: 10/24/2023
Last Update Date: 11/28/2023
Author: Omar Ibrahim
Version: 1.1
"""
from user import Admin, Student, login
from utility import load_csv, load_admin_csv, save_to_csv, is_unique, get_formatted_output
from course import Course
from enrollment import Enrollment

admins = load_admin_csv('admins.csv', Admin)
students = load_csv('students.csv', Student)
courses = load_csv('courses.csv', Course)
enrollments = load_csv('enrollments.csv', Enrollment)

def admin_module():
    attempts = 0
    while attempts < 5:
        admin_username = input("Enter admin username: ")
        admin_password = input("Enter admin password: ")

        admin = login(admins, admin_username, admin_password)
        if admin:
            break
        else:
            attempts += 1
            print("Invalid credentials. Please try again.")

    if attempts == 5:
        print("Too many login attempts. Exiting...")
        return

    while True:
        print("\nAdmin Module Options:")
        print("1. Add a new student")
        print("2. Add a new course")
        print("3. Add a course enrollment")
        print("4. See all student information")
        print("5. See all course information")
        print("6. See all enrollment information")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_new_student()
        elif choice == '2':
            add_new_course()
        elif choice == '3':
            add_course_enrollment()
        elif choice == '4':
            view_students()
        elif choice == '5':
            view_courses()
        elif choice == '6':
            view_enrollments()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")


def add_new_student():
    new_student_username = input("Enter new student username: ")
    if not is_unique(students, new_student_username, 'username'):
        print("Username already exists. Try a different one.")
        return

    new_student_password = input("Enter new student password: ")
    new_student_first_name = input("Enter new student first name: ")
    new_student_last_name = input("Enter new student last name: ")

    new_student = Student(new_student_username, new_student_password, new_student_first_name, new_student_last_name)
    students.append(new_student)
    print([student.__dict__ for student in students])
    save_to_csv('students.csv', [student.__dict__ for student in students])

    print("Student added successfully.")


def add_new_course():
    new_course_number = input("Enter new course number: ")
    if not is_unique(courses, new_course_number, 'course_number'):
        print("Course number already exists. Try a different one.")
        return

    new_course_title = input("Enter new course title: ")

    new_course = Course(new_course_number, new_course_title)
    courses.append(new_course)
    save_to_csv('courses.csv', [new_course.__dict__])

    print("Course added successfully.")

def add_course_enrollment():
    student_username = input("Enter student username: ")
    course_number = input("Enter course number: ")

    if not is_unique(enrollments, (student_username, course_number), ('student_username', 'course_number')):
        print("Enrollment already exists.")
        return

    if not any(student.username == student_username for student in students):
        print("Student not found.")
        return

    if not any(course.course_number == course_number for course in courses):
        print("Course not found.")
        return

    new_enrollment = Enrollment(student_username, course_number)
    enrollments.append(new_enrollment)
    save_to_csv('enrollments.csv', [new_enrollment.__dict__])

    print("Enrollment added successfully.")

def view_students():
    print("All Students:")
    print(get_formatted_output(students))


def view_courses():
    print("All Courses:")
    print(get_formatted_output(courses))

def view_enrollments():
    print("All Enrollments:")
    print(get_formatted_output(enrollments))



if __name__ == "__main__":
    admin_module()
