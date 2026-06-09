from datetime import datetime


# Simple Student Organizer
# Each student is a dict: {id, name, age, grade, dob, subjects}
students = []


def welcome():
    print("Welcome to the Student Data Organizer!")
    print("Add, list, update, or delete simple student records.\n")


def input_text(prompt):
    return input(prompt).strip()


def input_int(prompt, min_value=None):
    while True:
        s = input(prompt).strip()
        if not s:
            print("Please enter a value.")
            continue
        try:
            n = int(s)
        except ValueError:
            print("Enter a whole number.")
            continue
        if min_value is not None and n < min_value:
            print(f"Enter a number >= {min_value}.")
            continue
        return n


def input_date(prompt):
    while True:
        s = input(prompt).strip()
        try:
            datetime.strptime(s, "%Y-%m-%d")
            return s
        except ValueError:          
            print("Use YYYY-MM-DD format.")


def input_subjects(prompt):
    s = input(prompt).strip()
    return [p.strip() for p in s.split(",") if p.strip()]


def find_student(student_id):
    for s in students:
        if s["id"] == student_id:
            return s
    return None


def add_student():
    print("\nAdd a new student:")
    sid = input_int("Student ID: ", min_value=1)
    if find_student(sid):
        print("A student with that ID already exists.\n")
        return
    name = input_text("Name: ")
    age = input_int("Age: ", min_value=1)
    grade = input_text("Grade: ")
    dob = input_date("Date of birth (YYYY-MM-DD):")
    subjects = input_subjects("Subjects (comma-separated): ")
    students.append({"id": sid, "name": name, "age": age, "grade": grade, "dob": dob, "subjects": subjects})
    print("Student added.\n")


def list_students():
    if not students:
        print("\nNo students yet.\n")
        return
    print("\nStudents:")
    for s in students:
        subs = ", ".join(s["subjects"]) if s["subjects"] else "-"
        print(f"ID: {s['id']} | {s['name']} | Age: {s['age']} | Grade: {s['grade']} | Subjects: {subs} | DOB: {s['dob']}")
    print()


def update_student():
    if not students:
        print("\nNo students to update.\n")
        return
    sid = input_int("Enter student ID to update: ", min_value=1)
    s = find_student(sid)
    if not s:
        print("Student not found.\n")
        return
    print("Press Enter to keep current value.")
    name = input(f"Name [{s['name']}]: ").strip() or s["name"]
    age_in = input(f"Age [{s['age']}]: ").strip()
    age = s["age"]
    if age_in:
        try:
            age = int(age_in)
        except ValueError:
            print("Invalid age entered; keeping previous value.")
    grade = input(f"Grade [{s['grade']}]: ").strip() or s["grade"]
    subjects_in = input(f"Subjects (comma-separated) [{', '.join(s['subjects'])}]: ").strip()
    subjects = s["subjects"]
    if subjects_in:
        subjects = [p.strip() for p in subjects_in.split(",") if p.strip()]
    s.update({"name": name, "age": age, "grade": grade, "subjects": subjects})
    print("Student updated.\n")


def delete_student():
    if not students:
        print("\nNo students to delete.\n")
        return
    sid = input_int("Enter student ID to delete: ", min_value=1)
    for i, s in enumerate(students):
        if s["id"] == sid:
            del students[i]
            print("Student deleted.\n")
            return
    print("Student not found.\n")


def list_subjects():
    all_subs = set()
    for s in students:
        all_subs.update(s["subjects"])
    if not all_subs:
        print("\nNo subjects available.\n")
        return
    print("\nSubjects offered:")
    for sub in sorted(all_subs):
        print(f"- {sub}")
    print()


def menu():
    print("Select an option:")
    print("1. Add student")
    print("2. List students")
    print("3. Update student")
    print("4. Delete student")
    print("5. List subjects")
    print("6. Exit")


def main():
    welcome()
    while True:
        menu()
        choice = input("Choice: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            list_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            list_subjects()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")


main()
