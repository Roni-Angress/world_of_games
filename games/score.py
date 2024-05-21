import os
import utils

scores_file_path = utils.SCORES_FILE_NAME

def add_score(difficulty: int):
    """
    Adds the score based on the difficulty level to the scores file.

    Parameters:
    difficulty (int): The difficulty level to determine the points to be added.
    """
    points_of_winning = (difficulty * 3) + 5

    # Initialize the current score
    current_score = 0

    if os.path.isfile(scores_file_path):
        with open(scores_file_path, 'r') as scores_file:
            # Read the first line and attempt to parse the score
            first_line = scores_file.readline().strip()
            if first_line.isdigit():
                current_score = int(first_line)
            else:
                print(f"Warning: Invalid score found in {scores_file_path}. Starting from 0.")

    # Calculate the new score
    new_score = current_score + points_of_winning

    # Write the new score back to the file. If the file does not exist it will be created regardless.
    with open(scores_file_path, 'w') as scores_file:
        scores_file.write(str(new_score))
