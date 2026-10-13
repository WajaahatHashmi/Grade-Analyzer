# Grade Analyzer
 
A command-line Python application for tracking student grades, calculating averages, and generating class performance reports. Built as a learning project to practice data structures, file persistence, and input validation in Python.
 
## Features
 
- **Student records** stored as name-to-subject-marks mappings, with sample data seeded by default
- **Automatic grade calculation** based on average marks (A, B, C, or D)
- **Full leaderboard** ranking all students by average, correctly handling tied scores
- **Top student lookup** that also accounts for ties
- **Individual student reports** showing average, grade, strongest subject, and weakest subject
- **Class average** calculation across all students
- **Add, edit, and delete** student records directly from the menu
- **Input validation** on all marks (must be a number between 0 and 100) and menu choices
- **Persistent storage** via a `students.json` file, so your data is saved between runs
- **Guard clauses** to safely handle an empty student list without crashing
## Getting Started
 
### Requirements
- Python 3.x (no external libraries needed — uses only the built-in `json` and `os` modules)
### Running the program
1. Clone or download this repository
2. Open a terminal in the `grade-analyzer` folder
3. Run:
```
   python grade_analyzer.py
```
4. On first run, the program loads a set of sample students. From then on, it saves and reloads your data automatically from `students.json`.
> **Note:** Run this as a local `.py` file (e.g. in VS Code or Terminal), not in an online compiler like Programiz — online compilers don't allow file saving, so your data won't persist between runs.
 
## Usage Example
 
```
======MAIN MENU======
1. Show all student results
2. Show top student(s)
3. Show class average
4. View individual student report
5. Add a student
6. Edit a student
7. Delete a student
8. Exit
 
Enter your choice: 1
 
wuji - Average: 80.00 - Grade: A
ali - Average: 74.00 - Grade: B
abdul - Average: 66.67 - Grade: B
tyler - Average: 54.33 - Grade: C
edu - Average: 56.67 - Grade: C
```
 
## Grading Scale
 
| Average Range | Grade |
|---|---|
| 80 – 100 | A |
| 60 – 79 | B |
| 40 – 59 | C |
| 0 – 39 | D |
 
## What's New in v2
 
The original version (v1) was a basic script with hardcoded student data and no persistence. Version 2 adds:
 
- Fixed a `ZeroDivisionError` risk when calculating averages with no marks
- Fixed `top_student` to return *all* tied top scorers instead of just the first one found
- Added full leaderboard view (not just top student)
- Added individual student reports (strongest/weakest subject breakdown)
- Added input validation for marks and menu choices
- Added JSON-based save/load so data persists between runs
- Added ability to add, edit, and delete students
- Added `if __name__ == "__main__"` guard so the program only runs when executed directly
## Project Structure
 
```
grade-analyzer/
├── grade_analyzer.py
├── students.json          (created automatically, ignored by git)
├── .gitignore
└── README.md
```
 
## Roadmap
 
- [ ] Add a graphical interface (Tkinter or Streamlit)
- [ ] Export results to CSV
- [ ] Add charts for grade distribution
## Author
 
Wajaahat Hashmi — Computer Science student (AI & Big Data) at the University of Wollongong Dubai
