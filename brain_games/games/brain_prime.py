#!/usr/bin/env python
"""Game prime."""
from random import randint

from brain_games.consts import NUMBER_FINISH_RND, NUMBER_START_RND

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def creates_question():
    """Func creates question and correct answer for the 'Brain-gcd' game data.

    Returns:
        return the question and correct answer.
    """
    question = randint(NUMBER_START_RND, NUMBER_FINISH_RND)
    correct_answer = search_prime(question)
    return question, correct_answer


def search_prime(num):
    """Func search prime number.

    Args:
        num: Number for search prime.

    Returns:
        return the correct answer.
    """
    if num < 2:
        return 'no'
    res = 0
    for index in range(2, num // 2 + 1):
        if num % index == 0:
            res = res + 1
    if res <= 0:
        return 'yes'
    return 'no'
