#!/usr/bin/env python
"""Core module. Game engine."""
import prompt

NUMBER_OF_ROUNDS = 3


def play(game=None):
    """Engine for the 'Brain Game'.

    Args:
        game: The game.
    """
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name_user))
    if game is None:
        return
    print(game.DESCRIPTION)
    iteration = 0

    while iteration < NUMBER_OF_ROUNDS:
        question, correct_answer = game.create_game_data()
        print('Question: {0}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            iteration += 1
        else:
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(user_answer, correct_answer))  # noqa: E501
            print("Let's try again, {0}!".format(name_user))
            return

    print('Congratulations, {0}!'.format(name_user))
