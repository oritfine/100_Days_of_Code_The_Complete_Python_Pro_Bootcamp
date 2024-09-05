import art
import random

def calculate_score(cards):
    score = sum(cards)
    if len(cards) == 2 and score == 21:
        #TODO check if the len check needed
        return 0
    while score > 21 and 11 in cards:
        cards[cards.index(11)] = 1
        score -= 10
    return score

def print_final_results(user_cards, computer_cards):
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, final score: {user_score}")
    print(f"Computer's first card: {computer_cards}, final score: {computer_score}")
    if user_score > 21:
        print("You Lose!")
    elif

def print_current_status(user_cards, computer_first_card, score):
    print(f"Your cards: {user_cards}, current score: {score}")
    print(f"Computer's first card: {computer_first_card}")


def computer_turn(cards, computer_cards):
    computer_score = calculate_score(computer_cards)
    while computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score = calculate_score(computer_cards)
    return computer_score

def user_turn(cards, computer_first_card, user_cards):
    get_card = True
    score = 0
    while get_card:
        score = calculate_score(user_cards)
        print_current_status(user_cards, computer_first_card, score)
        if score > 20 or score == 0:
            break
        get_card = input("type 'y' to get another card, type 'no' to pass").lower()
        if get_card == 'y':
            user_cards.append(random.choice(cards))
        elif get_card == 'n':
            get_card = False
        else:
            print("Invalid answer. Type again and choose on of the valid options.")
    return score

def black_jack():
    print(art.logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]
    user_score = user_turn(cards, computer_cards[0], user_cards)
    if user_score > 21:
        print("You lost!")
    else:
        computer_score = calculate_score(computer_cards)
        if computer_score == user_score == 0:
            print("Its a draw!")
        elif computer_score == 0:
            print("You lost!")
        elif user_score == 0:
            print("You won!")
        else:
            computer_score = computer_turn(cards, computer_cards)
    print_final_results(user_cards, computer_cards)


if __name__ == '__main__':
    game_on = True
    while game_on:
        answer = input("Do you want to play a game of Blackjack? type 'y' or 'no' ").lower()
        if answer == 'y':
            black_jack()
        elif answer == 'n':
            game_on = False
        else:
            print("Invalid answer. Type again and choose on of the valid options.")