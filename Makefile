# Makefile
install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

# For unix
#package-install:
#	python3 -m pip install --user dist/*.whl

# For win
package-install:
	python -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games
