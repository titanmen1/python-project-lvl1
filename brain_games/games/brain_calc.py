#!/usr/bin/env python
"""Game calc."""
import operator
from random import choice, randint

from brain_games.consts import NUMBER_FINISH_RND, NUMBER_START_RND

DESCRIPTION = 'What is the result of the expression?'

operators = ['+', '-', '*']


def creates_question():
    """Func creates question and correct answer for the 'Brain-Calc' game data.

    Returns:
        return the question and correct answer.
    """
    num1 = randint(NUMBER_START_RND, NUMBER_FINISH_RND)
    num2 = randint(NUMBER_START_RND, NUMBER_FINISH_RND)
    current_operator = choice(operators)

    question = '{0} {1} {2}'.format(num1, current_operator, num2)
    correct_answer = str(calculator(num1, num2, current_operator))
    return question, correct_answer


def calculator(num1, num2, sign):
    """Func for calculations.

    Args:
        num1: Number for calc.
        num2: Number for calc.
        sign: Operation sign.

    Returns:
        return Number.
    """
    if sign == '+':
        result_calculations = operator.add(num1, num2)
    if sign == '-':
        result_calculations = operator.sub(num1, num2)
    if sign == '*':
        result_calculations = operator.mul(num1, num2)
    return result_calculations
