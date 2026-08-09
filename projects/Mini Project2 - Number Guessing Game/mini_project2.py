import json
import random 
import os 

history_file = os.path.join(os.path.dirname(__file__), "history.json")
if os.path.exists("history.json"):
    with open("history.json","r")as file:
        history = json.load(file)

else:
    history = []

while True:
    secret_number = random.randint(1,100)
    attempt = 0 

    while True:
        try:
            user_number = int(input("Enter a number:"))
            if user_number < 1 or user_number > 100:
                raise ValueError("Number should be between 1 to 100")

        except ValueError as e:
            print(e)
            continue
        attempt += 1

        if user_number == secret_number:
            print("You won!")
            print("Attempt:",attempt)
            break

        elif user_number < secret_number:
            print("Too low!")

        elif user_number > secret_number:
            print("Too high!")

    history_dict = {"attempts" : attempt, 
                    "secret_number" : secret_number}

    history.append(history_dict)

    with open("history.json", "w")as file:
        json.dump(history, file)

    user_choice = input("Do you want to play again? (y/n):")
    if user_choice.lower() == "n":
        print("Thanks for playing!")
        break

