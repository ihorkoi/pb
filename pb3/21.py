
def sequence_is_correct(sequence):
    etalon = [i for i in range(1, len(sequence)+1)]
    for i in range(len(sequence)):
        if sequence[i] != etalon[i]:
            return False
    return True


def computer_turn(sequence):
    return


def player_turn(sequence):
    return


def start():
    sequence = []
    while True:
        try:
            player_1_turn = int(input('Say your number: '))
            sequence.append(player_1_turn)
        except ValueError:
            print('Enter a valid number, please!')
        if sequence_is_correct(sequence):
            print(sequence)
            continue
        else:
            break
    print('This is it!')


if __name__ == "__main__":
    greetings = input('Hi! Ready to play the game? [Y/n]:')
    if greetings == 'Y' or greetings == '':
        start()
    elif greetings == 'n':
        print("Ok! Have a nice day!")
    else:
        print("Sory, I didn't get it")
