import random
def take_input():
    while True:
        try:
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")
            print("4. Exit")
            user_input = int(input("Enter your choice: "))
            if user_input<1 or user_input>4:
                print("Invalid input, please try again.")
                print("--------------------------------")
                continue
            break
        except ValueError:
            print("Invalid input, please try again.")
            print("--------------------------------")
    return user_input
def perform_operation(choice,computer_choice):
    if choice==1:
        if computer_choice==1:
            print("You chose Rock")
            print("Computer chose Rock")
            print("It's a tie!")
            return 1
        elif computer_choice==2:
            print("You chose Rock")
            print("Computer chose Paper")
            print("Computer won the round!")
            return 2
        else:
            print("You chose Rock")
            print("Computer chose Scissors")
            print("You won the round!")
            return 0
    elif choice==2:
        if computer_choice==1:
            print("You chose Paper")
            print("Computer chose Rock")
            print("You won the round!")
            return 0
        elif computer_choice==2:
            print("You chose Paper")
            print("Computer chose Paper")
            print("It's a tie!")
            return 1
        else:
            print("You chose Paper")
            print("Computer chose Scissors")
            print("Computer won the round!")
            return 2
    else:
        if computer_choice==1:
            print("You chose Scissors")
            print("Computer chose Rock")
            print("Computer won the round!")
            return 2
        elif computer_choice==2:
            print("You chose Scissors")
            print("Computer chose Paper")
            print("You won the round!")
            return 0
        else:
            print("You chose Scissors")
            print("Computer chose Scissors")
            print("It's a tie!")
            return 1
def main():
    print("-----------------------------------------------")
    print("          ROCK PAPER SCISSORS GAME             ")
    print("-----------------------------------------------")
    userscore=0
    computerscore=0
    tiescore=0
    while True:
        choice=take_input()
        if choice==4:
            if userscore==0 and computerscore==0 and tiescore==0:
                print("No game played! Thank you!")
            else:
                print("Total rounds played:",userscore+computerscore+tiescore)
                print("You won",userscore,"rounds")
                print("Computer won",computerscore,"rounds")
                print("Tie rounds",tiescore)
                if userscore>computerscore:
                    print("So, You won the game!")
                elif userscore==computerscore:
                    print("So, It's a tie!")
                else:
                    print("So, Computer won the game!")
                print("Thank you for playing!")
            break
        computer_choice=random.randint(1,3)
        winner_no = perform_operation(choice,computer_choice)
        if winner_no==0:
            userscore+=1
        elif winner_no==1:
            tiescore+=1 
        else:
            computerscore+=1
        print("-----------------------------------------------")
        while True:
            try:
                print("1. Yes")
                print("2. No")
                ch=int(input("Do you want to play another round? "))
                print("------------------------------------------")
                if ch<1 or ch>2:
                    print("Invalid input, please try again.")
                    print("--------------------------------")
                    continue
                break
            except ValueError:
                print("Invalid input, please try again.")
                print("--------------------------------")
        if ch==2:
            print("Total rounds played:",userscore+computerscore+tiescore)
            print("You won",userscore,"rounds")
            print("Computer won",computerscore,"rounds")
            print("Tie rounds",tiescore)
            if userscore>computerscore:
                print("So, You won the game!")
            elif userscore==computerscore:
                print("So, It's a tie!")
            else:
                print("So, Computer won the game!")
            print("Thank you for playing!")
            break
if __name__ == "__main__":
    main()