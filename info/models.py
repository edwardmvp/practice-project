from django.db import models
from django.urls import reverse
from tinymce import models as tinymce_models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        
        return self.name

class Book(models.Model):
    name = models.CharField(name="Название",max_length=50)
    genre = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    amount = models.IntegerField()
    image = models.ImageField()
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    

class Project(models.Model):
    name = models.CharField(verbose_name="Название", max_length=50)
    image = models.ImageField(verbose_name="Прикрепите фото",blank=True)
    text = tinymce_models.HTMLField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('info', args=[str(self.id)])
    
    
class Section(models.Model):
    