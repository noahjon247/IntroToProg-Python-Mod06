# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   Noah Jon,11/16/2024,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.
file = None

# Collection of functions that read and write JSON files
class FileProcessor:

    # Function that reads data from existing JSON file
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data
    
    # Function that writes data to existing JSON file
    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            IO.output_student_courses(student_data = student_data)
        except Exception as e:
            IO.output_error_messages("There was a problem with writing the data to the file", e)
        finally:
            if file.closed == False:
                file.close()
# Collection of functions that work with inputs and outputs
class IO:

    # Function that displays the corresponding error message
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message --")
            print(error, error.__doc__, type(error), sep="\n")
    
    # Function that displays the menu choices to the user
    @staticmethod
    def output_menu(menu: str):
        print()
        print(menu)
        print()
    
    # Function that registers the menu choice input from the user
    @staticmethod
    def input_menu_choice():
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice
    
    # Function that displays the current student and course information to the user
    @staticmethod
    def output_student_courses(student_data: list):
        print("-"*50)
        for student in student_data:
            print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in " \
                  f"{student["CourseName"]}")
        print("-"*50)    

    # Function that promps the user to enter the first, last, and course name and saves the selected inputs
    @staticmethod
    def input_student_data(student_data: list):
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("One of the input values was the wrong type of data", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error", e)
        return student_data

# Code that is running the functions to achieve the goal of the assignment

# Start of code always starts with reading existing data from JSON file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

while True:
    # Presents menu choices
    IO.output_menu(menu=MENU)

    # Menu Choice Option is requested and processed
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":
        students = IO.input_student_data(student_data=students)
        continue
    
    # Print current data
    elif menu_choice == "2":
        IO.output_student_courses
        continue
    
    # Write and save current data to JSON file
    elif menu_choice =="3":
        FileProcessor.write_data_to_file(FILE_NAME, student_data=students)
        continue

    # End program
    elif menu_choice == "4":
        break

    else:
        print("Choose options 1, 2, 3, or 4")