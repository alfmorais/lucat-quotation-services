format:
	@ruff check . --fix && ruff format .

run:
	@python lucat/manage.py runserver

migrate:
	@python lucat/manage.py migrate

migrations:
	@python lucat/manage.py makemigrations