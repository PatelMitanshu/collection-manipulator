"""Student Data Organizer.

This script demonstrates string formatting, list/dictionary/set/tuple usage,
type casting, and deleting records with ``del``.
"""

from datetime import datetime


PROGRAM_NAME = "Student Data Organizer"

student_records = []
student_index = {}


def print_welcome_message():
	print("Welcome to the {0}!".format(PROGRAM_NAME))
	print("This program stores student data in a list, tuple, set, and dictionary.")
	print("You can add, display, update, and delete student records from one menu.\n")


def read_non_empty_text(prompt):
	while True:
		value = input(prompt).strip()
		if value:
			return value
		print("Input cannot be empty. Please try again.")


def read_int(prompt, minimum=None):
	while True:
		value = input(prompt).strip()
		try:
			number = int(value)
		except ValueError:
			print("Please enter a valid whole number.")
			continue

		if minimum is not None and number < minimum:
			print("Please enter a number greater than or equal to {0}.".format(minimum))
			continue

		return number


def read_date(prompt):
	while True:
		value = input(prompt).strip()
		try:
			datetime.strptime(value, "%Y-%m-%d")
			return value
		except ValueError:
			print("Please use the YYYY-MM-DD format, for example 2002-05-14.")


def read_subjects(prompt):
	while True:
		raw_value = input(prompt).strip()
		subjects = [subject.strip() for subject in raw_value.split(",") if subject.strip()]
		if subjects:
			return subjects
		print("Enter at least one subject, separated by commas if needed.")


def collect_student_record():
	print("\nEnter student details:")
	student_id = read_int("Student ID: ", minimum=1)

	if student_id in student_index:
		print("A student with this ID already exists. Use update instead.\n")
		return None

	name = read_non_empty_text("Name: ")
	age = read_int("Age: ", minimum=1)
	grade = read_non_empty_text("Grade: ")
	date_of_birth = read_date("Date of Birth (YYYY-MM-DD): ")
	subjects = read_subjects("Subjects (comma-separated): ")

	record = {
		"student_id": student_id,
		"identity": (student_id, date_of_birth),
		"details": {
			"name": name,
			"age": age,
			"grade": grade,
			"subjects": subjects,
		},
		"subjects_set": set(subjects),
	}
	return record


def add_student():
	record = collect_student_record()
	if record is None:
		return

	student_records.append(record)
	student_index[record["student_id"]] = record
	print("Student added successfully!")
	print("Stored record for %s with %d subject(s).\n" % (record["details"]["name"], len(record["details"]["subjects"])))


def format_student_line(record):
	details = record["details"]
	subjects = ", ".join(details["subjects"])
	return (
		f"Student ID: {record['student_id']} | "
		f"Name: {details['name']} | Age: {details['age']} | "
		f"Grade: {details['grade']} | Subjects: {subjects} | "
		f"Date of Birth: {record['identity'][1]}"
	)


def display_all_students():
	if not student_records:
		print("\nNo student records available yet.\n")
		return

	print("\n--- Display All Students ---")
	for record in student_records:
		print(format_student_line(record))
	print()


def find_student_record(student_id):
	return student_index.get(student_id)


def update_student_information():
	if not student_records:
		print("\nNo student records available to update.\n")
		return

	student_id = read_int("Enter the student ID to update: ", minimum=1)
	record = find_student_record(student_id)

	if record is None:
		print("No student found with that ID.\n")
		return

	details = record["details"]
	print("\nPress Enter to keep the current value for any field.")

	new_name = input(f"Current name is {details['name']}. New name: ").strip()
	new_age = input(f"Current age is {details['age']}. New age: ").strip()
	new_grade = input(f"Current grade is {details['grade']}. New grade: ").strip()
	new_subjects = input("New subjects (comma-separated): ").strip()

	if new_name:
		details["name"] = new_name

	if new_age:
		try:
			details["age"] = int(new_age)
		except ValueError:
			print("Age was not updated because the value was not a valid number.")

	if new_grade:
		details["grade"] = new_grade

	if new_subjects:
		subject_list = [subject.strip() for subject in new_subjects.split(",") if subject.strip()]
		if subject_list:
			details["subjects"] = subject_list
			record["subjects_set"] = set(subject_list)

	print("Student information updated successfully.\n")


def delete_student():
	if not student_records:
		print("\nNo student records available to delete.\n")
		return

	student_id = read_int("Enter the student ID to delete: ", minimum=1)
	record = find_student_record(student_id)

	if record is None:
		print("No student found with that ID.\n")
		return

	for index, current_record in enumerate(student_records):
		if current_record["student_id"] == student_id:
			del student_records[index]
			break

	del student_index[student_id]
	print("Student record deleted successfully.\n")


def display_subjects_offered():
	if not student_records:
		print("\nNo subjects available yet because no students have been added.\n")
		return

	unique_subjects = sorted(
		{
			subject
			for record in student_records
			for subject in record["details"]["subjects"]
		}
	)

	print("\n--- Subjects Offered ---")
	for subject in unique_subjects:
		print(f"- {subject}")
	print()


def show_menu():
	print("Select an option:")
	print("1. Add Student")
	print("2. Display All Students")
	print("3. Update Student Information")
	print("4. Delete Student")
	print("5. Display Subjects Offered")
	print("6. Exit")


def main():
	print_welcome_message()

	while True:
		show_menu()
		choice = input("Enter your choice: ").strip()

		if choice == "1":
			add_student()
		elif choice == "2":
			display_all_students()
		elif choice == "3":
			update_student_information()
		elif choice == "4":
			delete_student()
		elif choice == "5":
			display_subjects_offered()
		elif choice == "6":
			print("\nThank you for using the Student Data Organizer. Goodbye!")
			break
		else:
			print("Invalid choice. Please select a number from the menu.\n")


if __name__ == "__main__":
	main()
