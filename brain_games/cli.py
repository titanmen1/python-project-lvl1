#!/usr/bin/env python
"""CLI."""
import prompt


def welcome_user():
    """Welcome."""
    print('Welcome to the Brain Games!')  # noqa: WPS421
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))  # noqa: WPS421, P101
    return name
