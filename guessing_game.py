# -Challenge 1
from numpy import random


def guessing_game():
    print("Guess a number from 1 to 10. You have 3 tries.")
    random_num = random.randint(1, 10)
    tries = 3
    while tries > 0:
        your_guess = int(input())

        if your_guess < random_num:
            print("Not quite, that's too low.")
            tries -= 1
        elif your_guess > random_num:
            print("Oof! That's too high.")
            tries -= 1
        else:
            if input("You got it! Nice Job. Wanna play again? ") == "yes":
                guessing_game()
            else:
                print("See ya later!")
                break
    if tries == 0:
        if input("Oh no, you're out of tries. Wanna play again? ") == "yes":
            guessing_game()
        else:
            print("See ya later!")
            return


guessing_game()

# -Challenge 2


# def organizer_5000(some_straaangz):
#     split_string = some_straaangz.split("-")
#     organized = sorted(split_string)
#     return "-".join(organized)


# print(organizer_5000("this-is-another-string"))
