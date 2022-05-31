from words import words
import string
import random

def valid_word(words):
    word = random.choice(words)
    while '-' in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        print("You have already used these characters: "," ".join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current Word: "," ".join(word_list))

    #getting the user input
        user_input = input("Guess a letter: ").upper()
        if(user_input in alphabet - used_letters):
            used_letters.add(user_input)
            if(user_input in word_letters):
                word_letters.remove(user_input)

        elif user_input in used_letters:
            print("You have already used that letter, Please enter another character")

        else:
            print("Invalid character, Please try again.")
    
    print("YAY!! you have guessed the right word: ", word)


if __name__ == '__main__':
    hangman()