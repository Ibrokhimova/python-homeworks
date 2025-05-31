import csv
from collections import defaultdict

grades_data = [
    ["Name", "Subject", "Grade"],
    ["Alice", "Math", 85],
    ["Bob", "Science", 78],
    ["Carol", "Math", 92],
    ["Dave", "History", 74]
]

with open("grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(grades_data)


grades = []
with open("grades.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["Grade"] = int(row["Grade"])  
        grades.append(row)

subject_totals = defaultdict(list)
for entry in grades:
    subject = entry["Subject"]
    grade = entry["Grade"]
    subject_totals[subject].append(grade)


average_grades = []
for subject, grades_list in subject_totals.items():
    average = sum(grades_list) / len(grades_list)
    average_grades.append({
        "Subject": subject,
        "Average Grade": round(average, 1)
    })

with open("average_grades.csv", "w", newline="") as file:
    fieldnames = ["Subject", "Average Grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(average_grades)

print(" average_grades.csv fayli muvaffaqiyatli yaratildi.")
