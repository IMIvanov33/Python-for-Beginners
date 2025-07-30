try:  # Try block: Python will try to run the code inside the block.
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
# If user enters someting that can't be converted to an integer (like letters),  this block runs
except ZeroDivisionError:
    print("Age cannot be 0.")
except ValueError:
    print("Invalid value")
