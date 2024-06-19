#Eva Georgieva 8v no12
import random

def read_word_file(file_name):
    word_list = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                word = line.strip().lower()
                if word:
                    word_list.append(word)
            if word_list:
                return random.choice(word_list)
            else:
                print("The file is empty.")
                return None
    except FileNotFoundError:
        print("No such file.")
        return None

def letters_entered():
    return input("Enter one letter: ").strip().lower()

def hiddenword(word, guessed_letters):
    hidden_word = ""
    for letter in word:
        if letter in guessed_letters:
            hidden_word += letter + " "
        else:
            hidden_word += "_ "
    return hidden_word.strip()

def checkguessedletters(word, guessed_letters, letter):
    if letter in word:
        guessed_letters.add(letter)
    return guessed_letters

def start(file_name):
    word = read_word_file(file_name)
    if not word:
        return

    guessed_letters = set()
    mistakes = 0
    max_mistakes = 6

    while mistakes < max_mistakes:
        print(hiddenword(word, guessed_letters))
        letter = letters_entered()

        if letter in guessed_letters:
            print("Letter already guessed.")
            continue

        guessed_letters = checkguessedletters(word, guessed_letters, letter)

        if letter not in word:
            mistakes += 1
            print(f"You have {max_mistakes - mistakes} more tries.")

        if all(letter in guessed_letters for letter in word):
            print(f"Word guessed: {word}")
            return

    print("You've lost.")
    print(f"The word was: {word}")
    print(" _______")
    print("  |/    |")
    print("  |    (_)")
    print("  |    \\|/")
    print("  |     |")
    print("  |    / \\")
    print("  |")
    print("  |___")

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    start(file_name)