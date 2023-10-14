app:=
p:=.
id:=

all:
	echo "Makefile settings"

setup:
	pip install -r requirements.txt
	make folder-setup -i

setup-dev: setup
	pip install -r requirements_dev.txt

run:
	python manage.py runserver

check:
	python manage.py check

shell:
	python manage.py shell

dbshell:
	python manage.py dbshell

m-show:
	python manage.py showmigrations

m-create:
	python manage.py makemigrations $(app)

m-migrate:
	python manage.py migrate $(app)

f-check:
	autoflake . --check --config pyproject.toml
	isort . --check --settings-path pyproject.toml
	black . --check --config pyproject.toml

f-format:
	autoflake . --config pyproject.toml
	isort . --settings-path pyproject.toml
	black . --config pyproject.toml

unit:
	python manage.py test -k $(p)

prready: f-check unit

folder-setup:
	mkdir upload logs
	> logs/notia.log

db-setup:
	python manage.py shell -c "from annotations.db.notia import main; main();" > logs/notia.log

annotations-execute:
	echo python manage.py shell -c "from annotations.db.notia.modifications import $(id); $(id)()"

docker-up:
	docker compose up --build -d --wait

docker-down:
	docker compose down
