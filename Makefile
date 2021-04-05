
all: drop migration migrate create run

migration:
	python manage.py makemigrations

migrate:
	python manage.py migrate

drop:
	echo "drop database assesment" | /Applications/Postgres.app/Contents/Versions/13/bin/psql
	echo "create database assesment" | /Applications/Postgres.app/Contents/Versions/13/bin/psql

run:
	python manage.py runserver

create:
	python manage.py createsuperuser