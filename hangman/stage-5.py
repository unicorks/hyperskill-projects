import random

print("H A N G M A N\n")

# List of choices-
lang = ['python', 'java', 'kotlin', 'javascript']
choice = random.choice(lang)
ans = list('-' * len(choice))  # The hint

lives = 8  # No. of tries the player has.

while lives > 0:
    # Using 'join' to print hint as string and not list
    print("".join(ans))
    print("Input a letter: ")
    letter = input()
    print()

    # Knocking off the lives in case user already inputted that letter
    if letter in ans:
        lives = lives - 1

    # Updating the hint + checking if the letter is in the word
    elif letter in choice:
        for i in range(0, len(choice)):
            if letter == choice[i]:
                ans[i] = letter
        lives = lives - 1

    else:
        print("That letter doesn't appear in the word\n")
        lives = lives - 1

print("""Thanks for playing!
We'll see how well you did in the next stage""")
