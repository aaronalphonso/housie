.PHONY: help
help:
	@echo "---------------COMMANDS-----------------"
	@echo -e "make help\nmake lint\nmake flake\nmake format\nmake bandit\nmake test"
	@echo "------------------------------------"

.PHONY: lint
lint:
	@python -m bandit --version
	@echo -e "Running bandit on all files...\n"
	@bandit -c bandit.yml -r .

	@python -m mypy --version
	@echo -e "Running mypy on all files...\n"
	@mypy . --config-file mypy.ini 

	@python -m flake8 --version
	@echo -e "Running flake8 on all files...\n"
	@flake8 .

	@python -m pylint --version
	@echo -e "Running pylint on all .py files...\n"
	@pylint --recursive=y "."

.PHONY: flake
flake:
	@python -m flake8 --version
	@echo -e "Running flake8 on all files...\n"
	@flake8 .

.PHONY: format
format:
	@python -m black --version
	@echo -e "Formatting using black..."
	@black .

	@python -m isort --version
	@echo -e "Formatting using isort..."
	@isort .

.PHONY: bandit
bandit: 
	@python -m bandit --version
	@bandit -c bandit.yml -r .
	
.PHONY: test
test:
	@python -m pytest --version
	@python -m pytest tests
	