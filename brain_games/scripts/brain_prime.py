#!/usr/bin/env python
"""Script game prime."""
from brain_games.game_engine import play_game
from brain_games.games import brain_prime


def main():
    """main func for game prime."""
    play_game(brain_prime)


if __name__ == '__main__':
    main()
