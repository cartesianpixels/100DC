ascii_art = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
"""

print(ascii_art)

import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "language"]
    word = random.choice(words)
    return word

def display(word, guessed_letters):
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    print(display_word)

def draw_hangman(attempts):
    stages = [
        """
           +---+
           |   |
               |
               |
               |
               |
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """
    ]
    print(stages[attempts])

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nAttempts left:", attempts)
        draw_hangman(6 - attempts)
        display(word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)

        if guess in word:
            if set(guessed_letters) == set(word):
                display(word, guessed_letters)
                print("Congratulations! You've guessed the word:", word)
                break
        else:
            attempts -= 1
            print("Incorrect guess. Try again.")
    
    if attempts == 0:
        print("Sorry, you've run out of attempts. The word was:", word)

hangman()