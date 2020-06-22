from django.db import models

# Create your models here.
class Musician(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} : {self.age}'

class Album(models.Model):
    # Musician과 1:N 관계
    title = models.CharField(max_length=150)
    
    def __str__(self):
        return f'{self.title}'
