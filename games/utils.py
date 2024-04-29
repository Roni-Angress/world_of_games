def validate_number_input(message: str) -> float:
    """
    Prompts the user to enter a number.
    The function returns the user input as a float.
    """
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")


def validate_int_input(message: str) -> int:
    """
    Prompts the user to enter an integer within the range of 1 to 101.
    The function returns the user input as an integer.
    """
    while True:
        user_input = input(message)
        if user_input.isdigit():  # Check if input is composed only of digits
            number = int(user_input)
            if 1 <= number <= 101:  # Check if number is within the desired range
                return number
            else:
                print("Number must be in the range of 1 - 101.")
        else:
            print("Invalid input. Please enter an integer.")
