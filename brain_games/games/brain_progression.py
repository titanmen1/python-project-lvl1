#!/usr/bin/env python
"""Game progression."""
from random import randint

from brain_games.consts import NUMBER_FINISH_RND, NUMBER_START_RND

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
NUMBER_FINISH_RND_FOR_DELTA = 9
LENGTH = 10


def create_game():
    """Create the 'Brain-progression' game data.

    Returns:
        return the question.
    """
    number_start = randint(  # noqa: S311
        NUMBER_START_RND, NUMBER_FINISH_RND,
    )
    delta = randint(  # noqa: S311
        NUMBER_START_RND, NUMBER_FINISH_RND_FOR_DELTA,
    )
    index_hidden_num = randint(0, LENGTH - 1)  # noqa: S311
    result_game = []
    for index in range(LENGTH):
        if index == index_hidden_num:
            result_game.append('..')
        else:
            result_game.append(str(number_start))
        number_start += delta
    return ' '.join(result_game)


def correct_answer(question):
    """Create correct answer.

    Args:
        question: Number progression.

    Returns:
        return the correct answer.
    """
    all_numbers = question.split(' ')
    index = 0
    for item_game in all_numbers:
        if item_game == '..':
            break
        index += 1
    if index <= 5:
        delta = int(all_numbers[index + 2]) - int(all_numbers[index + 1])  # noqa: WPS221, E501
        current_answer = int(all_numbers[index + 1]) - delta
    if index > 5:
        delta = int(all_numbers[index - 1]) - int(all_numbers[index - 2])  # noqa: WPS221, E501
        current_answer = int(all_numbers[index - 1]) + delta
    return str(current_answer)
