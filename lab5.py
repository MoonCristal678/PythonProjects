# Create a dictionary to store student information
students = {
    1: {
        "id": 1,
        "name": "John",
        "age": 18,
        "school_name": "Humber College",
        "completed_courses": {
            "Math": 90,
            "Science": 85,
            "Computer Science": 78,
        },
        "ongoing_courses": {
            "English": 50,
            "Hair Styling": 90,
        },
    },
    2: {
        "id": 2,
        "name": "Alice",
        "age": 17,
        "school_name": "George Brown College",
        "completed_courses": {
            "Math": 92,
            "Science": 88,
            "History": 75,
        },
        "ongoing_courses": {
            "English": 90,
            "Spanish": 100,
        },
    },
    3: {
        "id": 3,
        "name": "Bob",
        "age": 19,
        "school_name": "Monsignor Percy Johnson",
        "completed_courses": {
            "Math": 85,
            "Science": 92,
            "Philosophy": 80,
        },
        "ongoing_courses": {
            "English": 85,
            "French": 45,
        },
    },
    4: {
        "id": 4,
        "name": "Sarah",
        "age": 17,
        "school_name": "Humber College",
        "completed_courses": {
            "Hair Styling": 88,
            "Science": 85,
            "History": 76,
        },
        "ongoing_courses": {
            "English": 88,
            "Computer Science": 66,
        },
    },
    5: {
        "id": 5,
        "name": "David",
        "age": 18,
        "school_name": "York University",
        "completed_courses": {
            "Math": 90,
            "Biology": 82,
            "History": 70,
        },
        "ongoing_courses": {
            "English": 92,
            "Chemistry": 77,
        },
    },
    6: {
        "id": 6,
        "name": "Eva",
        "age": 17,
        "school_name": "York University",
        "completed_courses": {
            "Math": 91,
            "Science": 87,
            "Social Studies": 79,
        },
        "ongoing_courses": {
            "English": 100,
            "Art": 80,
        },
    },
    7: {
        "id": 7,
        "name": "Michael",
        "age": 18,
        "school_name": "Seneca College",
        "completed_courses": {
            "Math": 86,
            "English": 88,
            "History": 77,
        },
        "ongoing_courses": {
            "Science": 63,
            "Art": 90,
        },
    },
    8: {
        "id": 8,
        "name": "Sophia",
        "age": 17,
        "school_name": "George Brown College",
        "completed_courses": {
            "Math": 92,
            "Art": 89,
            "English": 74,
        },
        "ongoing_courses": {
            "History": 84,
            "Science": 65,
        },
    },
    9: {
        "id": 9,
        "name": "William",
        "age": 18,
        "school_name": "Waterloo University",
        "completed_courses": {
            "English": 87,
            "Science": 86,
            "History": 75,
        },
        "ongoing_courses": {
            "Math": 66,
            "Art": 99,
        },
    },
    10: {
        "id": 10,
        "name": "Olivia",
        "age": 17,
        "school_name": "Ryerson University",
        "completed_courses": {
            "Math": 89,
            "Science": 90,
            "English": 78,
        },
        "ongoing_courses": {
            "History": 67,
            "Music": 76,
        },
    },
}

# Function to view all students' information (including age, school name, completed courses, and ongoing courses)
def view_all_students():
    for student_id, student_info in students.items():
        print(f"ID: {student_info['id']} \nName: {student_info['name']}")
        print(f"Age: {student_info['age']} \nSchool Name: {student_info['school_name']}")
        print("Completed Courses:")
        for course, grade in student_info['completed_courses'].items():
            print(f"Course: {course}, Grade: {grade}%")
        print("Ongoing Courses:")
        for course, status in student_info['ongoing_courses'].items():
            print(f"Course: {course}, Grade: {status}%")
        print("\n")

# Function to view information on a specific student (including age, school name, completed courses, and ongoing courses)
def view_specific_student():
    student_id = int(input("Enter the student's ID: "))
    student = students.get(student_id)
    if student:
        print(f"ID: {student['id']}\nName: {student['name']}")
        print(f"Age: {student['age']}\nSchool Name: {student['school_name']}")
        print("Completed Courses:")
        for course, grade in student['completed_courses'].items():
            print(f"Course: {course}, Grade: {grade}%")
        print("Ongoing Courses:")
        for course, status in student['ongoing_courses'].items():
            print(f"Course: {course}, Grade: {status}%")
    else:
        print("Student not found.")

# Function to view ongoing grades of a specific student
def view_ongoing_grades():
    student_id = int(input("Enter the student's ID: "))
    student = students.get(student_id)
    if student:
        ongoing_courses = student['ongoing_courses']
        if ongoing_courses:
            print(f"Ongoing Courses for {student['name']}:")
            for course, status in ongoing_courses.items():
                print(f"Course: {course}, Grade: {status}%")
        else:
            print(f"No ongoing courses for {student['name']}.")
    else:
        print("Student not found.")

# Function to view completed grades of a specific student
def view_completed_grades():
    student_id = int(input("Enter the student's ID: "))
    student = students.get(student_id)
    if student:
        completed_courses = student['completed_courses']
        if completed_courses:
            print(f"Completed Courses for {student['name']}:")
            for course, grade in completed_courses.items():
                print(f"Course: {course}, Grade: {grade}%")
        else:
            print(f"No completed courses for {student['name']}.")

    else:
        print("Student not found.")

# Function to view the average completed grades of a specific student
def view_average_completed_grades():
    student_id = int(input("Enter the student's ID: "))
    student = students.get(student_id)
    if student:
        completed_courses = student['completed_courses']
        if completed_courses:
            total_grades = sum(completed_courses.values())
            average_grade = total_grades / len(completed_courses)
            print(f"Average of Completed courses for {student['name']}: {average_grade:.2f}%")
        else:
            print(f"No completed courses for {student['name']}.")

    else:
        print("Student not found.")

# Function to view a specific grade of a specific student
def view_specific_grade():
    student_id = int(input("Enter the student's ID: "))
    student = students.get(student_id)
    if student:
        course_name = input("Enter the course name: ")
        completed_courses = student['completed_courses']
        ongoing_courses = student['ongoing_courses']
        if course_name in completed_courses:
            grade = completed_courses.get(course_name)
            if grade is not None:
                print(f"Grade for {student['name']} in {course_name}: {grade}%")
            else:
                print(f"{student['name']} has not completed {course_name}.")
        elif course_name in ongoing_courses:
            grade = ongoing_courses.get(course_name)
            if grade is not None:
                print(f"Grade for {student['name']} in ongoing {course_name}: {grade}%")
            else:
                print(f"{student['name']} has {grade}% so far in ongoing {course_name}.")
        else:
            print(f"{student['name']} is/was not enrolled in {course_name}.")
    else:
        print("Student not found.")

# Main program loop
while True:
    print("\nOptions:")
    print("1. View all students' information")
    print("2. View information on a specific student")
    print("3. View ongoing grades of a specific student")
    print("4. View completed grades of a specific student")
    print("5. View average completed grades of a specific student")
    print("6. View a specific grade of a specific student")
    print("7. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        view_all_students()
    elif choice == "2":
        view_specific_student()
    elif choice == "3":
        view_ongoing_grades()
    elif choice == "4":
        view_completed_grades()
    elif choice == "5":
        view_average_completed_grades()
    elif choice == "6":
        view_specific_grade()
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please try again.")