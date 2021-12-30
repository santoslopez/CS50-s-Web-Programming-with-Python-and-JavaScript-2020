# Lecture 4
[SQL, Models and Migrations - Lecture 4 - CS50's Web Programming with Python and JavaScript 2020](https://www.youtube.com/watch?v=YzP164YANAU&t=2068s).

## Create model
# 
```
python manage.py makemigrations

```

## Run python migrate 
# 
```
python manage.py migrate

```

## I can begin to write python commands: InteractiveConsole

```
    python manage.py shell
```

# Here I see I get back a query set
```
    f = Flight(origin="New York",destination="London",duration=415)
    >>> f.save()
    >>> Flight.objects.all()
```

[GitHub Pages Markdown](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).
