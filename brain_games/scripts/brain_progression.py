#!/usr/bin/env python
"""Script game progression."""
from brain_games.game_engine import play_game
from brain_games.games import brain_progression


def main():
    """main func for game progression."""
    play_game(brain_progression)


if __name__ == '__main__':
    main()
