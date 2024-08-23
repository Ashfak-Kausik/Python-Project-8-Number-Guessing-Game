import random

def guess_number():
    number = random.randint(1, 100)
    guess = None

    while guess != number:
        guess = int(input("Guess the number between 1 and 100: "))

        if guess < number:
            print("Higher...")
        elif guess > number:
            print("Lower...")
        else:
            print("Congratulations! You've guessed the number!")

guess_number()
