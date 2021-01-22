#!/usr/bin/env python
"""Script game calc."""
from brain_games.game_engine import play
from brain_games.games import brain_calc


def main():
    """Start game calc."""
    play(brain_calc)


if __name__ == '__main__':
    main()
