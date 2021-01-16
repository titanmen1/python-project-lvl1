#!/usr/bin/env python
"""Game gcd."""
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def create_game():
    """The Brain-gcd data.  # noqa: D401, D400

    Returns:
        return the 2 numbers.
    """
    return str(randint(1, 100))



def correct_answer(question):
    """Create correct answer.  # noqa: DAR201, D400

    Args:
        question: Number from game.

    Returns:
        return the correct answer.
    """
    num = int(question)
    if num < 2:
        return 'no'
    k = 0
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            k = k + 1
    if (k <= 0):
        return 'yes'
    else:
        return 'no'

