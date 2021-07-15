from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=30)
    duration = models.FloatField()
    rating = models.FloatField()
    typ = models.CharField(max_length=200,default='action')

    image = models.ImageField(upload_to='api/images' ,default='api/images/Noimg.jpg')
    def __str__(self):
        return self.name
    