from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
"""
Functions
1. test_scores_service - it’s purpose is to test our web service. It will get the application
URL as an input, open a browser to that URL, select the score element in our web page,
check that it is a number between 1 to 1000 and return a boolean value if it’s true or not.
2. main_function to call our tests function. The main function will return -1 as an OS exit
code if the tests failed and 0 if they passed.
"""


def test_scores_service(url: str) -> bool:
    driver = webdriver.Chrome()
    driver.get(url)

    score_element = driver.find_element(By.XPATH, '//*[@id="score"]')
    score_text = score_element.text
    print(f"Score: {score_text}")
    if score_text.isdigit():
        score_text_number = int(score_text)
        return 1 <= score_text_number <= 1000
    else:
        return False


def main_function(url):
    if test_scores_service(url):
        return sys.exit(0)
    else:
        return sys.exit(-1)
