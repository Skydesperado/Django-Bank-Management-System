.PHONY: check
check:
	cd backend && pipenv run python manage.py check

.PHONY: runserver
runserver:
	cd backend && pipenv run python manage.py runserver

.PHONY: migrations
migrations:
	cd backend && pipenv run python manage.py makemigrations

.PHONY: migrate
migrate:
	cd backend && pipenv run python manage.py migrate

.PHONY: superuser
superuser:
	cd backend && pipenv run python manage.py createsuperuser

.PHONY: test
test:
	cd backend && pipenv run python manage.py test

# .PHONY: install-precommit
# install-precommit:
# 	pipenv run pre-commit uninstall; pipenv run pre-commit install

# .PHONY: lint
# lint:
# 	pipenv run pre-commit run --all-files
