'''

Build a student grade management system using the following Python concepts:
- List of dictionaries
- Function with required arguments, *args, **kwargs
- Function decorator
- Loops and control statements

Requirements
1. Use a **decorator** to log function activity.
2. Use a function to **add student data** using `*args` and `**kwargs`.
3. Store student records in a **list of dictionaries**.
4. Use **loops and conditionals** to calculate and display results.

'''

from datetime import datetime


def log_activity(func):
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now()}] Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[{datetime.now()}] Completed function: {func.__name__}")
        return result
    return wrapper


student_records = []


@log_activity
def register_student(*args, **kwargs):
    record = {}
    if args:
        record["student_id"] = args[0]
    record.update(kwargs)
    student_records.append(record)
    print(f"Student '{record.get('name', 'Unknown')}' registered.\n")


@log_activity
def show_student_performance():
    for record in student_records:
        print(f"Student ID: {record['student_id']}, Name: {record['name']}")
        marks = record.get("marks", {})
        if not marks:
            print("  No marks available.")
            continue

        total_score = sum(marks.values())
        avg_score = total_score / len(marks)

        # Grade assignment
        if avg_score >= 90:
            grade_letter = 'A'
        elif avg_score >= 75:
            grade_letter = 'B'
        elif avg_score >= 60:
            grade_letter = 'C'
        else:
            grade_letter = 'D'

        print("  Marks:")
        for course, score in marks.items():
            print(f"    {course}: {score}")
        print(f"  Average Score: {avg_score:.2f}")
        print(f"  Grade: {grade_letter}\n")


register_student(101, name="Alice", marks={"Math": 99, "Science": 92, "English": 85})
register_student(102, name="Bob", marks={"Math": 45, "Science": 65, "English": 70})
register_student(103, name="Charlie", marks={"Math": 75, "Science": 98, "English": 93})


show_student_performance()
