#!/usr/bin/env python


"""An "Even game" runner."""

import sys

from brain_games import engine, games


def main():
    """Run a game."""
    engine.run(games.even)


if __name__ == '__main__':
    sys.exit(main() or 0)
