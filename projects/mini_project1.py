def read_students():
    with open("marks.txt", "r") as file:
        return file.readlines()

def display_students():
    lines = read_students()
    for line in lines:
        parts = line.strip().split()
        if not parts:
            continue
        name = parts[0]
        marks = int(parts[1])   
        print(f"{name} -> {marks}")

def search_student():
    lines = read_students()  
    asked_name = input("Enter student name:").lower()
    for line in lines:
        parts = line.strip().split()
        continue
        name = parts[0]
        marks = int(parts[1])  
        if asked_name.lower() == name.lower():
            return f"{name} {marks}"
    return "Student not found."

def add_student():
    lines = read_students() 
    updated_lines = []
    new_name = input("Enter new student name:").lower()
    new_marks = int(input("Enter marks:"))
    found = False
    for line in lines:
        parts = line.strip().split()
        if not parts:
            continue
        name = parts[0]
        marks = int(parts[1])   
        if name.lower() == new_name.lower():
            found = True
        updated_lines.append(f"{name} {marks}\n")
    if not found:
        updated_lines.append(f"{new_name} {new_marks}\n")
        print("Student added successfully.")
    else:
        print("Student already exists.")

    with open("marks.txt", "w") as file:
        file.writelines(updated_lines)

def update_student():
    lines = read_students() 
    updated_lines = []
    update_name = input("Enter a name:").lower()
    update_marks = int(input("Enter marks:"))
    found = False
    for line in lines:
        parts = line.strip().split()
        if not parts:
            continue
        name = parts[0]
        marks = int(parts[1]) 
        if name.lower() == update_name.lower():
            updated_lines.append(f"{update_name} {update_marks}\n")
            found = True
        else:
            updated_lines.append(f"{name} {marks}\n")
    if not found:
        return "Student not found"
    else:
        print("Student updated successfully.")
    with open("marks.txt", "w") as file:
        file.writelines(updated_lines)

def delete_name():
    lines = read_students() 
    updated_lines = []
    delete_name = input("Enter a name:").lower()
    found = False
    for line in lines:
        parts = line.strip().split()
        if not parts:
            continue
        name = parts[0]
        marks = int(parts[1]) 
        if name.lower() == delete_name.lower():
            found = True
            pass
        else:
            updated_lines.append(f"{name} {marks}\n")
    if not found:
        return f"Student not found" 
    else:
        print(f"Student Deleted Successfully.") 
    with open("marks.txt", "w") as file:
        file.writelines(updated_lines)

def avg_marks():
    lines = read_students() 
    count = 0
    total = 0
    for line in lines:
        parts = line.strip().split()
        if not parts:
            continue
        marks = int(parts[1])
        count += 1
        total += marks
    average_marks = total / count
    print("Average marks:",average_marks)


def highest_marks():
    lines = read_students() 
    first_parts = lines[0].split()
    largest = int(first_parts[1])
    top_student = first_parts[0]
    for line in lines:
        parts = line.strip().split()
        if not parts:
            continue
        name = parts[0]
        marks = int(parts[1])
        if marks > largest:
            largest = marks
            top_student = name
    print("Highest Marks:\n", top_student, "->", largest)


def show_grades():
    lines = read_students() 
    for line in lines:
        parts = line.strip().split()
        if not parts:
            continue
        name = parts[0]
        marks = int(parts[1])   
        if marks >= 90:
            print(f"{name} -> {marks} -> A")
        elif marks >= 80:
            print(f"{name} -> {marks} -> B")
        elif marks >= 70:
            print(f"{name} -> {marks} -> C")
        elif marks >= 60:
            print(f"{name} -> {marks} -> D")
        else:
            print(f"{name} -> {marks} -> F")


def grade_summary():
    lines = read_students() 
    count_A = 0
    count_B = 0
    count_C = 0
    count_D = 0
    count_F = 0
    for line in lines:
        parts = line.split()
        name = parts[0]
        marks = int(parts[1])
        if marks >= 90:
            count_A += 1
            print(f"{name} -> {marks} -> A")
        elif marks >= 80:
            count_B += 1
            print(f"{name} -> {marks} -> B")
        elif marks >= 70:
            count_C +=1 
            print(f"{name} -> {marks} -> C")
        elif marks >= 60:
            count_D += 1
            print(f"{name} -> {marks} -> D")
        else:
            count_F += 1
            print(f"{name} -> {marks} -> F")

    print(f"A : {count_A}")
    print(f"B : {count_B}")
    print(f"C : {count_C}")
    print(f"D : {count_D}")
    print(f"F : {count_F}")


while True:
    print(f"1. Display Students")
    print(f"2. Search Student")
    print(f"3. Add Student")
    print(f"4. Update Student")
    print(f"5. Delete Student")
    print(f"6. Average Marks")
    print(f"7. Highest Marks")
    print(f"8. Show Grades")
    print(f"9. Grade Summary")
    print(f"10. Exit")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        display_students()

    elif choice == 2:
        print(search_student())

    elif choice == 3:
        add_student()

    elif choice == 4:
        result = update_student()
        if result:
            print(result)

    elif choice == 5:
        result = delete_name()
        if result:
            print(result)

    elif choice == 6:
        avg_marks()

    elif choice == 7:   
        highest_marks()

    elif choice == 8:
        show_grades()

    elif choice == 9:
        grade_summary()

    elif choice == 10:
        break
    