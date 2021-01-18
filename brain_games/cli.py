#!/usr/bin/env python
"""Script for CLI."""
import prompt


def welcome_user():
    """Func welcome user.

    Returns:
        return the name user.
    """
    print('Welcome to the Brain Games!')  # noqa: WPS421
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))  # noqa: WPS421
    return name
