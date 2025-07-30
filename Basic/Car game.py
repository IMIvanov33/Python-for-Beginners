started = False
command = ""

while command != "quit":
    command = input("> ").lower()

    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
        print("""
Available commands:
  start - to start the car
  stop  - to stop the car
  quit  - to exit the program
  help  - to show this help
""")
    elif command == "quit":
        break
    else:
        print("I don't understand that command.")
print("Goodbye!")
