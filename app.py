def welcome():
    # This function takes a person's name as input and displays a personalized welcome message
    username = input("What's your name? ")
    print (f'Hi {username} and welcome to the World of Games: The Epic Journey')


def start_play():
    # This function presents a list of available games to the user
    intro_text ="Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n2. Guess Game - guess a number and see if you chose like the computer.\n3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
    game_choice = input(intro_text)
    while not game_choice.isnumeric() or int(game_choice) < 1 or int(game_choice) > 3:
        game_choice = input("A correct numeric number is expected: ")

    difficulty_level = input("select a difficulty level between 1 and 5:")
    while not difficulty_level.isnumeric() or int(difficulty_level) < 1 or int(difficulty_level) > 3:
        difficulty_level = input("A correct numeric number is expected: ")
