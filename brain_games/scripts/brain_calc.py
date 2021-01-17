#!/usr/bin/env python
"""Script game calc."""
from brain_games.game_engine import play_game
from brain_games.games import brain_calc


def main():
    """main func for game calc."""
    play_game(brain_calc)


if __name__ == '__main__':
    main()
