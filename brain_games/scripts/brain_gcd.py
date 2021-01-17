#!/usr/bin/env python
"""Script game gcd."""
from brain_games.game_engine import play_game
from brain_games.games import brain_gcd


def main():
    """Start game gcd."""
    play_game(brain_gcd)


if __name__ == '__main__':
    main()
