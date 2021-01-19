#!/usr/bin/env python
"""Game progression."""
from random import randint

from brain_games.consts import NUMBER_FINISH_RND, NUMBER_START_RND

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
NUMBER_FINISH_RND_FOR_DELTA = 9
LENGTH = 10


def create_game():
    """Func creates question and correct answer for the 'Brain-progression' game data.

    Returns:
        return the question and correct answer.
    """
    number_start = randint(
        NUMBER_START_RND, NUMBER_FINISH_RND,
    )
    delta = randint(
        NUMBER_START_RND, NUMBER_FINISH_RND_FOR_DELTA,
    )
    index_hidden_num = randint(0, LENGTH - 1)
    question = []
    for index in range(LENGTH):
        if index == index_hidden_num:
            correct_answer = number_start + delta * index
            question.append("..")
        else:
            next_step = number_start + delta * index
            question.append(next_step)

    return question, correct_answer
