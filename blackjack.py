# Pretty barebones creation of 2 player blackjack I ripped out in the middle of a lecture because I was bored 
# Maybe one day I'll create a GUI
# Aces are 1 or 11 (player choice)

from random import randint

def play():
    last_turn = 0 
    dealer_cards = [randint(1,10), randint(1,10)]
    player_cards = [randint(1,10), randint(1,10)]
    total = sum(player_cards)
    for i in player_cards:
        if i == 1:
            ace_choice = input("You have recieved an Ace, would you like it to be 1 point, or 11 points?")
            player_cards[i] = int(''.join(ace_choice))
        
    while sum(player_cards) < 21 and sum(dealer_cards) < 21:
        print("\n" + "Your cards: " + str(player_cards))
        print("Score: " + str(total))
        get_move = input("Hit or Stand: ") 
        move = ''.join(i.lower() for i in get_move.split())
        if move == 'hit':
            player_cards.append(randint(1,10))
            total = sum(player_cards)
            if total >= 21:
                print("You lose, card total above 21!")
                return None
        else:
            while sum(dealer_cards) < 17:
                dealer_cards.append(randint(0,10))
                if sum(dealer_cards) >= 21:
                    print("Dealers card total: " + str(sum(dealer_cards)))
                    print("You win!")
                    return 

            

play()
