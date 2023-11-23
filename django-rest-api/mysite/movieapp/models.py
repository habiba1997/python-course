from django.db import models

# Create your models here.
class Movie(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    rating = models.FloatField()
    image = models.ImageField(default='default.jpeg', upload_to='Images/')
