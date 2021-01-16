#!/usr/bin/env python
"""File with Game even."""

import prompt
import random
from brain_games.cli import welcome_user


def game_even():
    """Game even."""
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')  # noqa: WPS421
    result = 0
    while True:
        if result == 3:
            print('Congratulations, {}!'.format(name))  # noqa: WPS421
            break
        number = random.randint(1, 99)
        print('Question: {}'.format(number))  # noqa: WPS421
        ask = prompt.string('Your answer: ')
        if number % 2 == 0:
            if ask == 'yes':
                print('Correct!')
                result += 1
            else:
                print("'{}' is wrong answer ;(. Correct answer was 'yes'.".format(ask))  # noqa: WPS421
                print("Let's try again, {}!".format(name))  # noqa: WPS421
                result = 0
        if number % 2 == 1:
            if ask == 'no':
                print('Correct!')  # noqa: WPS421
                result += 1
            else:
                print("'{}' is wrong answer ;(. Correct answer was 'no'.".format(ask))  # noqa: WPS421
                print("Let's try again, {}!".format(name))  # noqa: WPS421
                result = 0
