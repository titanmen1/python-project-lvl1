#!/usr/bin/env python
"""Script game progression."""
from brain_games.game_engine import play
from brain_games.games import brain_progression


def main():
    """Start game progression."""
    play(brain_progression)


if __name__ == '__main__':
    main()
