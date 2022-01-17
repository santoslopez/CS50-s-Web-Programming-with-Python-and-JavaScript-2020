# Lecture 4
[SQL, Models and Migrations - Lecture 4 - CS50's Web Programming with Python and JavaScript 2020](https://www.youtube.com/watch?v=YzP164YANAU&t=2068s).

## Create model
# 
```
python manage.py makemigrations

```

## Run python migrate: database is now up to date.
# 
```
python manage.py migrate

```

## Run new changes the have been made to models.py 
# 
```
python manage.py makemigrations

```


## I can begin to write python commands: InteractiveConsole

```
    python manage.py shell
```

## Code
```
>>> from flights.models import *
>>> jfk = Airport(code="JFK",city="New York")
>>> jfk.save()
>>> lhr = Airport(code="LHR",city="London")
>>> lhr.save()
>>> cdg = Airport(code="CDG",city="Paris")
>>> cdg.save()
>>> nrt = Airport(code="NRT",city="Tokyo")
>>> nrt.save()
>>> f = Flight(origin=jfk,destination=lhr,duration=415)
>>> f.save()
f
f.origin
f.origin.city
f.origin.code
lhr.arrivals.all()
```



## Here I see I get back a query set
```
    f = Flight(origin="New York",destination="London",duration=415)
    >>> f.save()
    >>> Flight.objects.all()
```

## Filter
```
    AirportOrName.objects.filter(city="New York")
    AirportOrName.objects.filter(city="New York").first()
    AirportOrName.objects.get(city="New York")
```


## Create: **ADMIN: app**
```
    python manage.py createsuperuser

```

## Login: **ADMIN: app**. Write username and password.
```
    http://127.0.0.1:8000/admin/
```

# Github Pages Markdown
[GitHub Pages Markdown](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).
