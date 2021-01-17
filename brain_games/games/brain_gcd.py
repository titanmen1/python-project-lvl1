#!/usr/bin/env python
"""Game gcd."""
from random import randint

from brain_games.consts import NUMBER_FINISH_RND, NUMBER_START_RND

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def create_game():
    """Create the 'Brain-gcd' game data.  # noqa: D401, D400

    Returns:
        return the 2 numbers.
    """
    return '{0} {1}'.format(
        randint(NUMBER_START_RND, NUMBER_FINISH_RND),  # noqa: S311
        randint(NUMBER_START_RND, NUMBER_FINISH_RND),  # noqa: S311
    )


def correct_answer(question):
    """Create correct answer.  # noqa: DAR201, D400

    Args:
        question: Number from game.

    Returns:
        return the correct answer.
    """
    num1 = int(question.split(' ')[0])
    num2 = int(question.split(' ')[1])

    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return str(num1 + num2)
