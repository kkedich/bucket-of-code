SRC_DIRS := src

# Code formatter - PEP 8 style guide
pep8.all:
	python3 -m autopep8 --max-line-length 100 --recursive --in-place $(SRC_DIRS)

# Static code analysis tool
pylint.all:
	python3 -m pylint --rcfile=.pylintrc $(SRC_DIRS)

# Sorts the imports in python files following PEP-style
# https://github.com/timothycrosley/isort/
isort.all:
	python3 -m isort $(SRC_DIRS)

# Another tool to check the code style and quality
flake.all:
	python3 -m flake8 --ignore E501,W503,W504 $(SRC_DIRS)


pre-commit: isort.all pep8.all flake.all pylint.all
