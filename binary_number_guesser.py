from random import randint
import sys


def print_binary(binary):
    for i in range(len(binary)):
        print(binary[i], end="")

while True:
    try:
        number_bits = int(input("How many bits would you like to use? > "))
        if number_bits < 4:
            raise ValueError
    except:
        print("Invalid input")
    else:
        break

while True:
    binary = []

    for i in range(number_bits):
        binary.append(randint(0, 1))

    while True:
        try:
            print_binary(binary)
            player_guess = input(" > ")
            if player_guess.lower() == 'quit':
                sys.exit()
            player_guess = int(player_guess)
            if number_bits < 0:
                raise ValueError
        except ValueError:
            print("Invalid input")
        else:
            break 

    number = sum([binary[i] * 2 ** (number_bits - i - 1) for i in range(number_bits)])

    if player_guess != number:
        print("Incorrect. The number was", number)
