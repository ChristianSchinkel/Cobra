"""Crack
This module is used to generate all possible combinations of
4 characters, which can be:
- digits,
- ascii letters, or
- punctuation.
It can be used for cracking passwords or other similar tasks.
The module contains three functions:
- generate_digits,
- generate_ascii_letters and
- generate_digits_ascii_letters_punctuation.
Each function generates a different set of combinations, and
prints them to the console.
The main function calls the first two functions to
demonstrate their functionality.
"""
# Implementation goes here:
from string import digits
from string import ascii_letters
from string import punctuation


def generate_digits():
    """Generate 4 digits and print them.
    Arguments:
    None
    Returns:
    None
    """
    for i in digits:
        for j in digits:
            for k in digits:
                # use "m" instead of "l" can be missunderstood
                # as "1" or "I" in some textfonts.
                for m in digits:
                    print(i, j, k, m)


def generate_ascii_letters():
    """Generate 4 ascii_letters and print them.
    Arguments:
    None
    Returns:
    None
    """
    for i in ascii_letters:
        for j in ascii_letters:
            for k in ascii_letters:
                # use "m" instead of "l" can be missunderstood
                # as "1" or "I" in some textfonts.
                for m in ascii_letters:
                    print(i, j, k, m)


def generate_digits_ascii_letters_punctuation():
    """Generate 4 digits, ascii_letters, punctuation and print them.
    Arguments:
    None
    Returns:
    None
    """
    for i in ascii_letters+digits+punctuation:
        for j in ascii_letters+digits+punctuation:
            for k in ascii_letters+digits+punctuation:
                # use "m" instead of "l" can be missunderstood
                # as "1" or "I" in some textfonts.
                for m in ascii_letters+digits+punctuation:
                    print(i, j, k, m)


def main():
    """
    Main function to run the 'Main'-module
    """
    # 'pass' is a placeholder it does nothing
    # it is used when a statement is required syntactically
    # but no action is needed.

    # Call the functions to demonstrate their functionality.
    generate_digits()  # 4 digits and prints them.
    generate_ascii_letters()  # 4 ascii letters and prints them.


if __name__ == "__main__":
    # To test the modules funtionality.
    main()
