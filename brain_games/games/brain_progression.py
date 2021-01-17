#!/usr/bin/env python
"""Game progression."""
from random import randint

from brain_games.consts import NUMBER_FINISH_RND, NUMBER_START_RND

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def create_game():  # noqa: WPS210
    """Create the 'Brain-progression' game data.  # noqa: D401, D400

    Returns:
        return the question.
    """
    number_start = randint(  # noqa: S311
        NUMBER_START_RND, NUMBER_FINISH_RND,
    )
    number_finish_rnd_for_delta = 9
    delta = randint(  # noqa: S311
        NUMBER_START_RND, number_finish_rnd_for_delta,
    )
    length = 10
    index_hidden_num = randint(0, length - 1)  # noqa: S311
    result_game = []
    for index in range(length):
        if index == index_hidden_num:
            result_game.append('..')
        else:
            result_game.append(str(number_start))
        number_start = number_start + delta  # noqa: WPS350
    return ' '.join(result_game)


def correct_answer(question):
    """Create correct answer.  # noqa: DAR201, D400

    Args:
        question: Number progression.

    Returns:
        return the correct answer.
    """
    all_numbers = question.split(' ')
    index = 0
    for item in all_numbers:  # noqa: WPS110
        if item == '..':
            break
        index += 1
    if index <= 5:
        delta = int(all_numbers[index + 2]) - int(all_numbers[index + 1])  # noqa: WPS221, E501
        current_answer = int(all_numbers[index + 1]) - delta
    if index > 5:
        delta = int(all_numbers[index - 1]) - int(all_numbers[index - 2])  # noqa: WPS221, E501
        current_answer = int(all_numbers[index - 1]) + delta
    return str(current_answer)
