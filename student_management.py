# Student Management System
# Simple Python project for BCA students

students = []


def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    student = {
        "roll_no": roll_no,
        "name": name,
        "course": course,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!\n")


def view_students():
    if not students:
        print("No student records found.\n")
        return

    print("\n--- Student Records ---")
    for student in students:
        print("Roll Number:", student["roll_no"])
        print("Name:", student["name"])
        print("Course:", student["course"])
        print("Marks:", student["marks"])
        print("-----------------------")
    print()


def search_student():
    roll_no = input("Enter Roll Number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print("Roll Number:", student["roll_no"])
            print("Name:", student["name"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])
            print()
            return

    print("Student not found.\n")


def delete_student():
    roll_no = input("Enter Roll Number to delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


def main():
    while True:
        print("===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Thank you for using Student Management System!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
