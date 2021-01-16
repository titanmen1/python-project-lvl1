#!/usr/bin/env python
"""6."""
from brain_games.game_engine import play_game
from brain_games.games import brain_prime


def main():
    """Script game calc."""
    play_game(brain_prime)


if __name__ == '__main__':
    main()
