import random


def guess_number(secret_number, guess):
    while True:
        if guess < secret_number:
            guess = int(input("Too low!:"))
        if guess > secret_number:
            guess = int(input("Too high!:"))
        if guess == secret_number:
            print("Congratulations! You've guessed the number!")
            break


if __name__ == "__main__":
    secret_number = random.randint(1, 100)
    guess = int(input("Guess a number between 1 and 100: "))
    guess_number(secret_number, guess)
