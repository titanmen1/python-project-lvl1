#!/usr/bin/env python
"""Script game gcd."""
from brain_games.game_engine import play
from brain_games.games import brain_gcd


def main():
    """Start game gcd."""
    play(brain_gcd)


if __name__ == '__main__':
    main()
