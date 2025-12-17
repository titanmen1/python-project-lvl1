#!/usr/bin/env python


"""A "Progression game" runner."""

import sys

from brain_games import engine, games


def main():
    """Run a game."""
    engine.run(games.progression)


if __name__ == '__main__':
    sys.exit(main() or 0)
