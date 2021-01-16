#!/usr/bin/env python
"""File with Game even."""
import random

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def create_game():
    """The Brain-Even data.  # noqa: D401, D400

    Returns:
        return the number.
    """
    return random.randint(1, 100)  # noqa: S311


def correct_answer(number):
    """Create correct answer.  # noqa: DAR201, D400

    Args:
        number: Number from game.

    Returns:
        return the correct answer.
    """
    return 'yes' if number % 2 == 0 else 'no'
