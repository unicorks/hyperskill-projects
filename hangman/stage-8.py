import random

print("H A N G M A N")
menu = input('Type "play" to play the game, "exit" to quit: ')

if menu == "play":
    # List of choices-
    lang = ['python', 'java', 'kotlin', 'javascript']
    choice = random.choice(lang)
    ans = list('-' * len(choice))  # The hint
    lives = 8  # No. of tries the player has.

    guesses = set()  # Handling repeated letters

    while lives > 0:

        # Checking if user won
        if "".join(ans) == choice:
            print(f"You guessed the word {choice}!\nYou survived!")
            exit()

        # Using 'join' to print hint as string and not list
        print()
        print("".join(ans))
        letter = input("Input a letter: ")

        # Updating the hint + checking if the letter is in the word
        if letter in choice:
            for i in range(0, len(choice)):
                if letter == choice[i]:
                    ans[i] = letter

        # Checking args
        args = len(letter)
        if args != 1:
            print("You should input a single letter")
            continue

        # Checking if input is a letter
        lower_check = letter.islower()
        if lower_check is not True:
            print("Please enter a lowercase English letter")
            continue

        if letter not in choice and letter not in guesses:
            print("That letter doesn't appear in the word")
            lives = lives - 1

        # Handling repeated letters
        if letter in guesses:
            print("You've already guessed this letter")

        guesses.add(letter)  # keeps track of guessed letters

    # Print losing statement
    if lives == 0:
        print("You lost!")

elif menu == "exit":
    exit()
