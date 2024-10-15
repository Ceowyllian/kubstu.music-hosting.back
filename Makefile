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

migrations:
	$(v) && python src\manage.py makemigrations

migrate:
	$(v) && python src\manage.py migrate

version:
	$(v) && git checkout master && git rebase --onto dev \
	&& semantic-release version --no-vcs-release --no-push \
	&& git checkout dev && git rebase --onto master && git push --all