#!/usr/bin/env python
"""4."""
from brain_games.game_engine import play_game
from brain_games.games import brain_gcd


def main():
    """Script game calc."""
    play_game(brain_gcd)


if __name__ == '__main__':
    main()
