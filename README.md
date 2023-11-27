# PythonProjects
### ReadMe for Student Information System

This Python script creates and manages a simple student information system using a dictionary to store information about students, including their ID, name, age, school name, completed courses, and ongoing courses.

### Student Data Structure
The student information is organized as follows:
```python
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
    # ... (similar structure for other students)
}
```

### Functions
1. **View All Students' Information**
   - Prints information about all students, including ID, name, age, school name, completed courses, and ongoing courses.

2. **View Information on a Specific Student**
   - Prompts the user to enter a student's ID and displays detailed information about that specific student, including completed and ongoing courses.

3. **View Ongoing Grades of a Specific Student**
   - Prompts the user to enter a student's ID and displays the ongoing courses and their grades for that specific student.

4. **View Completed Grades of a Specific Student**
   - Prompts the user to enter a student's ID and displays the completed courses and their grades for that specific student.

5. **View Average Completed Grades of a Specific Student**
   - Prompts the user to enter a student's ID and calculates and displays the average grade for completed courses for that specific student.

6. **View a Specific Grade of a Specific Student**
   - Prompts the user to enter a student's ID and a course name, then displays the grade for that specific course for the student, whether it is completed or ongoing.

### Main Program Loop
The program runs in a continuous loop, providing the user with a menu of options:
- **1:** View all students' information
- **2:** View information on a specific student
- **3:** View ongoing grades of a specific student
- **4:** View completed grades of a specific student
- **5:** View average completed grades of a specific student
- **6:** View a specific grade of a specific student
- **7:** Exit

The user can input their choice, and the corresponding function is executed. If the user chooses option 7, the program exits the loop.

### Note
- The student information is hardcoded for demonstration purposes.
- The script can be extended to include functionalities like adding new students, updating information, or storing data in external files for persistence.
