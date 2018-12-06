from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=250)
    value = models.ImageField(upload_to='product_images/')
    def __str__(self):
        return self.name