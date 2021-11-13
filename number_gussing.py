import random
print("Welcome to number Gussing Game")

while True:
    playgame = input("Do you want to play (y/n) :")
    if playgame == "y":
        print("Start")
        computer = random.randint(0, 9)
        user_input = None
        user_input = int(input("Guess a number between 0 and 9: "))

        # there are 3 ways to check that if user input is not in (0-9) range then invalid choice

        # if user_input == "0" or user_input == "1" or user_input == "2" or user_input == "3" or user_input == "4" \
        #         or user_input == "5" or user_input == "6"  or user_input == "7"  or user_input == "8" or user_input == "9" :

        if user_input in range(0, 10):

        # if user_input>=0 & user_input <=9:
            print("the Computer Choose the Number")
            print(computer)

            if user_input == computer:
                 print("Congratulations! You Won")
            else:
                 print("Nope, sorry. try again!")
        else:
            print(" Invalid choice, Please choose number from 0-9 & try again")

    else:
        print("Thankyou! Game exit")
        exit(1)


