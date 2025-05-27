'''
You're building a system to manage student data for a university. Each student is identified by a unique student ID and has the following details:

- Name
- Major
- Enrolled Courses (each course has a course name and a dictionary of assessment scores like midterm, final, and project)



 Sample Data (Nested Dictionary):


university_data = {
"S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}
Q1: Print all student names and their majors
Q2: Average score per course per student 
Q3: Find students who scored >90 in final of Python101 
Q4: Add new course AI101 for student S101
Q5: Print average for each course
'''




university_data = {
"S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}

#print student name and major
for j,i in university_data.items():
    print(f"Name : {i['name']}  Major : {i['major']}")


#Average score per course per student 
for i,j in university_data.items():
    print(f"Name : {j['name']}")
    for c,s in j['courses'].items():
        avgscore= sum(s.values())//len(s)
        print(f"Course : {c} Average score : {avgscore:.2f}")
    print()


#Find students who scored >90 in final of Python101

for i,j in university_data.items():
    c=j["courses"]
    if 'Physics101' in c and c['Physics101']['final'] > 90:
        print(f"Name: {j['name']}")

#Q4: Add new course AI101 for student S101

university_data["S101"]["courses"]["AI101"] = {"midterm": 85, "final": 88, "project": 90}
print("Added AI101 for S101:")
print(university_data["S101"]["courses"]["AI101"])


#Print average for each course
for i,j in university_data.items():
    course=j['courses']
    for c,a in course.items():
        avg=sum(a.values())/len(a)
        print(f"Course : {c}  Averagescore : {avg:.2f}")

    print()
