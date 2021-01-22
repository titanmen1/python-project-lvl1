#!/usr/bin/env python
"""Game progression."""
from random import choice, randint

from brain_games.consts import NUMBER_FINISH_RND, NUMBER_START_RND

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
NUMBER_FINISH_RND_FOR_DELTA = 9
LENGTH = 10


def create_game_data():
    """Func creates question and correct answer for the 'Brain-progression'.

    Returns:
        return the question and correct answer.
    """
    number_start = randint(
        NUMBER_START_RND, NUMBER_FINISH_RND,
    )
    delta = randint(
        NUMBER_START_RND, NUMBER_FINISH_RND_FOR_DELTA,
    )
    progression = range(number_start, number_start + (LENGTH * delta), delta)
    index_hidden_num = choice(progression)
    question = []

    for num in progression:
        if num == index_hidden_num:
            question.append('..')
        else:
            question.append(str(num))

    return ' '.join(question), str(index_hidden_num)
