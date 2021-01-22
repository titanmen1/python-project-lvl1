#!/usr/bin/env python
"""Script game even."""
from brain_games.game_engine import play
from brain_games.games import brain_even


def main():
    """Start game even."""
    play(brain_even)


if __name__ == '__main__':
    main()
