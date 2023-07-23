dev-down:
	docker-compose down -v

dev-migrate:
	docker-compose exec web python manage.py makemigrations bike_geometry
	docker-compose exec web python manage.py migrate --noinput

dev-build:
	docker-compose up -d --build

dev-build-it:
	docker-compose up --build

dev-up:
	make dev-build
	make dev-migrate

dev-admin:
	docker-compose exec web python manage.py createsuperuser

dev-populate:
	docker-compose exec web python manage.py loaddata db.dump.yaml

dev-dump:
	docker-compose exec web python manage.py dumpdata bike_geometry --format yaml > app/bike_geometry/fixtures/db.dump.yaml

dev-restart:
	make dev-down
	make dev-up
	make dev-migrate