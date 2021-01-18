#!/usr/bin/env python
"""Game prime."""
from random import randint

from brain_games.consts import NUMBER_FINISH_RND, NUMBER_START_RND

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def create_game():
    """Create the 'Brain-gcd' game data.

    Returns:
        return the number.
    """
    return str(randint(NUMBER_START_RND, NUMBER_FINISH_RND))  # noqa: S311


def correct_answer(question):
    """Create correct answer.

    Args:
        question: Number from game.

    Returns:
        return the correct answer.
    """
    num = int(question)
    if num < 2:
        return 'no'
    res = 0
    for index in range(2, num // 2 + 1):
        if num % index == 0:
            res = res + 1
    if res <= 0:
        return 'yes'
    return 'no'
