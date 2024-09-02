v=.venv\Scripts\activate

freeze-requirements:
	$(v) \
	&& pipenv requirements > src\requirements.txt \
 	&& pipenv requirements > src\requirements-dev.txt --dev-only

 black:
	$(v) && black .

isort:
	$(v) && isort .

flake8:
	$(v) && flake8 .

format:
	$(v) && black . && isort .
