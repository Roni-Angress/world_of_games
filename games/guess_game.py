import random
from games.utils import validate_int_input


def generate_number(difficulty):
    """
    Generates a random number between 0 and the specified difficulty.

    Args:
        difficulty (int): The upper limit of the range for generating the secret number.

    Returns:
        int: The randomly generated secret number.
    """
    return random.randint(0, difficulty)


def get_guess_from_user(difficulty):
    """
    Prompts the user to input a number within the range of 0 to the specified difficulty.

    Args:
        difficulty (int): The upper limit of the range for user's guess.

    Returns:
        int: The user's guess.
    """
    msg = f'Welcome to the Guess Game!\nPlease enter a number within the range of 0 to {difficulty}: '
    guess = validate_int_input(msg)
    return guess


def compare_results(a, b):
    """
    Compares the secret number with the user's guess.

    Args:
        a (int): The randomly generated secret number.
        b (int): The user's guess.

    Returns:
        bool: True if the user's guess matches the secret number, False otherwise.
    """
    return a == b


def play(difficulty: int) -> bool:
    """
    Initiates the game by generating a secret number, getting user's guess, and comparing the results.

    Args:
        difficulty (int): The upper limit of the range for generating the secret number and user's guess.

    Returns:
        bool: True if the user wins, False if the user loses.
    """
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    print(f'The generated number is {secret_number}, and your guess was {user_guess}.')
    win = compare_results(secret_number, user_guess)
    print(win)
    return win
