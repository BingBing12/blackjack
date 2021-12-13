## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
from art import logo
#deal a card function
def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    # check for blackjack(ace +10) which ill set to 0 to represent
    if len(cards)==2 and sum(cards)==21:
        return 0
    elif 11 in cards and sum(cards)>21:
        cards[cards.index(11)]=1
    return sum(cards)
def compare(player_score, computer_score):
    if(player_score==computer_score):
        return "Draw"
    elif(computer_score==0):
        return "computer scored blackjack, you lose"
    elif(player_score==0):
        return "You won with blackjack"
    elif(player_score>21):
        return "you went over, you lose"
    elif(computer_score>21):
        return "computer went over, you win"
    elif(player_score>computer_score):
        return "You win"
    else:
        return "You lose"
def play():
    print(logo)
    player_hand = []
    computer_hand = []
    game_over = False
    #deal 2 cards to player and computer
    for i in range(2):
        player_hand.append(deal())
        computer_hand.append(deal())
    while not game_over:
        player_score=calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computers first card is: {computer_hand[0]}")
        if player_score==0 or computer_score==0 or player_score>21:
            game_over=True
        else:
            hit = input("type 'y' to get another card, or type 'n' to pass. ").lower()
            if(hit!='y'):
                game_over=True
            else:
                player_hand.append(deal())
    while computer_score!=0 and computer_score<17:
        computer_hand.append(deal())
        computer_score=calculate_score(computer_hand)

    
    print(f"Your hand: {player_hand}\tScore: {player_score} \nComputer's hand: {computer_hand}\tScore: {computer_score} ")
    print(compare(player_score, computer_score))
while(input("would you like to play a game of blackjack? 'y' or 'n'").lower()=='y'):
    play()
print("Goodbye!")