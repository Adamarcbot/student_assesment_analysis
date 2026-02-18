import json
from analyzer import analyze_students

file = open("../data/sample_students.json", "r")
students = json.load(file)
file.close()

report, at_risk_students = analyze_students(students)

print("Student Performance Report:\n")

for student in report:
    print(student)

print("\nStudents who need attention:")
print(at_risk_students)
