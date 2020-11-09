command = ""
started = False
i = 1
while i <= 50:
    print("*" * i)
    i += 1
print("""
        Car Game
    Type help for help
    """)
while command.lower() != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("Car Started")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car Stopped")
    elif command == "help":
        print("""
Start - to start your car
Stop - To Stop Your Car
Quit - To end game
        """)
    elif command == "":
        print("input a function")
    elif command == "quit":
        print("Game terminated")
        break
    elif command != "stop" or command != "start" or command != "help" or command != "quit" or command != "":
        print("Wrong input")
