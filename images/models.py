from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=250)
    value = models.ImageField()
    def __str__(self):
        return self.name