import sys
import random
import string
import animation
import time
from termcolor import colored, cprint

password = []
characters_left = -1
error = lambda x: cprint(x, "red", attrs=["bold"])

# Functions


def update_characters_letters(number_of_characters):
    global characters_left

    if number_of_characters < 0 or number_of_characters > characters_left:
        print(
            colored("Błąd! Liczba znaków przekracza przedział od 0 do", "red"),
            colored(characters_left, "red"),
        )
        print()
        sys.exit(0)
    else:
        characters_left -= number_of_characters
        print(colored("Pozostało znaków: ", "cyan"), colored(characters_left, "cyan"))
        print()


wheel = ("#", "##", "###", "####")


@animation.wait(wheel, color="green")
def long_running_function():
    time.sleep(2)
    return


###
title = colored("[  Password Generator  ]", "red", attrs=["bold"])
print()
print(title)
print()
password_length = input(colored("Jak długie ma być hasło: ", "yellow"))
print()

# Kiedy podany znak nie jest prawidłowy (nie jest liczbą) wyświetla się bład
while not password_length.isdigit():
    error("Błąd! Wprowadź cyfrę.")
    password_length = input(colored("Jak długie ma być hasło: ", "yellow"))
    print()

password_length = int(password_length)

while password_length < 8:
    error("Błąd! Hasło musi mieć minimum 8 znaków, spróbuj jeszcze raz.")
    password_length = int(input(colored("Jak długie ma być hasło: ", "yellow")))
    print()

characters_left = password_length

lowercase_letters = input("Ile małych liter ma mieć hasło: ")
while not lowercase_letters.isdigit():
    error("Błąd! Wprowadź cyfrę.")
    lowercase_letters = input("Ile małych liter ma mieć hasło: ")
    print()

lowercase_letters = int(lowercase_letters)
update_characters_letters(lowercase_letters)

uppercase_letters = input("Ile dużych liter ma mieć hasło: ")
while not uppercase_letters.isdigit():
    error("Błąd! Wprowadź cyfrę.")
    uppercase_letters = input("Ile dużych liter ma mieć hasło: ")
    print()

uppercase_letters = int(uppercase_letters)
update_characters_letters(uppercase_letters)

special_characters = input("Ile znaków specjalnych ma mieć hasło: ")
while not special_characters.isdigit():
    error("Błąd! Wprowadź cyfrę.")
    special_characters = input("Ile specjalnych znaków ma mieć hasło: ")
    print()

special_characters = int(special_characters)
update_characters_letters(special_characters)

digits = input("Ile cyfr ma mieć hasło: ")
while not digits.isdigit():
    error("Błąd! Wprowadź cyfrę.")
    digits = input("Ile cyfr ma mieć hasło: ")
    print()

digits = int(digits)
update_characters_letters(digits)

while characters_left > 0:
    print(
        colored(
            "[ Nie wszystkie znaki zostały wykorzystane. Hasło zostanie uzupełnione małymi literami ]",
            "yellow",
        )
    )
    lowercase_letters += characters_left
    # Results
    print()
    print(colored("Podsumowanie: ", "magenta"))
    print(
        colored(" - długość hasła: ", "magenta"),
        colored(password_length, "white", attrs=["bold"]),
    )
    print(
        colored(" - małe litery: ", "magenta"),
        colored(lowercase_letters, "white", attrs=["bold"]),
    )
    print(
        colored(" - duże litery: ", "magenta"),
        colored(uppercase_letters, attrs=["bold"]),
    )
    print(
        colored(" - znaki specjalne: ", "magenta"),
        colored(special_characters, "white", attrs=["bold"]),
    )
    print(
        colored(" - ilość cyfr: ", "magenta"),
        colored(digits, "white", attrs=["bold"]),
    )
    print()

    break

# Generating password
for _ in range(password_length):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1

    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1

    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1

    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)

# Animation
long_running_function()  # [100.00 %]

# Generated password
print(
    "[",
    colored("Wygenerowane hasło", "green", attrs=["bold"]),
    "] - ",
    colored("".join(password), "blue", attrs=["bold"]),
)
print()
