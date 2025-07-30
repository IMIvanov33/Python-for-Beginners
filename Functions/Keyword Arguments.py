# Defines a function with two parameters: first_name and last_name
def greet_user(first_name, last_name):
    # Prints a greeting message using the provided first and last names
    print(f'Hi {first_name} {last_name}!')
    print('Welcome')                             # Prints a welcome message


# Prints "Start" to mark the beginning of the program
print("Start")

# Calls the greet_user function using keyword arguments:
# Here, 'last_name' and 'first_name' are explicitly specified by name, so their order can be different
greet_user(last_name="Bravo", first_name='Bobi')

# Prints "Finish" to mark the end of the program
print('Finish')
