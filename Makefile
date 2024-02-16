.PHONY: clean-build
clean-build:
	
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/

	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +
	find . -type d -name __pycache__ -exec rm -rv {} +

.PHONY: clean-docs
clean-docs:
	rm -fr site/

.PHONY: clean-pyc
clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.DS_Store' -exec rm -fr {} +

.PHONY: clean-test
clean-test: clean-cache

	rm -fr htmlcov/
	rm -f .coverage
	rm -fr coverage.xml

	find . -name ".coverage*" -not -name ".coveragerc" -exec rm -fr "{}" \;
	find . -name 'log.txt' -exec rm -fr {} +
	find . -name 'log.*.txt' -exec rm -fr {} +

.PHONY: clean-cache
clean-cache:
	rm -fr .tox/
	rm -fr .hypothesis/
	rm -fr .pytest_cache
	rm -fr .mypy_cache/

.PHONY: clean
clean: clean-test clean-build clean-pyc clean-docs

.PHONY: dist
dist: clean
	poetry build

.PHONY: format-code
format-code:
	tox -e isort
	tox -e black

.PHONY: check-code
check-code:
	tox -p -e isort-check -e black-check -e flake8 -e mypy -e pylint

.PHONY: codegen
codegen:
	python scripts/render/html.py
	python scripts/render/css.py
	python scripts/render/style.py