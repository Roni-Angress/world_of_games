from flask import Flask, render_template
import games.score as score
import utils
"""This file’s sole purpose is to serve the user’s score currently in the scores.txt file over HTTP with HTML.
This will be done by using python’s flask library."""
scores_file_path = utils.SCORES_FILE_NAME

app = Flask(__name__)

@app.route("/")
def score_server():
    current_score = str(score.get_score())
    return render_template('score.html', SCORE=current_score)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)