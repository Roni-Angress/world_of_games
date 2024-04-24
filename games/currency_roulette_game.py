from typing import Any
import requests
import random

"""
The Currency Roulette Game module utilizes a free currency API(package) to retrieve the current
exchange rate from USD to ILS (Israeli Shekel). Players are tasked with guessing the value of a newly
generated random number (between 1 to 100) in USD converted to ILS. The accuracy of their guess
depends on the game's difficulty level.
The allowed difference is found by subtracting the given difficulty level from 10 NIS. For instance, if
the difficulty level is 3, the acceptable difference is 10 - 3, which equals 7 NIS. Therefore, the
acceptable range is 7 NIS.
"""


def validate_number_input(message: str) -> float:
    """
    Prompts the user to enter an integer within the range of 1 to 101.
    The function returns the user input as a float.
    """
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")


def generate_random_number() -> int:
    return random.randint(1, 100)


def get_money_interval(difficulty: int, generated_number: int) -> tuple[float | Any, float | Any]:
    """
    Retrieves the current USD to ILS exchange rate and calculates an
    interval for the correct answer based on the game's difficulty level.
    """
    # Retrieve the exchange rate from USD to ILS from a currency API
    response = requests.get('https://v6.exchangerate-api.com/v6/55d4e75c2615a6280f2aca69/latest/USD')
    data = response.json()
    exchange_rate = data['conversion_rates']["ILS"]

    # Calculate the interval for the correct answer based on the game's difficulty level
    acceptable_range = 10 - difficulty
    value_after_exchange = generated_number * exchange_rate

    lower_bound = value_after_exchange - acceptable_range
    upper_bound = value_after_exchange + acceptable_range

    return lower_bound, upper_bound


def get_guess_from_user():
    """
    Prompts the user to input a guess for the converted value of a
    specified amount in USD.
    """
    message = "Guess the value converted to ILS.\nWhat is your guess? "
    guess = validate_number_input(message)
    return guess


def compare_results(lower_bound, upper_bound, guess) -> bool:
    return lower_bound <= guess <= upper_bound


def play(difficulty: int) -> bool:
    random_generated_number = generate_random_number()
    print(f'The generated number is {random_generated_number} USD.')

    guess = get_guess_from_user()
    lower_bound, upper_bound = get_money_interval(difficulty, random_generated_number)

    win = compare_results(lower_bound, upper_bound, guess)
    print(win)
    return win
