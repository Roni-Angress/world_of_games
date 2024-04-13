import random
import os
from time import sleep


def generate_sequence(difficulty: int) -> list[int]:
    """
    Generates a list of random numbers between 1 and 101, with length equal to difficulty.
    """
    random_numbers = [random.randint(1, 101) for _ in range(difficulty)]
    return random_numbers


def validate_number_input(message: str) -> int:
    """
    Prompts the user to enter an integer within the range of 1 to 101.
    The function returns the user input as an integer.
    """
    while True:
        try:
            number = int(input(message))
            if 1 <= number <= 101:
                return number
            else:
                print("Number must be in the range of 1 - 101.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def get_list_from_user(difficulty: int) -> list[int]:
    """
    Prompts the user to input a list of numbers matching the length of the generated sequence.
    """
    user_input = []
    for i in range(difficulty):
        remaining_numbers = difficulty - len(user_input)
        msg = f'Please enter {remaining_numbers} more numbers in the range of 1 - 101: '
        number = validate_number_input(msg)
        user_input.append(number)
    return user_input


def is_list_equal(list_a: list[int], list_b: list[int]) -> bool:
    """
    Checks if two lists are equal.
    """
    return list_a == list_b


def play(difficulty: int) -> bool:
    """
    Executes the game by invoking the functions above and prints the result.
    """
    generated_numbers = generate_sequence(difficulty)
    print(generated_numbers)
    sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')
    user_input = get_list_from_user(difficulty)
    win = is_list_equal(generated_numbers, user_input)
    print(win)
    return win
