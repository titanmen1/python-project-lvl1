#!/usr/bin/env python
"""Script game prime."""
from brain_games.game_engine import play
from brain_games.games import brain_prime


def main():
    """Start game prime."""
    play(brain_prime)


if __name__ == '__main__':
    main()
