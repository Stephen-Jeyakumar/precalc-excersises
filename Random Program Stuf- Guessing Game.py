# Random Program Stuf
# 12-8-2020
# Guessing Game

import random

def guessing_game(number, max_tries):
    number_of_tries = 1
    user_number = int(input("Enter number here:"))
    while(number != user_number) and number_of_tries < max_tries:
        if(number > user_number):
            print("Your number is too small")
        else:
            print("Your number is too big")
        user_number = int(input("Enter number here:"))
        number_of_tries = number_of_tries + 1
    return number_of_tries


def print_resuslts(number_of_tries, max_tries):
    if(number_of_tries < max_tries):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n Congradulations! You found the number!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    else:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n OOF you didn't find the number soon enough. Try again.\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


number = random.randint(1,111)
max_tries = 10
number_of_tries = guessing_game(number, max_tries)
print_resuslts(number_of_tries, max_tries)



