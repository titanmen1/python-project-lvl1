#!/usr/bin/env python
"""Game even."""
import random

from brain_games.consts import NUMBER_FINISH_RND, NUMBER_START_RND

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def create_game():
    """Create the 'Brain-Even' game data.  # noqa: D401, D400

    Returns:
        return the number.
    """
    return random.randint(NUMBER_START_RND, NUMBER_FINISH_RND)  # noqa: S311


def correct_answer(question):
    """Create correct answer.  # noqa: DAR201, D400

    Args:
        question: Number from game.

    Returns:
        return the correct answer.
    """
    return 'yes' if question % 2 == 0 else 'no'
