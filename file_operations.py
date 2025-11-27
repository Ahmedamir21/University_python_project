# ============================================
# File Operations Module
# Member 1: Ahmed Amir Ibrahim (202507440)
# ============================================
# This module handles all file read/write operations
# ============================================

import os

# ============================================
# File Paths
# ============================================
DATA_FOLDER = "data"
STUDENTS_FILE = DATA_FOLDER + "/students.txt"
COURSES_FILE = DATA_FOLDER + "/courses.txt"
REGISTRATIONS_FILE = DATA_FOLDER + "/registrations.txt"
CREDENTIALS_FILE = DATA_FOLDER + "/credentials.txt"
STATISTICS_FILE = DATA_FOLDER + "/statistics.txt"

# ============================================
# Initialize Files
# ============================================
def initialize_files():
    """
    Create data folder and files if they don't exist
    """
    # Create data folder
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)
    
    # Create empty files if they don't exist
    files = [STUDENTS_FILE, COURSES_FILE, REGISTRATIONS_FILE, CREDENTIALS_FILE]
    for file in files:
        if not os.path.exists(file):
            f = open(file, "w")
            f.close()
    
    # Add default admin credentials if file is empty
    if os.path.getsize(CREDENTIALS_FILE) == 0:
        f = open(CREDENTIALS_FILE, "w")
        f.write("admin,admin123,admin\n")
        f.close()
    
    # Add sample courses if file is empty
    if os.path.getsize(COURSES_FILE) == 0:
        add_sample_courses()

# ============================================
# Read Students
# ============================================
def read_students():
    """
    Read all students from file
    Returns: list of dictionaries
    """
    students = []
    f = open(STUDENTS_FILE, "r")
    lines = f.readlines()
    f.close()
    
    for line in lines:
        line = line.strip()
        if line != "":
            parts = line.split(",")
            student = {
                "id": parts[0],
                "name": parts[1],
                "program": parts[2],
                "year": parts[3]
            }
            students.append(student)
    
    return students

# ============================================
# Write Students
# ============================================
def write_students(students):
    """
    Write all students to file
    """
    f = open(STUDENTS_FILE, "w")
    for student in students:
        line = student["id"] + "," + student["name"] + "," + student["program"] + "," + student["year"] + "\n"
        f.write(line)
    f.close()

# ============================================
# Add Student
# ============================================
def add_student(student_id, name, program, year):
    """
    Add a new student to file
    """
    students = read_students()
    
    # Check if student already exists
    for s in students:
        if s["id"] == student_id:
            return False  # Student already exists
    
    # Add new student
    new_student = {
        "id": student_id,
        "name": name,
        "program": program,
        "year": year
    }
    students.append(new_student)
    write_students(students)
    
    # Add credentials for student
    add_credentials(student_id, "pass" + student_id, "student")
    
    return True

# ============================================
# Read Courses
# ============================================
def read_courses():
    """
    Read all courses from file
    """
    courses = []
    f = open(COURSES_FILE, "r")
    lines = f.readlines()
    f.close()
    
    for line in lines:
        line = line.strip()
        if line != "":
            parts = line.split(",")
            course = {
                "code": parts[0],
                "name": parts[1],
                "credits": int(parts[2]),
                "type": parts[3]
            }
            courses.append(course)
    
    return courses

# ============================================
# Write Courses
# ============================================
def write_courses(courses):
    """
    Write all courses to file
    """
    f = open(COURSES_FILE, "w")
    for course in courses:
        line = course["code"] + "," + course["name"] + "," + str(course["credits"]) + "," + course["type"] + "\n"
        f.write(line)
    f.close()

# ============================================
# Add Sample Courses
# ============================================
def add_sample_courses():
    """
    Add sample courses to the system
    """
    courses = [
        {"code": "CS101", "name": "Introduction to Programming", "credits": 3, "type": "Core"},
        {"code": "CS102", "name": "Data Structures", "credits": 3, "type": "Core"},
        {"code": "MATH101", "name": "Calculus I", "credits": 3, "type": "Core"},
        {"code": "MATH102", "name": "Linear Algebra", "credits": 3, "type": "Core"},
        {"code": "PHY101", "name": "Physics I", "credits": 4, "type": "Core"},
        {"code": "ENG101", "name": "English Communication", "credits": 2, "type": "Elective"}
    ]
    write_courses(courses)

# ============================================
# Read Registrations
# ============================================
def read_registrations():
    """
    Read all course registrations
    """
    registrations = []
    f = open(REGISTRATIONS_FILE, "r")
    lines = f.readlines()
    f.close()
    
    for line in lines:
        line = line.strip()
        if line != "":
            parts = line.split(",")
            reg = {
                "student_id": parts[0],
                "course_code": parts[1]
            }
            registrations.append(reg)
    
    return registrations

# ============================================
# Write Registrations
# ============================================
def write_registrations(registrations):
    """
    Write all registrations to file
    """
    f = open(REGISTRATIONS_FILE, "w")
    for reg in registrations:
        line = reg["student_id"] + "," + reg["course_code"] + "\n"
        f.write(line)
    f.close()

# ============================================
# Read Credentials
# ============================================
def read_credentials():
    """
    Read login credentials
    """
    credentials = []
    f = open(CREDENTIALS_FILE, "r")
    lines = f.readlines()
    f.close()
    
    for line in lines:
        line = line.strip()
        if line != "":
            parts = line.split(",")
            cred = {
                "username": parts[0],
                "password": parts[1],
                "role": parts[2]
            }
            credentials.append(cred)
    
    return credentials

# ============================================
# Add Credentials
# ============================================
def add_credentials(username, password, role):
    """
    Add new login credentials
    """
    f = open(CREDENTIALS_FILE, "a")
    f.write(username + "," + password + "," + role + "\n")
    f.close()

# ============================================
# Export Statistics to File
# ============================================
def export_statistics(stats_text):
    """
    Export statistics to a text file
    """
    f = open(STATISTICS_FILE, "w")
    f.write(stats_text)
    f.close()
    print("Statistics exported to", STATISTICS_FILE)
