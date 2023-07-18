- [Development](#development)
  - [buiding and tearing down contaniners](#buiding-and-tearing-down-contaniners)
      - [tear down volumes and containers](#tear-down-volumes-and-containers)
      - [build containers](#build-containers)
  - [manage.py commands](#managepy-commands)
      - [add a new app to project](#add-a-new-app-to-project)
      - [migrations](#migrations)
      - [create admin account](#create-admin-account)
  - [hosted on](#hosted-on)
- [Production](#production)
  - [buiding and tearing down contaniners](#buiding-and-tearing-down-contaniners-1)
      - [tear down volumes and containers](#tear-down-volumes-and-containers-1)
      - [build containers](#build-containers-1)
  - [manage.py commands](#managepy-commands-1)
      - [add a new app to project](#add-a-new-app-to-project-1)
      - [migrations](#migrations-1)
      - [create admin account](#create-admin-account-1)
  - [hosted on](#hosted-on-1)
- [API](#api)
  - [create python shell to run API - Dev](#create-python-shell-to-run-api---dev)
  - [create python shell to run API - Prod](#create-python-shell-to-run-api---prod)
  - [example 1 API question creation](#example-1-api-question-creation)
  - [example 2 API question filtering and choice creation](#example-2-api-question-filtering-and-choice-creation)
- [Testing](#testing)
  - [Dev](#dev)
  - [Prod](#prod)



# Development

## buiding and tearing down contaniners

#### tear down volumes and containers
```shell
docker-compose down -v
```

#### build containers
```shell
docker-compose up --build
```

## manage.py commands

#### add a new app to project
- run from same folder as manage.py (app)
```shell
docker-compose exec web python manage.py startapp bike_geometry
```

-flush the database
```
docker-compose exec web python manage.py flush --no-input
```

#### migrations
- create migration script
```shell
docker-compose exec web python manage.py makemigrations bike_geometry
```

- view migration script - 0001 refers to script to view in ./upload/migrations
```shell
docker-compose exec web python manage.py sqlmigrate bike_geometry 0004
```

- run migration script
```shell
docker-compose exec web python manage.py migrate --noinput
```

#### create admin account
```shell
docker-compose exec web python manage.py createsuperuser
```

## hosted on
- http://localhost:8000/bike-geometry/admin/
- http://localhost:8000/bike-geometry/
- http://localhost:8000/bike-geometry/upload/  
  
    
# Production

## buiding and tearing down contaniners

#### tear down volumes and containers
```shell
docker-compose -f docker-compose.prod.yml down -v
```

#### build containers
```shell
docker-compose -f docker-compose.prod.yml up -d --build
```

## manage.py commands

#### add a new app to project
```shell
docker-compose -f docker-compose.prod.yml  exec web python manage.py startapp upload
```

#### migrations
```shell
- create migration script
docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations upload
```

- view migration script - 0001 refers to script to view in ./upload/migrations
```shell
docker-compose -f docker-compose.prod.yml exec web python manage.py sqlmigrate upload 0001
```
- run migration script
```shell
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
```
- migrate static files
```shell
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```

#### create admin account
```shell
docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
```

## hosted on
- http://localhost:1337/admin/
- http://localhost:1337/bike-geometry/
- http://localhost:1337/bike-geometry/upload/



# API

## create python shell to run API - Dev
```shell
docker-compose exec web python manage.py shell
```

## create python shell to run API - Prod
```shell
docker-compose -f docker-compose.prod.yml exec web python manage.py shell
```

## example 1 API question creation
```python
from upload.models import Choice, Question  # Import the model classes we just wrote.

# No questions are in the system yet.
print(Question.objects.all())

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())
q1 = Question(question_text="Do you like dogs?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
q.save()
q1.save()

# Now it has an ID.
print(q.id)

# Access model field values via Python attributes.
print(q.question_text)
print(q.pub_date)

# Change values by changing the attributes, then calling save().
q.question_text = "What's up?"
q.save()

# objects.all() displays all the questions in the database.
print(Question.objects.all())
exit()
```

## example 2 API question filtering and choice creation
```python
from upload.models import Choice, Question

# Make sure our __str__() addition worked.
print(Question.objects.all())


# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
print(Question.objects.filter(id=1))
print(Question.objects.filter(question_text__startswith="What"))


# Get the question that was published this year.
from django.utils import timezone
current_year = timezone.now().year
print(Question.objects.get(pub_date__year=current_year))


# Request an ID that doesn't exist, this will raise an exception.
print(Question.objects.get(id=200))

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
print(Question.objects.get(pk=1))


# Make sure our custom method worked.
q = Question.objects.get(pk=1)
print(q.was_published_recently())


# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
print(q.choice_set.all())


# Create three choices.
q.choice_set.create(choice_text="Not much", votes=0)

q.choice_set.create(choice_text="The sky", votes=0)

c = q.choice_set.create(choice_text="Just hacking again", votes=0)

# Choice objects have API access to their related Question objects.
print(c.question)

# And vice versa: Question objects get access to Choice objects.
print(q.choice_set.all())
print(q.choice_set.count())


# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
print(Choice.objects.filter(question__pub_date__year=current_year))


# Let's delete one of the choices. Use delete() for that.
c = q.choice_set.filter(choice_text__startswith="Just hacking")
c.delete()
exit()
```



# Testing

## Dev
```shell
docker-compose exec web python manage.py test upload
```

## Prod
```shell
docker-compose -f docker-compose.prod.yml exec web python manage.py test upload
```