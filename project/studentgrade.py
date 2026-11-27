
# Project 3: Student Grade Calculator

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")

subjects = ["Python", "DBMS", "DSA", "OS", "CN"]

marks = {}

for subject in subjects:
    while True:
        try:
            mark = float(input(f"Enter marks for {subject}: "))

            if 0 <= mark <= 100:
                marks[subject] = mark
                break
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

total = sum(marks.values())
maximum = len(subjects) * 100
percentage = (total / maximum) * 100

grade = calculate_grade(percentage)

if all(mark >= 35 for mark in marks.values()):
    result = "PASS"
else:
    result = "FAIL"
    grade = "F"

print("\n===== STUDENT RESULT =====")
print("Student Name:", name)

for subject, mark in marks.items():
    print(f"{subject}: {mark:g}")

print("Total Marks:", total, "/", maximum)
print(f"Percentage: {percentage:.2f}%")
print("Grade:", grade)
print("Result:", result)
