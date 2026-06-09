# Student Data Organizer

## Overview

Student Data Organizer is a small Python console program for managing a collection of student records. The program stores all student records in a single list; each student is represented by a dictionary with the fields: `id`, `name`, `age`, `grade`, `dob`, and `subjects`.

The script is intentionally lightweight and runs in-memory only (no file or database persistence).

## Data Model

- Students: a list of dictionaries, e.g. {"id": 1, "name": "Alice", "age": 14, "grade": "9", "dob": "2007-05-21", "subjects": ["Math", "Science"]}
- Subjects: stored per-student as lists; the program uses a temporary `set` when listing unique subjects.

## Features

- Add a new student record (ID, name, age, grade, date of birth, subjects)
- List all students with formatted output
- Update mutable fields: name, age, grade, and subjects
- Delete a student record by student ID
- List all unique subjects offered (collected from student records)
- Input validation for integers and dates

## Input & Formatting

- Date of birth must be entered in `YYYY-MM-DD` format.
- Subjects are entered as a comma-separated list and stored as a list of strings.
- The program uses `f-strings` for formatted output.

## How To Run

From the project folder, run:

```bash
python pr3.py
```

## Example Flow

1. Run the script and choose `1` to add a student.
2. Enter the student's ID, name, age, grade, date of birth, and subjects (comma-separated).
3. Choose `2` to list students and review saved records.
4. Choose `3` to update a student's name, age, grade, or subjects.
5. Choose `4` to delete a student by ID.
6. Choose `5` to list all unique subjects.

## File Notes

- [pr3.py](pr3.py) contains the full interactive program. The implementation keeps data in memory and uses simple console input/output.

If you'd like, I can add persistent storage (JSON file), unit tests, or example data to demo the program.