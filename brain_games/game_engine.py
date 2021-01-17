#!/usr/bin/env python
"""Core module. Game engine"""
import prompt

from brain_games.cli import welcome_user

NUMBER_OF_ROUNDS = 3


def play_game(game):
    """Engine for the 'Brain Game'.

    Args:
        game: The game.
    """
    name_user = welcome_user()
    print(game.DESCRIPTION)  # noqa: WPS421
    iteration = 0

    while iteration < NUMBER_OF_ROUNDS:
        question = game.create_game()
        correct_answer = game.correct_answer(question)
        print('Question: {0}'.format(question))  # noqa: WPS421
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')  # noqa: WPS421
            iteration += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(user_answer, correct_answer))  # noqa: WPS421, E501
            print("Let's try again, {0}!".format(name_user))  # noqa: WPS421
            return

    print('Congratulations, {0}!'.format(name_user))  # noqa: WPS421
