## Prod

- tear down volumes and containers
```
docker-compose -f docker-compose.prod.yml down -v
```

- build containers
```
docker-compose -f docker-compose.prod.yml up -d --build
```

- make migrations for an app - upload being the app to migrate
```
docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations upload
```

- View migration scripts that will be run by the commands below
```
docker-compose -f docker-compose.prod.yml exec web python manage.py sqlmigrate upload 0001
```


- run the migrations
```
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```

- create admin account
```
docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
```



## Dev

- tear down volumes and containers
```
docker-compose down -v
```

- build containers
```
docker-compose up -d --build
```
- make migrations for an app - upload being the app to migrate
```
docker-compose exec web python manage.py makemigrations upload
```

### manage.py commands

- View migration scripts that will be run by the commands below
```
docker-compose exec web python manage.py sqlmigrate upload 0001
```

- run the migrations
```
docker-compose exec web python manage.py migrate --noinput
```
 
- create admin account
```
docker-compose exec web python manage.py createsuperuser
```

- create python shell to run api
```
docker-compose -f docker-compose.prod.yml exec web python manage.py shell
```