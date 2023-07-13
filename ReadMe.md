## Prod

- tear down volumes and containers
docker-compose -f docker-compose.prod.yml down -v

- build containers
docker-compose -f docker-compose.prod.yml up -d --build

- make migrations for an app - upload being the app to migrate
docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations upload

- run the migrations
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput



## Dev

- tear down volumes and containers
docker-compose down -v

- build containers
docker-compose up -d --build

- make migrations for an app - upload being the app to migrate
docker-compose exec web python manage.py makemigrations upload

- run the migrations
docker-compose exec web python manage.py migrate --noinput

