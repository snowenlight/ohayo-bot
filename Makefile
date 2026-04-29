.PHONY: install test run

install:
	pip install -e ".[dev]"

test:
	pytest tests/

run:
	python -m ohayo_bot.main
