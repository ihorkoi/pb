import random


def word_guesser(selected_word, tries):
    word = '*' * len(selected_word)
    entered_letters = set()
    guesses = 0
    while guesses < tries:
        try:
            letter = input('Try to guess a word! Type a letter:')
            if not letter.isalpha() or len(letter) < 1:
                print('Please, provide a correct input')
                continue
            if letter in entered_letters:
                print('You have already tried this letter!')
                continue
            else:
                entered_letters.add(letter)
        except:
            print('Enter a valid letter!')
            continue

        word = ''.join(letter if letter == selected_word[i] else word[i]
                       for i in range(len(selected_word)))

        print(word)
        print(f'You have {tries - guesses-1} tries left!')
        guesses += 1
        if word == selected_word:
            print('Winner!')
            return
    return


if __name__ == "__main__":
    words_list = ["go", "python", "java", "javascript", "ruby", "html", "css", "swift", "kotlin", "typescript", "csharp", "php", "sql",
                  "rust", "dart", "scala", "elixir", "clojure", "haskell", "erlang", "groovy", "perl", "lua", "bash", "powershell", "matlab", "r", "julia"]
    selected_word = random.choice(words_list)
    tries = 7
    word_guesser(selected_word, tries)
