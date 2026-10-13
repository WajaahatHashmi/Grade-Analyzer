students = {
    'Hashmi' : {'Math': 95, 'Physics': 73, 'Chemistry': 72},
    'Mohammed' : {'Math': 70, 'Physics': 65, 'Chemistry': 87},
    'Grace' : {'Math': 65, 'Physics': 75, 'Chemistry': 60},
    'Bob' : {'Math': 69, 'Physics': 59, 'Chemistry': 35},
    'Fatima' : {'Math': 40, 'Physics': 67, 'Chemistry': 63}
}

def calculate_average(marks):
    total = sum(marks.values())
    return total/len(marks)

def get_grade(avg):
    if avg > 79 and avg <= 100:
        return 'A'
    elif avg > 59 and avg <= 79:
        return 'B'
    elif avg > 39 and avg <= 59:
        return 'C'
    elif avg <= 39 and avg >= 0:
        return 'D'
    else:
        return 'error' 

def top_student(students):
    best = ''
    highest = 0

    for name, marks in students.items():
        avg = calculate_average(marks)

        if avg >highest:
            highest = avg
            best = name
    
    return best, highest

def show_results(students):
    for name, marks in students.items():
        avg = calculate_average(marks)
        grade = get_grade(avg)
        print("{0} - Average: {1:.2f} - Grade: {2}".format(name,avg,grade))

def class_average(students):
    total = 0
    for marks in students.values():
        total += calculate_average(marks)
    return total / len(students)

while True:

    print("\n******MAIN MENU******")
    print("\n1. Show all student results")
    print("2. Show top student")
    print("3. Show class average")
    print("4. Exit")

    user_input = input("\nEnter your choice: ")

    if user_input == '1':
        show_results(students)
    elif user_input == '2':
        name, avg = top_student(students)
        print("{0} - Average: {1:.2f}".format(name,avg))
    elif user_input == '3':
        print("The class average: {0:.2f}".format(class_average(students)))
    elif user_input == '4':
        print("Goodbye!!")
        break

    else:
        print('invalid choice')





