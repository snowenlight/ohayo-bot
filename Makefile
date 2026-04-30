.PHONY: install test test-integration run

install:
	pip install -e ".[dev]"

test:
	pytest tests/ -v

test-integration:
	pytest tests/test_integration.py -v -s

run:
	python -m ohayo_bot.main
