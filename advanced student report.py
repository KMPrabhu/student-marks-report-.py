import json
import os
records = []
def load_data():
    global records
    if os.path.exists("students.json"):
        with open("students.json", "r") as f:
            records = json.load(f)

def save_data():
    with open("students.json", "w") as f:
        json.dump(records, f, indent=4)

def get_valid_number(prompt, min_value=0, max_value=100):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Enter value between {min_value} and {max_value}")
        except ValueError:
            print("Invalid input! Please enter numbers only.")

def calculate_grade(percentage, attendance):
    if attendance < 75:
        return "Fail", "Not eligible (Low Attendance)"

    if percentage >= 75:
        return "Excellent", "Promoted"
    elif percentage >= 60:
        return "Good", "Promoted"
    elif percentage >= 35:
        return "Pass", "Promoted"
    else:
        return "Fail", "Not eligible"

def add_student():
    print("\n------ Add Student ------")

    while True:
        name = input("Enter student name: ").strip()
        if name.replace(" ", "").isalpha():
            break
        print("Name must contain only letters.")

    s1 = get_valid_number("Enter marks for Subject 1: ")
    s2 = get_valid_number("Enter marks for Subject 2: ")
    s3 = get_valid_number("Enter marks for Subject 3: ")
    attendance = get_valid_number("Enter attendance %: ")

    total = s1 + s2 + s3
    percentage = round((total / 300) * 100, 2)

    grade, result = calculate_grade(percentage, attendance)

    student = {
        "name": name,
        "s1": s1,
        "s2": s2,
        "s3": s3,
        "attendance": attendance,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "result": result
    }

    records.append(student)
    save_data()
    print("Student added successfully!\n")

def view_report():
    if not records:
        print("No student records found.")
        return

    print("\n---------------- STUDENT REPORT ----------------")
    print(f"{'Name':<15}{'Total':<10}{'Percent':<10}{'Grade':<12}{'Result':<15}")
    print("-" * 60)

    for student in records:
        print(f"{student['name']:<15}{student['total']:<10}{student['percentage']:<10}{student['grade']:<12}{student['result']:<15}")

    print("-" * 60)

def search_student():
    name = input("Enter student name to search: ").strip().lower()
    for student in records:
        if student["name"].lower() == name:
            print("\nStudent Found:")
            for key, value in student.items():
                print(f"{key.capitalize()} : {value}")
            return
    print("Student not found.")

def delete_student():
    name = input("Enter student name to delete: ").strip().lower()
    for student in records:
        if student["name"].lower() == name:
            records.remove(student)
            save_data()
            print("Student deleted successfully.")
            return
    print("Student not found.")

def edit_student():
    name = input("Enter student name to edit: ").strip().lower()
    for student in records:
        if student["name"].lower() == name:
            print("Enter new marks:")
            student["s1"] = get_valid_number("Subject 1: ")
            student["s2"] = get_valid_number("Subject 2: ")
            student["s3"] = get_valid_number("Subject 3: ")
            student["attendance"] = get_valid_number("Attendance %: ")

            student["total"] = student["s1"] + student["s2"] + student["s3"]
            student["percentage"] = round((student["total"] / 300) * 100, 2)
            student["grade"], student["result"] = calculate_grade(student["percentage"], student["attendance"])

            save_data()
            print("Student updated successfully.")
            return
    print("Student not found.")

def show_topper():
    if not records:
        print("No records available.")
        return

    topper = max(records, key=lambda x: x["percentage"])
    print("\n🏆 TOPPER DETAILS")
    for key, value in topper.items():
        print(f"{key.capitalize()} : {value}")

def show_ranks():
    if not records:
        print("No records available.")
        return

    sorted_students = sorted(records, key=lambda x: x["percentage"], reverse=True)

    print("\n------ RANK LIST ------")
    rank = 1
    for student in sorted_students:
        print(f"Rank {rank}: {student['name']} - {student['percentage']}%")
        rank += 1
def main_menu():
    load_data()

    while True:
        print("""======== STUDENT MANAGEMENT SYSTEM ========
1. Add Student
2. View Report
3. Search Student
4. Edit Student
5. Delete Student
6. Show Topper
7. Show Rank List
8. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_report()
        elif choice == "3":
            search_student()
        elif choice == "4":
            edit_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            show_topper()
        elif choice == "7":
            show_ranks()
        elif choice == "8":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Try again.")

main_menu()  
