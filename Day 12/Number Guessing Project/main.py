import random
import art
if __name__ == '__main__':
    print(art.logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    lives = 5 if difficulty == "hard" else 10
    number = random.randint(1,100)
    for i in range(lives, 0, -1):
        print(f"You have {i} attempts remaining to guess the number.")
        guess = int(input("make a guess: "))
        if guess == number:
            print(f"You got it! The number was {number}")
            break
        if guess < number:
            print("Too low.")
        else:
            print("Too high.")
        if i != 1: print("Guess again.")
    else:
        print(f"You lost. The number was {number}")
