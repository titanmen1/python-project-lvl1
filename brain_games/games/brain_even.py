#!/usr/bin/env python
"""Game even."""
from random import randint

from brain_games.consts import NUMBER_FINISH_RND, NUMBER_START_RND

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def creates_question():
    """Func creates question and correct answer for the 'Brain-Even'.

    Returns:
        return the question and correct answer.
    """
    question = randint(NUMBER_START_RND, NUMBER_FINISH_RND)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer
