import random


def guess_number(secret_number, guess, tries):
    fails = 0
    while fails < tries:
        if guess < secret_number:
            fails += 1
            guess = int(input(f"Too low! You have {tries-fails} left!:"))
        if guess > secret_number:
            fails += 1
            guess = int(input(f"Too high! You have {tries-fails} left!:"))
        if guess == secret_number:
            print("Congratulations! You've guessed the number!")
            break
    print('You lost! Try your luck again')


if __name__ == "__main__":
    secret_number = random.randint(1, 100)
    tries = 7
    guess = int(input("Guess a number between 1 and 100: "))
    guess_number(secret_number, guess, tries)
