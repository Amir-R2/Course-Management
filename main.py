import os
import csv
import uuid
# bug: if the user adds a student to the 1st course , then adds students to the 2nd course and wants to add more students to the 1st course, the order will be ruined in the final csv file


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
    if len(split_date[0]) < 2 or len(split_date[0]) > 4:
        return False
    try:
        split_date[0] = int(split_date[0])
        split_date[1] = int(split_date[1])
        split_date[2] = int(split_date[2])
    except:
        return False
    if len(split_date) == 3:
        if (split_date[0] in range(1900, 3000) or split_date[0] in range(0, 99)) and split_date[1] in range(1, 13) and split_date[2] in range(1, 32):
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
    course_name = get_name("\nCourse Name: ")
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
    student_id = uuid.uuid4()
    student_name = get_name("\nFirst Name: ")
    student_last_name = get_name("Last Name: ")
    student_age = get_int("Age: ")
    student_phone_number = get_phone_number("Student Phone Number: ")
    student_info = {"course id": course_id, "student id": student_id, "name": student_name, "last name": student_last_name,
                    "age": student_age, "phone number": student_phone_number}
    return student_info


def find_student(student_list, student_id):
    for item in range(len(student_list)):
        if student_list[item]["student id"] == student_id:
            return item


def edit_student_info(student_list, student_id):
    choice = get_int(
        " 1.Edit Name \n 2.Edit Last Name \n 3.Edit Age \n 4.Edit Phone Number \n 5.Exit\n")
    choice = int(choice)
    student_location = find_student(student_list, student_id)
    if student_location is None:
        return ("Student is not on the list")
    if choice == 1:
        student_list[student_location]["name"] = get_name(
            "Edit First Name: ")
    elif choice == 2:
        student_list[student_location]["last name"] = get_name(
            "Edit Last Name: ")
    elif choice == 3:
        student_list[student_location]["age"] = get_int("Edit Age: ")
    elif choice == 4:
        student_list[student_location]["phone number"] = get_phone_number(
            "Edit Phone number: ")


def remove_student(student_list, student_id):
    pass


def add_student_score(student_list, student_id):
    pass


def student_rollcall(student_list, student_id):
    pass


def save_to_csv(data,  csv_file_name, *headers):
    with open(csv_file_name, 'a', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        if csv_file.tell() == 0:
            writer.writeheader()
        writer.writerows(data)


course_list = []
student_list = []
id = 0
if __name__ == "__main__":
    while True:
        choice = get_int(
            "\nMenu:\n 1.Add Courses\n 2.Remove Course(Coming Soon!)\n 3.Edit Course Info(Coming Soon!)\n 4.Add Students\n 5.Edit Student Info\n 6.Remove Student(Coming Soon!)\n 7.Add Student Score(Coming Soon!)\n 8.Student Attendance(Coming Soon!)\n 9.Exit\n\n")
        choice = int(choice)
        if choice == 1:
            while True:
                id += 1
                course_list.append(add_course(id))
                forward = input("Countinue (y or n)? ")

                if forward == "n":
                    break

        elif choice == 4:
            if not course_list:
                print("No Courses Available!")
                continue
            for index in range(len(course_list)):
                print(course_list[index])
            while True:
                count = get_int("\nAmount of students in this course: ")
                id = get_int("Course ID: ")
                for index in range(count):
                    student_list.append(add_student(id))
                forward = input("Countinue (y or n)? ")
                if forward == "n":
                    break

        elif choice == 5:
            if not student_list:
                print("No Students Added!")
                continue
            for index in range(len(student_list)):
                print(student_list[index])
            while True:
                student_id = input("Student ID: ")
                try:
                    student_id = uuid.UUID(student_id)
                    break
                except:
                    print("Invalid Student ID")
            edit_student_info(student_list, student_id)
        elif choice == 9:
            break

if course_list:
    save_to_csv(course_list, "Course.csv", "ID", "Course Name",
                "Start Date", "End Date", "Session Count")
if student_list:
    save_to_csv(student_list, "Student.csv", "course id", "student id", "name", "last name",
                "age", "phone number")
