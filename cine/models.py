from django.db import models


# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField('Actor', blank=True, related_name='movies')

    def __str__(self):
        return f'{self.title}'


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Review(models.Model):
    grade = models.PositiveSmallIntegerField(default=5)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='reviews')
