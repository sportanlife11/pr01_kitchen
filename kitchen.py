print("Welcome to the kitchen.")

name = input("What's your name? ")
print(f"Hi there, {name}")

drinkChoice = input("What would you like to drink?")
if drinkChoice == "tea":
    print("Have a nice tea!")
elif drinkChoice == "coffee":
    print("Feeling tired?")
else:
    print("We only serve water.")
