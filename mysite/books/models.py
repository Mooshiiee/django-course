from django.db import models

# Create your models here.

# from csv -> to relational, then describe models

# First lets create a model for an author
class Author(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    dob = models.DateField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    year = models.IntegerField()
    # foriegn key field        on delete cascade means when AUTHOR is deleted, it will delete these books aswell
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' by ' + self.author.first_name + ' ' + self.author.last_name

