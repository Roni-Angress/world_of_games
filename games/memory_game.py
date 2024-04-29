import random
import os
from time import sleep
from games.utils import validate_int_input



def generate_sequence(difficulty: int) -> list[int]:
    """
    Generates a list of random numbers between 1 and 101, with length equal to difficulty.
    """
    random_numbers = [random.randint(1, 101) for _ in range(difficulty)]
    return random_numbers





def get_list_from_user(difficulty: int) -> list[int]:
    """
    Prompts the user to input a list of numbers matching the length of the generated sequence.
    """
    user_input = []
    for i in range(difficulty):
        remaining_numbers = difficulty - len(user_input)
        msg = f'Please enter {remaining_numbers} more numbers in the range of 1 - 101: '
        number = validate_int_input(msg)
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
