

# Dev

### buiding and tearing down contaniners

#### tear down volumes and containers
```
$ docker-compose down -v
```

#### build containers
```
$ docker-compose up -d --build
```

### manage.py commands

#### add a new app to project
```
$ docker-compose exec web python manage.py startapp upload
```

#### migrations
```
# create migration script
$ docker-compose exec web python manage.py makemigrations upload

# view migration script - 0001 refers to script to view in ./upload/migrations
$ docker-compose exec web python manage.py sqlmigrate upload 0001

# run migration script
$ docker-compose exec web python manage.py migrate --noinput
```

#### create admin account
```
$ docker-compose exec web python manage.py createsuperuser
```

#### create python shell to run api
```
$ docker-compose -f docker-compose.prod.yml exec web python manage.py shell
```

#### hosted on
- http://localhost:8000/bike-geometry/admin/
- http://localhost:8000/bike-geometry/
- http://localhost:8000/bike-geometry/upload/  
  


  
  
  
# Prod

### buiding and tearing down contaniners

#### tear down volumes and containers
```
$ docker-compose -f docker-compose.prod.yml down -v
```

#### build containers
```
$ docker-compose -f docker-compose.prod.yml up -d --build
```

### manage.py commands

#### add a new app to project
```
$ docker-compose -f docker-compose.prod.yml  exec web python manage.py startapp upload
```

#### migrations
```
# create migration script
$ docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations upload

# view migration script - 0001 refers to script to view in ./upload/migrations
$ docker-compose -f docker-compose.prod.yml exec web python manage.py sqlmigrate upload 0001

# run migration script
$ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput

# migrate static files
$ docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```

#### create admin account
```
$ docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
```

#### hosted on
- http://localhost:1337/admin/
- http://localhost:1337/bike-geometry/
- http://localhost:1337/bike-geometry/upload/
