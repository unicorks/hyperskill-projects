import random

print("H A N G M A N\n")

# List of choices-
lang = ['python', 'java', 'kotlin', 'javascript']
choice = random.choice(lang)
ans = list('-' * len(choice))  # The hint

lives = 8  # No. of tries the player has.

while lives > 0:

    # Checking if user won
    if ans == choice and lives > 0:
        print("""You guessed the word!
        You survived!""")
        break

    # Using 'join' to print hint as string and not list
    print("".join(ans))
    print("Input a letter: ")
    letter = input()
    print()

    # Knocking off the lives in case user already inputted that letter
    if letter in ans:
        lives = lives - 1
        print("No improvements\n")

    # Updating the hint + checking if the letter is in the word
    elif letter in choice:
        for i in range(0, len(choice)):
            if letter == choice[i]:
                ans[i] = letter

    else:
        print("That letter doesn't appear in the word\n")
        lives = lives - 1

# Print losing statement
if lives == 0:
    print("You lost!")
