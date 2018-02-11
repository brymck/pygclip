.PHONY: all install-dev test coverage cov test-all tox audit upload dist clean-pyc clean-dist

all: test

install-dev:
	pip install --quiet --editable .[dev]

test: clean-pyc install-dev
	pytest

coverage: clean-pyc install-dev
	coverage run -m pytest
	coverage report
	coverage html

cov: coverage

test-all: install-dev
	tox

tox: test-all

audit:
	python setup.py audit

upload: dist
	python setup.py upload

dist: clean-dist
	python setup.py sdist bdist_wheel

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-dist:
	rm -rf dist/
