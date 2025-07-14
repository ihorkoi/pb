import random


def guess_number(secret_number, tries):
    fails = 0
    while fails < tries:
        try:
            guess = int(
                input(f"Guess a number between 1 and 100. {tries-fails} attempts left: "))
        except:
            print('Invalid number!')
            continue
        if guess < secret_number:
            fails += 1
            print("Too low!")
        elif guess > secret_number:
            fails += 1
            print("Too high!")
        else:
            print("Congratulations! You've guessed the number!")
            return
    print('You lost! Try your luck again')


if __name__ == "__main__":
    secret_number = random.randint(1, 100)
    tries = 7
    guess_number(secret_number, tries)
