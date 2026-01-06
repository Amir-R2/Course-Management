import csv


def csv_create(*headers):
    with open('Course_List.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        return headers


def add_course(headers, course_name, start_date, end_date, session_count):
    with open('Course_List.csv', 'a', ) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writerows([{'Course Name': course_name, 'Start Date': start_date,
                         'End Date': end_date, 'Session Count': session_count}])


def add_student(course_name, first_name, last_name, age):
    pass


csv_file_header = csv_create(
    'Course Name', 'Start Date', 'End Date', 'Session Count')
