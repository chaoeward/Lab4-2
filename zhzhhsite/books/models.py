from django.db import models

# Create your models here.
class Author(models.Model):
    AuthorID = models.CharField(max_length = 30,primary_key = True)
    Name = models.CharField(max_length = 30)
    Age = models.IntegerField()
    Country = models.CharField(max_length = 30)
        

class Books(models.Model):
    ISBN = models.CharField(max_length = 13,primary_key = True)
    Title = models.CharField(max_length = 30)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length = 30)
    Publisher_Date = models.DateField()
    Price = models.FloatField()