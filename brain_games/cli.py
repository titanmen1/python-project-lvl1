#!/usr/bin/env python
"""CLI."""
import prompt


def welcome_user():
    """Func welcome user.

    Returns:
        return the name user.
    """
    print('Welcome to the Brain Games!')  # noqa: WPS421
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))  # noqa: WPS421, P101
    return name
