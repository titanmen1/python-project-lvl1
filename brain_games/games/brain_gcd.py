#!/usr/bin/env python
"""Game gcd."""
from random import randint

from brain_games.consts import NUMBER_FINISH_RND, NUMBER_START_RND

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def create_game_data():
    """Func creates question and correct answer for the 'Brain-gcd'.

    Returns:
        return the question and correct answer.
    """
    num1 = randint(NUMBER_START_RND, NUMBER_FINISH_RND)
    num2 = randint(NUMBER_START_RND, NUMBER_FINISH_RND)
    question = '{0} {1}'.format(num1, num2)
    correct_answer = str(search_gcd(num1, num2))
    return question, correct_answer


def search_gcd(num1, num2):
    """Func search gcd.

    Args:
        num1: Number for search gcd.
        num2: Number for search gcd.

    Returns:
        return the number gcd.
    """
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 + num2
