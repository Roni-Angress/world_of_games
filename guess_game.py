import random

def generate_number(difficulty):
    # Generates a random number between 0 and the specified difficulty, saving it as the secret_number.
    secret_number = random.randint(0, difficulty)
    return secret_number