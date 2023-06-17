from django.db import models
from django.urls import reverse


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    amount = models.IntegerField()
    image = models.ImageField()
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    


    
    
    