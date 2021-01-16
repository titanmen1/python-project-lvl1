#!/usr/bin/env python
"""5."""
from brain_games.game_engine import play_game
from brain_games.games import brain_progression


def main():
    """Script game progression."""
    play_game(brain_progression)


if __name__ == '__main__':
    main()
