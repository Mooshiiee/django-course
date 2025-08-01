from django.apps import AppConfig

# copy this `BooksConfig` class name for the settings.py file
class BooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'books'
