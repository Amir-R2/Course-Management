import csv
student_list = []
course_list = []
id = 0
while True:
    id += 1
    course_name = input("Course Name: ")
    if course_name == '':
        break
    start_date = input("Start Date: ")
    end_date = input("End Date: ")
    session_count = input("Session Count: ")
    course_info = {'ID': id, 'Course Name': course_name, 'Start Date': start_date,
                   'End Date': end_date, 'Session Count': session_count}
    course_list.append(course_info)
print(course_list)
while True:
    course_id = int(input("\nCourse id: "))
    name = input("Student Name: ")
    if name == '':
        break
    last_name = input("Student Last Name: ")
    age = input("Student Age: ")
    phone_number = input("Student Phone Number: ")
    student_info = {"course id": course_id, "name": name, "last name": last_name,
                    "age": age, "phone number": phone_number}
    student_list.append(student_info)

for i in range(len(course_list)):
    print(course_list[i])
    for j in range(len(student_list)):
        if student_list[j]["course id"] == course_list[i]["ID"]:
            print(student_list[j])
