import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.json")

DEFAULT_STUDENTS = {
    'Hashmi' : {'Math': 95, 'Physics': 73, 'Chemistry': 72},
    'Mohammed' : {'Math': 70, 'Physics': 65, 'Chemistry': 87},
    'Grace' : {'Math': 65, 'Physics': 75, 'Chemistry': 60},
    'Bob' : {'Math': 69, 'Physics': 59, 'Chemistry': 35},
    'Fatima' : {'Math': 40, 'Physics': 67, 'Chemistry': 63}
}


# ---------- Persistence ----------
def load_students():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return dict(DEFAULT_STUDENTS)
    return dict(DEFAULT_STUDENTS)


def save_students(students):
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=2)


# ---------- Core calculations ----------
def calculate_average(marks):
    if len(marks) == 0:
        return 0
    total = sum(marks.values())
    return total / len(marks)


def get_grade(avg):
    if avg > 79 and avg <= 100:
        return "A"
    elif avg > 59 and avg <= 79:
        return "B"
    elif avg > 39 and avg <= 59:
        return "C"
    elif avg >= 0 and avg <= 39:
        return "D"
    else:
        return "Invalid"


def class_average(students):
    if len(students) == 0:
        return 0
    total = 0
    for marks in students.values():
        total += calculate_average(marks)
    return total / len(students)


# ---------- Leaderboard with ties ----------
def leaderboard(students):
    if len(students) == 0:
        return []

    ranked = []
    for name, marks in students.items():
        avg = calculate_average(marks)
        ranked.append((name, avg))

    ranked.sort(key=lambda pair: pair[1], reverse=True)
    return ranked


def top_students(students):
    ranked = leaderboard(students)
    if not ranked:
        return [], 0

    highest = ranked[0][1]
    winners = [name for name, avg in ranked if avg == highest]
    return winners, highest


# ---------- Individual student report ----------
def student_report(students, name):
    name = name.lower().strip()
    if name not in students:
        print(f"No student named '{name}' found.")
        return

    marks = students[name]
    if len(marks) == 0:
        print(f"{name.capitalize()} has no marks recorded yet.")
        return

    avg = calculate_average(marks)
    grade = get_grade(avg)
    best_subject = max(marks, key=marks.get)
    worst_subject = min(marks, key=marks.get)

    print(f"\n----- Report for {name.capitalize()} -----")
    for subject, score in marks.items():
        print(f"{subject}: {score}")
    print(f"\nAverage: {avg:.2f}")
    print(f"Grade: {grade}")
    print(f"Strongest subject: {best_subject} ({marks[best_subject]})")
    print(f"Weakest subject: {worst_subject} ({marks[worst_subject]})")


# ---------- Display helpers ----------
def show_results(students):
    if len(students) == 0:
        print("No students recorded yet.")
        return
    for name, marks in students.items():
        avg = calculate_average(marks)
        grade = get_grade(avg)
        print("{0} - Average: {1:.2f} - Grade: {2}".format(name.capitalize(), avg, grade))


def show_leaderboard(students):
    ranked = leaderboard(students)
    if not ranked:
        print("No students recorded yet.")
        return

    print("\n----- Leaderboard -----")
    for position, (name, avg) in enumerate(ranked, start=1):
        print(f"{position}. {name.capitalize()} - {avg:.2f}")


def show_top_students(students):
    winners, highest = top_students(students)
    if not winners:
        print("No students recorded yet.")
        return

    names = ", ".join(name.capitalize() for name in winners)
    if len(winners) == 1:
        print(f"{names} - Average: {highest:.2f}")
    else:
        print(f"Tied for first: {names} - Average: {highest:.2f}")


# ---------- Input validation ----------
def prompt_mark(subject):
    while True:
        raw = input(f"Enter mark for {subject} (0-100): ").strip()
        try:
            value = float(raw)
        except ValueError:
            print("Please enter a number.")
            continue

        if value < 0 or value > 100:
            print("Mark must be between 0 and 100.")
            continue

        return value


# ---------- Add, edit, delete ----------
def add_student(students):
    name = input("Enter new student's name: ").lower().strip()
    if not name:
        print("Name cannot be empty.")
        return

    if name in students:
        print(f"{name.capitalize()} already exists. Use edit instead.")
        return

    marks = {}
    print("Enter marks one subject at a time. Leave the subject name blank to finish.")
    while True:
        subject = input("Subject name: ").strip()
        if not subject:
            break
        marks[subject] = prompt_mark(subject)

    students[name] = marks
    save_students(students)
    print(f"Added {name.capitalize()}.")


def edit_student(students):
    name = input("Enter the student's name to edit: ").lower().strip()
    if name not in students:
        print(f"No student named '{name}' found.")
        return

    subject = input("Which subject's mark do you want to change? ").strip()
    students[name][subject] = prompt_mark(subject)
    save_students(students)
    print(f"Updated {subject} for {name.capitalize()}.")


def delete_student(students):
    name = input("Enter the student's name to delete: ").lower().strip()
    if name not in students:
        print(f"No student named '{name}' found.")
        return

    del students[name]
    save_students(students)
    print(f"Removed {name.capitalize()}.")


# ---------- Main menu ----------
def main_menu():
    students = load_students()

    while True:
        print("\n******MAIN MENU******")
        print("1. Show all student results")
        print("2. Show leaderboard")
        print("3. Show top student(s)")
        print("4. Show class average")
        print("5. Individual student report")
        print("6. Add a student")
        print("7. Edit a student's mark")
        print("8. Delete a student")
        print("9. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            show_results(students)
        elif choice == "2":
            show_leaderboard(students)
        elif choice == "3":
            show_top_students(students)
        elif choice == "4":
            print("The class average: {0:.2f}".format(class_average(students)))
        elif choice == "5":
            name = input("Enter student name: ")
            student_report(students, name)
        elif choice == "6":
            add_student(students)
        elif choice == "7":
            edit_student(students)
        elif choice == "8":
            delete_student(students)
        elif choice == "9":
            print("Goodbye!!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main_menu()
