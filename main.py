import os
import csv


def insert_header_to_csv(*headers, csv_file_name: None | str = None):
    if csv_file_name is None:
        csv_file_name = "course management.csv"
    with open(csv_file_name, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        return headers


def insert_data_to_csv(data, *headers, csv_file_name: None | str = None):
    if csv_file_name is None:
        csv_file_name = "course management.csv"
    with open(csv_file_name, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writerows([data])


def insert_seperator_to_csv(csv_file_name: None | str = None, seperation_count=5):
    if csv_file_name is None:
        csv_file_name = "course management.csv"
    with open(csv_file_name, 'a', newline='') as csvfile:
        for index in range(seperation_count):
            csvfile.write("\n,,,,,,\n")


def csv_assembeler(course_list, student_list):
    for i in range(len(course_list)):
        if i >= 1:
            insert_seperator_to_csv()
        insert_header_to_csv('ID', 'Course Name', 'Start Date',
                             'End Date', 'Session Count')
        insert_data_to_csv(course_list[i],
                           'ID', 'Course Name', 'Start Date',
                           'End Date', 'Session Count')
        insert_header_to_csv("course id", "name", "last name",
                             "age", "phone number")
        for j in range(len(student_list)):
            if student_list[j]["course id"] == course_list[i]["ID"]:
                insert_data_to_csv(student_list[j],
                                   "course id", "name", "last name",
                                   "age", "phone number")


def is_name(name):
    clean_name = name.replace(" ", "")
    if clean_name.isalpha():
        return True
    return False


def get_name(prompt: str | None = None):
    if prompt is None:
        prompt = "Name: "
    while True:
        name = input(prompt)
        if is_name(name):
            return name
        else:
            print(f"Error: {name} is not a name!")


def is_date(date):
    split_date = date.split("/")
    if len(split_date) == 3:
        if (len(split_date[0]) <= 4 and len(split_date[0]) > 1) and len(split_date[1]) == 2 and len(split_date[2]) == 2:
            return True
        return False


def get_date(prompt: str | None = None):
    if prompt is None:
        prompt = "Date (Format: 2026/01/01 or 26/01/01): "
    while True:
        date = input(prompt)
        if is_date(date):
            return date
        else:
            print(f"Error: {date} is not a valid date!")


def is_int(number):
    if number.isnumeric():
        return True
    return False


def get_int(prompt: str | None = None):
    if prompt is None:
        prompt = "Number: "
    while True:
        number = input(prompt)
        if is_int(number):
            return int(number)
        else:
            print(f"Error: {number} is not an Int!")


def is_phone_number(phone_number):
    if len(phone_number) == 11 and phone_number.isnumeric() and phone_number.startswith("09"):
        return True
    return False


def get_phone_number(prompt: str | None = None):
    if prompt is None:
        prompt = "Phone Number: "
    while True:
        phone_number = input(prompt)
        if is_phone_number(phone_number):
            return phone_number
        else:
            print(f"Error: {phone_number} is not a valid phone number!")


def add_course(id):
    course_name = get_name("Course Name: ")
    start_date = get_date("Start Date: ")
    end_date = get_date("End Date: ")
    session_count = get_int("Session Count: ")
    course_info = {'ID': id, 'Course Name': course_name, 'Start Date': start_date,
                   'End Date': end_date, 'Session Count': session_count}
    return (course_info)


def edit_course(id):
    pass


def remove_course(id):
    # this should -1 every id in the course list and student list
    pass


def add_student(course_id):
    student_name = get_name("First Name: ")
    student_name_last_name = get_name("Last Name: ")
    student_age = get_int("Age: ")
    student_phone_number = get_phone_number("Student Phone Number: ")
    student_info = {"course id": course_id, "name": student_name, "last name": student_name_last_name,
                    "age": student_age, "phone number": student_phone_number}
    return student_info


def edit_student_info(id):
    pass


def remove_student(id):
    pass


def add_student_score():
    pass


course_list = []
student_list = []
id = 0
if __name__ == "__main__":
    while True:
        id += 1
        course_list.append(add_course(id))
        forward = input("Countinue(y or n)? ")
        if forward == "n":
            break
    while True:
        count = get_int("Amount of students in this course: ")
        id = get_int("Course ID: ")
        for index in range(count):
            student_list.append(add_student(id))
        forward = input("Countinue (y or n)? ")
        if forward == "n":
            break
    csv_assembeler(course_list, student_list)
