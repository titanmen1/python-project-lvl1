#!/usr/bin/env python
"""Game gcd."""
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def create_game():  # noqa: WPS210
    """The Brain-gcd data.  # noqa: D401, D400

    Returns:
        return the 2 numbers.
    """
    number_start = randint(1, 99)  # noqa: S311, WPS432
    delta = randint(1, 9)  # noqa: S311
    length = 10
    index_hidden_num = randint(0, length - 1)  # noqa: S311
    result_game = []
    for index in range(length):
        if index == index_hidden_num:
            result_game.append('..')
        else:
            result_game.append(str(number_start))
        number_start = number_start + delta  # noqa: WPS350
    return ' '.join(result_game)


def correct_answer(question):
    """Create correct answer.  # noqa: DAR201, D400

    Args:
        question: Number from game.

    Returns:
        return the correct answer.
    """
    all_numbers = question.split(' ')
    index = 0
    for item in all_numbers:  # noqa: WPS110
        if item == '..':
            break
        index += 1
    if index <= 5:
        delta = int(all_numbers[index + 2]) - int(all_numbers[index + 1])  # noqa: WPS221, E501
        current_answer = int(all_numbers[index - 1]) + delta
    if index > 5:
        delta = int(all_numbers[index - 1]) - int(all_numbers[index - 2])  # noqa: WPS221, E501
        current_answer = int(all_numbers[index - 1]) + delta
    return str(current_answer)
