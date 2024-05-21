import flask
import utils
"""This file’s sole purpose is to serve the user’s score currently in the scores.txt file over HTTP with HTML.
This will be done by using python’s flask library."""

scores_file_path = utils.SCORES_FILE_NAME

def score_server():
    """This function will serve the score. It will read the score from the scores file and
        will return an HTML"""