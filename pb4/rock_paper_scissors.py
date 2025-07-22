import random


def players_turn():
    try:
        choise = int(input('''What is your choise?: 
                           1 - Rock
                           2 - Paper 
                           3 - Scissors
'''))
    except ValueError:
        print('Choose between 1-3')

    return transform_choise(choise)


def computers_turn():
    print("Now it's Computer's Turn")
    choise = random.randint(1, 3)
    return transform_choise(choise)


def transform_choise(choise):
    if choise == 1:
        return 'Rock'
    elif choise == 2:
        return 'Paper'
    else:
        return 'Scissors'


if __name__ == "__main__":
    choises = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print("""Winning rules of the game ROCK PAPER SCISSORS are:
Rock vs Paper -> Paper wins 
Rock vs Scissors -> Rock wins 
Paper vs Scissors -> Scissors wins """)
    while True:
        human_choise = players_turn()
        computer_choise = computers_turn()
        print(f"{human_choise} VS {computer_choise}")
        if (human_choise == "Rock" and computer_choise == 'Paper') or (human_choise == "Paper" and computer_choise == 'Rock'):
            result = "Paper"
        elif (human_choise == "Scissors" and computer_choise == 'Paper') or (human_choise == "Paper" and computer_choise == 'Scissors'):
            result = "Scissors"
        elif (human_choise == "Scissors" and computer_choise == 'Rock') or (human_choise == "Rock" and computer_choise == 'Scissors'):
            result = "Rock"
        else:
            result = "Draw"
        if human_choise == result:
            print('Human wins!')
        elif computer_choise == result:
            print('Computer wins!')
        else:
            print(result)
