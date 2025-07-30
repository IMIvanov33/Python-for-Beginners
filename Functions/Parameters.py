# Defines a function that takes two parameters: first_name and last_name
def greet_user(first_name, last_name):
    # Prints a personalized greeting with first and last name
    print(f'Hi {first_name} {last_name}!')
    print('Welcome')                       # Prints a welcome message


# Prints "Start" to indicate the beginning of the program
print("Start")

# Calls the greet_user function with "Bobi" and "Bravo" as arguments
greet_user("Bobi", "Bravo")
# Calls the greet_user function with "Ivan" and "Bravo" as arguments
greet_user("Ivan", "Bravo")

# Prints "Finish" to indicate the end of the program
print('Finish')
