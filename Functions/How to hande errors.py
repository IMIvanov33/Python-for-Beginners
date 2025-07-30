try:  # Try block: Python will try to run the code inside the block.
    age = int(input("Age: "))
    print(age)
# If user enters someting that can't be converted to an integer (like letters),  this block runs
except ValueError:
    print("Invalid value")
