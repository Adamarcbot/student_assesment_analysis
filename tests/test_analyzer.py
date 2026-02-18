from src.analyzer import analyze_students

def test_analysis_logic():
    students = [
        {
            "name": "Student1",
            "marks": {"Math": 30, "Physics": 45}
        },
        {
            "name": "Student2",
            "marks": {"Math": 70, "Physics": 80}
        }
    ]

    report, at_risk = analyze_students(students)

    assert report[0]["status"] == "Needs Attention"
    assert report[1]["status"] == "Good"
    assert "Student1" in at_risk
