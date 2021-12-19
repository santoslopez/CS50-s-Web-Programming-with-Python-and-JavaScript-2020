# Install DJango
pip3 install Django

## Create a new project
django-admin startproject PROJECT_NAME

## Create app Django
python manage.py startapp NAME_APP


## Configurations
File settings.py in code. I'll just add nameApp:

INSTALLED_APPS = [
    'addNameApp',
    ...
    
]

## Name projects file: views.py
So here is the default file, again, from views.py
# Create your view here
def index(request):
    
# Create Environment 
https://flask.palletsprojects.com/en/2.0.x/installation/

# Run 
python manage.py runserver