"""
File Name: Lab11Utility.py
    Purpose: This file is the student module which stores the defined
    functions of a student.
First Create Date: 10/24/2023
Last Update Date: 11/28/2023
Author: Omar Ibrahim
Version: 1.1
"""
from user import Student, login
from utility import load_csv, get_formatted_output
from enrollment import Enrollment

students = load_csv('students.csv', Student)
enrollments = load_csv('enrollments.csv', Enrollment)

def student_module():
    attempts = 0
    while attempts < 5:
        student_username = input("Enter student username: ")
        student_password = input("Enter student password: ")

        student = login(students, student_username, student_password)
        if student:
            break
        else:
            attempts += 1
            print("Invalid credentials. Please try again.")

    if attempts == 5:
        print("Too many login attempts. Exiting...")
        return

    while True:
        print("\nStudent Module Options:")
        print("1. View enrolled courses")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_enrolled_courses(student.username)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")


def view_enrolled_courses(student_username):
    enrolled_courses = [enrollment for enrollment in enrollments if enrollment.student_username == student_username]
    if not enrolled_courses:
        print("You are not enrolled in any courses.")
    else:
        print("Enrolled Courses:")
        print(get_formatted_output(enrolled_courses))



if __name__ == "__main__":
    student_module()
