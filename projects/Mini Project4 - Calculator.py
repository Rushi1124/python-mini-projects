
# Calculator

# Input number
def get_number():
    try:
        value = input("Enter a number: ")
        if "." in value:
            return float(value)
        else:
            return int(value)
    except ValueError:
        return "Enter a valid number."


# Addition
def add():
    a = get_number()
    b = get_number()

    if not isinstance(a, (int, float)):
        return a
    if not isinstance(b, (int, float)):
        return b

    return a + b


# Subtraction
def sub():
    a = get_number()
    b = get_number()

    if not isinstance(a, (int, float)):
        return a
    if not isinstance(b, (int, float)):
        return b

    return a - b


# Multiplication
def mul():
    a = get_number()
    b = get_number()

    if not isinstance(a, (int, float)):
        return a
    if not isinstance(b, (int, float)):
        return b

    return a * b


# Division
def div():
    a = get_number()
    b = get_number()

    if not isinstance(a, (int, float)):
        return a
    if not isinstance(b, (int, float)):
        return b

    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."


# Menu
while True:
    print("\nType A to Add")
    print("Type S to Subtract")
    print("Type M to Multiply")
    print("Type D to Divide")
    print("Type E to Exit")

    choice = input("Enter your choice: ").upper()

    if choice == "A":
        result = add()
    elif choice == "S":
        result = sub()
    elif choice == "M":
        result = mul()
    elif choice == "D":
        result = div()
    elif choice == "E":
        print("Calculator closed.")
        break
    else:
        print("Invalid choice. Try again.")
        continue
    
#Result 
    if isinstance(result, (int, float)):
        print("Result:", round(result, 2))
    else:
        print(result)


