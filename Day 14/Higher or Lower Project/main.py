import art
from game_data import data
import random

# print logo
# create dict of instagram accounts as keys with amount of followers as value
# When choosing randomly we need to pull the account out of dict.
# When we replace it we need to add the account back to dict
# choose first account randomly from dict as default for the start of the game
# create score set to 0
# while user didn't fail - choose randomly another account from dict
# print to the user both to decide who have more followers
# if the user fails - break and stop the game, print final score
# if the user succeeds -
# 1. add 1 to score
# 2. replace first account with second account
# 3. print score


def choose_account(first_account):
    account = random.choice(data)
    while account == first_account:
        account = random.choice(data)
    return account


def higher_or_lower():
    score = 0
    first_account = random.choice(data)
    win = True
    while win:

        second_account = choose_account(first_account)
        print(f"Compare A: {first_account['name']}, {first_account['description']} from {first_account['country']}.")
        print(art.vs)
        print(f"Against B: {second_account['name']}, {second_account['description']} from {second_account['country']}.")

        answer = 'A' if first_account['follower_count'] > second_account['follower_count'] else 'B'
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        while guess not in ['A', 'B']:
            print("You typed invalid answer.")
            guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        if guess == answer:
            score += 1
            print(f"You're right! Current score: {score}.")
            first_account = second_account
        else:
            print(f"Sorry, that's wrong. Total score: {score}")
            win = False


if __name__ == '__main__':
    playing = True
    while playing:
        print(art.logo)
        higher_or_lower()
        play_again = input("Do you want to play again? Type 'Y' or 'N': ").upper()
        while play_again not in ['Y', 'N']:
            print("You typed invalid answer.")
            play_again = input("Do you want to play again? Type 'Y' or 'N': ").upper()
        if play_again == 'N':
            playing = False


