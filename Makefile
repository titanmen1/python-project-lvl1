install:
	uv sync

build:
	uv build

lint:
	uv run ruff check brain_games

brain-games:
	uv run brain-games

brain-even:
	uv run brain-even

brain-prime:
	uv run brain-prime

brain-calc:
	uv run brain-calc

brain-gcd:
	uv run brain-gcd

brain-progression:
	uv run brain-progression
