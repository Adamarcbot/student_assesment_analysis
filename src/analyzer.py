from config import PASS_MARK, RISK_AVERAGE

def analyze_students(students):
    final_report = []
    students_needing_attention = []

    for student in students:
        name = student["name"]
        marks = student["marks"]

        total_marks = 0
        subject_count = 0
        weak_subjects = []

        for subject, mark in marks.items():
            total_marks += mark
            subject_count += 1

            if mark < PASS_MARK:
                weak_subjects.append(subject)

        average = total_marks / subject_count

        if average < RISK_AVERAGE or len(weak_subjects) > 0:
            status = "Needs Attention"
            students_needing_attention.append(name)
        else:
            status = "Good"

        result = {
            "name": name,
            "average": round(average, 2),
            "status": status,
            "weak_subjects": weak_subjects
        }

        final_report.append(result)

    return final_report, students_needing_attention
