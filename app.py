from games.currency_roulette_game import play as currency_roulette_game_play
from games.memory_game import play as memory_game_play
from games.guess_game import play as guess_game_play
from games.utils import validate_int_input
from score import add_score as add_score


# def validate_input():
# the function receives three variables: inp, start and end, and will check whether inp is in the range of start-end
#     pass
def welcome():
    # This function takes a person's name as input and displays a personalized welcome message
    username = input("What's your name? ")
    print(f"Hi {username}! Welcome to the World of Games: The Epic Journey")


def start_play():
    # This function presents a list of available games to the user
    intro_text = (
        "Please choose a game to play:\n"
        "1. Memory Game - A sequence of numbers will appear for 1 second, and you have to guess it back.\n"
        "2. Guess Game - Guess a number and see if you chose like the computer.\n"
        "3. Currency Roulette - Try to guess the value of a random amount of USD in ILS.\n"
    )

    game_choice = validate_int_input(intro_text)
    while not 1 <= game_choice <= 3:
        game_choice = validate_int_input("Only a number from 1 to 3 is allowed: ")

    difficulty_level = validate_int_input("Select a difficulty level between 1 and 5: ")
    while not 1 <= difficulty_level <= 5:
        difficulty_level = validate_int_input("Please enter a numeric value between 1 and 5: ")

    win = None
    if game_choice == 1:
        win = memory_game_play(difficulty_level)
    if game_choice == 2:
        win = guess_game_play(difficulty_level)
    if game_choice == 3:
        win = currency_roulette_game_play(difficulty_level)

    if win:
        add_score(difficulty_level)



