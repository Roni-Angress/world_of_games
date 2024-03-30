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
    game_choice = input(intro_text)
    while game_choice not in ["1", "2", "3"]:
        game_choice = input("Please enter a valid option (1, 2, or 3): ")
    game_choice = int(game_choice)

    difficulty_level = input("Select a difficulty level between 1 and 5: ")
    while difficulty_level not in ["1", "2", "3", "4", "5"]:
        difficulty_level = input("Please enter a numeric value between 1 and 5: ")
    difficulty_level = int(difficulty_level)
