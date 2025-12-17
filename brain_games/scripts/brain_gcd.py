#!/usr/bin/env python


"""A "GCD game" runner."""

import sys

from brain_games import engine, games


def main():
    """Run a game."""
    engine.run(games.gcd)


if __name__ == '__main__':
    sys.exit(main() or 0)
