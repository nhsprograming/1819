import random
continuegame = True

while continuegame is True:

    user_in = input("R,P,S (Q): ")
    options = ["R","P","S"]

    choice = random.choice(options)
    print(choice)

    if user_in == "Q":
        continuegame = False

    elif choice == user_in:
        print("Draw")

    elif choice == "R" and user_in == "P":
        print("Player Wins")

    elif choice == "P" and user_in == "S":
        print("Player Wins")

    elif choice == "S" and user_in == "R":
        print("Player Wins")

    elif choice == "P" and user_in == "R":
        print("Computer Wins")

    elif choice == "S" and user_in == "P":
        print("Computer Wins")

    elif choice == "R" and user_in == "S":
        print("Computer Wins")
