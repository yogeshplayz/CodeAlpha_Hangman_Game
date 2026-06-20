import random

def play_hangman():
    # Setup: 5 predefined words and game limits
    words = ['python', 'coding', 'script', 'logic', 'system']
    word_to_guess = random.choice(words)
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")

    # Main game loop
    while attempts_left > 0:
        # Display current progress (e.g., "p _ t h _ n")
        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nWord: {display_word.strip()}")
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed so far: {', '.join(guessed_letters)}")

        # Check if the player has won
        if "_" not in display_word:
            print("Congratulations! You won!")
            break

        # Get player input
        guess = input("Guess a letter: ").lower()

        # Input validation and game logic
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
        elif guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
            guessed_letters.append(guess)
        else:
            print(f"Sorry, '{guess}' is not there.")
            guessed_letters.append(guess)
            attempts_left -= 1

    # Check if the player lost
    if attempts_left == 0:
        print(f"\nGame Over! The word was: {word_to_guess}")

if __name__ == "__main__":
    play_hangman()
