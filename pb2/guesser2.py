import random


def word_guesser(selected_word, tries):
    word = '*' * len(selected_word)
    guesses = 0
    while guesses < tries:
        letter = input('Try to guess a word! Type a letter:')
        for letter_idx in range(len(selected_word)):
            if selected_word[letter_idx] == letter:
                word = list(word)
                word[letter_idx] = letter
                word = ''.join(word)
        print(word)
        guesses += 1
        if word == selected_word:
            print('Winner!')
            return
    return


if __name__ == "__main__":
    words_list = ["go", "python", "java", "javascript", "ruby", "html", "css", "swift", "kotlin", "typescript", "csharp", "php", "sql",
                  "rust", "dart", "scala", "elixir", "clojure", "haskell", "erlang", "groovy", "perl", "lua", "bash", "powershell", "matlab", "r", "julia"]
    selected_word = words_list[random.randint(0, len(words_list))]
    tries = 7
    word_guesser(selected_word, tries)
