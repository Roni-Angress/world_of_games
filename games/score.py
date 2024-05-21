import os
import utils
path = utils.SCORES_FILE_NAME

def add_score(difficulty: int):
    """The function’s input is a variable called difficulty. The function will try to read
    the current score in the scores file, if it fails it will create a new one and will use it to save the
    current score."""
    points_of_winning = (difficulty * 3) + 5
    current_score = 0

    if os.path.isfile(path):
        with open(path, 'r') as scores_file:
            file_content = scores_file.readlines()
            current_score = int(file_content[0])

    else:
        with open(path, 'w') as scores_file:
            scores_file.write("")

    # now add the new score to the file

    new_score = current_score + points_of_winning
    with open(path, 'w') as scores_file:
        scores_file.write(str(new_score))
