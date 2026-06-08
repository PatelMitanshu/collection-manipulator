# Student Data Organizer

## Overview

Student Data Organizer is a small Python console program for managing a collection of student records. It was written to match the assignment requirements for string formatting, collection data types, mutability and immutability, type casting, and the `del` keyword.

The program keeps the student data in a few different collection types so each one has a clear purpose:

- a **list** stores all student records in the order they were added
- a **dictionary** provides quick lookup by student ID
- a **tuple** stores each student's ID and date of birth as fixed identity data
- a **set** removes duplicate subjects and helps show the unique subjects offered

## Features

- add a new student record
- display every stored student in formatted output
- update mutable fields such as name, age, grade, and subjects
- delete a student record by student ID using `del`
- display the full list of unique subjects
- validate numeric input and date input before saving data

## String Formatting Used

The script demonstrates all three formatting styles requested in the assignment:

- `f-strings` for the main record display
- `.format()` for the welcome message
- `%` formatting for the add-student confirmation message

## Assumptions

- Student IDs are unique positive integers.
- Date of birth must be entered in `YYYY-MM-DD` format.
- Subjects are entered as a comma-separated list.
- Updating the date of birth is intentionally not offered because it is stored inside an immutable tuple.

## How To Run

From the project folder, run:

```bash
python pr3.py
```

## Example Flow

1. Choose `Add Student`.
2. Enter the student's ID, name, age, grade, date of birth, and subjects.
3. Use `Display All Students` to review the saved records.
4. Use `Update Student Information` to change mutable fields.
5. Use `Delete Student` to remove a record by ID.

## File Notes

- [`pr3.py`](pr3.py) contains the full interactive program.
- [`README.md`](README.md) explains the structure and assumptions in plain language.