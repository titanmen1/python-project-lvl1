#!/usr/bin/env python
"""Game calc."""
import operator
from random import choice, randint

from brain_games.consts import NUMBER_FINISH_RND, NUMBER_START_RND

DESCRIPTION = 'What is the result of the expression?'

operators = ['+', '-', '*']


def create_game():
    """Create the 'Brain-Calc' game data.

    Returns:
        return the question.
    """
    num1 = randint(NUMBER_START_RND, NUMBER_FINISH_RND)  # noqa: S311
    num2 = randint(NUMBER_START_RND, NUMBER_FINISH_RND)  # noqa: S311
    current_operator = choice(operators)  # noqa: S311
    return '{0} {1} {2}'.format(num1, current_operator, num2)


def correct_answer(question):
    """Create correct answer.

    Args:
        question: Numbers and operator from game.

    Returns:
        return the correct answer.
    """
    num1 = int(question.split(' ')[0])
    num2 = int(question.split(' ')[2])
    current_operator = question.split(' ')[1]
    if current_operator == '+':
        result_calculations = operator.add(num1, num2)
    if current_operator == '-':
        result_calculations = operator.sub(num1, num2)
    if current_operator == '*':
        result_calculations = operator.mul(num1, num2)
    return str(result_calculations)
