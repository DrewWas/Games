# Twenty-One Rules

"""
Two players alternate turns, on which they can add 1, 2, or 3 to the
current total. The total starts at 0 and the game ends whenever the
total is 21 or more. The last player to add to the total loses

The opponent is an ai that chooses a random number between 1 and 3
"""
from random import randint

def play(initial):
    total = initial
    turn = 1
    while total < 21:
        print("\nScore: " + str(total))
        if turn > 0:
            player_choice = ''.join(input("Add 1, 2, or 3: "))
            if int(player_choice) not in [1,2,3]:
                print("You must choose either 1, 2, or 3")
                play(total)
            else: 
                total += int(player_choice)
                turn = -turn

        else:
            x = randint(1,3)
            print("AI adds " + str(x))
            total += x
            turn = -turn



    print("Final score: " + str(total))
    if turn > 0:
        print("\nYou win!")            
    else:
        print("\nYou lose")            

play(0)

